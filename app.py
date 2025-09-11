"""
PHL 101 Day 1 - Simple Working Version
Fixed indentation and syntax issues
"""

import streamlit as st
import time
import json
import io
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
if 'assignment1_progress' not in st.session_state:
    st.session_state.assignment1_progress = {
        'questions_asked': {'Durkheim': [], 'Tylor': [], 'Tillich': []},
        'responses_received': {'Durkheim': [], 'Tylor': [], 'Tillich': []},
        'notes': {'Durkheim': '', 'Tylor': '', 'Tillich': ''},
        'essays': {'Durkheim': '', 'Tylor': '', 'Tillich': ''},
        'completed_philosophers': set()
    }

# Slide data
SLIDES = [
    {
        "id": "welcome",
        "title": "Welcome & Introductions",
        "content": """
        # What is Religion? What is Philosophy?
        
        ## PHL 101 - Comparative Religions I
        **Professor Xavier Honablue, M.Ed.**
        
        **Background:** Mathematics - Computer Science - Philosophy - Education
        
        > "We're going to explore the great traditions of the world - Judaism, Christianity, Islam, but also Eastern, African, and Indigenous traditions. Our job is not to judge, but to think critically, compare, and engage."
        """,
        "presenter_notes": "Welcome students warmly. Share your background briefly. Set collaborative tone for the semester."
    },
    {
        "id": "objectives",
        "title": "Course Objectives",
        "content": """
        # Our Journey Together
        
        ## What We'll Explore:
        * **World Religions:** Christianity, Islam, Judaism, Hinduism, Buddhism, Taoism
        * **Indigenous Traditions:** Native American, African, Australian Aboriginal
        * **Philosophical Approaches:** Western and Eastern philosophical traditions
        * **Critical Thinking:** Comparing beliefs, practices, and worldviews
        * **Personal Reflection:** Understanding your own beliefs and assumptions
        
        ## Our Approach
        We approach each tradition with respect, curiosity, and scholarly rigor. We seek to understand rather than judge, to compare rather than compete, and to engage thoughtfully with humanity's greatest questions.
        """,
        "presenter_notes": "Emphasize comparative approach and respect for all traditions."
    },
    {
        "id": "defining_religion",
        "title": "Defining Religion",
        "content": """
        # How Scholars Define Religion
        
        ## Three Famous Definitions:
        
        ### Emile Durkheim (1858-1917)
        **"Religion is the social glue that binds communities together."**
        
        *Focus:* Religion creates solidarity, shared identity, and moral order in society. Think of how religious holidays bring families together, or how shared beliefs unite communities.
        
        ### Edward Tylor (1832-1917)
        **"Religion is belief in spiritual beings."**
        
        *Focus:* At its core, religion involves belief in gods, spirits, souls, or supernatural forces. From ancestor worship to monotheism, spiritual beings are central.
        
        ### Paul Tillich (1886-1965)
        **"Religion is ultimate concern."**
        
        *Focus:* Religion addresses what matters most to us - our deepest values, fears, and hopes. It's about what we're willing to sacrifice everything for.
        
        ## Discussion Question:
        Which definition resonates most with you? Why? Can you think of examples that fit one definition but not the others?
        """,
        "presenter_notes": "Ask students which resonates most. This is where students start to see the complexity of defining religion."
    }
]

# Philosopher profiles for Assignment 1
PHILOSOPHER_PROFILES = {
    "Durkheim": {
        "name": "Emile Durkheim",
        "years": "1858-1917",
        "background": "I am a French sociologist who founded the academic discipline of sociology. I studied how societies hold together and function, with particular interest in the role of religion in creating social solidarity.",
        "key_ideas": [
            "Religion is the social glue that binds communities together",
            "Sacred rituals create collective effervescence - shared emotional experiences that unite people",
            "Religious beliefs reflect society's deepest values and moral order"
        ]
    },
    "Tylor": {
        "name": "Edward Burnett Tylor",
        "years": "1832-1917",
        "background": "I am an English anthropologist, often called the father of cultural anthropology. I developed evolutionary theories of culture and religion, studying how beliefs develop from primitive to advanced forms.",
        "key_ideas": [
            "Religion is belief in spiritual beings - this is the minimum definition",
            "Culture is 'that complex whole which includes knowledge, belief, art, morals, law, custom'",
            "Religious beliefs evolved from animism to polytheism to monotheism"
        ]
    },
    "Tillich": {
        "name": "Paul Tillich",
        "years": "1886-1965",
        "background": "I am a German-American theologian and philosopher. I lived through both World Wars and experienced exile from Nazi Germany. I sought to bridge theology and modern philosophy, making religious thought relevant to contemporary life.",
        "key_ideas": [
            "Religion is ultimate concern - what matters most deeply to a person",
            "God is not a being but Being-itself, the ground of all existence",
            "Faith is not belief despite evidence, but ultimate concern about ultimate reality"
        ]
    }
}

