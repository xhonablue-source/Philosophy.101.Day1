"""
PHL 101 Day 1 - Complete Interactive Philosophy & Religion App
Combines presentation slides with student activities, quizzes, and resources
"""

import streamlit as st
import time
import json
from datetime import datetime
from typing import List, Dict, Optional

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

# Enhanced slide data with the new word origins content
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
        "title": "Wrap-Up & Homework",
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
        * **Argument Structure:** How to build and evaluate philosophical arguments
        * **Logic:** Deductive vs. inductive reasoning
        * **Fallacies:** Common mistakes in reasoning
        * **Critical Thinking Tools:** For analyzing religious and philosophical claims
        
        Get ready to develop your philosophical toolkit!
        """,
        "presenter_notes": "Collect exit tickets - valuable data for shaping the course. Preview Day 2 on argument structure."
    }
]

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
        },
        {
            "title": "What is Wisdom? - BBC Ideas", 
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "description": "Exploring different concepts of wisdom across cultures",
            "duration": "6 minutes"
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
        },
        {
            "title": "What Is It Like to Be Religious? - The Atlantic",
            "url": "https://www.theatlantic.com/politics/archive/2017/08/what-is-it-like-to-be-religious/537579/",
            "description": "Personal perspectives on religious experience"
        }
    ],
    "interactive": [
        {
            "title": "Philosophy Slam - Interactive Game",
            "url": "https://philosophyslam.org/",
            "description": "Fun way to explore philosophical questions through games"
        },
        {
            "title": "Religion News Service",
            "url": "https://religionnews.com/",
            "description": "Current news and analysis about religion worldwide"
        }
    ]
}

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
                    st.success("Response saved! 📝")
    
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
                st.experimental_rerun()
            else:
                st.balloons()
                st.success("⏰ Time's up!")
                st.session_state.timer_active = False

def start_timer(minutes: int) -> None:
    """Start activity timer"""
    st.session_state.timer_active = True
    st.session_state.timer_end = time.time() + (minutes * 60)

def display_quiz(quiz_id: str) -> None:
    """Display interactive quiz with LLM feedback"""
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
        
        submitted = st.form_submit_button("Submit Quiz 🎯")
        
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
                st.success(f"🎉 Excellent work! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            elif score_pct >= 60:
                st.success(f"👍 Good job! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            else:
                st.warning(f"📚 Keep studying! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            
            # Personalized feedback
            if score_pct < 60:
                st.info("💡 **Tip:** Review the slide content and try the quiz again. Focus on understanding the key differences between Durkheim, Tylor, and Tillich's definitions.")

def display_resources() -> None:
    """Display enhanced resources page"""
    st.markdown("# 📚 Learning Resources")
    st.markdown("Explore these carefully selected resources to deepen your understanding!")
    
    # Videos section
    st.markdown("## 🎥 Videos")
    col1, col2 = st.columns(2)
    
    for i, video in enumerate(RESOURCES["videos"]):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
                <h4>📺 {video['title']}</h4>
                <p>{video['description']}</p>
                <p><strong>Duration:</strong> {video['duration']}</p>
                <a href="{video['url']}" target="_blank" style="text-decoration: none;">
                    <button style="background: #ff4b4b; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer;">
                        ▶️ Watch Now
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    # Articles section
    st.markdown("## 📖 Articles & Readings")
    for article in RESOURCES["articles"]:
        st.markdown(f"""
        - **[{article['title']}]({article['url']})** - {article['description']}
        """)
    
    # Interactive section
    st.markdown("## 🎮 Interactive Resources")
    for resource in RESOURCES["interactive"]:
        st.markdown(f"""
        - **[{resource['title']}]({resource['url']})** - {resource['description']}
        """)
    
    # Study tips
    st.markdown("## 💡 Study Tips")
    st.info("""
    **How to get the most from these resources:**
    1. **Watch actively** - Take notes on key concepts
    2. **Ask questions** - What confuses you? What interests you most?
    3. **Connect ideas** - How do these resources relate to our class discussions?
    4. **Discuss** - Share interesting points with classmates
    5. **Apply** - Try using these concepts to analyze religions you're familiar with
    """)

def sidebar_navigation() -> None:
    """Enhanced sidebar with navigation and controls"""
    st.sidebar.markdown("# 📚 PHL 101 Day 1")
    
    # Mode selection
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["📊 Presentation", "📝 Student Activities", "📚 Resources", "👨‍🎓 Study Guide"]
    )
    
    if mode == "📊 Presentation":
        st.sidebar.markdown("## 🎯 Slide Navigation")
        
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
            st.experimental_rerun()
        
        # Navigation buttons
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("⬅️ Previous") and st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
                st.experimental_rerun()
        
        with col2:
            if st.button("Next ➡️") and st.session_state.current_slide < len(SLIDES) - 1:
                st.session_state.current_slide += 1
                st.experimental_rerun()
        
        # Timer controls
        current_slide = SLIDES[st.session_state.current_slide]
        if "timer_minutes" in current_slide:
            st.sidebar.markdown("---")
            st.sidebar.markdown("⏰ **Activity Timer**")
            if st.sidebar.button(f"Start {current_slide['timer_minutes']} min timer"):
                start_timer(current_slide["timer_minutes"])
                st.experimental_rerun()
        
        # Presenter notes
        st.sidebar.markdown("---")
        if st.sidebar.checkbox("📋 Show Presenter Notes"):
            st.sidebar.markdown("**Notes:**")
            st.sidebar.info(current_slide.get("presenter_notes", "No notes for this slide."))
            
    elif mode == "📝 Student Activities":
        # Add export functionality for student mode
        st.sidebar.markdown("---")
        if st.sidebar.button("💾 Export My Work"):
            json_str = export_student_work()
            st.sidebar.download_button(
                "📄 Download Progress",
                json_str,
                file_name=f"phl101_day1_progress_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
        return "student_activities"
    elif mode == "📚 Resources":
        return "resources"
    elif mode == "👨‍🎓 Study Guide":
        return "study_guide"
    
    return "presentation"

def display_study_guide() -> None:
    """Display comprehensive study guide"""
    st.markdown("# 👨‍🎓 Study Guide")
    
    tab1, tab2, tab3 = st.tabs(["📝 Key Concepts", "🔍 Practice Questions", "📊 Progress Tracker"])
    
    with tab1:
        st.markdown("## 🎯 Key Concepts to Master")
        
        st.markdown("### 📖 Philosophy Definition")
        st.markdown("""
        - **Etymology:** Philo (love) + Sophia (wisdom) = Love of wisdom
        - **Practice:** Active pursuit through questioning, reasoning, logic
        - **Methods:** Rational inquiry rather than tradition/revelation alone
        """)
        
        st.markdown("### 🕊️ Three Definitions of Religion")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **Durkheim (Social)**
            - Religion as social glue
            - Creates solidarity
            - Shared rituals unite communities
            - Example: Holiday gatherings
            """)
        
        with col2:
            st.markdown("""
            **Tylor (Spiritual)**
            - Belief in spiritual beings
            - Gods, spirits, supernatural
            - Focus on metaphysical realm
            - Example: Prayer to deities
            """)
        
        with col3:
            st.markdown("""
            **Tillich (Ultimate Concern)**
            - What matters most deeply
            - Willing to sacrifice for
            - Can include secular devotions
            - Example: Environmental activism
            """)
    
    with tab2:
        st.markdown("## 🤔 Practice Questions")
        
        practice_questions = [
            "How would you explain the difference between philosophy and religion to a friend?",
            "Which definition of religion (Durkheim, Tylor, or Tillich) best explains modern sports fandom?",
            "Is Buddhism a religion according to each definition? Why or why not?",
            "What are examples of 'ultimate concerns' in contemporary society?",
            "How do Plato's Cave and the Exodus story both represent the human search for truth?"
        ]
        
        for i, question in enumerate(practice_questions, 1):
            with st.expander(f"Question {i}: {question}"):
                answer = st.text_area(f"Your answer:", key=f"practice_q_{i}")
                if answer:
                    st.success("Answer recorded! Discuss with classmates or bring to office hours.")
    
    with tab3:
        st.markdown("## 📊 Your Progress")
        
        # Quiz progress
        completed_quizzes = len(st.session_state.quiz_attempts)
        total_quizzes = len(QUIZ_DATA)
        
        progress_pct = (completed_quizzes / total_quizzes) * 100 if total_quizzes > 0 else 0
        st.progress(progress_pct / 100)
        st.markdown(f"**Quizzes completed:** {completed_quizzes}/{total_quizzes}")
        
        # Response tracking
        total_responses = len(st.session_state.student_responses)
        st.markdown(f"**Discussion responses:** {total_responses}")
        
        # Study recommendations
        if progress_pct < 50:
            st.info("🎯 **Recommendation:** Complete the quizzes to test your understanding!")
        elif progress_pct < 100:
            st.info("🎯 **Recommendation:** Review any quiz questions you missed and check out the resources page!")
        else:
            st.success("🎉 **Great work!** You've engaged with all the materials. Ready for Day 2!")

