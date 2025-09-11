"""
PHL 101 Day 1 - Complete Interactive Philosophy & Religion App
Fixed version with corrected URLs and complete HTML presentation
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

# Enhanced slide data
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

# Enhanced resources with corrected URLs
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
            "url": "https://www.youtube.com/watch?v=kZY2eeozdo8",
            "description": "Animated exploration of different definitions of religion",
            "duration": "5 minutes"
        },
        {
            "title": "The Cave: An Adaptation of Plato's Allegory",
            "url": "https://www.youtube.com/watch?v=1RWOpQXTltA",
            "description": "Beautiful animated version of Plato's famous allegory",
            "duration": "7 minutes"
        },
        {
            "title": "Introduction to Philosophy of Religion",
            "url": "https://www.youtube.com/watch?v=QVPKiNjZLXM",
            "description": "Academic introduction to major questions in philosophy of religion",
            "duration": "12 minutes"
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
    """Display the complete beautiful HTML presentation"""
    st.markdown("# 🎓 Professor Lecture - Interactive Presentation")
    st.markdown("*Click the presentation below to begin the interactive lecture*")
    
    # Complete HTML presentation from the document
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
                color:
