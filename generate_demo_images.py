#!/usr/bin/env python3
"""
Generate demo images for MindMirror project
Creates visual representations of the UI components
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def create_directory():
    """Create images directory if it doesn't exist"""
    if not os.path.exists('docs/images'):
        os.makedirs('docs/images')

def create_main_interface():
    """Create main recording interface screenshot"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Background gradient effect
    gradient = np.linspace(0, 1, 100)
    for i, alpha in enumerate(gradient):
        ax.axhspan(i*0.08, (i+1)*0.08, alpha=alpha*0.1, color='gray')
    
    # Main card
    card = FancyBboxPatch((1, 1), 10, 6, 
                         boxstyle="round,pad=0.1", 
                         facecolor='white', 
                         edgecolor='black',
                         linewidth=2,
                         alpha=0.95)
    ax.add_patch(card)
    
    # Title
    ax.text(6, 6.5, 'MindMirror', fontsize=24, fontweight='bold', 
            ha='center', va='center', style='italic')
    
    # Subtitle
    ax.text(6, 6, 'Your gentle companion for emotional reflection', 
            fontsize=12, ha='center', va='center', color='gray')
    
    # Microphone button
    mic_circle = Circle((6, 4), 1.2, facecolor='black', edgecolor='black', linewidth=2)
    ax.add_patch(mic_circle)
    ax.text(6, 4, '🎙️', fontsize=20, ha='center', va='center')
    
    # Recording text
    ax.text(6, 2.5, 'Click to start recording your thoughts', 
            fontsize=14, ha='center', va='center', color='gray')
    
    # Floating background elements
    for i in range(3):
        x = 2 + i * 3
        y = 1.5 + (i % 2) * 0.5
        circle = Circle((x, y), 0.3, facecolor='lightgray', alpha=0.3)
        ax.add_patch(circle)
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/images/main-interface.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_analysis_results():
    """Create analysis results screenshot"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # Background
    ax.set_facecolor('#f7fafc')
    
    # Main card
    card = FancyBboxPatch((0.5, 0.5), 11, 9, 
                         boxstyle="round,pad=0.1", 
                         facecolor='white', 
                         edgecolor='black',
                         linewidth=2,
                         alpha=0.95)
    ax.add_patch(card)
    
    # Title
    ax.text(6, 9, 'Your Reflection', fontsize=20, fontweight='bold', 
            ha='center', va='center', style='italic')
    
    # Transcript section
    transcript_box = FancyBboxPatch((1, 7.5), 10, 1, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor='#dbeafe', 
                                   edgecolor='#3b82f6',
                                   linewidth=1)
    ax.add_patch(transcript_box)
    ax.text(1.2, 8, 'What you shared:', fontsize=12, fontweight='bold', va='center')
    ax.text(1.2, 7.7, '"Today was really stressful at work. I had three meetings back-to-back..."', 
            fontsize=10, va='center', style='italic')
    
    # Emotion badge
    emotion_box = FancyBboxPatch((1, 6.5), 3, 0.8, 
                                boxstyle="round,pad=0.05", 
                                facecolor='#ef4444', 
                                edgecolor='#dc2626',
                                linewidth=1)
    ax.add_patch(emotion_box)
    ax.text(2.5, 6.9, 'Stressed', fontsize=12, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # AI Insights
    insights_box = FancyBboxPatch((1, 5), 10, 1.2, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor='#f3e8ff', 
                                 edgecolor='#8b5cf6',
                                 linewidth=1)
    ax.add_patch(insights_box)
    ax.text(1.2, 5.8, 'MindMirror\'s insight:', fontsize=12, fontweight='bold', va='center')
    ax.text(1.2, 5.4, 'You\'re experiencing significant work-related stress. The constant changes', 
            fontsize=10, va='center')
    ax.text(1.2, 5.2, 'and back-to-back meetings are creating pressure that\'s affecting your mental state.', 
            fontsize=10, va='center')
    
    # Reflection prompt
    reflection_box = FancyBboxPatch((1, 3), 10, 1.2, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor='#dcfce7', 
                                   edgecolor='#22c55e',
                                   linewidth=1)
    ax.add_patch(reflection_box)
    ax.text(1.2, 3.8, 'Reflection prompt:', fontsize=12, fontweight='bold', va='center')
    ax.text(1.2, 3.4, 'What boundaries could you set to create more breathing room in your workday?', 
            fontsize=10, va='center', fontweight='bold')
    
    # Navigation hint
    ax.text(6, 1.5, '← Navigate to History to see your emotional trends', 
            fontsize=10, ha='center', va='center', color='gray')
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/images/analysis-results.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_navigation():
    """Create navigation bar screenshot"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')
    
    # Navigation background
    nav_bg = FancyBboxPatch((0, 0), 12, 2, 
                           boxstyle="round,pad=0.05", 
                           facecolor='white', 
                           edgecolor='lightgray',
                           linewidth=1,
                           alpha=0.95)
    ax.add_patch(nav_bg)
    
    # Logo
    ax.text(1, 1, '🪞 MindMirror', fontsize=16, fontweight='bold', 
            ha='left', va='center', style='italic')
    
    # Navigation items
    nav_items = ['Home', 'Reflection', 'History']
    for i, item in enumerate(nav_items):
        x = 8 + i * 1.2
        if item == 'Home':
            # Active state
            nav_box = FancyBboxPatch((x-0.4, 0.3), 0.8, 1.4, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor='black', 
                                   edgecolor='black',
                                   linewidth=1)
            ax.add_patch(nav_box)
            ax.text(x, 1, item, fontsize=12, fontweight='bold', 
                    ha='center', va='center', color='white')
        else:
            ax.text(x, 1, item, fontsize=12, ha='center', va='center', color='gray')
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/images/navigation.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_history_page():
    """Create history page screenshot"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Background
    ax.set_facecolor('#f7fafc')
    
    # Main card
    card = FancyBboxPatch((0.5, 0.5), 11, 7, 
                         boxstyle="round,pad=0.1", 
                         facecolor='white', 
                         edgecolor='black',
                         linewidth=2,
                         alpha=0.95)
    ax.add_patch(card)
    
    # Title
    ax.text(6, 7.2, 'Your Emotional History', fontsize=20, fontweight='bold', 
            ha='center', va='center', style='italic')
    
    # Time period selector
    periods = ['7 Days', '14 Days', '30 Days']
    for i, period in enumerate(periods):
        x = 3 + i * 2
        if period == '7 Days':
            # Active state
            period_box = FancyBboxPatch((x-0.6, 6.2), 1.2, 0.6, 
                                       boxstyle="round,pad=0.05", 
                                       facecolor='black', 
                                       edgecolor='black',
                                       linewidth=1)
            ax.add_patch(period_box)
            ax.text(x, 6.5, period, fontsize=10, fontweight='bold', 
                    ha='center', va='center', color='white')
        else:
            period_box = FancyBboxPatch((x-0.6, 6.2), 1.2, 0.6, 
                                       boxstyle="round,pad=0.05", 
                                       facecolor='lightgray', 
                                       edgecolor='gray',
                                       linewidth=1)
            ax.add_patch(period_box)
            ax.text(x, 6.5, period, fontsize=10, ha='center', va='center', color='gray')
    
    # Mood distribution chart (simplified)
    ax.text(3, 5, 'Mood Distribution', fontsize=14, fontweight='bold', ha='center')
    
    # Pie chart representation
    colors = ['#fbbf24', '#3b82f6', '#f97316', '#10b981', '#ef4444']
    labels = ['Happy', 'Sad', 'Anxious', 'Excited', 'Stressed']
    sizes = [25, 15, 30, 20, 10]
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, 
                                     autopct='%1.0f%%', startangle=90,
                                     radius=1.2, center=(3, 3))
    
    # Trend chart
    ax.text(9, 5, 'Emotional Trends', fontsize=14, fontweight='bold', ha='center')
    
    # Simple line chart
    days = [1, 2, 3, 4, 5, 6, 7]
    values = [3, 4, 2, 5, 3, 4, 3]
    ax.plot([8.5, 9, 9.5, 10, 10.5, 11, 11.5], values, 
            marker='o', linewidth=2, color='black')
    ax.set_xlim(8, 12)
    ax.set_ylim(1, 6)
    ax.set_xticks([8.5, 9.5, 10.5, 11.5])
    ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu'])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['', 'Sad', 'Neutral', 'Happy', ''])
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/images/history-page.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_mobile_view():
    """Create mobile responsive view screenshot"""
    fig, ax = plt.subplots(1, 1, figsize=(6, 10))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # Background
    ax.set_facecolor('#f7fafc')
    
    # Mobile frame
    frame = FancyBboxPatch((0.2, 0.2), 5.6, 9.6, 
                          boxstyle="round,pad=0.1", 
                          facecolor='black', 
                          edgecolor='black',
                          linewidth=3)
    ax.add_patch(frame)
    
    # Screen
    screen = FancyBboxPatch((0.4, 0.4), 5.2, 9.2, 
                           boxstyle="round,pad=0.05", 
                           facecolor='white', 
                           edgecolor='none')
    ax.add_patch(screen)
    
    # Title
    ax.text(3, 8.5, 'MindMirror', fontsize=18, fontweight='bold', 
            ha='center', va='center', style='italic')
    
    # Subtitle
    ax.text(3, 8, 'Your gentle companion', fontsize=10, ha='center', va='center', color='gray')
    
    # Microphone button (smaller for mobile)
    mic_circle = Circle((3, 5), 0.8, facecolor='black', edgecolor='black', linewidth=2)
    ax.add_patch(mic_circle)
    ax.text(3, 5, '🎙️', fontsize=16, ha='center', va='center')
    
    # Recording text
    ax.text(3, 3.5, 'Tap to record', fontsize=12, ha='center', va='center', color='gray')
    
    # Bottom navigation
    nav_items = ['🏠', '💭', '📊']
    for i, item in enumerate(nav_items):
        x = 1.5 + i * 1.5
        nav_circle = Circle((x, 1), 0.3, facecolor='lightgray', edgecolor='gray', linewidth=1)
        ax.add_patch(nav_circle)
        ax.text(x, 1, item, fontsize=12, ha='center', va='center')
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/images/mobile-view.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def main():
    """Generate all demo images"""
    print("Creating demo images for MindMirror...")
    
    create_directory()
    create_main_interface()
    create_analysis_results()
    create_navigation()
    create_history_page()
    create_mobile_view()
    
    print("✅ Demo images created successfully!")
    print("📁 Images saved in: docs/images/")
    print("🖼️  Generated files:")
    print("   - main-interface.png")
    print("   - analysis-results.png")
    print("   - navigation.png")
    print("   - history-page.png")
    print("   - mobile-view.png")

if __name__ == "__main__":
    main() 