import os
import json
import logging
from typing import Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        """Initialize OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "your_openai_api_key_here":
            raise ValueError("OPENAI_API_KEY environment variable is required. Please add your OpenAI API key to the .env file.")
        
        self.client = OpenAI(api_key=api_key)
        
    async def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Transcribe audio file using OpenAI Whisper API
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            
            logger.info(f"Successfully transcribed audio: {len(transcript)} characters")
            return transcript
            
        except Exception as e:
            logger.error(f"Error transcribing audio: {str(e)}")
            raise Exception(f"Transcription failed: {str(e)}")
    
    async def analyze_emotion_and_reflect(self, transcript: str) -> Dict[str, Any]:
        """
        Analyze emotional tone and generate reflection using GPT-4
        """
        try:
            # System prompt for emotion analysis and reflection
            system_prompt = """You are a compassionate AI journal guide. Your job is to analyze the user's tone and generate a calm, encouraging summary + one custom reflection question.

Analyze the emotional content and provide:
1. A single word mood (e.g., anxious, joyful, confused, peaceful, stressed, excited, sad, content)
2. A gentle summary of their mental state
3. One thoughtful reflection question to encourage deeper self-discovery

Keep responses warm, supportive, and non-judgmental. Focus on emotional awareness and growth."""

            user_prompt = f"Here is the user's thought dump transcript: {transcript}"

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            # Parse the response
            content = response.choices[0].message.content.strip()
            
            # Extract mood, summary, and reflection from the response
            analysis = self._parse_analysis_response(content)
            
            logger.info(f"Successfully analyzed emotion: {analysis['mood']}")
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing emotion: {str(e)}")
            # Fallback response
            return {
                "mood": "neutral",
                "summary": "I heard your thoughts. Thank you for sharing.",
                "reflection": "What's one thing you'd like to explore further about your day?",
                "confidence": 0.5
            }
    
    async def generate_reflection_prompt(
        self, 
        current_mood: str, 
        recent_entries: Optional[list] = None,
        focus_area: Optional[str] = None
    ) -> str:
        """
        Generate a personalized reflection prompt based on current mood and history
        """
        try:
            system_prompt = """You are a thoughtful AI companion helping users reflect on their emotional journey. Generate one gentle, open-ended reflection question that encourages self-discovery and emotional awareness.

The question should be:
- Personalized to their current emotional state
- Non-judgmental and supportive
- Open-ended to encourage deeper thinking
- Focused on growth and self-understanding"""

            # Build context from recent entries
            context = f"Current mood: {current_mood}"
            if recent_entries:
                recent_moods = [entry.get('mood', 'neutral') for entry in recent_entries[-3:]]
                context += f"\nRecent moods: {', '.join(recent_moods)}"
            
            if focus_area:
                context += f"\nFocus area: {focus_area}"

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context}
                ],
                temperature=0.8,
                max_tokens=150
            )
            
            reflection = response.choices[0].message.content.strip()
            logger.info(f"Generated reflection prompt: {reflection}")
            return reflection
            
        except Exception as e:
            logger.error(f"Error generating reflection: {str(e)}")
            return "What's one thing you'd like to explore about your emotional state today?"
    
    def _parse_analysis_response(self, content: str) -> Dict[str, Any]:
        """
        Parse the GPT response to extract mood, summary, and reflection
        """
        try:
            # Try to find structured response patterns
            lines = content.split('\n')
            mood = "neutral"
            summary = ""
            reflection = ""
            
            for line in lines:
                line = line.strip()
                if line.lower().startswith('mood:'):
                    mood = line.split(':', 1)[1].strip().lower()
                elif line.lower().startswith('summary:'):
                    summary = line.split(':', 1)[1].strip()
                elif line.lower().startswith('reflection:'):
                    reflection = line.split(':', 1)[1].strip()
            
            # If structured parsing failed, try to extract from free text
            if not summary or not reflection:
                # Split content into parts
                parts = content.split('\n\n')
                if len(parts) >= 2:
                    summary = parts[0].strip()
                    reflection = parts[1].strip()
                else:
                    # Fallback: use the entire content as summary
                    summary = content.strip()
                    reflection = "What would you like to explore further about your thoughts?"
            
            # Clean up mood (extract first word if multiple words)
            mood = mood.split()[0] if mood else "neutral"
            
            return {
                "mood": mood,
                "summary": summary,
                "reflection": reflection,
                "confidence": 0.8
            }
            
        except Exception as e:
            logger.error(f"Error parsing analysis response: {str(e)}")
            return {
                "mood": "neutral",
                "summary": "I heard your thoughts. Thank you for sharing.",
                "reflection": "What's one thing you'd like to explore further about your day?",
                "confidence": 0.5
            } 