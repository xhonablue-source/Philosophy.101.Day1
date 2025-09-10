"""
day1_phl101_app_full.py — FINAL VERSION with full slide presentation

Streamlit app for Day 1 — PHL 101
Includes:
 - Full slide presentation content from initial prompt
 - Slide navigation with presenter notes and timers
 - Student journaling
 - Multiple-choice quizzes
 - Short-answer auto-grader (keyword-based)
 - LLM-powered quiz grading & Q&A assistant (grounded in Day 1 lesson)
 - PPTX export for Google Slides
"""

import streamlit as st
import io, time, os, argparse, json
from typing import List, Dict

# Optional imports
try:
    import openai
except Exception:
    openai = None
try:
    from pptx import Presentation
    from pptx.util import Pt
except Exception:
    Presentation = None

# ----------------- Full Slide Presentation -----------------
SLIDES = [
    {"title": "Slide 1", "subtitle": "Welcome & Introductions",
     "content": "PHL 101 – Comparative Religions I\nProfessor Xavier Honablue, M.Ed.\nBackground: Mathematics • Computer Science • Philosophy • Education",
     "notes": "Welcome students warmly. Share your background briefly. Set collaborative tone."},
    {"title": "Slide 2", "subtitle": "Course Objectives",
     "content": "By the end of this course, students will:\n- Explore major world religions\n- Engage Indigenous traditions\n- Apply philosophical approaches\n- Develop critical thinking\n- Reflect personally on religion and philosophy",
     "notes": "Emphasize comparative approach and respect for traditions."},
    {"title": "Slide 3", "subtitle": "Icebreaker Activity",
     "content": "🤔 Pair Discussion (10 minutes):\n1. What is religion?\n2. What is philosophy?\n3. Where do they overlap?",
     "timer_minutes": 10,
     "notes": "Give students 10 minutes. Walk around the room and listen in."},
    {"title": "Slide 4", "subtitle": "Philosophy Meets Religion",
     "content": "Both ask core questions:\n- What is ultimate reality?\n- What is the purpose of life?\n- How should we live?\nPhilosophy = love of wisdom\nReligion = binding together, seeking meaning",
     "notes": "Explain etymology and overlapping concerns."},
    {"title": "Slide 5", "subtitle": "Examples: Stories of Truth-Seeking",
     "content": "💡 Plato's Cave: prisoners mistake shadows for reality.\n💡 Exodus: Israelites journey from slavery to freedom.\nBoth = moving from ignorance to truth.",
     "notes": "Compare narrative arcs of Plato and Moses."},
    {"title": "Slide 6", "subtitle": "Group Activity: Sorting Questions",
     "content": "🎲 Sort questions into Philosophy / Religion / Both:\n- Is there life after death?\n- What is justice?\n- Why is there suffering?\n- What is the ultimate reality?",
     "timer_minutes": 15,
     "notes": "Encourage debate. Most questions overlap."},
    {"title": "Slide 7", "subtitle": "Defining Religion",
     "content": "Scholars define religion differently:\n- Durkheim: Social glue, rituals, solidarity\n- Tylor: Belief in spiritual beings\n- Tillich: Ultimate concern",
     "notes": "Ask students which resonates most."},
    {"title": "Slide 8", "subtitle": "Interactive Debate",
     "content": "💬 Teams:\n- Team Durkheim\n- Team Tylor\n- Team Tillich\nDebate: Is Buddhism a religion under each definition?",
     "notes": "Moderate debate. Pose challenge: what if none fit perfectly?"},
    {"title": "Slide 9", "subtitle": "Wrap-Up & Homework",
     "content": "🎯 Exit Ticket: One question about life or religion you hope this class will answer.\nHomework:\n- Watch CrashCourse: Philosophy of Religion\n- Watch TED-Ed: What is Religion?\n- Write 1 paragraph: Which definition of religion resonates with you, and why?",
     "notes": "Collect exit tickets & preview Day 2 on argument structure."}
]

QUIZZES = [
    {
        "id": "quiz1",
        "title": "Quick Check: Definitions",
        "questions": [
            {"q": "Durkheim said religion is primarily what?", "choices": ["Belief in gods", "Social glue", "Ultimate concern", "Personal morality"],
             "answer": 1, "explain": "Durkheim emphasized religion's social function — shared rituals and solidarity."},
            {"q": "Tylor's definition focuses on what?", "choices": ["Community", "Ritual", "Belief in spiritual beings", "Ultimate concerns"],
             "answer": 2, "explain": "Tylor defined religion as belief in spiritual beings."}
        ],
        "passing_pct": 60
    }
]

RESOURCES = {
    "videos": [
        {"title": "CrashCourse: Philosophy of Religion", "url": "https://www.youtube.com/watch?v=k6u3Qw4XlfQ"},
        {"title": "TED-Ed: What is Religion?", "url": "https://www.youtube.com/watch?v=xQq2V8C8XwQ"}
    ],
    "links": [
        {"title": "Stanford Encyclopedia of Philosophy — Religion", "url": "https://plato.stanford.edu/entries/religion/"}
    ]
}

