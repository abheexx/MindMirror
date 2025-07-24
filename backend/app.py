from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import json
import base64
import tempfile
from datetime import datetime, timedelta
from typing import Optional, List
import logging
from dotenv import load_dotenv

from services.openai_service import OpenAIService
from services.pinecone_service import PineconeService
from models.schemas import (
    VoiceAnalysisRequest,
    VoiceAnalysisResponse,
    EmotionEntry,
    ReflectionRequest,
    ReflectionResponse,
    UserHistory
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MindMirror API",
    description="AI Emotional Companion for Voice-Based Reflection",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
try:
    openai_service = OpenAIService()
    pinecone_service = PineconeService()
except Exception as e:
    print(f"Warning: Service initialization failed: {e}")
    print("Running in demo mode without OpenAI/Pinecone")
    openai_service = None
    pinecone_service = None

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "MindMirror API is running", "status": "healthy"}

@app.post("/api/analyze", response_model=VoiceAnalysisResponse)
async def analyze_voice(
    audio_file: UploadFile = File(...),
    user_id: str = Form("default_user")
):
    """
    Analyze voice input and generate emotional insights
    """
    try:
        # Validate audio file
        if not audio_file.filename.endswith(('.wav', '.mp3', '.m4a', '.webm')):
            raise HTTPException(status_code=400, detail="Invalid audio format")
        
        # Save audio file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.filename.split('.')[-1]}") as temp_file:
            content = await audio_file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            if openai_service is None:
                # Demo mode - return mock data
                transcript = "This is a demo transcript. Please add your OpenAI API key for real voice analysis."
                analysis = {
                    "mood": "neutral",
                    "summary": "This is a demo response. Add your OpenAI API key to get real emotional analysis.",
                    "reflection": "What would you like to explore about your thoughts today?",
                    "confidence": 0.5
                }
            else:
                # Transcribe audio using Whisper
                transcript = await openai_service.transcribe_audio(temp_file_path)
                
                # Analyze emotion and generate reflection
                analysis = await openai_service.analyze_emotion_and_reflect(transcript)
            
            # Create emotion entry
            emotion_entry = EmotionEntry(
                user_id=user_id,
                timestamp=datetime.now().isoformat(),
                transcript=transcript,
                mood=analysis["mood"],
                summary=analysis["summary"],
                reflection=analysis["reflection"],
                confidence=analysis.get("confidence", 0.8)
            )
            
            # Store in Pinecone for memory
            if pinecone_service:
                await pinecone_service.store_emotion_entry(emotion_entry)
            
            return VoiceAnalysisResponse(
                success=True,
                transcript=transcript,
                mood=analysis["mood"],
                summary=analysis["summary"],
                reflection=analysis["reflection"],
                timestamp=emotion_entry.timestamp
            )
            
        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)
            
    except Exception as e:
        logger.error(f"Error analyzing voice: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/api/history/{user_id}", response_model=UserHistory)
async def get_user_history(
    user_id: str,
    days: int = 7
):
    """
    Retrieve user's emotional history and trends
    """
    try:
        # Get entries from Pinecone
        if pinecone_service:
            entries = await pinecone_service.get_user_history(user_id, days)
        else:
            entries = []
        
        # Calculate trends
        trends = calculate_emotional_trends(entries)
        
        return UserHistory(
            user_id=user_id,
            entries=entries,
            trends=trends,
            total_entries=len(entries)
        )
        
    except Exception as e:
        logger.error(f"Error retrieving history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve history: {str(e)}")

@app.post("/api/reflection", response_model=ReflectionResponse)
async def generate_reflection(request: ReflectionRequest):
    """
    Generate a personalized reflection prompt based on user's emotional state
    """
    try:
        if openai_service is None:
            # Demo mode - return mock reflection
            reflection = f"Demo reflection for {request.current_mood} mood. Add your OpenAI API key for personalized reflections."
        else:
            reflection = await openai_service.generate_reflection_prompt(
                request.current_mood,
                request.recent_entries,
                request.focus_area
            )
        
        return ReflectionResponse(
            success=True,
            reflection=reflection,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Error generating reflection: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to generate reflection: {str(e)}")

@app.get("/api/trends/{user_id}")
async def get_emotional_trends(user_id: str, days: int = 30):
    """
    Get detailed emotional trends and insights
    """
    try:
        entries = await pinecone_service.get_user_history(user_id, days)
        trends = calculate_emotional_trends(entries)
        
        return {
            "user_id": user_id,
            "period_days": days,
            "trends": trends,
            "insights": generate_trend_insights(trends)
        }
        
    except Exception as e:
        logger.error(f"Error calculating trends: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to calculate trends: {str(e)}")

def calculate_emotional_trends(entries: List[EmotionEntry]) -> dict:
    """Calculate emotional trends from user entries"""
    if not entries:
        return {"mood_distribution": {}, "weekly_patterns": {}, "overall_trend": "neutral"}
    
    # Mood distribution
    mood_counts = {}
    for entry in entries:
        mood = entry.mood.lower()
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    
    # Weekly patterns (simplified)
    weekly_patterns = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
    
    for entry in entries:
        date = datetime.fromisoformat(entry.timestamp)
        day_name = date.strftime("%A").lower()
        if day_name in weekly_patterns:
            weekly_patterns[day_name].append(entry.mood)
    
    # Overall trend (simplified sentiment analysis)
    positive_moods = ["happy", "joyful", "excited", "content", "peaceful"]
    negative_moods = ["sad", "anxious", "stressed", "angry", "frustrated"]
    
    positive_count = sum(mood_counts.get(mood, 0) for mood in positive_moods)
    negative_count = sum(mood_counts.get(mood, 0) for mood in negative_moods)
    
    if positive_count > negative_count:
        overall_trend = "positive"
    elif negative_count > positive_count:
        overall_trend = "negative"
    else:
        overall_trend = "neutral"
    
    return {
        "mood_distribution": mood_counts,
        "weekly_patterns": weekly_patterns,
        "overall_trend": overall_trend,
        "total_entries": len(entries)
    }

def generate_trend_insights(trends: dict) -> List[str]:
    """Generate insights from emotional trends"""
    insights = []
    
    mood_dist = trends.get("mood_distribution", {})
    overall_trend = trends.get("overall_trend", "neutral")
    
    if mood_dist:
        most_common_mood = max(mood_dist.items(), key=lambda x: x[1])
        insights.append(f"Your most frequent mood has been '{most_common_mood[0]}' ({most_common_mood[1]} times)")
    
    if overall_trend == "positive":
        insights.append("You've been experiencing more positive emotions lately")
    elif overall_trend == "negative":
        insights.append("You've been experiencing more challenging emotions lately")
    
    total_entries = trends.get("total_entries", 0)
    if total_entries >= 7:
        insights.append(f"You've been consistent with {total_entries} reflection sessions")
    
    return insights

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "True").lower() == "true"
    ) 