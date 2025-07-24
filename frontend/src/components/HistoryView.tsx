import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { BarChart3, Calendar, TrendingUp, Clock } from 'lucide-react';
import axios from 'axios';
import { format, parseISO } from 'date-fns';

interface EmotionEntry {
  user_id: string;
  timestamp: string;
  transcript: string;
  mood: string;
  summary: string;
  reflection: string;
  confidence: number;
}

interface UserHistory {
  user_id: string;
  entries: EmotionEntry[];
  trends: {
    mood_distribution: { [key: string]: number };
    weekly_patterns: { [key: string]: string[] };
    overall_trend: string;
    total_entries: number;
  };
  total_entries: number;
}

const HistoryView: React.FC = () => {
  const [history, setHistory] = useState<UserHistory | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedDays, setSelectedDays] = useState(7);

  useEffect(() => {
    fetchHistory();
  }, [selectedDays]);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`/api/history/default_user?days=${selectedDays}`);
      setHistory(response.data);
    } catch (err) {
      setError('Failed to load history. Please try again.');
      console.error('History fetch error:', err);
    } finally {
      setLoading(false);
    }
  };

  const getMoodColor = (mood: string) => {
    const moodColors: { [key: string]: string } = {
      happy: 'bg-yellow-100 text-yellow-800',
      sad: 'bg-blue-100 text-blue-800',
      anxious: 'bg-orange-100 text-orange-800',
      excited: 'bg-green-100 text-green-800',
      peaceful: 'bg-teal-100 text-teal-800',
      stressed: 'bg-red-100 text-red-800',
      neutral: 'bg-gray-100 text-gray-800',
    };
    return moodColors[mood.toLowerCase()] || moodColors.neutral;
  };

  const getTrendIcon = (trend: string) => {
    switch (trend) {
      case 'positive':
        return '📈';
      case 'negative':
        return '📉';
      default:
        return '➡️';
    }
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto">
        <div className="card text-center">
          <div className="flex items-center justify-center gap-3">
            <div className="w-6 h-6 border-2 border-primary-500 border-t-transparent rounded-full animate-spin"></div>
            <span className="text-calm-600">Loading your emotional journey...</span>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="card"
      >
        <div className="text-center mb-6">
          <h2 className="text-3xl font-bold text-gradient mb-4">
            <BarChart3 className="inline mr-2" />
            Your Emotional Journey
          </h2>
          <p className="text-calm-600 text-lg">
            Track your emotional patterns and growth over time.
          </p>
        </div>

        {/* Time Period Selector */}
        <div className="flex justify-center gap-2 mb-6">
          {[7, 14, 30].map((days) => (
            <motion.button
              key={days}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => setSelectedDays(days)}
              className={`px-4 py-2 rounded-lg font-medium transition-all duration-200 ${
                selectedDays === days
                  ? 'bg-primary-500 text-white shadow-lg'
                  : 'bg-white text-calm-600 border border-calm-200 hover:border-primary-300'
              }`}
            >
              {days} days
            </motion.button>
          ))}
        </div>

        {/* Error Message */}
        {error && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg"
          >
            {error}
          </motion.div>
        )}
      </motion.div>

      {history && (
        <>
          {/* Summary Stats */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="grid grid-cols-1 md:grid-cols-3 gap-6"
          >
            <div className="card text-center">
              <div className="text-3xl font-bold text-primary-600 mb-2">
                {history.total_entries}
              </div>
              <div className="text-calm-600">Total Reflections</div>
            </div>
            
            <div className="card text-center">
              <div className="text-3xl font-bold text-lavender-600 mb-2">
                {getTrendIcon(history.trends.overall_trend)}
              </div>
              <div className="text-calm-600 capitalize">
                {history.trends.overall_trend} Trend
              </div>
            </div>
            
            <div className="card text-center">
              <div className="text-3xl font-bold text-teal-600 mb-2">
                {Object.keys(history.trends.mood_distribution).length}
              </div>
              <div className="text-calm-600">Mood Varieties</div>
            </div>
          </motion.div>

          {/* Mood Distribution */}
          {Object.keys(history.trends.mood_distribution).length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
              className="card"
            >
              <h3 className="text-2xl font-bold text-calm-800 mb-6">
                <TrendingUp className="inline mr-2" />
                Mood Distribution
              </h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {Object.entries(history.trends.mood_distribution).map(([mood, count]) => (
                  <div key={mood} className="text-center p-4 bg-calm-50 rounded-lg">
                    <div className={`mood-badge ${getMoodColor(mood)} mb-2`}>
                      {mood}
                    </div>
                    <div className="text-2xl font-bold text-calm-800">{count}</div>
                    <div className="text-sm text-calm-600">times</div>
                  </div>
                ))}
              </div>
            </motion.div>
          )}

          {/* Recent Entries */}
          {history.entries.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
              className="card"
            >
              <h3 className="text-2xl font-bold text-calm-800 mb-6">
                <Calendar className="inline mr-2" />
                Recent Reflections
              </h3>
              <div className="space-y-6">
                {history.entries.slice(0, 5).map((entry, index) => (
                  <motion.div
                    key={entry.timestamp}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 0.1 * index }}
                    className="border border-calm-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                  >
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex items-center gap-3">
                        <span className={`mood-badge ${getMoodColor(entry.mood)}`}>
                          {entry.mood}
                        </span>
                        <span className="text-sm text-calm-500">
                          <Clock className="inline mr-1" size={14} />
                          {format(parseISO(entry.timestamp), 'MMM d, yyyy h:mm a')}
                        </span>
                      </div>
                    </div>
                    
                    <div className="mb-3">
                      <h4 className="font-semibold text-calm-800 mb-1">What you shared:</h4>
                      <p className="text-calm-600 italic text-sm">
                        "{entry.transcript.length > 100 
                          ? entry.transcript.substring(0, 100) + '...' 
                          : entry.transcript}"
                      </p>
                    </div>
                    
                    <div className="mb-3">
                      <h4 className="font-semibold text-calm-800 mb-1">MindMirror's insight:</h4>
                      <p className="text-calm-600 text-sm">{entry.summary}</p>
                    </div>
                    
                    <div>
                      <h4 className="font-semibold text-calm-800 mb-1">Reflection prompt:</h4>
                      <p className="text-primary-600 text-sm font-medium">{entry.reflection}</p>
                    </div>
                  </motion.div>
                ))}
              </div>
            </motion.div>
          )}

          {/* Empty State */}
          {history.entries.length === 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="card text-center py-12"
            >
              <div className="text-6xl mb-4">🎙️</div>
              <h3 className="text-2xl font-bold text-calm-800 mb-2">
                Start Your Journey
              </h3>
              <p className="text-calm-600 mb-6">
                You haven't recorded any reflections yet. Begin by sharing your thoughts!
              </p>
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => window.location.href = '/'}
                className="btn-primary"
              >
                Record Your First Reflection
              </motion.button>
            </motion.div>
          )}
        </>
      )}
    </div>
  );
};

export default HistoryView; 