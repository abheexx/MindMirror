# 🚀 MindMirror Setup Guide

This guide will help you set up MindMirror, your AI emotional companion, on your local machine.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 16+** - [Download here](https://nodejs.org/)
- **npm** - Usually comes with Node.js
- **OpenAI API Key** - [Get one here](https://platform.openai.com/api-keys)
- **Pinecone API Key** (Optional) - [Get one here](https://www.pinecone.io/)

## 🔧 Quick Start (Recommended)

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd MindMirror
   ```

2. **Run the startup script**:
   ```bash
   ./start.sh
   ```

   This script will:
   - Check prerequisites
   - Set up Python virtual environment
   - Install dependencies
   - Start both backend and frontend servers

3. **Configure your API keys**:
   - Copy `backend/env.example` to `backend/.env`
   - Add your OpenAI API key (required)
   - Add your Pinecone credentials (optional)

4. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🔧 Manual Setup

If you prefer to set up manually or the startup script doesn't work:

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

5. **Start the backend server**:
   ```bash
   python app.py
   ```

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

## 🔑 API Configuration

### Required: OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add it to `backend/.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Optional: Pinecone (for persistent memory)

1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create a new project and index
3. Get your API key and environment
4. Add to `backend/.env`:
   ```
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_ENVIRONMENT=your_environment_here
   PINECONE_INDEX_NAME=mindmirror-emotions
   ```

## 🧪 Testing the Setup

1. **Test the backend API**:
   ```bash
   cd backend
   python test_api.py
   ```

2. **Test voice recording**:
   - Open http://localhost:3000
   - Allow microphone permissions
   - Try recording a short message
   - Check if analysis works

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check if Python 3.8+ is installed: `python3 --version`
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Check if port 8000 is available

**Frontend won't start:**
- Check if Node.js 16+ is installed: `node --version`
- Ensure all dependencies are installed: `npm list`
- Check if port 3000 is available

**Voice recording doesn't work:**
- Ensure microphone permissions are granted in browser
- Try refreshing the page
- Check browser console for errors

**API calls fail:**
- Verify OpenAI API key is correct
- Check if backend server is running
- Ensure CORS is properly configured

**Pinecone errors:**
- Verify Pinecone credentials are correct
- Check if index exists and is properly configured
- The app will work without Pinecone (uses in-memory storage)

### Getting Help

1. Check the browser console for JavaScript errors
2. Check the backend terminal for Python errors
3. Verify all environment variables are set correctly
4. Ensure all ports are available and not blocked by firewall

## 📱 Usage

Once everything is set up:

1. **Record your thoughts**: Click the microphone button and speak freely
2. **Get AI insights**: Receive emotional analysis and personalized reflections
3. **Track your journey**: View your emotional history and trends
4. **Generate reflections**: Get custom reflection prompts based on your mood

## 🔒 Privacy & Security

- All voice data is processed through OpenAI's Whisper API
- Emotional analysis is done through OpenAI's GPT-4
- Data is stored locally or in your Pinecone instance
- No data is shared with third parties beyond OpenAI/Pinecone

## 🚀 Deployment

For production deployment:

1. **Backend**: Deploy to services like Heroku, Railway, or AWS
2. **Frontend**: Build with `npm run build` and deploy to Vercel, Netlify, or similar
3. **Database**: Use Pinecone for production data storage
4. **Environment**: Set production environment variables

## 📈 Next Steps

- Set up scheduled reminders for daily reflection
- Add user authentication
- Implement more advanced analytics
- Add export functionality for your data
- Integrate with other wellness apps

---

Happy reflecting! 🌟 