from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class VoiceAnalysisRequest(BaseModel):
    """Request model for voice analysis"""
    user_id: str = Field(..., description="User identifier")
    audio_data: Optional[str] = Field(None, description="Base64 encoded audio data")

class VoiceAnalysisResponse(BaseModel):
    """Response model for voice analysis"""
    success: bool = Field(..., description="Whether the analysis was successful")
    transcript: str = Field(..., description="Transcribed text from voice input")
    mood: str = Field(..., description="Detected emotional mood")
    summary: str = Field(..., description="AI-generated summary of mental state")
    reflection: str = Field(..., description="Personalized reflection prompt")
    timestamp: str = Field(..., description="ISO timestamp of the analysis")
    confidence: Optional[float] = Field(0.8, description="Confidence score of the analysis")

class EmotionEntry(BaseModel):
    """Model for storing emotional entries"""
    user_id: str = Field(..., description="User identifier")
    timestamp: str = Field(..., description="ISO timestamp of the entry")
    transcript: str = Field(..., description="Original voice transcript")
    mood: str = Field(..., description="Detected emotional mood")
    summary: str = Field(..., description="AI-generated summary")
    reflection: str = Field(..., description="Reflection prompt provided")
    confidence: float = Field(0.8, description="Confidence score")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

class ReflectionRequest(BaseModel):
    """Request model for generating reflection prompts"""
    current_mood: str = Field(..., description="Current emotional state")
    recent_entries: Optional[List[EmotionEntry]] = Field(default_factory=list, description="Recent emotional entries")
    focus_area: Optional[str] = Field(None, description="Specific area to focus reflection on")

class ReflectionResponse(BaseModel):
    """Response model for reflection generation"""
    success: bool = Field(..., description="Whether the reflection was generated successfully")
    reflection: str = Field(..., description="Generated reflection prompt")
    timestamp: str = Field(..., description="ISO timestamp of the response")

class UserHistory(BaseModel):
    """Model for user's emotional history"""
    user_id: str = Field(..., description="User identifier")
    entries: List[EmotionEntry] = Field(default_factory=list, description="List of emotional entries")
    trends: Dict[str, Any] = Field(default_factory=dict, description="Calculated emotional trends")
    total_entries: int = Field(0, description="Total number of entries")

class EmotionalTrends(BaseModel):
    """Model for emotional trend analysis"""
    mood_distribution: Dict[str, int] = Field(default_factory=dict, description="Distribution of moods over time")
    weekly_patterns: Dict[str, List[str]] = Field(default_factory=dict, description="Mood patterns by day of week")
    overall_trend: str = Field("neutral", description="Overall emotional trend (positive/negative/neutral)")
    total_entries: int = Field(0, description="Total number of entries analyzed")

class HealthCheck(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Current timestamp")
    version: str = Field(..., description="API version")

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    timestamp: str = Field(..., description="Error timestamp") 