def display_student_activities() -> None:
    """Display student-focused activities and assessments"""
    st.markdown("# 📝 Student Activities")
    
    activity_tab = st.selectbox(
        "Choose an activity:",
        ["Quick Check Quizzes", "Reflection Exercises", "Discussion Responses", "Self-Assessment"]
    )
    
    if activity_tab == "Quick Check Quizzes":
        st.markdown("## 🧠 Test Your Understanding")
        
        quiz_choice = st.selectbox(
            "Select a quiz:",
            ["definitions_quiz", "philosophy_basics"],
            format_func=lambda x: QUIZ_DATA[x]["title"]
        )
        
        display_quiz(quiz_choice)
    
    elif activity_tab == "Reflection Exercises":
        st.markdown("## 💭 Personal Reflection")
        
        st.markdown("### Exercise 1: Your Definition of Religion")
        religion_def = st.text_area(
            "Based on what we've learned, how would YOU define religion? (1-2 paragraphs)",
            key="personal_religion_def",
            placeholder="Consider the three scholarly definitions we discussed. Which resonates with you? Why? Can you think of a better way to define religion?"
        )
        
        st.markdown("### Exercise 2: Philosophy in Your Life")
        philosophy_life = st.text_area(
            "How do you see philosophy ('love of wisdom') playing a role in your daily life?",
            key="philosophy_in_life",
            placeholder="Think about times when you question assumptions, think critically about issues, or seek deeper understanding..."
        )
        
        st.markdown("### Exercise 3: Your Big Question")
        big_question = st.text_area(
            "What's one philosophical or religious question you hope this course will help you explore?",
            key="big_question",
            placeholder="What keeps you up at night wondering? What would you really like to understand better about life, meaning, or existence?"
        )
        
        if st.button("Save Reflections"):
            reflections = {
                "religion_definition": religion_def,
                "philosophy_in_life": philosophy_life,
                "big_question": big_question,
                "timestamp": datetime.now().isoformat()
            }
            st.session_state.student_responses.update(reflections)
            st.success("Reflections saved! You can return to these throughout the semester.")
    
    elif activity_tab == "Discussion Responses":
        st.markdown("## 💬 Discussion Participation")
        
        # Show saved responses
        if st.session_state.student_responses:
            st.markdown("### Your Responses So Far:")
            for key, response in st.session_state.student_responses.items():
                if key.startswith("response_"):
                    slide_id = key.replace("response_", "")
                    slide_title = next((s["title"] for s in SLIDES if s["id"] == slide_id), "Unknown")
                    with st.expander(f"Response to: {slide_title}"):
                        st.write(response)
        else:
            st.info("No discussion responses yet. Navigate to the presentation slides to participate!")
    
    elif activity_tab == "Self-Assessment":
        st.markdown("## 🎯 Self-Assessment Checklist")
        
        st.markdown("Rate your understanding of each concept (1-5 scale):")
        
        concepts = [
            "Etymology and meaning of 'philosophy'",
            "Durkheim's definition of religion (social glue)",
            "Tylor's definition of religion (spiritual beings)",
            "Tillich's definition of religion (ultimate concern)",
            "How philosophy and religion overlap",
            "Examples like Plato's Cave and Exodus",
            "Ability to analyze whether something is a religion"
        ]
        
        ratings = {}
        for concept in concepts:
            rating = st.slider(
                concept,
                min_value=1,
                max_value=5,
                value=3,
                key=f"rating_{concept.replace(' ', '_').replace('(', '').replace(')', '')}"
            )
            ratings[concept] = rating
        
        if st.button("Calculate Assessment"):
            avg_rating = sum(ratings.values()) / len(ratings)
            
            if avg_rating >= 4.5:
                st.success("🌟 Excellent! You have a strong grasp of the material.")
            elif avg_rating >= 4.0:
                st.success("👍 Very good understanding! Keep up the great work.")
            elif avg_rating >= 3.0:
                st.warning("📚 Good foundation, but review areas where you rated 3 or below.")
            else:
                st.info("📖 Spend more time with the materials and consider visiting office hours for help.")
            
            # Specific recommendations
            low_areas = [concept for concept, rating in ratings.items() if rating <= 2]
            if low_areas:
                st.markdown("**Areas to focus on:**")
                for area in low_areas:
                    st.markdown(f"- {area}")

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
    .quiz-container {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
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
    
    elif current_mode == "student_activities":
        display_student_activities()
    
    elif current_mode == "resources":
        display_resources()
    
    elif current_mode == "study_guide":
        display_study_guide()

# Optional LLM integration for advanced features
def get_llm_feedback(student_response: str, context: str) -> str:
    """Generate LLM feedback on student responses (requires API key)"""
    # This would integrate with OpenAI or other LLM APIs
    # For now, return placeholder feedback
    return f"Thank you for your thoughtful response about {context}. Your insights show good engagement with the material."

# Initialize session state and run app
if __name__ == "__main__":
    main()

# Optional: Add export functionality for student work
def export_student_work():
    """Export student responses and quiz results"""
    if st.sidebar.button("📄 Export My Work"):
        work_summary = {
            "student_responses": st.session_state.student_responses,
            "quiz_attempts": st.session_state.quiz_attempts,
            "timestamp": datetime.now().isoformat()
        }
        
        # Convert to downloadable format
        json_str = json.dumps(work_summary, indent=2)
        st.sidebar.download_button(
            "Download My Progress",
            json_str,
            file_name=f"phl101_day1_progress_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

# Add this to sidebar in appropriate mode
if st.sidebar.button("💾 Export My Work"):
    export_student_work()
