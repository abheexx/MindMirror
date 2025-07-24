import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Mic, MicOff, Play, Pause, RotateCcw, Send } from 'lucide-react';
import axios from 'axios';

interface AnalysisResult {
  transcript: string;
  mood: string;
  summary: string;
  reflection: string;
  timestamp: string;
}

const VoiceRecorder: React.FC = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    // Request microphone permissions on component mount
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(() => console.log('Microphone permission granted'))
      .catch(err => console.error('Microphone permission denied:', err));
  }, []);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' });
        setAudioBlob(audioBlob);
        const url = URL.createObjectURL(audioBlob);
        setAudioUrl(url);
      };

      mediaRecorder.start();
      setIsRecording(true);
      setError(null);
    } catch (err) {
      setError('Failed to start recording. Please check microphone permissions.');
      console.error('Recording error:', err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop());
      setIsRecording(false);
    }
  };

  const playRecording = () => {
    if (audioRef.current && audioUrl) {
      audioRef.current.play();
      setIsPlaying(true);
    }
  };

  const pauseRecording = () => {
    if (audioRef.current) {
      audioRef.current.pause();
      setIsPlaying(false);
    }
  };

  const resetRecording = () => {
    setAudioBlob(null);
    setAudioUrl(null);
    setAnalysisResult(null);
    setError(null);
    if (audioRef.current) {
      audioRef.current.pause();
      setIsPlaying(false);
    }
  };

  const analyzeVoice = async () => {
    if (!audioBlob) return;

    setIsAnalyzing(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('audio_file', audioBlob, 'recording.wav');
      formData.append('user_id', 'default_user');

      const response = await axios.post('/api/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setAnalysisResult(response.data);
    } catch (err) {
      setError('Failed to analyze voice. Please try again.');
      console.error('Analysis error:', err);
    } finally {
      setIsAnalyzing(false);
    }
  };

  const getMoodColor = (mood: string) => {
    const moodColors: { [key: string]: string } = {
      happy: 'mood-happy',
      sad: 'mood-sad',
      anxious: 'mood-anxious',
      excited: 'mood-excited',
      peaceful: 'mood-peaceful',
      stressed: 'mood-stressed',
      neutral: 'mood-neutral',
    };
    return moodColors[mood.toLowerCase()] || moodColors.neutral;
  };

  return (
    <div className="max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="card-modern p-12"
      >
        <div className="text-center mb-12">
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="inline-block mb-6"
          >
            <div className="text-5xl mb-4">🎙️</div>
          </motion.div>
          
          <h2 className="text-5xl font-handwriting font-bold text-gradient-modern mb-6">
            Share Your Thoughts
          </h2>
          
          <p className="text-xl text-dark max-w-2xl mx-auto leading-relaxed font-medium">
            Speak freely about your day. I'm here to listen with care and help you discover insights about yourself.
          </p>
        </div>

        {/* Recording Controls */}
        <div className="flex flex-col items-center gap-8 mb-12">
          {!audioBlob ? (
            <motion.div
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              transition={{ duration: 0.5, delay: 0.4 }}
            >
              <button
                onClick={isRecording ? stopRecording : startRecording}
                className={`mic-button ${isRecording ? 'recording' : ''}`}
              >
                {isRecording ? <MicOff size={32} /> : <Mic size={32} />}
              </button>
            </motion.div>
          ) : (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="flex gap-4"
            >
              <button
                onClick={isPlaying ? pauseRecording : playRecording}
                className="btn-primary-modern flex items-center gap-2"
              >
                {isPlaying ? <Pause size={20} /> : <Play size={20} />}
                {isPlaying ? 'Pause' : 'Play'}
              </button>
              
              <button
                onClick={resetRecording}
                className="btn-secondary-modern flex items-center gap-2"
              >
                <RotateCcw size={20} />
                Reset
              </button>
            </motion.div>
          )}
        </div>

        {/* Recording Status */}
        {isRecording && (
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="text-center mb-8"
          >
            <div className="inline-flex items-center gap-3 text-red-500 bg-red-50 px-6 py-3 rounded-full">
              <div className="w-3 h-3 bg-red-500 rounded-full animate-pulse"></div>
              <span className="font-medium">Recording... Click to stop</span>
            </div>
          </motion.div>
        )}

        {/* Audio Player */}
        {audioUrl && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-8"
          >
            <div className="bg-gray-50 rounded-2xl p-6">
              <h3 className="text-xl font-handwriting font-semibold text-dark mb-4">Your Recording</h3>
              <audio
                ref={audioRef}
                src={audioUrl}
                onEnded={() => setIsPlaying(false)}
                className="w-full"
                controls
              />
            </div>
          </motion.div>
        )}

        {/* Analyze Button */}
        {audioBlob && !analysisResult && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center mb-8"
          >
            <button
              onClick={analyzeVoice}
              disabled={isAnalyzing}
              className="btn-primary-modern disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-3 mx-auto"
            >
              {isAnalyzing ? (
                <>
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  <span>Analyzing your thoughts...</span>
                </>
              ) : (
                <>
                  <Send size={20} />
                  <span>Discover Insights</span>
                </>
              )}
            </button>
          </motion.div>
        )}

        {/* Error Message */}
        <AnimatePresence>
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6"
            >
              {error}
            </motion.div>
          )}
        </AnimatePresence>

        {/* Analysis Results */}
        <AnimatePresence>
          {analysisResult && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="space-y-6"
            >
              <div className="border-t border-gray-200 pt-6">
                <h3 className="text-3xl font-handwriting font-bold text-gradient-modern mb-6">
                  Your Reflection
                </h3>
                
                {/* Transcript */}
                <div className="mb-8">
                  <h4 className="text-xl font-handwriting font-semibold text-dark mb-3">
                    What you shared:
                  </h4>
                  <div className="bg-blue-50 p-6 rounded-2xl border-2 border-blue-100">
                    <p className="text-dark italic text-lg leading-relaxed">"{analysisResult.transcript}"</p>
                  </div>
                </div>

                {/* Mood */}
                <div className="mb-8">
                  <h4 className="text-xl font-handwriting font-semibold text-dark mb-3">
                    Your emotional state:
                  </h4>
                  <span className={`mood-badge-modern ${getMoodColor(analysisResult.mood)}`}>
                    {analysisResult.mood}
                  </span>
                </div>

                {/* Summary */}
                <div className="mb-8">
                  <h4 className="text-xl font-handwriting font-semibold text-dark mb-3">
                    MindMirror's insight:
                  </h4>
                  <div className="bg-gradient-to-r from-purple-50 to-indigo-50 p-6 rounded-2xl border-2 border-purple-100">
                    <p className="text-dark text-lg leading-relaxed">{analysisResult.summary}</p>
                  </div>
                </div>

                {/* Reflection Question */}
                <div>
                  <h4 className="text-xl font-handwriting font-semibold text-dark mb-3">
                    Reflection prompt:
                  </h4>
                  <div className="bg-gradient-to-r from-green-50 to-teal-50 p-6 rounded-2xl border-2 border-green-100">
                    <p className="text-dark font-semibold text-lg leading-relaxed">{analysisResult.reflection}</p>
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
};

export default VoiceRecorder; 