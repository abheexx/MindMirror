#!/usr/bin/env python3
"""
Simple test script for MindMirror API
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")

def test_reflection_generation():
    """Test reflection generation endpoint"""
    print("\n🔍 Testing reflection generation...")
    try:
        data = {
            "current_mood": "anxious",
            "focus_area": "stress management",
            "recent_entries": []
        }
        response = requests.post(f"{BASE_URL}/api/reflection", json=data)
        if response.status_code == 200:
            print("✅ Reflection generation passed")
            result = response.json()
            print(f"   Reflection: {result.get('reflection', 'N/A')}")
        else:
            print(f"❌ Reflection generation failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Reflection generation error: {e}")

def test_history_endpoint():
    """Test history endpoint"""
    print("\n🔍 Testing history endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/history/default_user?days=7")
        if response.status_code == 200:
            print("✅ History endpoint passed")
            result = response.json()
            print(f"   Total entries: {result.get('total_entries', 0)}")
        else:
            print(f"❌ History endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ History endpoint error: {e}")

def test_trends_endpoint():
    """Test trends endpoint"""
    print("\n🔍 Testing trends endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/trends/default_user?days=30")
        if response.status_code == 200:
            print("✅ Trends endpoint passed")
            result = response.json()
            print(f"   Overall trend: {result.get('trends', {}).get('overall_trend', 'N/A')}")
        else:
            print(f"❌ Trends endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Trends endpoint error: {e}")

def main():
    """Run all tests"""
    print("🧪 MindMirror API Test Suite")
    print("=" * 40)
    
    # Check if server is running
    try:
        requests.get(f"{BASE_URL}/", timeout=5)
    except:
        print("❌ Backend server is not running!")
        print("   Please start the backend server first:")
        print("   cd backend && python app.py")
        return
    
    test_health_check()
    test_reflection_generation()
    test_history_endpoint()
    test_trends_endpoint()
    
    print("\n🎉 Test suite completed!")

if __name__ == "__main__":
    main() 