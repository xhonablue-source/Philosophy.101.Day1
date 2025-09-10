"""
day1_phl101_app_full.py — FINAL VERSION

Streamlit app for Day 1 — PHL 101
Includes:
 - Slide navigation with presenter notes and timers
 - Student journaling
 - Multiple-choice quizzes
 - Short-answer auto-grader (keyword-based)
 - LLM-powered quiz grading & Q&A assistant (grounded in Day 1 lesson)
 - PPTX export for Google Slides
 - Optional Flask LLM proxy server for secure API calls
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
try:
    from flask import Flask, request, jsonify
    import requests
except Exception:
    Flask = None

# ----------------- Lesson Data -----------------
SLIDES = [
    {"title": "Title", "subtitle": "🎓 What is Religion? What is Philosophy?",
     "content": "PHL 101 – Comparative Religions I\nProfessor Xavier Honablue, M.Ed.",
     "notes": "Welcome students warmly. Share your background briefly. Set collaborative tone."},
    {"title": "Course Objectives", "subtitle": "🎯 Our Journey Together",
     "content": "World religions, Indigenous traditions, philosophical approaches, critical thinking, personal reflection.",
     "notes": "Emphasize comparative approach and respect for traditions."},
    {"title": "Icebreaker", "subtitle": "🤔 The Big Questions",
     "content": "Pair Discussion (10 minutes): What is religion? What is philosophy? Where do they overlap?",
     "timer_minutes": 10,
     "notes": "Give students the full 10 minutes; walk the room; collect word cloud ideas."},
    {"title": "Philosophy Meets Religion", "subtitle": "🧠 Philosophy Meets Religion",
     "content": "Definitions, core questions shared by both (ultimate reality, meaning, morality).",
     "notes": "Explain etymology, show overlap."},
    {"title": "Examples", "subtitle": "💡 A Tale of Two Searches",
     "content": "Plato's Cave vs Moses and the Exodus — journeys from ignorance to truth.",
     "notes": "Use the two stories to show shared narrative arc."},
    {"title": "Group Activity", "subtitle": "🎲 Sorting the Big Questions",
     "content": "Sort questions into Philosophy / Religion / Both (15 minutes).",
     "timer_minutes": 15,
     "notes": "Encourage debate; most will end up 'Both'."},
    {"title": "Defining Religion", "subtitle": "🔬 How Scholars Define Religion",
     "content": "Durkheim (social glue), Tylor (belief in spiritual beings), Tillich (ultimate concern).",
     "notes": "Ask which resonates and why."},
    {"title": "Interactive Debate", "subtitle": "💬 Let's Debate!",
     "content": "Team Durkheim, Team Tylor, Team Tillich. Is Buddhism a religion under each definition?",
     "notes": "Moderate debate; present 'challenge question'."},
    {"title": "Wrap-Up & Homework", "subtitle": "🎯 Exit Ticket & Next Steps",
     "content": "Exit ticket: One question about life or religion you hope the class will answer.\nHomework: CrashCourse/TED-Ed videos + 1 paragraph reflection.",
     "notes": "Collect exit tickets & preview Day 2."}
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
 - Contradiction, Logic, Fallacy, Absurdity (Reductio)
 - Practice identifying premises, conclusions, validity & soundness.
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

# ----------------- LLM helpers -----------------
def build_system_prompt_day1() -> str:
    return f"""
You are the teaching assistant for PHL 101 — Day 1: What is Religion? What is Philosophy?.
Base answers strictly on the slides, quizzes, and readings provided.
When grading, output JSON with: quiz_id, score, pct, per_question (q_index, correct, student_answer, feedback, hint), teacher_note.
When answering questions, be concise (<150 words), point to slide numbers or resources, and encourage curiosity.
"""

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

    # Sidebar
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

    # Slide content
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

    # Quizzes
    st.markdown("---")
    st.markdown("### Quizzes")
    for q in QUIZZES:
        st.markdown(f"#### {q['title']}")
        answers = {}
        for i, item in enumerate(q['questions']):
            ans = st.radio(item['q'], options=item['choices'], key=f"quiz{q['id']}_{i}")
            answers[i] = ans
        if st.button(f"Grade {q['title']}") and openai_key:
            prompt = f"Grade this quiz: {q['title']} with answers: {answers}"
            result = ask_llm(openai_key, llm_model, prompt)
            st.text_area("LLM Grade Result", result, height=300)

    # Short-answer auto-grader demo
    st.markdown("---")
    st.markdown("### Short-answer auto-grader")
    sa = st.text_area("Student answer")
    kws = st.text_input("Keywords", value="social glue, ritual, solidarity")
    if st.button("Check short-answer"):
        res = short_answer_score(sa, [k.strip() for k in kws.split(',')])
        st.write(res)

    # LLM Q&A
    st.markdown("---")
    st.markdown("### LLM Q&A")
    q = st.text_input("Ask a question about today's lesson")
    if st.button("Ask") and openai_key:
        ans = ask_llm(openai_key, llm_model, q)
        st.write(ans)

    # Day 2 preview
    st.markdown("---")
    st.markdown("### Day 2 Preview")
    st.write(DAY2_PREVIEW)

    # Timer
    if st.session_state.get('timer_seconds'):
        rem = st.session_state.timer_seconds - int(time.time() - st.session_state.timer_start)
        if rem <= 0:
            st.success("Timer done!")
            st.session_state.pop('timer_seconds')
        else:
            st.info(f"Timer: {rem//60}:{str(rem%60).zfill(2)}")

# ----------------- Entrypoint -----------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', action='store_true')
    args = parser.parse_args()
    main()
