# MindMirror UI Mockups & Visual Design

## Screenshot Descriptions for Project Showcase

### 1. Main Recording Interface (Home Page)

**Layout Description**:
- **Background**: Light gray gradient (f7fafc to edf2f7)
- **Header**: "MindMirror" in large handwriting font (Caveat, 7xl) with black gradient
- **Subtitle**: "Your gentle companion for emotional reflection and mental wellness" in dark text
- **Main Card**: White glass-morphism card with rounded corners (28px radius)
- **Microphone Button**: Large circular button (80px) with black gradient and white microphone icon
- **Recording State**: Pulsing red animation when recording
- **Playback Controls**: Modern buttons with black/white styling

**Key Visual Elements**:
- Floating background circles (gray tones, blurred)
- Smooth entrance animations
- High contrast black and white design
- Handwriting font for personal touch

### 2. Analysis Results Display

**Layout Description**:
- **Section Headers**: Handwriting font (Caveat, xl) in black
- **Transcript Box**: Light blue background (#dbeafe) with dark text
- **Emotion Badge**: Gradient background (varies by mood) with white text
- **AI Insights Box**: Purple gradient background (#f3e8ff) with dark text
- **Reflection Box**: Green gradient background (#dcfce7) with dark text

**Color Scheme**:
- **Happy**: Yellow gradient (#fbbf24 to #f59e0b)
- **Sad**: Blue gradient (#3b82f6 to #1d4ed8)
- **Anxious**: Orange gradient (#f97316 to #ea580c)
- **Excited**: Green gradient (#10b981 to #059669)
- **Peaceful**: Teal gradient (#14b8a6 to #0d9488)
- **Stressed**: Red gradient (#ef4444 to #dc2626)

### 3. Navigation Bar

**Layout Description**:
- **Background**: Semi-transparent white with blur effect
- **Logo**: Mirror emoji (🪞) + "MindMirror" in handwriting font
- **Navigation Links**: Three items with hover effects
- **Active State**: Black gradient background for current page

**Navigation Items**:
- Home (Voice Recorder)
- Reflection
- History

### 4. History & Trends Page

**Layout Description**:
- **Time Period Selector**: Toggle buttons for 7/14/30 days
- **Mood Distribution Chart**: Pie chart with gradient colors
- **Trend Line Chart**: Line graph showing emotional patterns
- **History List**: Scrollable list of past entries with timestamps

**Chart Colors**:
- Consistent with emotion badge colors
- Smooth gradients and animations
- Clear data labels and legends

### 5. Reflection Generator Page

**Layout Description**:
- **Mood Selector**: Grid of emotion buttons with icons
- **Focus Area Dropdown**: Categories like work, relationships, personal growth
- **Generate Button**: Black gradient button with white text
- **Results Display**: Similar styling to main analysis results

## Design System

### Typography
- **Primary Font**: Inter (sans-serif)
- **Handwriting Font**: Caveat (for headings and personal elements)
- **Font Weights**: 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold)

### Color Palette
- **Primary Black**: #000000
- **Secondary Black**: #1a202c
- **Light Gray**: #f7fafc
- **Medium Gray**: #edf2f7
- **Dark Gray**: #4a5568
- **White**: #ffffff

### Spacing System
- **Container**: max-width 6xl, centered
- **Card Padding**: 12 (48px)
- **Section Margins**: 8 (32px)
- **Button Padding**: 14px 28px
- **Border Radius**: 16px (buttons), 28px (cards)

### Animations
- **Entrance**: Fade in with slide up (0.6s ease-out)
- **Hover**: Scale and shadow changes
- **Recording**: Pulsing animation (2s infinite)
- **Background**: Floating circles (6s infinite)

## Responsive Design

### Mobile (320px - 768px)
- Single column layout
- Stacked navigation
- Full-width cards
- Larger touch targets

### Tablet (768px - 1024px)
- Two-column layout where appropriate
- Side navigation
- Medium card widths

### Desktop (1024px+)
- Multi-column layouts
- Top navigation
- Maximum card widths
- Hover effects

## Accessibility Features

### Visual
- High contrast black and white design
- Clear typography hierarchy
- Consistent color coding
- Adequate touch target sizes

### Interactive
- Keyboard navigation support
- Focus indicators
- Screen reader compatibility
- Alternative text for icons

## Animation Specifications

### Microphone Button
```css
.mic-button {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.mic-button:hover {
  transform: scale(1.05);
}

.mic-button.recording {
  animation: pulse-recording 2s ease-in-out infinite;
}
```

### Card Entrances
```css
.card-enter {
  animation: fade-in 0.6s ease-out, slide-up 0.4s ease-out;
}
```

### Background Elements
```css
.floating-circle {
  animation: float-smooth 6s ease-in-out infinite;
}
```

## Screenshot Checklist

### Required Screenshots
1. **Home Page (Empty State)**: Clean interface with microphone button
2. **Recording State**: Microphone pulsing red during recording
3. **Playback Controls**: Audio player with play/pause/reset buttons
4. **Analysis Results**: Complete analysis display with all sections
5. **Navigation Bar**: Top navigation with active states
6. **History Page**: Charts and data visualization
7. **Reflection Page**: Mood selector and generator
8. **Mobile View**: Responsive design on smaller screen
9. **Error State**: Graceful error handling display
10. **Loading State**: Smooth loading animations

### Optional Screenshots
- **Dark Mode**: Alternative color scheme
- **Different Emotions**: Various mood badge examples
- **Trend Charts**: Different time period views
- **API Documentation**: FastAPI auto-generated docs
- **Deployment**: Production environment setup

## Image Specifications

### Screenshot Requirements
- **Resolution**: 1920x1080 (desktop), 375x812 (mobile)
- **Format**: PNG with transparency
- **Quality**: High resolution, crisp text
- **File Naming**: descriptive-names-with-hyphens.png

### GIF Requirements
- **Duration**: 3-5 seconds for feature demonstrations
- **Frame Rate**: 30fps for smooth animations
- **Size**: Optimized for web (max 5MB)
- **Content**: User interactions and animations

## Brand Guidelines

### Logo Usage
- Mirror emoji (🪞) + "MindMirror" text
- Handwriting font (Caveat) for personal touch
- Black gradient for primary usage
- Minimum size: 24px height

### Color Usage
- **Primary**: Black gradients for important elements
- **Secondary**: White backgrounds with subtle borders
- **Accent**: Emotion-specific gradients for mood indicators
- **Text**: High contrast black on light backgrounds

### Voice & Tone
- **Friendly**: Warm and approachable
- **Professional**: Clean and trustworthy
- **Personal**: Handwriting elements for intimacy
- **Calming**: Smooth animations and gentle colors 