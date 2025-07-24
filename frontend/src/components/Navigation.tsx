import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Mic, Heart, BarChart3 } from 'lucide-react';

const Navigation: React.FC = () => {
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'Record', icon: Mic },
    { path: '/reflection', label: 'Reflect', icon: Heart },
    { path: '/history', label: 'History', icon: BarChart3 },
  ];

  return (
    <nav className="nav-modern sticky top-0 z-50">
      <div className="container-custom">
        <div className="flex items-center justify-between h-20">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3">
            <motion.div
              whileHover={{ scale: 1.05 }}
              className="text-3xl"
            >
              🪞
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="text-3xl font-handwriting font-bold text-gradient-modern"
            >
              MindMirror
            </motion.div>
          </Link>

          {/* Navigation Links */}
          <div className="flex items-center space-x-2">
            {navItems.map((item, index) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              
              return (
                <motion.div
                  key={item.path}
                  initial={{ opacity: 0, y: -20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3, delay: index * 0.1 }}
                >
                  <Link
                    to={item.path}
                    className={`nav-link flex items-center space-x-2 ${
                      isActive ? 'active' : ''
                    }`}
                  >
                    <Icon size={18} />
                    <span className="font-medium">{item.label}</span>
                  </Link>
                </motion.div>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation; 