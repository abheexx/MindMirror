# MindMirror

An AI-powered emotional reflection and mental wellness companion that helps users process their thoughts through voice analysis and personalized insights.

## Overview

MindMirror is a full-stack web application that combines voice-to-text transcription, emotion analysis, and AI-powered reflection prompts to support users in their mental wellness journey. The application provides a safe space for users to speak freely about their day while receiving gentle, personalized insights and reflection questions.

## Features

- **Voice Recording**: Real-time audio recording with playback functionality
- **Emotion Analysis**: AI-powered sentiment analysis to detect emotional states
- **Personalized Insights**: Contextual summaries of user's mental state
- **Reflection Prompts**: AI-generated questions to encourage deeper self-reflection
- **Historical Tracking**: Store and analyze emotional patterns over time
- **Trend Analysis**: Visual representation of emotional trends and patterns
- **Responsive Design**: Clean, minimalist interface optimized for all devices

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **AI Services**: OpenAI GPT-4 for text analysis and reflection generation
- **Audio Processing**: OpenAI Whisper API for voice-to-text transcription
- **Database**: Pinecone for vector storage of emotional history
- **Authentication**: JWT-based user authentication
- **API Documentation**: Auto-generated with FastAPI

### Frontend
- **Framework**: React 18 with TypeScript
- **Styling**: Tailwind CSS with custom design system
- **Animations**: Framer Motion for smooth user interactions
- **Charts**: Recharts for data visualization
- **HTTP Client**: Axios for API communication
- **Routing**: React Router DOM for navigation

## Architecture

The application follows a modern microservices architecture with clear separation of concerns:

```
MindMirror/
├── backend/                 # FastAPI server
│   ├── app.py              # Main application entry point
│   ├── models/             # Pydantic data models
│   ├── services/           # Business logic services
│   └── requirements.txt    # Python dependencies
├── frontend/               # React application
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.tsx         # Main application component
│   │   └── index.css       # Global styles
│   └── package.json        # Node.js dependencies
└── README.md               # Project documentation
```

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key
- Pinecone API credentials (optional for demo mode)

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# Edit .env with your API keys
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Environment Variables
Create a `.env` file in the backend directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_INDEX_NAME=mindmirror-emotions
```

## API Endpoints

### Core Endpoints
- `POST /api/analyze` - Analyze voice recording and generate insights
- `POST /api/reflection` - Generate personalized reflection prompts
- `GET /api/history/{user_id}` - Retrieve user's emotional history
- `GET /api/trends/{user_id}` - Get emotional trend analysis

### Health Check
- `GET /` - Application health status

## Usage

1. **Voice Recording**: Click the microphone button to start recording your thoughts
2. **Playback**: Listen to your recording before analysis
3. **Analysis**: Submit for AI-powered emotion analysis and insights
4. **Reflection**: Review personalized reflection prompts
5. **History**: Track your emotional patterns over time

## Development

### Code Style
- Python: Follow PEP 8 guidelines
- TypeScript: Use strict mode and ESLint configuration
- CSS: Follow Tailwind CSS utility-first approach

### Testing
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Deployment

#### Backend Deployment
- **Platform**: Heroku, Railway, or AWS
- **Requirements**: Python 3.8+, environment variables
- **Database**: Pinecone for production, in-memory for development

#### Frontend Deployment
- **Platform**: Vercel, Netlify, or GitHub Pages
- **Build**: `npm run build`
- **Environment**: Production-optimized React build

## Security Considerations

- API keys are stored securely in environment variables
- User data is anonymized and encrypted in storage
- HTTPS is required for all production deployments
- Input validation and sanitization on all endpoints

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository or contact the development team.

## Roadmap

- [ ] User authentication and profiles
- [ ] Advanced emotion tracking with biometric data
- [ ] Integration with calendar and scheduling apps
- [ ] Mobile application development
- [ ] Multi-language support
- [ ] Advanced analytics and reporting 