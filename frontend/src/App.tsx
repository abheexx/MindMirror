import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { motion } from 'framer-motion';
import VoiceRecorder from './components/VoiceRecorder';
import ReflectionView from './components/ReflectionView';
import HistoryView from './components/HistoryView';
import Navigation from './components/Navigation';
import './App.css';

function App() {
  return (
    <Router>
      <div className="min-h-screen relative overflow-hidden">
                    {/* Background Elements */}
            <div className="absolute inset-0 overflow-hidden">
              <div className="absolute -top-40 -right-40 w-80 h-80 bg-gray-200 rounded-full mix-blend-multiply filter blur-xl opacity-50 animate-float-smooth"></div>
              <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-gray-300 rounded-full mix-blend-multiply filter blur-xl opacity-50 animate-float-smooth" style={{ animationDelay: '2s' }}></div>
              <div className="absolute top-40 left-40 w-80 h-80 bg-gray-100 rounded-full mix-blend-multiply filter blur-xl opacity-50 animate-float-smooth" style={{ animationDelay: '4s' }}></div>
            </div>

        <Navigation />
        
        <main className="relative z-10 container-custom py-12">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="text-center mb-16"
          >
            <motion.div
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="inline-block mb-6"
            >
              <div className="text-6xl mb-4">🪞</div>
            </motion.div>
            
            <h1 className="text-7xl font-handwriting font-bold text-gradient-modern mb-6 tracking-tight">
              MindMirror
            </h1>
            
            <motion.p 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.8, delay: 0.4 }}
              className="text-2xl text-dark font-medium max-w-3xl mx-auto leading-relaxed"
            >
              Your gentle companion for emotional reflection and mental wellness. 
              Speak freely, discover insights, and grow with every conversation.
            </motion.p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.6 }}
          >
            <Routes>
              <Route path="/" element={<VoiceRecorder />} />
              <Route path="/reflection" element={<ReflectionView />} />
              <Route path="/history" element={<HistoryView />} />
            </Routes>
          </motion.div>
        </main>

                    <motion.footer 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.8, delay: 1 }}
              className="relative z-10 text-center py-12 text-dark/70"
            >
              <p className="text-lg font-light">
                Built with care for your mental wellness journey
              </p>
            </motion.footer>
      </div>
    </Router>
  );
}

export default App; 