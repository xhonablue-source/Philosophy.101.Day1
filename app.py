def display_professor_lecture():
    """Display the complete beautiful HTML presentation"""
    st.markdown("# 🎓 Professor Lecture - Interactive Presentation")
    st.markdown("*Click the presentation below to begin the interactive lecture*")
    
    # Complete HTML presentation from your document
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>What is Religion? What is Philosophy?</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                overflow: hidden;
            }

            .presentation-container {
                width: 100vw;
                height: 100vh;
                position: relative;
            }

            .slide {
                width: 100%;
                height: 100%;
                display: none;
                padding: 60px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                position: relative;
                overflow-y: auto;
            }

            .slide.active {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .slide-number {
                position: absolute;
                top: 20px;
                right: 30px;
                background: rgba(102, 126, 234, 0.8);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
            }

            h1 {
                font-size: 3.5em;
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                animation: fadeInUp 1s ease-out;
            }

            h2 {
                font-size: 2.8em;
                color: #34495e;
                text-align: center;
                margin-bottom: 40px;
                animation: fadeInUp 1s ease-out 0.2s both;
            }

            h3 {
                font-size: 2em;
                color: #2980b9;
                margin-bottom: 25px;
                text-align: center;
                animation: fadeInUp 1s ease-out 0.4s both;
            }

            .subtitle {
                font-size: 1.3em;
                color: #7f8c8d;
                text-align: center;
                margin-bottom: 50px;
                font-style: italic;
                animation: fadeInUp 1s ease-out 0.3s both;
            }

            .course-info {
                background: rgba(255, 255, 255, 0.9);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
                margin-bottom: 40px;
                animation: slideInUp 1s ease-out 0.5s both;
            }

            .content-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                width: 100%;
                max-width: 1200px;
                margin: 0 auto;
            }

            .content-card {
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                transform: translateY(20px);
                opacity: 0;
                animation: slideInUp 0.8s ease-out forwards;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .content-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            }

            .content-card:nth-child(1) { animation-delay: 0.1s; }
            .content-card:nth-child(2) { animation-delay: 0.3s; }
            .content-card:nth-child(3) { animation-delay: 0.5s; }

            .icon {
                font-size: 3em;
                margin-bottom: 20px;
                display: block;
                text-align: center;
            }

            .philosophy-icon { color: #3498db; }
            .religion-icon { color: #e74c3c; }
            .overlap-icon { color: #9b59b6; }

            .big-questions {
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                justify-content: center;
                margin: 30px 0;
            }

            .question-tag {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                padding: 12px 20px;
                border-radius: 25px;
                font-weight: bold;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                animation: fadeInScale 0.8s ease-out forwards;
                transform: scale(0);
            }

            .question-tag:nth-child(1) { animation-delay: 0.1s; }
            .question-tag:nth-child(2) { animation-delay: 0.2s; }
            .question-tag:nth-child(3) { animation-delay: 0.3s; }
            .question-tag:nth-child(4) { animation-delay: 0.4s; }
            .question-tag:nth-child(5) { animation-delay: 0.5s; }

            .definition-box {
                background: linear-gradient(135deg, #ff9a56 0%, #ff6b6b 100%);
                color: white;
                padding: 25px;
                margin: 15px 0;
                border-radius: 10px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                animation: slideInLeft 1s ease-out forwards;
                transform: translateX(-50px);
                opacity: 0;
            }

            .definition-box:nth-child(even) {
                background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                animation: slideInRight 1s ease-out forwards;
                transform: translateX(50px);
            }

            .definition-box:nth-child(1) { animation-delay: 0.2s; }
            .definition-box:nth-child(2) { animation-delay: 0.4s; }
            .definition-box:nth-child(3) { animation-delay: 0.6s; }

            .example-section {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
                margin: 40px 0;
                width: 100%;
                max-width: 1000px;
            }

            .example-card {
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                text-align: center;
            }

            .philosophy-example {
                border-left: 5px solid #3498db;
            }

            .religion-example {
                border-left: 5px solid #e74c3c;
            }

            .navigation {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 15px;
                z-index: 1000;
            }

            .nav-btn {
                background: rgba(102, 126, 234, 0.9);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }

            .nav-btn:hover {
                background: rgba(102, 126, 234, 1);
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            }

            .nav-btn:disabled {
                background: rgba(149, 165, 166, 0.5);
                cursor: not-allowed;
                transform: none;
            }

            .slide-indicator {
                position: fixed;
                bottom: 100px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 8px;
                z-index: 1000;
            }

            .indicator-dot {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.5);
                cursor: pointer;
                transition: all 0.3s ease;
            }

            .indicator-dot.active {
                background: #667eea;
                transform: scale(1.3);
            }

            .homework-section {
                background: rgba(46, 204, 113, 0.1);
                border-left: 5px solid #2ecc71;
                padding: 30px;
                border-radius: 10px;
                margin-top: 30px;
            }

            .activity-timer {
                position: fixed;
                top: 20px;
                left: 30px;
                background: rgba(231, 76, 60, 0.9);
                color: white;
                padding: 10px 20px;
                border-radius: 20px;
                font-weight: bold;
                display: none;
            }

            ul {
                text-align: left;
                margin: 20px 0;
            }

            li {
                margin: 10px 0;
                font-size: 1.1em;
                line-height: 1.6;
            }

            .objective-list {
                background: rgba(52, 152, 219, 0.1);
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid #3498db;
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes slideInUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes slideInLeft {
                from {
                    opacity: 0;
                    transform: translateX(-50px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            @keyframes slideInRight {
                from {
                    opacity: 0;
                    transform: translateX(50px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            @keyframes fadeInScale {
                from {
                    opacity: 0;
                    transform: scale(0);
                }
                to {
                    opacity: 1;
                    transform: scale(1);
                }
            }

            @media (max-width: 768px) {
                .slide {
                    padding: 30px 20px;
                }
                
                h1 {
                    font-size: 2.5em;
                }
                
                h2 {
                    font-size: 2em;
                }
                
                .example-section {
                    grid-template-columns: 1fr;
                    gap: 20px;
                }
                
                .content-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="presentation-container">
            <div class="activity-timer" id="timer"></div>

            <!-- Slide 1: Title -->
            <div class="slide active">
                <div class="slide-number">1 / 9</div>
                <h1>📚 What is Religion?<br>What is Philosophy?</h1>
                <div class="course-info">
                    <h3>PHL 101 — Comparative Religions I</h3>
                    <p class="subtitle">Professor Xavier Honablue, M.Ed.</p>
                    <p><strong>Background: Mathematics • Computer Science • Philosophy • Education</strong></p>
                </div>
                <div class="subtitle">
                    "We're going to explore the great traditions of the world — Judaism, Christianity, Islam, 
                    but also Eastern, African, and Indigenous traditions. Our job is not to judge, 
                    but to think critically, compare, and engage."
                </div>
            </div>

            <!-- Slide 2: Course Objectives -->
            <div class="slide">
                <div class="slide-number">2 / 9</div>
                <h2>🎯 Our Journey Together</h2>
                <div class="objective-list">
                    <h3>What We'll Explore:</h3>
                    <ul>
                        <li><strong>World Religions:</strong> Christianity, Islam, Judaism, Hinduism, Buddhism, Taoism</li>
                        <li><strong>Indigenous Traditions:</strong> Native American, African, Australian Aboriginal</li>
                        <li><strong>Philosophical Approaches:</strong> Western and Eastern philosophical traditions</li>
                        <li><strong>Critical Thinking:</strong> Comparing beliefs, practices, and worldviews</li>
                        <li><strong>Personal Reflection:</strong> Understanding your own beliefs and assumptions</li>
                    </ul>
                </div>
                <div class="content-card">
                    <h3>🌍 Our Approach</h3>
                    <p>We approach each tradition with respect, curiosity, and scholarly rigor. 
                    We seek to understand rather than judge, to compare rather than compete, 
                    and to engage thoughtfully with humanity's greatest questions.</p>
                </div>
            </div>

            <!-- Slide 3: Icebreaker Questions -->
            <div class="slide">
                <div class="slide-number">3 / 9</div>
                <h2>🤔 The Big Questions</h2>
                <h3>Pair Discussion (10 minutes)</h3>
                <div class="content-grid">
                    <div class="content-card">
                        <div class="icon religion-icon">🕊️</div>
                        <h3>What do you think religion is?</h3>
                        <p>Consider: rituals, beliefs, communities, sacred texts, personal experiences, traditions passed down through generations.</p>
                    </div>
                    <div class="content-card">
                        <div class="icon philosophy-icon">🤔</div>
                        <h3>What do you think philosophy is?</h3>
                        <p>Think about: questioning, reasoning, logic, ethics, exploring fundamental concepts about existence and knowledge.</p>
                    </div>
                    <div class="content-card">
                        <div class="icon overlap-icon">🔗</div>
                        <h3>Where do the two overlap?</h3>
                        <p>Consider: ultimate questions about reality, meaning, morality, and the nature of existence itself.</p>
                    </div>
                </div>
                <p style="text-align: center; margin-top: 30px; font-size: 1.2em; color: #2c3e50;">
                    <strong>Share your thoughts with a partner, then we'll create our class word cloud!</strong>
                </p>
            </div>

            <!-- Slide 4: Philosophy Meets Religion -->
            <div class="slide">
                <div class="slide-number">4 / 9</div>
                <h2>🧠 Philosophy Meets Religion</h2>
                
                <div class="content-grid">
                    <div class="content-card philosophy-example">
                        <h3>📚 Philosophy</h3>
                        <p><strong>From Greek: "Philosophia" = Love of Wisdom</strong></p>
                        <ul>
                            <li>Asking fundamental questions</li>
                            <li>Using reason and logic</li>
                            <li>Challenging assumptions</li>
                            <li>Seeking understanding through inquiry</li>
                            <li>Socrates, Plato, Aristotle, Kant, Nietzsche</li>
                        </ul>
                    </div>
                    
                    <div class="content-card religion-example">
                        <h3>🕊️ Religion</h3>
                        <p><strong>From Latin: "Religare" = To Bind Together</strong></p>
                        <ul>
                            <li>Lived traditions and practices</li>
                            <li>Sacred stories and myths</li>
                            <li>Rituals and ceremonies</li>
                            <li>Community and belonging</li>
                            <li>Moses, Jesus, Muhammad, Buddha</li>
                        </ul>
                    </div>
                </div>

                <div class="content-card" style="margin-top: 30px;">
                    <h3>🤝 Both Ask the Same Core Questions:</h3>
                    <div class="big-questions">
                        <div class="question-tag">What is ultimate reality?</div>
                        <div class="question-tag">Why are we here?</div>
                        <div class="question-tag">How should we live?</div>
                        <div class="question-tag">What happens after death?</div>
                        <div class="question-tag">What is the meaning of life?</div>
                    </div>
                </div>
            </div>

            <!-- Slide 5: Examples -->
            <div class="slide">
                <div class="slide-number">5 / 9</div>
                <h2>💡 A Tale of Two Searches</h2>
                <div class="example-section">
                    <div class="example-card philosophy-example">
                        <h3>🏛️ Philosophy: Plato's Cave</h3>
                        <p><strong>The Story:</strong> Prisoners chained in a cave mistake shadows on the wall for reality until one escapes and discovers the true world of sunlight.</p>
                        <p><strong>The Message:</strong> We must question what we think we know. True knowledge comes through reason, not just accepting what we see.</p>
                        <p><strong>The Search:</strong> Truth through questioning and rational inquiry.</p>
                    </div>
                    
                    <div class="example-card religion-example">
                        <h3>⛰️ Religion: Moses and the Exodus</h3>
                        <p><strong>The Story:</strong> Moses leads the Israelites out of slavery in Egypt, receives the Ten Commandments, and guides them to the Promised Land.</p>
                        <p><strong>The Message:</strong> God liberates the oppressed and provides moral guidance for how to live.</p>
                        <p><strong>The Search:</strong> Freedom and meaning through divine revelation and community.</p>
                    </div>
                </div>
                
                <div class="content-card">
                    <h3>🎯 Both Stories Share:</h3>
                    <p style="font-size: 1.3em; color: #2c3e50;">
                        <strong>A journey from darkness to light, from bondage to freedom, from ignorance to truth.</strong><br>
                        They represent humanity's eternal quest to understand reality and find meaning.
                    </p>
                </div>
            </div>

            <!-- Slide 6: Group Activity -->
            <div class="slide">
                <div class="slide-number">6 / 9</div>
                <h2>🎲 Activity: Sorting the Big Questions</h2>
                <h3>Small Groups (15 minutes)</h3>
                
                <div class="content-card">
                    <h3>📝 Your Mission:</h3>
                    <p>Sort these questions into three categories: <strong>Philosophy</strong>, <strong>Religion</strong>, or <strong>Both</strong></p>
                </div>

                <div class="big-questions">
                    <div class="question-tag">Does God exist?</div>
                    <div class="question-tag">What happens after we die?</div>
                    <div class="question-tag">Why is there suffering?</div>
                    <div class="question-tag">What is justice?</div>
                    <div class="question-tag">Do humans have free will?</div>
                    <div class="question-tag">What is the meaning of life?</div>
                    <div class="question-tag">How should we treat others?</div>
                    <div class="question-tag">What is consciousness?</div>
                    <div class="question-tag">Is there absolute truth?</div>
                    <div class="question-tag">What is love?</div>
                </div>

                <div class="content-card">
                    <h3>🔮 Prediction:</h3>
                    <p style="font-size: 1.2em;">Most questions will end up in the <strong>"Both"</strong> category! 
                    This shows how philosophy and religion are deeply interconnected in addressing 
                    humanity's most fundamental concerns.</p>
                </div>
            </div>

            <!-- Slide 7: Defining Religion -->
            <div class="slide">
                <div class="slide-number">7 / 9</div>
                <h2>🔬 How Scholars Define Religion</h2>
                <h3>Three Famous Definitions</h3>

                <div class="definition-box">
                    <h3>👥 Émile Durkheim (1858-1917)</h3>
                    <p><strong>"Religion is the social glue that binds communities together."</strong></p>
                    <p>Focus: Religion creates solidarity, shared identity, and moral order in society. 
                    Think of how religious holidays bring families together, or how shared beliefs unite communities.</p>
                </div>

                <div class="definition-box">
                    <h3>👻 Edward Tylor (1832-1917)</h3>
                    <p><strong>"Religion is belief in spiritual beings."</strong></p>
                    <p>Focus: At its core, religion involves belief in gods, spirits, souls, or supernatural forces. 
                    From ancestor worship to monotheism, spiritual beings are central.</p>
                </div>

                <div class="definition-box">
                    <h3>💖 Paul Tillich (1886-1965)</h3>
                    <p><strong>"Religion is ultimate concern."</strong></p>
                    <p>Focus: Religion addresses what matters most to us - our deepest values, fears, and hopes. 
                    It's about what we're willing to sacrifice everything for.</p>
                </div>

                <div class="content-card">
                    <h3>🤔 Discussion Question:</h3>
                    <p style="font-size: 1.2em;">Which definition resonates most with you? Why? 
                    Can you think of examples that fit one definition but not the others?</p>
                </div>
            </div>

            <!-- Slide 8: Interactive Discussion -->
            <div class="slide">
                <div class="slide-number">8 / 9</div>
                <h2>💬 Let's Debate!</h2>
                
                <div class="content-grid">
                    <div class="content-card">
                        <h3>🤝 Team Durkheim</h3>
                        <p><strong>Religion = Social Glue</strong></p>
                        <ul>
                            <li>Explains why religion is found in every society</li>
                            <li>Shows religion's practical social function</li>
                            <li>Helps understand religious conflicts</li>
                            <li>Examples: Christmas bringing families together, Islamic community prayers</li>
                        </ul>
                    </div>
                    
                    <div class="content-card">
                        <h3>👻 Team Tylor</h3>
                        <p><strong>Religion = Spiritual Beings</strong></p>
                        <ul>
                            <li>Clear, specific definition</li>
                            <li>Distinguishes religion from philosophy</li>
                            <li>Explains prayer, worship, and ritual</li>
                            <li>Examples: Hindu gods, Christian Trinity, ancestor spirits</li>
                        </ul>
                    </div>
                    
                    <div class="content-card">
                        <h3>💖 Team Tillich</h3>
                        <p><strong>Religion = Ultimate Concern</strong></p>
                        <ul>
                            <li>Includes secular "religions" (nationalism, sports)</li>
                            <li>Focuses on personal meaning</li>
                            <li>Explains religious passion and devotion</li>
                            <li>Examples: Environmental activism as religion, patriotism</li>
                        </ul>
                    </div>
                </div>

                <div class="content-card">
                    <h3>🎯 Challenge Question:</h3>
                    <p>Is Buddhism a religion? How would each definition handle this case? 
                    (Buddhism often lacks belief in gods but has communities, practices, and ultimate concerns about suffering and enlightenment.)</p>
                </div>
            </div>

            <!-- Slide 9: Wrap-Up & Homework -->
            <div class="slide">
                <div class="slide-number">9 / 9</div>
                <h2>🎯 Exit Ticket & Next Steps</h2>
                
                <div class="content-card">
                    <h3>📝 Before You Leave:</h3>
                    <p style="font-size: 1.3em;">Write on a card: <strong>One question about life/religion you hope this class will answer.</strong></p>
                    <p>We'll revisit these at the end of the semester to see how our journey has evolved your thinking!</p>
                </div>

                <div class="homework-section">
                    <h3>🏠 Homework (Fun & Low-Stakes)</h3>
                    <ul>
                        <li><strong>Watch:</strong> A short video
                            <ul>
                                <li>CrashCourse Philosophy of Religion (YouTube)</li>
                                <li>OR TedEd "What is Religion?"</li>
                            </ul>
                        </li>
                        <li><strong>Write:</strong> One paragraph answering: "How do you personally define religion?"</li>
                        <li><strong>Reflect:</strong> Think about a religious or philosophical question that intrigues you</li>
                    </ul>
                </div>

                <div class="content-card">
                    <h3>🌟 Looking Ahead</h3>
                    <p>Next class: We'll explore the origins of religious thought and begin our journey 
                    through the world's great traditions. Get ready to travel through time and across cultures!</p>
                </div>
            </div>
        </div>

        <!-- Navigation -->
        <div class="navigation">
            <button class="nav-btn" onclick="previousSlide()" id="prevBtn">← Previous</button>
            <button class="nav-btn" onclick="nextSlide()" id="nextBtn">Next →</button>
        </div>

        <!-- Slide Indicators -->
        <div class="slide-indicator" id="slideIndicator"></div>

        <script>
            let currentSlide = 0;
            const slides = document.querySelectorAll('.slide');
            const totalSlides = slides.length;

            // Create slide indicators
            const indicatorContainer = document.getElementById('slideIndicator');
            for (let i = 0; i < totalSlides; i++) {
                const dot = document.createElement('div');
                dot.className = 'indicator-dot';
                if (i === 0) dot.classList.add('active');
                dot.onclick = () => goToSlide(i);
                indicatorContainer.appendChild(dot);
            }

            function showSlide(n) {
                slides[currentSlide].classList.remove('active');
                currentSlide = (n + totalSlides) % totalSlides;
                slides[currentSlide].classList.add('active');
                
                // Update indicators
                document.querySelectorAll('.indicator-dot').forEach((dot, index) => {
                    dot.classList.toggle('active', index === currentSlide);
                });
                
                // Update navigation buttons
                document.getElementById('prevBtn').disabled = currentSlide === 0;
                document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
                
                // Hide timer by default
                document.getElementById('timer').style.display = 'none';
                
                // Start timer if applicable
                if (timerSlides[currentSlide]) {
                    startTimer(timerSlides[currentSlide]);
                }
            }

            function nextSlide() {
                if (currentSlide < totalSlides - 1) {
                    showSlide(currentSlide + 1);
                }
            """
PHL 101 Day 1 - Complete Interactive Philosophy & Religion App
Fixed version with Assignment 1: Philosopher Conversations & Professor Lecture
"""

import streamlit as st
import time
import json
import io
from datetime import datetime
from typing import List, Dict, Optional

# Optional imports for enhanced features
try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

# Configure page
st.set_page_config(
    page_title="PHL 101 - What is Religion? What is Philosophy?",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'timer_end' not in st.session_state:
    st.session_state.timer_end = None
if 'student_responses' not in st.session_state:
    st.session_state.student_responses = {}
if 'quiz_attempts' not in st.session_state:
    st.session_state.quiz_attempts = {}
if 'assignment1_progress' not in st.session_state:
    st.session_state.assignment1_progress = {
        'questions_asked': {'Durkheim': [], 'Tylor': [], 'Tillich': []},
        'responses_received': {'Durkheim': [], 'Tylor': [], 'Tillich': []},
        'notes': {'Durkheim': '', 'Tylor': '', 'Tillich': ''},
        'essays': {'Durkheim': '', 'Tylor': '', 'Tillich': ''},
        'completed_philosophers': set()
    }

# Enhanced slide data with corrected encoding
SLIDES = [
    {
        "id": "welcome",
        "title": "Welcome & Introductions",
        "content": """
        # 📚 What is Religion? What is Philosophy?
        
        ## PHL 101 — Comparative Religions I
        **Professor Xavier Honablue, M.Ed.**
        
        **Background:** Mathematics • Computer Science • Philosophy • Education
        
        > "We're going to explore the great traditions of the world — Judaism, Christianity, Islam, but also Eastern, African, and Indigenous traditions. Our job is not to judge, but to think critically, compare, and engage."
        """,
        "presenter_notes": "Welcome students warmly. Share your background briefly. Set collaborative tone for the semester. Emphasize respect and scholarly inquiry."
    },
    {
        "id": "word_origins",
        "title": "Word Origins: Philosophy",
        "content": """
        # 📖 Word Origins: Philosophy
        
        ## Breaking it Down:
        * **Philo (Greek: φίλος / *phílos*)** → love, affection, friendship
        * **Sophia (Greek: σοφία / *sophía*)** → wisdom, skill, deep knowledge
        
        ### So literally: 👉 **Philosophy = "the love of wisdom"**
        
        ## 🧠 What It Means in Practice
        Philosophy isn't just abstract ideas — it's the *active pursuit* of wisdom:
        * Asking **fundamental questions** (What is real? What is good? What can we know?)
        * Using **reason, logic, and argument** rather than tradition or revelation alone
        * Seeking **clarity** about life's biggest puzzles
        
        ## 🏛 Historical Context
        * Term first widely used by **ancient Greek thinkers** (Pythagoras, Socrates, Plato, Aristotle)
        * At first, *philosophy* included all areas of knowledge — what we now call science, ethics, politics, and metaphysics
        * Over time, philosophy became the discipline of **critical thinking** and **foundations of thought**
        """,
        "presenter_notes": "Ask students: If philosophy is 'love of wisdom,' what counts as wisdom today? Does wisdom mean knowing facts, living well, or something else?",
        "interactive": True,
        "discussion_prompt": "If philosophy is 'love of wisdom,' what counts as *wisdom* today? Does 'wisdom' mean knowing facts, living well, or something else?"
    },
    {
        "id": "objectives",
        "title": "Course Objectives",
        "content": """
        # 🎯 Our Journey Together
        
        ## What We'll Explore:
        * **World Religions:** Christianity, Islam, Judaism, Hinduism, Buddhism, Taoism
        * **Indigenous Traditions:** Native American, African, Australian Aboriginal
        * **Philosophical Approaches:** Western and Eastern philosophical traditions
        * **Critical Thinking:** Comparing beliefs, practices, and worldviews
        * **Personal Reflection:** Understanding your own beliefs and assumptions
        
        ## 🌍 Our Approach
        We approach each tradition with respect, curiosity, and scholarly rigor. We seek to understand rather than judge, to compare rather than compete, and to engage thoughtfully with humanity's greatest questions.
        """,
        "presenter_notes": "Emphasize comparative approach and respect for all traditions. Set expectations for academic rigor combined with personal reflection."
    },
    {
        "id": "icebreaker",
        "title": "Icebreaker Activity",
        "content": """
        # 🤔 The Big Questions
        
        ## Pair Discussion (10 minutes)
        
        ### Discuss with a partner:
        1. **What do you think religion is?**
           - Consider: rituals, beliefs, communities, sacred texts, personal experiences
        
        2. **What do you think philosophy is?**
           - Think about: questioning, reasoning, logic, ethics, exploring fundamental concepts
        
        3. **Where do the two overlap?**
           - Consider: ultimate questions about reality, meaning, morality, existence
        
        ### Share your thoughts, then we'll create our class word cloud!
        """,
        "presenter_notes": "Give students 10 minutes. Walk around and listen to conversations. Take notes for discussion.",
        "timer_minutes": 10,
        "activity_type": "discussion"
    },
    {
        "id": "philosophy_meets_religion",
        "title": "Philosophy Meets Religion",
        "content": """
        # 🧠 Philosophy Meets Religion
        
        ## 📚 Philosophy
        **From Greek: "Philosophia" = Love of Wisdom**
        * Asking fundamental questions
        * Using reason and logic
        * Challenging assumptions
        * Seeking understanding through inquiry
        * *Key figures: Socrates, Plato, Aristotle, Kant, Nietzsche*
        
        ## 🕊️ Religion
        **From Latin: "Religare" = To Bind Together**
        * Lived traditions and practices
        * Sacred stories and myths
        * Rituals and ceremonies
        * Community and belonging
        * *Key figures: Moses, Jesus, Muhammad, Buddha*
        
        ## 🤝 Both Ask the Same Core Questions:
        * What is ultimate reality?
        * Why are we here?
        * How should we live?
        * What happens after death?
        * What is the meaning of life?
        """,
        "presenter_notes": "Explain etymology and overlapping concerns. Make sure students understand both definitions."
    },
    {
        "id": "examples",
        "title": "Stories of Truth-Seeking",
        "content": """
        # 💡 A Tale of Two Searches
        
        ## 🏛️ Philosophy: Plato's Cave
        **The Story:** Prisoners chained in a cave mistake shadows on the wall for reality until one escapes and discovers the true world of sunlight.
        
        **The Message:** We must question what we think we know. True knowledge comes through reason, not just accepting what we see.
        
        **The Search:** Truth through questioning and rational inquiry.
        
        ---
        
        ## ⛰️ Religion: Moses and the Exodus
        **The Story:** Moses leads the Israelites out of slavery in Egypt, receives the Ten Commandments, and guides them to the Promised Land.
        
        **The Message:** God liberates the oppressed and provides moral guidance for how to live.
        
        **The Search:** Freedom and meaning through divine revelation and community.
        
        ## 🎯 Both Stories Share:
        **A journey from darkness to light, from bondage to freedom, from ignorance to truth.**
        They represent humanity's eternal quest to understand reality and find meaning.
        """,
        "presenter_notes": "Compare narrative arcs. Show how both philosophy and religion address human needs for understanding and meaning."
    },
    {
        "id": "sorting_activity",
        "title": "Group Activity: Sorting Questions",
        "content": """
        # 🎲 Activity: Sorting the Big Questions
        
        ## Small Groups (15 minutes)
        
        ### Your Mission:
        Sort these questions into three categories: **Philosophy**, **Religion**, or **Both**
        
        ### The Questions:
        * Does God exist?
        * What happens after we die?
        * Why is there suffering?
        * What is justice?
        * Do humans have free will?
        * What is the meaning of life?
        * How should we treat others?
        * What is consciousness?
        * Is there absolute truth?
        * What is love?
        
        ### Prediction:
        Most questions will end up in the **"Both"** category! This shows how philosophy and religion are deeply interconnected.
        """,
        "presenter_notes": "Give groups time to discuss. Encourage debate. The goal is for them to see most questions belong to 'both' categories.",
        "timer_minutes": 15,
        "activity_type": "group_work"
    },
    {
        "id": "defining_religion",
        "title": "Defining Religion",
        "content": """
        # 🔬 How Scholars Define Religion
        
        ## Three Famous Definitions:
        
        ### 👥 Émile Durkheim (1858-1917)
        **"Religion is the social glue that binds communities together."**
        
        *Focus:* Religion creates solidarity, shared identity, and moral order in society. Think of how religious holidays bring families together, or how shared beliefs unite communities.
        
        ### 👻 Edward Tylor (1832-1917)
        **"Religion is belief in spiritual beings."**
        
        *Focus:* At its core, religion involves belief in gods, spirits, souls, or supernatural forces. From ancestor worship to monotheism, spiritual beings are central.
        
        ### 💖 Paul Tillich (1886-1965)
        **"Religion is ultimate concern."**
        
        *Focus:* Religion addresses what matters most to us - our deepest values, fears, and hopes. It's about what we're willing to sacrifice everything for.
        
        ## 🤔 Discussion Question:
        Which definition resonates most with you? Why? Can you think of examples that fit one definition but not the others?
        """,
        "presenter_notes": "Ask students which resonates most. This is where students start to see the complexity of defining religion."
    },
    {
        "id": "debate",
        "title": "Interactive Debate",
        "content": """
        # 💬 Let's Debate!
        
        ## Team Up and Defend Your Definition:
        
        ### 🤝 Team Durkheim - "Religion = Social Glue"
        * Explains why religion is found in every society
        * Shows religion's practical social function
        * Helps understand religious conflicts
        * *Examples: Christmas bringing families together, Islamic community prayers*
        
        ### 👻 Team Tylor - "Religion = Spiritual Beings"
        * Clear, specific definition
        * Distinguishes religion from philosophy
        * Explains prayer, worship, and ritual
        * *Examples: Hindu gods, Christian Trinity, ancestor spirits*
        
        ### 💖 Team Tillich - "Religion = Ultimate Concern"
        * Includes secular "religions" (nationalism, sports)
        * Focuses on personal meaning
        * Explains religious passion and devotion
        * *Examples: Environmental activism as religion, patriotism*
        
        ## 🎯 Challenge Question:
        **Is Buddhism a religion?** How would each definition handle this case?
        
        *(Buddhism often lacks belief in gods but has communities, practices, and ultimate concerns about suffering and enlightenment.)*
        """,
        "presenter_notes": "Moderate debate. Let students get passionate - that means they're engaged! Pose the Buddhism challenge."
    },
    {
        "id": "wrap_up",
        "title": "Wrap-Up & Next Steps",
        "content": """
        # 🎯 Exit Ticket & Next Steps
        
        ## 📝 Before You Leave:
        Write on a card: **One question about life/religion you hope this class will answer.**
        
        *We'll revisit these at the end of the semester to see how our journey has evolved your thinking!*
        
        ## 🏠 Homework (Fun & Low-Stakes):
        * **Watch:** Choose one video from our Resources page
        * **Write:** One paragraph answering: "How do you personally define religion?"
        * **Reflect:** Think about a religious or philosophical question that intrigues you
        
        ## 🌟 Looking Ahead - Day 2 Preview:
        Next class we'll explore:
        * **Premise:** Basic building blocks of arguments
        * **Contradiction:** Incompatible claims that cannot both be true
        * **Logic:** Deductive vs. inductive reasoning
        * **Fallacies:** Common mistakes in reasoning (straw man, ad hominem, false cause)
        * **Absurdity:** Reductio ad absurdum - showing positions lead to absurd conclusions
        
        Get ready to develop your philosophical toolkit!
        """,
        "presenter_notes": "Collect exit tickets - valuable data for shaping the course. Preview Day 2 on argument structure."
    }
]

# Assignment 1 Philosopher Profiles for LLM
PHILOSOPHER_PROFILES = {
    "Durkheim": {
        "name": "Émile Durkheim",
        "years": "1858-1917",
        "background": "I am a French sociologist who founded the academic discipline of sociology. I studied how societies hold together and function, with particular interest in the role of religion in creating social solidarity.",
        "key_ideas": [
            "Religion is the social glue that binds communities together",
            "Sacred rituals create 'collective effervescence' - shared emotional experiences that unite people",
            "Religious beliefs reflect society's deepest values and moral order",
            "Modern societies shift from mechanical solidarity (similarity) to organic solidarity (interdependence)"
        ],
        "on_premise": "A premise must be grounded in empirical observation of social facts. I believe in studying society scientifically, so any premise about religion should be based on observable social phenomena, not personal beliefs.",
        "on_contradiction": "Contradictions in religious thought often reflect tensions within society itself. When religious ideas contradict each other, look for the underlying social conflicts they represent.",
        "on_logic": "Logic in sociology must be inductive - we observe patterns in social behavior and draw conclusions. Deductive reasoning from abstract principles misses the lived reality of how people actually behave in groups.",
        "on_fallacy": "The greatest fallacy is methodological individualism - trying to explain social phenomena by looking only at individuals. Society is more than the sum of its parts.",
        "on_absurdity": "What appears absurd in religious practice often serves vital social functions. Seemingly irrational rituals create the very social bonds that hold communities together.",
        "personality": "methodical, scientific, focused on empirical observation, believes strongly in the power of sociology to understand human behavior"
    },
    "Tylor": {
        "name": "Edward Burnett Tylor",
        "years": "1832-1917",
        "background": "I am an English anthropologist, often called the father of cultural anthropology. I developed evolutionary theories of culture and religion, studying how beliefs develop from primitive to advanced forms.",
        "key_ideas": [
            "Religion is belief in spiritual beings - this is the minimum definition",
            "Culture is 'that complex whole which includes knowledge, belief, art, morals, law, custom'",
            "Religious beliefs evolved from animism (spirits in objects) to polytheism to monotheism",
            "All cultures can be arranged on an evolutionary scale from savage to civilized"
        ],
        "on_premise": "A sound premise about religion must identify the essential element present in all religious systems. I argue this is belief in spiritual beings - gods, souls, spirits, or supernatural forces.",
        "on_contradiction": "Contradictions arise when we confuse the essential core of religion with its cultural variations. The belief in spiritual beings is universal; how societies express this varies widely.",
        "on_logic": "Logic requires clear definitions and careful comparison across cultures. We must distinguish between the universal elements of human thought and their particular cultural expressions.",
        "on_fallacy": "A common fallacy is cultural relativism taken too far - assuming all beliefs are equally valid. Some represent more advanced reasoning about the spiritual realm than others.",
        "on_absurdity": "What seems absurd in so-called 'primitive' religions often represents early attempts at scientific thinking - trying to explain natural phenomena through spiritual causation.",
        "personality": "confident in evolutionary progress, believes in objective scientific study of culture, somewhat paternalistic toward 'primitive' peoples but genuinely curious about human diversity"
    },
    "Tillich": {
        "name": "Paul Tillich",
        "years": "1886-1965",
        "background": "I am a German-American theologian and philosopher. I lived through both World Wars and experienced exile from Nazi Germany. I sought to bridge theology and modern philosophy, making religious thought relevant to contemporary life.",
        "key_ideas": [
            "Religion is ultimate concern - what matters most deeply to a person",
            "God is not a being but Being-itself, the ground of all existence",
            "Faith is not belief despite evidence, but ultimate concern about ultimate reality",
            "Secular movements can be religious if they involve ultimate commitment (nationalism, communism, etc.)"
        ],
        "on_premise": "A premise is religious if it deals with ultimate questions - not preliminary concerns like science or politics, but the final questions of existence, meaning, and value.",
        "on_contradiction": "Contradictions often arise when we confuse the finite with the infinite, or when ultimate concerns compete. True religion transcends these apparent contradictions.",
        "on_logic": "Religious logic is not the same as scientific logic. Religious truth is existential - it grasps us with ultimate concern rather than being grasped by our rational faculties.",
        "on_fallacy": "The greatest fallacy is literalism - treating religious symbols as if they were scientific descriptions. Religious language is symbolic, pointing beyond itself to ultimate reality.",
        "on_absurdity": "What seems absurd to scientific reason may reveal profound existential truth. The 'absurd' often points to the limits of finite reason when confronting the infinite.",
        "personality": "deeply philosophical, concerned with meaning and existence, bridges academic and pastoral concerns, speaks to modern anxiety and alienation"
    }
}

# Quiz questions with detailed explanations
QUIZ_DATA = {
    "definitions_quiz": {
        "title": "Understanding Definitions of Religion",
        "questions": [
            {
                "question": "According to Durkheim, religion primarily functions as:",
                "options": [
                    "A belief system about supernatural beings",
                    "Social glue that binds communities together", 
                    "Individual's ultimate concern",
                    "A search for absolute truth"
                ],
                "correct": 1,
                "explanation": "Durkheim emphasized religion's social function - shared rituals create solidarity and moral order in society. Think of how religious holidays bring families together or how shared beliefs unite communities."
            },
            {
                "question": "Tylor's definition focuses on:",
                "options": [
                    "Community rituals and practices",
                    "Personal meaning and values",
                    "Belief in spiritual beings",
                    "Social solidarity"
                ],
                "correct": 2,
                "explanation": "Tylor defined religion as 'belief in spiritual beings' - gods, spirits, souls, or supernatural forces. This definition emphasizes the metaphysical aspect of religion."
            },
            {
                "question": "Which definition would BEST explain why some people treat sports teams like a religion?",
                "options": [
                    "Durkheim's social glue",
                    "Tylor's spiritual beings", 
                    "Tillich's ultimate concern",
                    "None of these definitions"
                ],
                "correct": 2,
                "explanation": "Tillich's 'ultimate concern' definition would best explain this - sports can become what matters most to someone, what they're willing to sacrifice time, money, and energy for, even without supernatural beliefs."
            },
            {
                "question": "Buddhism presents a challenge to which definition of religion?",
                "options": [
                    "Only Durkheim's definition",
                    "Only Tylor's definition",
                    "Only Tillich's definition", 
                    "All three definitions work well for Buddhism"
                ],
                "correct": 1,
                "explanation": "Buddhism challenges Tylor's definition because many Buddhist traditions don't center on belief in gods or supernatural beings, but focus on practices for ending suffering and achieving enlightenment."
            }
        ]
    },
    "philosophy_basics": {
        "title": "Philosophy Fundamentals",
        "questions": [
            {
                "question": "The word 'philosophy' literally means:",
                "options": [
                    "Deep thinking",
                    "Love of wisdom",
                    "Search for truth", 
                    "Rational inquiry"
                ],
                "correct": 1,
                "explanation": "From Greek: 'philo' (love) + 'sophia' (wisdom) = love of wisdom. This emphasizes philosophy as an active pursuit and desire for understanding, not just abstract thinking."
            },
            {
                "question": "Both Plato's Cave and the Exodus story represent:",
                "options": [
                    "The importance of community",
                    "Belief in supernatural beings",
                    "A journey from ignorance to truth/freedom",
                    "The need for moral laws"
                ],
                "correct": 2,
                "explanation": "Both stories follow the same basic pattern: people start in bondage/ignorance, undergo a difficult journey, and emerge into light/truth/freedom. This represents humanity's quest for understanding and meaning."
            }
        ]
    }
}

# Assignment 1: Five Required Question Types
ARGUMENT_STRUCTURE_CONCEPTS = {
    "premise": {
        "definition": "The basic building blocks of arguments - the foundational claims or assumptions from which conclusions are drawn",
        "example": "Premise 1: All humans are mortal. Premise 2: Socrates is human. Conclusion: Therefore, Socrates is mortal."
    },
    "contradiction": {
        "definition": "Two or more claims that cannot all be true at the same time; they are logically incompatible",
        "example": "It cannot be both true that 'God knows everything that will happen' AND 'humans have free will to choose differently.'"
    },
    "logic": {
        "definition": "The study of valid reasoning; includes deductive logic (general to specific) and inductive logic (specific to general patterns)",
        "example": "Deductive: All religions involve ritual (general) → Buddhism involves ritual (specific). Inductive: This church, that mosque, and this temple all bring people together → Religion brings people together (pattern)."
    },
    "fallacy": {
        "definition": "Common errors in reasoning that make arguments invalid or weak, such as straw man, ad hominem, or false cause",
        "example": "Ad hominem fallacy: 'You can't trust Durkheim's theory about religion because he wasn't religious himself.'"
    },
    "absurdity": {
        "definition": "Reductio ad absurdum - a logical technique that shows a position must be false because it leads to absurd or contradictory conclusions",
        "example": "If Tylor's definition is right and religion requires belief in spiritual beings, then Buddhism isn't a religion - but that seems absurd since Buddhism is clearly religious."
    }
}

# Enhanced resources with current, engaging content
RESOURCES = {
    "videos": [
        {
            "title": "What is Philosophy? - Crash Course Philosophy #1",
            "url": "https://www.youtube.com/watch?v=1A_CAkYt3GY",
            "description": "Hank Green introduces philosophy with humor and clarity",
            "duration": "8 minutes"
        },
        {
            "title": "What is Religion? - TED-Ed",
            "url": "https://www.youtube.com/watch?v=xQq2V8C8XwQ", 
            "description": "Animated exploration of different definitions of religion",
            "duration": "5 minutes"
        },
        {
            "title": "Philosophy of Religion - Crash Course Philosophy #30",
            "url": "https://www.youtube.com/watch?v=k6u3Qw4XlfQ",
            "description": "Deep dive into how philosophy approaches religious questions",
            "duration": "10 minutes"
        },
        {
            "title": "The Cave: An Adaptation of Plato's Allegory",
            "url": "https://www.youtube.com/watch?v=1RWOpQXTltA",
            "description": "Beautiful animated version of Plato's famous allegory",
            "duration": "7 minutes"
        }
    ],
    "articles": [
        {
            "title": "Stanford Encyclopedia: Philosophy of Religion",
            "url": "https://plato.stanford.edu/entries/philosophy-religion/",
            "description": "Comprehensive academic overview"
        },
        {
            "title": "Internet Encyclopedia: Defining Religion",
            "url": "https://iep.utm.edu/religion/",
            "description": "Accessible discussion of different approaches to defining religion"
        }
    ]
}

def get_philosopher_response(philosopher_name: str, question: str, question_type: str, openai_api_key: str = None) -> str:
    """Generate a response from the specified philosopher based on their profile and the question type"""
    
    if not openai_api_key and not HAS_OPENAI:
        return f"""
        **{philosopher_name} responds** *(Note: This is a simulated response - connect your OpenAI API key for dynamic conversations)*:
        
        Based on my understanding of {question_type}, I would say that your question touches on fundamental issues about how we understand religious phenomena. Each of us - Durkheim, Tylor, and Tillich - approaches these questions from our unique perspectives shaped by our historical contexts and intellectual frameworks.
        
        Please provide your OpenAI API key in the sidebar to have dynamic conversations with us!
        """
    
    if not openai_api_key:
        # Return a static response based on the philosopher and question type
        profile = PHILOSOPHER_PROFILES[philosopher_name]
        concept_info = ARGUMENT_STRUCTURE_CONCEPTS.get(question_type, {})
        
        response_templates = {
            "premise": f"As {profile['name']}, I believe that any premise about religion must {profile.get('on_premise', 'be carefully considered')}",
            "contradiction": f"Regarding contradictions, I {profile['name']} would say: {profile.get('on_contradiction', 'they reveal important tensions in human thought')}",
            "logic": f"When it comes to logic, I {profile['name']} argue that {profile.get('on_logic', 'we must use systematic reasoning')}",
            "fallacy": f"About fallacies, I {profile['name']} warn that {profile.get('on_fallacy', 'we must avoid common errors in reasoning')}",
            "absurdity": f"Concerning what seems absurd, I {profile['name']} believe {profile.get('on_absurdity', 'we must look deeper for underlying truth')}"
        }
        
        return response_templates.get(question_type, f"I {profile['name']} find your question about {question_type} quite thought-provoking...")
    
    # Use OpenAI API for dynamic responses
    try:
        openai.api_key = openai_api_key
        profile = PHILOSOPHER_PROFILES[philosopher_name]
        concept = ARGUMENT_STRUCTURE_CONCEPTS.get(question_type, {})
        
        system_prompt = f"""
        You are {profile['name']} ({profile['years']}), responding to a philosophy student's question.
        
        Your background: {profile['background']}
        
        Your key ideas: {', '.join(profile['key_ideas'])}
        
        Your personality: {profile['personality']}
        
        The student is asking about '{question_type}' which is defined as: {concept.get('definition', 'a concept in argument structure')}
        
        Respond in character as {profile['name']}, drawing on your specific view of religion and your approach to {question_type}. Be educational but maintain your historical perspective and personality. Keep your response to 2-3 paragraphs and address their specific question about {question_type}.
        """
        
        user_message = f"Professor {profile['name']}, I'm studying argument structure and have a question about {question_type}: {question}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error generating response: {str(e)}. Please check your API key."

def display_professor_lecture():
    """Display the beautiful HTML presentation"""
    st.markdown("# 🎓 Professor Lecture - Interactive Presentation")
    st.markdown("*Click the presentation below to begin the interactive lecture*")
    
    # Embed the HTML presentation
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>What is Religion? What is Philosophy?</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                overflow: hidden;
            }

            .presentation-container {
                width: 100vw;
                height: 100vh;
                position: relative;
            }

            .slide {
                width: 100%;
                height: 100%;
                display: none;
                padding: 60px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                position: relative;
                overflow-y: auto;
            }

            .slide.active {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .slide-number {
                position: absolute;
                top: 20px;
                right: 30px;
                background: rgba(102, 126, 234, 0.8);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
            }

            h1 {
                font-size: 3.5em;
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                animation: fadeInUp 1s ease-out;
            }

            h2 {
                font-size: 2.8em;
                color: #34495e;
                text-align: center;
                margin-bottom: 40px;
                animation: fadeInUp 1s ease-out 0.2s both;
            }

            h3 {
                font-size: 2em;
                color: #2980b9;
                margin-bottom: 25px;
                text-align: center;
                animation: fadeInUp 1s ease-out 0.4s both;
            }

            .subtitle {
                font-size: 1.3em;
                color: #7f8c8d;
                text-align: center;
                margin-bottom: 50px;
                font-style: italic;
                animation: fadeInUp 1s ease-out 0.3s both;
            }

            .course-info {
                background: rgba(255, 255, 255, 0.9);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
                margin-bottom: 40px;
                animation: slideInUp 1s ease-out 0.5s both;
            }

            .content-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                width: 100%;
                max-width: 1200px;
                margin: 0 auto;
            }

            .content-card {
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                transform: translateY(20px);
                opacity: 0;
                animation: slideInUp 0.8s ease-out forwards;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .content-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            }

            .content-card:nth-child(1) { animation-delay: 0.1s; }
            .content-card:nth-child(2) { animation-delay: 0.3s; }
            .content-card:nth-child(3) { animation-delay: 0.5s; }

            .navigation {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 15px;
                z-index: 1000;
            }

            .nav-btn {
                background: rgba(102, 126, 234, 0.9);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }

            .nav-btn:hover {
                background: rgba(102, 126, 234, 1);
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes slideInUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="presentation-container">
            <!-- Slide 1: Title -->
            <div class="slide active">
                <div class="slide-number">1 / 9</div>
                <h1>📚 What is Religion?<br>What is Philosophy?</h1>
                <div class="course-info">
                    <h3>PHL 101 — Comparative Religions I</h3>
                    <p class="subtitle">Professor Xavier Honablue, M.Ed.</p>
                    <p><strong>Background: Mathematics • Computer Science • Philosophy • Education</strong></p>
                </div>
                <div class="subtitle">
                    "We're going to explore the great traditions of the world — Judaism, Christianity, Islam, 
                    but also Eastern, African, and Indigenous traditions. Our job is not to judge, 
                    but to think critically, compare, and engage."
                </div>
            </div>

            <!-- Additional slides would continue here -->
            <div class="slide">
                <div class="slide-number">2 / 9</div>
                <h2>Our Journey Together</h2>
                <div class="content-card">
                    <h3>What We'll Explore:</h3>
                    <ul style="text-align: left; margin: 20px 0;">
                        <li><strong>World Religions:</strong> Christianity, Islam, Judaism, Hinduism, Buddhism, Taoism</li>
                        <li><strong>Indigenous Traditions:</strong> Native American, African, Australian Aboriginal</li>
                        <li><strong>Philosophical Approaches:</strong> Western and Eastern philosophical traditions</li>
                        <li><strong>Critical Thinking:</strong> Comparing beliefs, practices, and worldviews</li>
                        <li><strong>Personal Reflection:</strong> Understanding your own beliefs and assumptions</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Navigation -->
        <div class="navigation">
            <button class="nav-btn" onclick="previousSlide()" id="prevBtn">← Previous</button>
            <button class="nav-btn" onclick="nextSlide()" id="nextBtn">Next →</button>
        </div>

        <script>
            let currentSlide = 0;
            const slides = document.querySelectorAll('.slide');
            const totalSlides = slides.length;

            function showSlide(n) {
                slides[currentSlide].classList.remove('active');
                currentSlide = (n + totalSlides) % totalSlides;
                slides[currentSlide].classList.add('active');
                
                document.getElementById('prevBtn').disabled = currentSlide === 0;
                document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
            }

            function nextSlide() {
                if (currentSlide < totalSlides - 1) {
                    showSlide(currentSlide + 1);
                }
            }

            function previousSlide() {
                if (currentSlide > 0) {
                    showSlide(currentSlide - 1);
                }
            }

            // Keyboard navigation
            document.addEventListener('keydown', function(e) {
                if (e.key === 'ArrowRight' || e.key === ' ') {
                    nextSlide();
                } else if (e.key === 'ArrowLeft') {
                    previousSlide();
                }
            });

            // Initialize
            showSlide(0);
        </script>
    </body>
    </html>
    """
    
    # Display the HTML in a component
    st.components.v1.html(html_content, height=600, scrolling=True)
    
    st.markdown("---")
    st.markdown("**Navigation Instructions:**")
    st.markdown("- Use arrow keys or click Previous/Next buttons")
    st.markdown("- Press 'F' for fullscreen mode")
    st.markdown("- Press 'N' to toggle presenter notes")

def display_assignment1():
    """Display Assignment 1: Philosopher Conversations"""
    st.markdown("# 📝 Assignment 1: Philosopher Conversations")
    st.markdown("## Explore Argument Structure Through Dialog")
    
    # Instructions
    with st.expander("📋 Assignment Instructions", expanded=True):
        st.markdown("""
        ### Your Mission:
        You will have conversations with three philosophers about **argument structure concepts**:
        
        **The Five Required Question Types:**
        1. **Premise** - Basic building blocks of arguments
        2. **Contradiction** - Claims that cannot both be true
        3. **Logic** - Valid reasoning (deductive/inductive)
        4. **Fallacy** - Common errors in reasoning
        5. **Absurdity** - Reductio ad absurdum technique
        
        ### Requirements:
        - Ask **each philosopher** at least **one question** about **each concept** (5 questions per philosopher minimum)
        - Take **notes** on their responses
        - Write a **150-200 word essay** about what you learned from each philosopher
        
        ### The Philosophers:
        - **Émile Durkheim** (1858-1917): Religion as social glue
        - **Edward Tylor** (1832-1917): Religion as belief in spiritual beings  
        - **Paul Tillich** (1886-1965): Religion as ultimate concern
        """)
    
    # API Key input
    st.sidebar.markdown("### 🔑 OpenAI Configuration")
    openai_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key for dynamic conversations")
    
    if not openai_key:
        st.info("💡 **Tip:** Add your OpenAI API key in the sidebar for dynamic philosopher conversations!")
    
    # Progress tracking
    st.markdown("## 📊 Your Progress")
    
    progress_data = st.session_state.assignment1_progress
    
    # Progress visualization
    col1, col2, col3 = st.columns(3)
    
    with col1:
        durkheim_questions = len(progress_data['questions_asked']['Durkheim'])
        st.metric("Durkheim Questions", f"{durkheim_questions}/5")
        if durkheim_questions >= 5:
            st.success("✅ Complete")
    
    with col2:
        tylor_questions = len(progress_data['questions_asked']['Tylor'])
        st.metric("Tylor Questions", f"{tylor_questions}/5")
        if tylor_questions >= 5:
            st.success("✅ Complete")
    
    with col3:
        tillich_questions = len(progress_data['questions_asked']['Tillich'])
        st.metric("Tillich Questions", f"{tillich_questions}/5")
        if tillich_questions >= 5:
            st.success("✅ Complete")
    
    # Philosopher selection
    st.markdown("## 💬 Choose Your Conversation Partner")
    
    philosopher = st.selectbox(
        "Select a philosopher to talk with:",
        ["Durkheim", "Tylor", "Tillich"],
        format_func=lambda x: f"{PHILOSOPHER_PROFILES[x]['name']} ({PHILOSOPHER_PROFILES[x]['years']})"
    )
    
    # Display philosopher info
    profile = PHILOSOPHER_PROFILES[philosopher]
    with st.expander(f"📚 About {profile['name']}", expanded=False):
        st.markdown(f"**Years:** {profile['years']}")
        st.markdown(f"**Background:** {profile['background']}")
        st.markdown("**Key Ideas:**")
        for idea in profile['key_ideas']:
            st.markdown(f"- {idea}")
    
    # Question type and input
    st.markdown(f"## 🗣️ Conversation with {profile['name']}")
    
    question_type = st.selectbox(
        "What concept do you want to ask about?",
        ["premise", "contradiction", "logic", "fallacy", "absurdity"],
        format_func=lambda x: f"{x.title()} - {ARGUMENT_STRUCTURE_CONCEPTS[x]['definition'][:50]}..."
    )
    
    # Show concept definition
    concept = ARGUMENT_STRUCTURE_CONCEPTS[question_type]
    st.info(f"**{question_type.title()}:** {concept['definition']}")
    st.markdown(f"**Example:** {concept['example']}")
    
    # Question input
    user_question = st.text_area(
        f"Ask {profile['name']} about {question_type}:",
        placeholder=f"Example: How do you think about {question_type} when studying religion?",
        key=f"question_{philosopher}_{question_type}"
    )
    
    # Ask question button
    if st.button(f"Ask {profile['name']}", key=f"ask_{philosopher}_{question_type}"):
        if user_question.strip():
            # Generate response
            with st.spinner(f"💭 {profile['name']} is thinking..."):
                response = get_philosopher_response(philosopher, user_question, question_type, openai_key)
            
            # Display response
            st.markdown(f"### 🎭 {profile['name']} responds:")
            st.markdown(response)
            
            # Save to progress
            progress_data['questions_asked'][philosopher].append({
                'type': question_type,
                'question': user_question,
                'timestamp': datetime.now().isoformat()
            })
            
            progress_data['responses_received'][philosopher].append({
                'type': question_type,
                'question': user_question,
                'response': response,
                'timestamp': datetime.now().isoformat()
            })
            
            st.success("Question and response saved to your progress!")
        else:
            st.warning("Please enter a question first!")
    
    # Notes section
    st.markdown(f"## 📝 Your Notes on {profile['name']}")
    
    notes_key = f"notes_{philosopher}"
    current_notes = st.text_area(
        f"Take notes on {profile['name']}'s responses:",
        value=progress_data['notes'][philosopher],
        height=150,
        key=notes_key,
        placeholder="What insights did you gain? How does their perspective on argument structure relate to their view of religion?"
    )
    
    if st.button(f"Save Notes for {profile['name']}", key=f"save_notes_{philosopher}"):
        progress_data['notes'][philosopher] = current_notes
        st.success("Notes saved!")
    
    # Essay section
    if len(progress_data['questions_asked'][philosopher]) >= 5:
        st.markdown(f"## ✍️ Essay about {profile['name']}")
        st.success(f"You've asked {profile['name']} all 5 required questions! Now write your essay.")
        
        essay_key = f"essay_{philosopher}"
        current_essay = st.text_area(
            f"Write 150-200 words about what you learned from {profile['name']} regarding argument structure:",
            value=progress_data['essays'][philosopher],
            height=200,
            key=essay_key,
            placeholder=f"Based on your conversations with {profile['name']}, what did you learn about how they approach premises, contradictions, logic, fallacies, and absurdity? How does their perspective on argument structure connect to their definition of religion?"
        )
        
        # Word count
        word_count = len(current_essay.split()) if current_essay else 0
        
        if word_count < 150:
            st.warning(f"Word count: {word_count}/150 (minimum) - Need {150-word_count} more words")
        elif word_count > 200:
            st.warning(f"Word count: {word_count}/200 (maximum) - Remove {word_count-200} words")
        else:
            st.success(f"Word count: {word_count} - Perfect length!")
        
        if st.button(f"Submit Essay for {profile['name']}", key=f"submit_essay_{philosopher}"):
            if 150 <= word_count <= 200:
                progress_data['essays'][philosopher] = current_essay
                progress_data['completed_philosophers'].add(philosopher)
                st.balloons()
                st.success(f"Essay submitted successfully for {profile['name']}!")
            else:
                st.error("Essay must be between 150-200 words.")
    
    # Overall progress
    st.markdown("## 🎯 Overall Assignment Progress")
    
    total_questions = sum(len(questions) for questions in progress_data['questions_asked'].values())
    total_essays = len(progress_data['completed_philosophers'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Questions Asked", f"{total_questions}/15")
    with col2:
        st.metric("Essays Completed", f"{total_essays}/3")
    
    # Check completion
    if total_questions >= 15 and total_essays >= 3:
        st.balloons()
        st.success("🎉 **Assignment 1 Complete!** You've successfully completed all conversations and essays.")
        
        # Export option
        if st.button("📄 Export Assignment 1 Results"):
            export_data = {
                'assignment': 'Assignment 1: Philosopher Conversations',
                'completion_date': datetime.now().isoformat(),
                'questions_and_responses': progress_data['responses_received'],
                'notes': progress_data['notes'],
                'essays': progress_data['essays'],
                'statistics': {
                    'total_questions': total_questions,
                    'total_essays': total_essays,
                    'completed_philosophers': list(progress_data['completed_philosophers'])
                }
            }
            
            json_str = json.dumps(export_data, indent=2)
            st.download_button(
                "Download Assignment Results",
                json_str,
                file_name=f"assignment1_results_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )

def display_slide(slide_data: dict) -> None:
    """Display a slide with enhanced formatting"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown(slide_data["content"])
        
        # Add interactive elements for specific slides
        if slide_data.get("interactive"):
            if "discussion_prompt" in slide_data:
                st.markdown("---")
                st.markdown("### 💭 Discussion Prompt:")
                st.info(slide_data["discussion_prompt"])
                
                # Student response area
                response_key = f"response_{slide_data['id']}"
                response = st.text_area(
                    "Share your thoughts:", 
                    key=response_key,
                    placeholder="What do you think? Type your response here..."
                )
                if response:
                    st.session_state.student_responses[response_key] = response
                    st.success("Response saved!")
    
    with col2:
        # Timer display
        if st.session_state.timer_active and st.session_state.timer_end:
            remaining = st.session_state.timer_end - time.time()
            if remaining > 0:
                mins, secs = divmod(int(remaining), 60)
                st.markdown(f"""
                <div style="background: linear-gradient(45deg, #ff6b6b, #ee5a24); 
                           color: white; padding: 15px; border-radius: 10px; text-align: center;">
                    <h3>⏰ Timer</h3>
                    <h2>{mins:02d}:{secs:02d}</h2>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)
                st.rerun()
            else:
                st.balloons()
                st.success("⏰ Time's up!")
                st.session_state.timer_active = False

def start_timer(minutes: int) -> None:
    """Start activity timer"""
    st.session_state.timer_active = True
    st.session_state.timer_end = time.time() + (minutes * 60)

def display_quiz(quiz_id: str) -> None:
    """Display interactive quiz"""
    if quiz_id not in QUIZ_DATA:
        st.error("Quiz not found!")
        return
        
    quiz = QUIZ_DATA[quiz_id]
    st.markdown(f"## 📝 {quiz['title']}")
    
    # Track attempts
    if quiz_id not in st.session_state.quiz_attempts:
        st.session_state.quiz_attempts[quiz_id] = 0
    
    with st.form(f"quiz_{quiz_id}"):
        answers = {}
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            answer = st.radio(
                "Choose your answer:",
                options=q["options"],
                key=f"q_{quiz_id}_{i}",
                index=None
            )
            if answer:
                answers[i] = q["options"].index(answer)
        
        submitted = st.form_submit_button("Submit Quiz")
        
        if submitted and len(answers) == len(quiz["questions"]):
            st.session_state.quiz_attempts[quiz_id] += 1
            
            # Grade quiz
            correct_count = 0
            total_questions = len(quiz["questions"])
            
            st.markdown("---")
            st.markdown("### 📊 Results:")
            
            for i, q in enumerate(quiz["questions"]):
                if i in answers:
                    is_correct = answers[i] == q["correct"]
                    if is_correct:
                        correct_count += 1
                        st.success(f"✅ Question {i+1}: Correct!")
                    else:
                        st.error(f"❌ Question {i+1}: Incorrect")
                        st.info(f"**Correct answer:** {q['options'][q['correct']]}")
                    
                    # Show explanation
                    st.markdown(f"**Explanation:** {q['explanation']}")
                    st.markdown("---")
            
            # Overall score
            score_pct = (correct_count / total_questions) * 100
            
            if score_pct >= 80:
                st.balloons()
                st.success(f"Excellent work! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            elif score_pct >= 60:
                st.success(f"Good job! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            else:
                st.warning(f"Keep studying! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")

def display_resources() -> None:
    """Display enhanced resources page"""
    st.markdown("# 📚 Learning Resources")
    st.markdown("Explore these carefully selected resources to deepen your understanding!")
    
    # Videos section
    st.markdown("## Videos")
    col1, col2 = st.columns(2)
    
    for i, video in enumerate(RESOURCES["videos"]):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"### {video['title']}")
            st.markdown(f"{video['description']}")
            st.markdown(f"**Duration:** {video['duration']}")
            st.markdown(f"[Watch Now]({video['url']})")
            st.markdown("---")
    
    # Articles section
    st.markdown("## Articles & Readings")
    for article in RESOURCES["articles"]:
        st.markdown(f"- **[{article['title']}]({article['url']})** - {article['description']}")

def sidebar_navigation() -> str:
    """Enhanced sidebar with navigation and controls"""
    st.sidebar.markdown("# 📚 PHL 101 Day 1")
    
    # Mode selection
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["📊 Presentation", "🎓 Professor Lecture", "📝 Assignment 1", "🧠 Quizzes", "📚 Resources"]
    )
    
    if mode == "📊 Presentation":
        st.sidebar.markdown("## Slide Navigation")
        
        # Slide selector
        slide_titles = [f"{i+1}. {slide['title']}" for i, slide in enumerate(SLIDES)]
        selected_slide = st.sidebar.selectbox(
            "Jump to slide:",
            options=range(len(SLIDES)),
            format_func=lambda x: slide_titles[x],
            index=st.session_state.current_slide
        )
        
        if selected_slide != st.session_state.current_slide:
            st.session_state.current_slide = selected_slide
        
        # Navigation buttons
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("⬅️ Previous") and st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
                st.rerun()
        
        with col2:
            if st.button("Next ➡️") and st.session_state.current_slide < len(SLIDES) - 1:
                st.session_state.current_slide += 1
                st.rerun()
        
        # Timer controls
        current_slide = SLIDES[st.session_state.current_slide]
        if "timer_minutes" in current_slide:
            st.sidebar.markdown("---")
            st.sidebar.markdown("⏰ **Activity Timer**")
            if st.sidebar.button(f"Start {current_slide['timer_minutes']} min timer"):
                start_timer(current_slide["timer_minutes"])
                st.rerun()
        
        # Presenter notes
        st.sidebar.markdown("---")
        if st.sidebar.checkbox("📋 Show Presenter Notes"):
            st.sidebar.markdown("**Notes:**")
            st.sidebar.info(current_slide.get("presenter_notes", "No notes for this slide."))
            
    return mode.split()[1].lower()  # Return just the key part

def main():
    """Main application function"""
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Determine current mode from sidebar
    current_mode = sidebar_navigation()
    
    if current_mode == "presentation":
        # Main presentation mode
        current_slide = SLIDES[st.session_state.current_slide]
        display_slide(current_slide)
        
        # Progress indicator
        progress = (st.session_state.current_slide + 1) / len(SLIDES)
        st.progress(progress)
        st.caption(f"Slide {st.session_state.current_slide + 1} of {len(SLIDES)}")
    
    elif current_mode == "professor":
        display_professor_lecture()
    
    elif current_mode == "assignment":
        display_assignment1()
    
    elif current_mode == "quizzes":
        st.markdown("# 🧠 Knowledge Check Quizzes")
        
        quiz_choice = st.selectbox(
            "Select a quiz:",
            ["definitions_quiz", "philosophy_basics"],
            format_func=lambda x: QUIZ_DATA[x]["title"]
        )
        
        display_quiz(quiz_choice)
    
    elif current_mode == "resources":
        display_resources()

if __name__ == "__main__":
    main()