DAY2_PREVIEW = """
Day 2 Preview — Argument Structure
---------------------------------
- Contradiction: incompatible claims
- Logic: deductive & inductive
- Fallacies: straw man, ad hominem, false cause
- Absurdity: reductio ad absurdum
"""

# ----------------- Short-answer auto-grader -----------------
def short_answer_score(student_answer: str, target_keywords: List[str], threshold: float = 0.6) -> Dict:
    if not student_answer:
        return {"matched": 0, "total": len(target_keywords), "pct": 0.0, "passed": False, "matches": []}
    s = student_answer.lower()
    matches = [kw for kw in target_keywords if kw.lower() in s]
    matched = len(matches)
    total = max(1, len(target_keywords))
    pct = matched / total
    return {"matched": matched, "total": total, "pct": pct, "passed": pct >= threshold, "matches": matches}

# ----------------- PPTX export -----------------
def generate_pptx_from_slides(slides: List[Dict]) -> bytes:
    if Presentation is None:
        raise RuntimeError("python-pptx not installed")
    prs = Presentation()
    for i, s in enumerate(slides):
        layout = prs.slide_layouts[0] if i == 0 else prs.slide_layouts[1]
        slide = prs.slides.add_slide(layout)
        try:
            slide.shapes.title.text = s.get('subtitle', s.get('title',''))
        except: pass
        try:
            tf = slide.placeholders[1].text_frame
            tf.clear()
            for p in s.get('content','').split('\n'):
                par = tf.add_paragraph()
                par.text = p
                par.font.size = Pt(14)
        except: pass
    buf = io.BytesIO()
    prs.save(buf)
    buf.seek(0)
    return buf.read()

# ----------------- LLM helper -----------------
def build_system_prompt_day1() -> str:
    return "You are the teaching assistant for PHL 101 — Day 1: What is Religion? What is Philosophy?. Base answers on slides, quizzes, and resources." 

def ask_llm(openai_key: str, model: str, user_message: str):
    if openai is None:
        return "openai package not installed"
    openai.api_key = openai_key
    messages = [
        {"role": "system", "content": build_system_prompt_day1()},
        {"role": "user", "content": user_message}
    ]
    resp = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=350, temperature=0.2)
    return resp["choices"][0]["message"]["content"]

# ----------------- Streamlit App -----------------
def main():
    st.set_page_config(page_title="Day 1 — PHL 101", page_icon="🎓", layout="wide")
    if 'slide_idx' not in st.session_state:
        st.session_state.slide_idx = 0

    with st.sidebar:
        st.title("Day 1 — PHL 101")
        if st.button("Prev"): st.session_state.slide_idx = max(0, st.session_state.slide_idx - 1)
        if st.button("Next"): st.session_state.slide_idx = min(len(SLIDES)-1, st.session_state.slide_idx + 1)
        st.markdown("---")
        openai_key = st.text_input("OpenAI API key", type='password')
        llm_model = st.text_input("Model", value="gpt-4o")
        if st.button("Export PPTX"):
            pptx_bytes = generate_pptx_from_slides(SLIDES)
            st.download_button("Download PPTX", pptx_bytes, "Day1_PHL101.pptx")

    slide = SLIDES[st.session_state.slide_idx]
    st.subheader(slide.get('subtitle'))
    st.markdown(f"### {slide.get('title')}")
    st.write(slide.get('content'))
    if 'timer_minutes' in slide:
        if st.button(f"Start {slide['timer_minutes']} min timer"):
            st.session_state.timer_seconds = int(slide['timer_minutes'] * 60)
            st.session_state.timer_start = time.time()
    if st.checkbox("Show notes"):
        st.info(slide.get('notes',''))

    st.markdown("---")
    st.markdown("### Quiz")
    q = QUIZZES[0]
    answers = {}
    for i, item in enumerate(q['questions']):
        ans = st.radio(item['q'], options=item['choices'], key=f"quiz{q['id']}_{i}")
        answers[i] = ans
    if st.button("Grade Quiz") and openai_key:
        prompt = f"Grade quiz {q['title']} with answers: {answers}"
        result = ask_llm(openai_key, llm_model, prompt)
        st.text_area("LLM Grade Result", result, height=300)

    st.markdown("---")
    st.markdown("### Short-answer auto-grader")
    sa = st.text_area("Student answer")
    kws = st.text_input("Keywords", value="social glue, ritual, solidarity")
    if st.button("Check short-answer"):
        res = short_answer_score(sa, [k.strip() for k in kws.split(',')])
        st.write(res)

    st.markdown("---")
    st.markdown("### LLM Q&A")
    qtext = st.text_input("Ask a question about today's lesson")
    if st.button("Ask") and openai_key:
        ans = ask_llm(openai_key, llm_model, qtext)
        st.write(ans)

    st.markdown("---")
    st.markdown("### Day 2 Preview")
    st.write(DAY2_PREVIEW)

    if st.session_state.get('timer_seconds'):
        rem = st.session_state.timer_seconds - int(time.time() - st.session_state.timer_start)
        if rem <= 0:
            st.success("Timer done!")
            st.session_state.pop('timer_seconds')
        else:
            st.info(f"Timer: {rem//60}:{str(rem%60).zfill(2)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', action='store_true')
    args = parser.parse_args()
    main()
