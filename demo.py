#!/usr/bin/env python3
"""
MindMirror Demo Script
This script demonstrates the core functionality of MindMirror
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"🎯 {title}")
    print("="*60)

def print_section(title):
    """Print a formatted section"""
    print(f"\n📋 {title}")
    print("-" * 40)

def demo_reflection_generation():
    """Demonstrate reflection generation"""
    print_section("Generating Personalized Reflections")
    
    moods = ["anxious", "happy", "stressed", "peaceful"]
    focus_areas = ["work", "relationships", "self-care", "personal growth"]
    
    for i, mood in enumerate(moods):
        focus = focus_areas[i % len(focus_areas)]
        print(f"\n🎭 Mood: {mood.title()}")
        print(f"🎯 Focus: {focus.title()}")
        
        try:
            response = requests.post(f"{BASE_URL}/api/reflection", json={
                "current_mood": mood,
                "focus_area": focus,
                "recent_entries": []
            })
            
            if response.status_code == 200:
                reflection = response.json().get("reflection", "No reflection generated")
                print(f"💭 Reflection: {reflection}")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Connection error: {e}")
        
        time.sleep(1)  # Be nice to the API

def demo_emotional_trends():
    """Demonstrate emotional trend analysis"""
    print_section("Analyzing Emotional Trends")
    
    try:
        response = requests.get(f"{BASE_URL}/api/trends/default_user?days=30")
        
        if response.status_code == 200:
            data = response.json()
            trends = data.get("trends", {})
            insights = data.get("insights", [])
            
            print(f"📊 Overall Trend: {trends.get('overall_trend', 'neutral').title()}")
            print(f"📈 Total Entries: {trends.get('total_entries', 0)}")
            
            mood_dist = trends.get("mood_distribution", {})
            if mood_dist:
                print("\n🎭 Mood Distribution:")
                for mood, count in mood_dist.items():
                    print(f"   • {mood.title()}: {count} times")
            
            if insights:
                print("\n💡 Insights:")
                for insight in insights:
                    print(f"   • {insight}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

def demo_api_endpoints():
    """Demonstrate all API endpoints"""
    print_section("Testing API Endpoints")
    
    endpoints = [
        ("Health Check", "GET", "/"),
        ("History", "GET", "/api/history/default_user?days=7"),
        ("Trends", "GET", "/api/trends/default_user?days=30"),
    ]
    
    for name, method, endpoint in endpoints:
        print(f"\n🔍 Testing {name}...")
        try:
            if method == "GET":
                response = requests.get(f"{BASE_URL}{endpoint}")
            else:
                response = requests.post(f"{BASE_URL}{endpoint}")
            
            if response.status_code == 200:
                print(f"✅ {name} - OK")
                if name == "Health Check":
                    data = response.json()
                    print(f"   Status: {data.get('status', 'unknown')}")
            else:
                print(f"❌ {name} - Error {response.status_code}")
                
        except Exception as e:
            print(f"❌ {name} - Connection error: {e}")

def show_feature_highlights():
    """Show feature highlights"""
    print_section("MindMirror Features")
    
    features = [
        ("🎙️ Voice-to-Text", "Record your thoughts naturally using your voice"),
        ("🧠 Emotion Analysis", "AI detects your emotional state and provides insights"),
        ("🪞 Mental State Summary", "Get a gentle summary of your current mental state"),
        ("💬 Personalized Reflections", "Receive custom reflection prompts for deeper self-discovery"),
        ("📈 Trend Tracking", "Track your emotional patterns over time"),
        ("🔒 Privacy-First", "Your data stays private and secure"),
        ("🎨 Beautiful UI", "Calming design with soothing gradients and animations"),
    ]
    
    for icon_title, description in features:
        print(f"{icon_title}: {description}")

def show_usage_scenarios():
    """Show usage scenarios"""
    print_section("How to Use MindMirror")
    
    scenarios = [
        ("🌅 Morning Reflection", "Start your day by sharing your thoughts and getting a positive reflection"),
        ("😰 Stress Relief", "When feeling overwhelmed, record your concerns and get calming insights"),
        ("🎉 Celebration", "Share your joys and get prompts to deepen your gratitude"),
        ("🤔 Decision Making", "Talk through a decision and get perspective on your thought process"),
        ("📊 Weekly Review", "Check your emotional trends and patterns over time"),
    ]
    
    for scenario, description in scenarios:
        print(f"{scenario}: {description}")

def main():
    """Run the demo"""
    print_header("MindMirror AI Emotional Companion Demo")
    
    print("🪞 Welcome to MindMirror - Your AI Emotional Companion!")
    print("This demo shows how MindMirror can help you reflect and grow emotionally.")
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code != 200:
            print("\n❌ Backend server is not responding properly!")
            print("   Please make sure the backend is running:")
            print("   cd backend && python app.py")
            return
    except:
        print("\n❌ Backend server is not running!")
        print("   Please start the backend server first:")
        print("   cd backend && python app.py")
        return
    
    show_feature_highlights()
    show_usage_scenarios()
    demo_api_endpoints()
    demo_reflection_generation()
    demo_emotional_trends()
    
    print_header("Demo Complete!")
    print("🎉 You've seen MindMirror in action!")
    print("\n🚀 To try it yourself:")
    print("   1. Open http://localhost:3000 in your browser")
    print("   2. Allow microphone permissions")
    print("   3. Start recording your thoughts")
    print("   4. Experience the magic of AI-powered emotional reflection!")
    
    print("\n💡 Tips for the best experience:")
    print("   • Speak naturally and from the heart")
    print("   • Be honest about your emotions")
    print("   • Take time to reflect on the prompts")
    print("   • Check your emotional trends regularly")
    
    print("\n🌟 Happy reflecting!")

if __name__ == "__main__":
    main() 