# Quiz data
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
                "explanation": "Durkheim emphasized religion's social function - shared rituals create solidarity and moral order in society."
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
                "explanation": "Tylor defined religion as 'belief in spiritual beings' - gods, spirits, souls, or supernatural forces."
            }
        ]
    }
}

# Argument structure concepts for Assignment 1
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
        "example": "Deductive: All religions involve ritual -> Buddhism involves ritual. Inductive: Churches, mosques, temples all bring people together -> Religion brings people together."
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

# Resources
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
            "url": "https://www.youtube.com/watch?v=m6dCxo7t_aE", 
            "description": "Animated exploration of different definitions of religion",
            "duration": "5 minutes"
        }
    ],
    "articles": [
        {
            "title": "Stanford Encyclopedia: Philosophy of Religion",
            "url": "https://plato.stanford.edu/entries/philosophy-religion/",
            "description": "Comprehensive academic overview"
        }
    ]
}

def get_philosopher_response(philosopher_name: str, question: str, question_type: str) -> str:
    """Generate a simple response from the specified philosopher"""
    profile = PHILOSOPHER_PROFILES[philosopher_name]
    
    # Simple static responses for now
    responses = {
        "premise": f"As {profile['name']}, I believe that any premise about religion must be grounded in careful observation and analysis.",
        "contradiction": f"From my perspective as {profile['name']}, contradictions in religious thought often reveal deeper truths about human nature and society.",
        "logic": f"I {profile['name']} argue that we must use systematic reasoning when studying religious phenomena.",
        "fallacy": f"As {profile['name']}, I warn against common errors in reasoning when analyzing religious beliefs and practices.",
        "absurdity": f"What may seem absurd in religious practice often serves important functions, as I {profile['name']} have observed."
    }
    
    base_response = responses.get(question_type, f"That's an interesting question about {question_type}.")
    
    return f"""**{profile['name']} responds:**

{base_response}

Your question: "{question}"

Based on my understanding, {question_type} is crucial for analyzing religious phenomena. In my work studying religion, I've found that we must be careful to use proper reasoning and avoid hasty conclusions.

*Note: This is a simplified response. For dynamic conversations, you would need to integrate with an AI service.*"""

