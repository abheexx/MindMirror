#!/bin/bash

echo "🚀 Starting MindMirror - AI Emotional Companion"
echo "================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Prerequisites check passed!"

# Setup backend
echo ""
echo "🔧 Setting up backend..."
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Please create one based on env.example"
    echo "   You'll need to add your OpenAI API key at minimum."
    echo "   Copy env.example to .env and edit it with your API keys."
    exit 1
fi

# Start backend in background
echo "🚀 Starting backend server..."
python app.py &
BACKEND_PID=$!

cd ..

# Setup frontend
echo ""
echo "🔧 Setting up frontend..."
cd frontend

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Start frontend
echo "🚀 Starting frontend development server..."
npm start &
FRONTEND_PID=$!

cd ..

echo ""
echo "🎉 MindMirror is starting up!"
echo "================================================"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "💡 Make sure you have:"
echo "   - OpenAI API key in backend/.env"
echo "   - Microphone permissions enabled in your browser"
echo ""
echo "🛑 To stop the servers, press Ctrl+C"

# Wait for user to stop
trap "echo ''; echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait 