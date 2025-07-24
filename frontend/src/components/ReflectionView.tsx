import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Heart, Sparkles, Lightbulb } from 'lucide-react';
import axios from 'axios';

const ReflectionView: React.FC = () => {
  const [currentMood, setCurrentMood] = useState('');
  const [focusArea, setFocusArea] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [reflection, setReflection] = useState('');
  const [error, setError] = useState('');

  const moods = [
    'happy', 'sad', 'anxious', 'excited', 'peaceful', 'stressed', 'confused', 'grateful', 'lonely', 'energetic'
  ];

  const focusAreas = [
    'relationships', 'work', 'health', 'personal growth', 'creativity', 'stress management', 'gratitude', 'self-care'
  ];

  const generateReflection = async () => {
    if (!currentMood) {
      setError('Please select your current mood');
      return;
    }

    setIsGenerating(true);
    setError('');

    try {
      const response = await axios.post('/api/reflection', {
        current_mood: currentMood,
        focus_area: focusArea || undefined,
        recent_entries: []
      });

      setReflection(response.data.reflection);
    } catch (err) {
      setError('Failed to generate reflection. Please try again.');
      console.error('Reflection generation error:', err);
    } finally {
      setIsGenerating(false);
    }
  };

  const getMoodColor = (mood: string) => {
    const moodColors: { [key: string]: string } = {
      happy: 'bg-yellow-100 text-yellow-800 border-yellow-200',
      sad: 'bg-blue-100 text-blue-800 border-blue-200',
      anxious: 'bg-orange-100 text-orange-800 border-orange-200',
      excited: 'bg-green-100 text-green-800 border-green-200',
      peaceful: 'bg-teal-100 text-teal-800 border-teal-200',
      stressed: 'bg-red-100 text-red-800 border-red-200',
      confused: 'bg-purple-100 text-purple-800 border-purple-200',
      grateful: 'bg-emerald-100 text-emerald-800 border-emerald-200',
      lonely: 'bg-gray-100 text-gray-800 border-gray-200',
      energetic: 'bg-pink-100 text-pink-800 border-pink-200',
    };
    return moodColors[mood] || moodColors.happy;
  };

  return (
    <div className="max-w-4xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="card"
      >
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gradient mb-4">
            <Heart className="inline mr-2" />
            Personalized Reflection
          </h2>
          <p className="text-calm-600 text-lg">
            Let me help you explore your thoughts with a thoughtful reflection prompt.
          </p>
        </div>

        {/* Mood Selection */}
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-calm-800 mb-4">
            How are you feeling right now?
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
            {moods.map((mood) => (
              <motion.button
                key={mood}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setCurrentMood(mood)}
                className={`p-3 rounded-lg border-2 transition-all duration-200 ${
                  currentMood === mood
                    ? getMoodColor(mood) + ' ring-2 ring-primary-500 ring-opacity-50'
                    : 'bg-white border-gray-200 hover:border-primary-300 text-calm-700'
                }`}
              >
                <span className="capitalize font-medium">{mood}</span>
              </motion.button>
            ))}
          </div>
        </div>

        {/* Focus Area Selection */}
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-calm-800 mb-4">
            What would you like to focus on? (Optional)
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {focusAreas.map((area) => (
              <motion.button
                key={area}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setFocusArea(focusArea === area ? '' : area)}
                className={`p-3 rounded-lg border-2 transition-all duration-200 ${
                  focusArea === area
                    ? 'bg-primary-50 border-primary-300 text-primary-700 ring-2 ring-primary-500 ring-opacity-50'
                    : 'bg-white border-gray-200 hover:border-primary-300 text-calm-700'
                }`}
              >
                <span className="capitalize font-medium">{area}</span>
              </motion.button>
            ))}
          </div>
        </div>

        {/* Generate Button */}
        <div className="text-center mb-8">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={generateReflection}
            disabled={isGenerating || !currentMood}
            className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isGenerating ? (
              <div className="flex items-center gap-2">
                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                Generating...
              </div>
            ) : (
              <div className="flex items-center gap-2">
                <Sparkles size={20} />
                Generate Reflection
              </div>
            )}
          </motion.button>
        </div>

        {/* Error Message */}
        {error && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6"
          >
            {error}
          </motion.div>
        )}

        {/* Reflection Result */}
        {reflection && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="border-t border-gray-200 pt-6"
          >
            <div className="bg-gradient-to-r from-lavender-50 to-teal-50 p-6 rounded-xl border border-lavender-200">
              <div className="flex items-center gap-3 mb-4">
                <Lightbulb className="text-primary-600" size={24} />
                <h3 className="text-xl font-bold text-calm-800">
                  Your Reflection Prompt
                </h3>
              </div>
              <p className="text-lg text-calm-700 leading-relaxed">
                {reflection}
              </p>
            </div>
          </motion.div>
        )}

        {/* Tips */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mt-8 bg-calm-50 p-6 rounded-xl border border-calm-200"
        >
          <h4 className="text-lg font-semibold text-calm-800 mb-3">
            💡 Reflection Tips
          </h4>
          <ul className="space-y-2 text-calm-600">
            <li>• Take a moment to breathe and center yourself before reflecting</li>
            <li>• Write down your thoughts in a journal if you'd like</li>
            <li>• Be honest with yourself - there are no right or wrong answers</li>
            <li>• Consider how this reflection might help you grow</li>
          </ul>
        </motion.div>
      </motion.div>
    </div>
  );
};

export default ReflectionView; 