def display_professor_lecture():
    """Display the HTML presentation"""
    st.markdown("# Professor Lecture - Interactive Presentation")
    st.markdown("*Your beautiful animated presentation would be embedded here*")
    
    # Simplified HTML for demo
    html_content = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 40px; border-radius: 15px; color: white; text-align: center;">
        <h1>What is Religion? What is Philosophy?</h1>
        <h3>PHL 101 - Comparative Religions I</h3>
        <p><strong>Professor Xavier Honablue, M.Ed.</strong></p>
        <p>Mathematics - Computer Science - Philosophy - Education</p>
        <p style="font-style: italic; margin-top: 20px;">
            "We're going to explore the great traditions of the world"
        </p>
    </div>
    """
    
    st.components.v1.html(html_content, height=300)
    st.markdown("*Full interactive presentation with all 9 slides, navigation, and animations*")

def display_assignment1():
    """Display Assignment 1: Philosopher Conversations"""
    st.markdown("# Assignment 1: Philosopher Conversations")
    st.markdown("## Explore Argument Structure Through Dialog")
    
    # Instructions
    with st.expander("Assignment Instructions", expanded=True):
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
        """)
    
    # Progress tracking
    st.markdown("## Your Progress")
    progress_data = st.session_state.assignment1_progress
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        durkheim_questions = len(progress_data['questions_asked']['Durkheim'])
        st.metric("Durkheim Questions", f"{durkheim_questions}/5")
    
    with col2:
        tylor_questions = len(progress_data['questions_asked']['Tylor'])
        st.metric("Tylor Questions", f"{tylor_questions}/5")
    
    with col3:
        tillich_questions = len(progress_data['questions_asked']['Tillich'])
        st.metric("Tillich Questions", f"{tillich_questions}/5")
    
    # Philosopher selection
    st.markdown("## Choose Your Conversation Partner")
    
    philosopher = st.selectbox(
        "Select a philosopher to talk with:",
        ["Durkheim", "Tylor", "Tillich"],
        format_func=lambda x: f"{PHILOSOPHER_PROFILES[x]['name']} ({PHILOSOPHER_PROFILES[x]['years']})"
    )
    
    # Display philosopher info
    profile = PHILOSOPHER_PROFILES[philosopher]
    with st.expander(f"About {profile['name']}", expanded=False):
        st.markdown(f"**Years:** {profile['years']}")
        st.markdown(f"**Background:** {profile['background']}")
        st.markdown("**Key Ideas:**")
        for idea in profile['key_ideas']:
            st.markdown(f"- {idea}")
    
    # Question type and input
    st.markdown(f"## Conversation with {profile['name']}")
    
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
            response = get_philosopher_response(philosopher, user_question, question_type)
            
            # Display response
            st.markdown(f"### {profile['name']} responds:")
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

def display_slide(slide_data: dict) -> None:
    """Display a slide"""
    st.markdown(slide_data["content"])
    
    # Show presenter notes if enabled
    if st.session_state.get('show_notes', False):
        st.info(f"**Notes:** {slide_data.get('presenter_notes', 'No notes for this slide.')}")

def display_quiz(quiz_id: str) -> None:
    """Display interactive quiz"""
    if quiz_id not in QUIZ_DATA:
        st.error("Quiz not found!")
        return
        
    quiz = QUIZ_DATA[quiz_id]
    st.markdown(f"## {quiz['title']}")
    
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
            # Grade quiz
            correct_count = 0
            total_questions = len(quiz["questions"])
            
            st.markdown("---")
            st.markdown("### Results:")
            
            for i, q in enumerate(quiz["questions"]):
                if i in answers:
                    is_correct = answers[i] == q["correct"]
                    if is_correct:
                        correct_count += 1
                        st.success(f"Question {i+1}: Correct!")
                    else:
                        st.error(f"Question {i+1}: Incorrect")
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
    """Display resources page"""
    st.markdown("# Learning Resources")
    st.markdown("Explore these carefully selected resources to deepen your understanding!")
    
    # Videos section
    st.markdown("## Videos")
    for video in RESOURCES["videos"]:
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
    """Sidebar navigation"""
    st.sidebar.markdown("# PHL 101 Day 1")
    
    # Mode selection
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["Presentation", "Professor Lecture", "Assignment 1", "Quizzes", "Resources"]
    )
    
    if mode == "Presentation":
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
            if st.button("Previous") and st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
                st.rerun()
        
        with col2:
            if st.button("Next") and st.session_state.current_slide < len(SLIDES) - 1:
                st.session_state.current_slide += 1
                st.rerun()
        
        # Presenter notes toggle
        st.sidebar.markdown("---")
        st.session_state.show_notes = st.sidebar.checkbox("Show Presenter Notes")
            
    return mode.lower().replace(" ", "_")

def main():
    """Main application function"""
    # Custom CSS
    st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
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
    
    elif current_mode == "professor_lecture":
        display_professor_lecture()
    
    elif current_mode == "assignment_1":
        display_assignment1()
    
    elif current_mode == "quizzes":
        st.markdown("# Knowledge Check Quizzes")
        
        quiz_choice = st.selectbox(
            "Select a quiz:",
            ["definitions_quiz"],
            format_func=lambda x: QUIZ_DATA[x]["title"]
        )
        
        display_quiz(quiz_choice)
    
    elif current_mode == "resources":
        display_resources()

if __name__ == "__main__":
    main()
