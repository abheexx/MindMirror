import os
import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import pinecone
from dotenv import load_dotenv

from models.schemas import EmotionEntry

load_dotenv()

logger = logging.getLogger(__name__)

class PineconeService:
    def __init__(self):
        """Initialize Pinecone client"""
        api_key = os.getenv("PINECONE_API_KEY")
        environment = os.getenv("PINECONE_ENVIRONMENT")
        index_name = os.getenv("PINECONE_INDEX_NAME", "mindmirror-emotions")
        
        if not api_key or not environment or api_key == "your_pinecone_api_key_here" or environment == "your_pinecone_environment_here":
            logger.warning("Pinecone credentials not found or using placeholder values. Running in memory-only mode.")
            self.pinecone_available = False
            self.memory_storage = []
            return
        
        try:
            pinecone.init(api_key=api_key, environment=environment)
            
            # Check if index exists, create if not
            if index_name not in pinecone.list_indexes():
                pinecone.create_index(
                    name=index_name,
                    dimension=1536,  # OpenAI embedding dimension
                    metric="cosine"
                )
                logger.info(f"Created Pinecone index: {index_name}")
            
            self.index = pinecone.Index(index_name)
            self.pinecone_available = True
            logger.info(f"Connected to Pinecone index: {index_name}")
            
        except Exception as e:
            logger.error(f"Failed to initialize Pinecone: {str(e)}")
            self.pinecone_available = False
            self.memory_storage = []
    
    async def store_emotion_entry(self, entry: EmotionEntry) -> bool:
        """
        Store an emotion entry in Pinecone or memory
        """
        try:
            if self.pinecone_available:
                # Create vector embedding (simplified - in production, use OpenAI embeddings)
                vector = self._create_simple_embedding(entry.transcript + " " + entry.mood)
                
                # Store in Pinecone
                self.index.upsert(
                    vectors=[{
                        "id": f"{entry.user_id}_{entry.timestamp}",
                        "values": vector,
                        "metadata": {
                            "user_id": entry.user_id,
                            "timestamp": entry.timestamp,
                            "transcript": entry.transcript,
                            "mood": entry.mood,
                            "summary": entry.summary,
                            "reflection": entry.reflection,
                            "confidence": entry.confidence
                        }
                    }]
                )
                logger.info(f"Stored emotion entry for user {entry.user_id}")
            else:
                # Store in memory
                self.memory_storage.append(entry.dict())
                logger.info(f"Stored emotion entry in memory for user {entry.user_id}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error storing emotion entry: {str(e)}")
            return False
    
    async def get_user_history(self, user_id: str, days: int = 7) -> List[EmotionEntry]:
        """
        Retrieve user's emotional history from Pinecone or memory
        """
        try:
            if self.pinecone_available:
                # Query Pinecone for user's entries
                cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
                
                # Query with filter for user_id and date range
                results = self.index.query(
                    vector=[0] * 1536,  # Dummy vector for metadata-only query
                    filter={
                        "user_id": {"$eq": user_id},
                        "timestamp": {"$gte": cutoff_date}
                    },
                    include_metadata=True,
                    top_k=100
                )
                
                entries = []
                for match in results.matches:
                    metadata = match.metadata
                    entry = EmotionEntry(
                        user_id=metadata["user_id"],
                        timestamp=metadata["timestamp"],
                        transcript=metadata["transcript"],
                        mood=metadata["mood"],
                        summary=metadata["summary"],
                        reflection=metadata["reflection"],
                        confidence=metadata.get("confidence", 0.8)
                    )
                    entries.append(entry)
                
                # Sort by timestamp (newest first)
                entries.sort(key=lambda x: x.timestamp, reverse=True)
                
            else:
                # Query memory storage
                cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
                entries = []
                
                for entry_data in self.memory_storage:
                    if (entry_data["user_id"] == user_id and 
                        entry_data["timestamp"] >= cutoff_date):
                        entry = EmotionEntry(**entry_data)
                        entries.append(entry)
                
                # Sort by timestamp (newest first)
                entries.sort(key=lambda x: x.timestamp, reverse=True)
            
            logger.info(f"Retrieved {len(entries)} entries for user {user_id}")
            return entries
            
        except Exception as e:
            logger.error(f"Error retrieving user history: {str(e)}")
            return []
    
    async def get_mood_statistics(self, user_id: str, days: int = 30) -> Dict[str, Any]:
        """
        Get mood statistics for a user
        """
        try:
            entries = await self.get_user_history(user_id, days)
            
            if not entries:
                return {
                    "total_entries": 0,
                    "mood_distribution": {},
                    "average_confidence": 0.0,
                    "most_common_mood": None
                }
            
            # Calculate mood distribution
            mood_counts = {}
            total_confidence = 0.0
            
            for entry in entries:
                mood = entry.mood.lower()
                mood_counts[mood] = mood_counts.get(mood, 0) + 1
                total_confidence += entry.confidence
            
            # Find most common mood
            most_common_mood = max(mood_counts.items(), key=lambda x: x[1])[0] if mood_counts else None
            
            return {
                "total_entries": len(entries),
                "mood_distribution": mood_counts,
                "average_confidence": total_confidence / len(entries),
                "most_common_mood": most_common_mood
            }
            
        except Exception as e:
            logger.error(f"Error calculating mood statistics: {str(e)}")
            return {
                "total_entries": 0,
                "mood_distribution": {},
                "average_confidence": 0.0,
                "most_common_mood": None
            }
    
    def _create_simple_embedding(self, text: str) -> List[float]:
        """
        Create a simple embedding vector for text
        Note: In production, use OpenAI's embedding API for better results
        """
        # Simple hash-based embedding (for demo purposes)
        import hashlib
        
        # Create a hash of the text
        hash_obj = hashlib.md5(text.encode())
        hash_hex = hash_obj.hexdigest()
        
        # Convert hash to 1536-dimensional vector
        vector = []
        for i in range(0, len(hash_hex), 2):
            # Convert hex pairs to float values
            hex_pair = hash_hex[i:i+2]
            value = int(hex_pair, 16) / 255.0  # Normalize to [0, 1]
            vector.append(value)
        
        # Pad or truncate to 1536 dimensions
        while len(vector) < 1536:
            vector.extend(vector[:min(len(vector), 1536 - len(vector))])
        
        return vector[:1536]
    
    async def delete_user_data(self, user_id: str) -> bool:
        """
        Delete all data for a specific user
        """
        try:
            if self.pinecone_available:
                # Delete from Pinecone
                self.index.delete(
                    filter={"user_id": {"$eq": user_id}}
                )
                logger.info(f"Deleted all data for user {user_id}")
            else:
                # Delete from memory
                self.memory_storage = [
                    entry for entry in self.memory_storage 
                    if entry["user_id"] != user_id
                ]
                logger.info(f"Deleted all data for user {user_id} from memory")
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting user data: {str(e)}")
            return False 