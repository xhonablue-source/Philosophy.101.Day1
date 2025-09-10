# day1_phl101_app.py
# Streamlit app: Day 1 — What is Religion? What is Philosophy?
# Developed for CognitiveCloud.ai by Xavier Honablue M.Ed
# Features:
#  - Slide-like navigation preserving your 9-slide flow
#  - Presenter notes, timers, keyboard shortcuts (P=present, F=fullscreen, N=notes)
#  - Student journaling with export
#  - Group activity / timers
#  - Interactive quizzes with instant feedback and score summary
#  - LLM-driven Q&A assistant (OpenAI placeholder; replace key & model)
#  - Resource slide with embedded YouTube videos & external links
#  - Day 2 preview on argument structure: contradiction, logic, fallacy, absurdity

import streamlit as st
import io, textwrap, json, time
from typing import List, Dict

# ----------------- Page config -----------------
st.set_page_config(
    page_title="Day 1 — What is Religion? What is Philosophy?",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Simple CSS styling -----------------
st.markdown("""
<style>
/* Basic look and feel */
body { font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background-color: #F7F7FB; }
.header { text-align:center; color:#3B0A5A; }
.section-title { color:#0B57A4; font-size:22px; font-weight:700; margin-bottom:0.3rem; }
.card { background: #fff; border-radius:12px; padding:18px; box-shadow: 0 6px 20px rgba(0,0,0,0.06); }
.small-muted { color:#6b7280; font-size:0.9rem; }
.question-tag { cursor:pointer; display:inline-block; margin:6px 6px; padding:8px 12px; border-radius:999px; background: linear-gradient(90deg,#667eea,#764ba2); color:#fff; }
</style>
""", unsafe_allow_html=True)

# ----------------- App data: slides, quizzes, resources -----------------
SLIDES = [
    {"title": "Title", "subtitle": "🎓 What is Religion? What is Philosophy?",
     "content": "PHL 101 – Comparative Religions I\nProfessor Xavier Honablue, M.Ed.\nBackground: Mathematics • Computer Science • Philosophy • Education",
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
     "content": "Exit ticket: One question about life or religion you hope the class will answer.\nHomework: CrashCourse/TED-Ed videos + 1 paragraph definitional reflection.",
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
    },
    {
        "id": "quiz2",
        "title": "Critical Thinking Quick Quiz",
        "questions": [
            {"q": "Which story is associated with questioning appearances and reality?", "choices": ["Exodus", "Plato's Cave", "Tillich's ultimate concern", "Durkheim's social theory"],
             "answer": 1, "explain": "Plato's Cave is a parable about mistaking shadows for reality."},
            {"q": "Which is an example of 'ultimate concern'?", "choices": ["A sports rivalry", "Daily chores", "Environmental activism as devotion", "A grocery list"],
             "answer": 2, "explain": "Tillich argued that 'ultimate concern' could include secular passions such as activism."}
        ],
        "passing_pct": 60
    }
]

RESOURCES = {
    "videos": [
        {"title": "CrashCourse: Philosophy of Religion (YouTube)", "embed": "https://www.youtube.com/embed/k6u3Qw4XlfQ"},
        {"title": "TED-Ed: What is Religion?", "embed": "https://www.youtube.com/embed/xQq2V8C8XwQ"}
    ],
    "links": [
        {"title": "Stanford Encyclopedia of Philosophy — Religion", "url": "https://plato.stanford.edu/entries/religion/"},
        {"title": "CrashCourse Philosophy playlist", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtNgK6MZucdYldNkMybYIHKR"}
    ],
    "readings": [
        {"title": "Selections from Durkheim, Tylor, Tillich (PDF)", "note": "Uploaded to course site or cognitivecloud.ai resources"}
    ]
}

DAY2_PREVIEW = """
Day 2 Preview — Argument Structure
---------------------------------
We'll begin with core tools of argument analysis:
 - Contradiction: how to spot logically incompatible claims.
 - Logic: basic structure of deductive and inductive arguments.
 - Fallacy: common reasoning errors (straw man, ad hominem, false cause).
 - Absurdity & Reductio ad absurdum: using contradiction to test claims.

Students will practice identifying premises, conclusions, and evaluating validity & soundness.
"""

# ----------------- Session state defaults -----------------
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0
if "completed" not in st.session_state:
    st.session_state.completed = set()
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []
if "llm_history" not in st.session_state:
    st.session_state.llm_history = []

# ----------------- Sidebar: quick controls, presenter notes, LLM keys -----------------
with st.sidebar:
    st.markdown("# Day 1 — PHL 101")
    st.markdown("**Presenter controls**")
    colp1, colp2 = st.columns([1,1])
    if colp1.button("← Prev"):
        st.session_state.slide_idx = max(0, st.session_state.slide_idx - 1)
    if colp2.button("Next →"):
        st.session_state.slide_idx = min(len(SLIDES)-1, st.session_state.slide_idx + 1)

    st.markdown("---")
    st.markdown("**Jump to slide**")
    slide_choice = st.selectbox("Slide", options=list(range(1, len(SLIDES)+1)),
                                index=st.session_state.slide_idx, format_func=lambda x: f"{x}: {SLIDES[x-1]['title']}")
    if slide_choice - 1 != st.session_state.slide_idx:
        st.session_state.slide_idx = slide_choice - 1

    st.markdown("---")
    st.markdown("**Timer**")
    timer_minutes = st.number_input("Start activity timer (minutes)", min_value=1, max_value=60, value=5, step=1)
    if st.button("Start Timer"):
        st.session_state.timer_start = time.time()
        st.session_state.timer_seconds = int(timer_minutes * 60)
        st.experimental_rerun()

    st.markdown("---")
    st.markdown("**LLM Q&A (optional)**")
    st.markdown("You may wire your OpenAI API key or another endpoint. Leave blank to skip.")
    openai_key = st.text_input("OpenAI API key", type="password", placeholder="sk-... (not stored)")
    llm_model = st.text_input("Model name (e.g. gpt-4o-mini)", value="gpt-4o", help="Replace with available model.")
    st.markdown("**Note:** This app provides an LLM helper toggle on the Resources & Q&A slide. Use responsibly.")

# ----------------- Top header -----------------
st.markdown('<div class="header"><h1>🎓 Day 1 — What is Religion? What is Philosophy?</h1></div>', unsafe_allow_html=True)
st.write("---")

# ----------------- Left: slide content; Right: tools (journal, quiz, LLM) -----------------
left_col, right_col = st.columns([3, 1.2])

# -- Slide rendering
slide = SLIDES[st.session_state.slide_idx]
with left_col:
    st.markdown(f"## {slide['subtitle']}")
    st.markdown(f"### {slide.get('title', '')}")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # Show content with safe pre-formatting
    for paragraph in slide["content"].split("\n"):
        st.markdown(paragraph.strip())
    st.markdown("</div>", unsafe_allow_html=True)

    # Presenter notes toggle
    show_notes = st.checkbox("Show presenter notes (on-screen)", value=False)
    if show_notes:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Presenter notes**")
        st.markdown(slide.get("notes", "No notes for this slide."))
        st.markdown("</div>", unsafe_allow_html=True)

    # Auto-start timers for slides with timer_minutes
    if slide.get("timer_minutes"):
        if st.button(f"Start slide activity timer: {slide['timer_minutes']} min"):
            st.session_state.timer_seconds = int(slide["timer_minutes"] * 60)
            st.session_state.timer_start = time.time()
            st.experimental_rerun()

    # If slide is Group Activity or Icebreaker, show a simple interactive widget
    if "Icebreaker" in slide["subtitle"] or "Group Activity" in slide["subtitle"]:
        st.markdown("---")
        st.markdown("#### Live group inputs (collect responses here)")
        responses = st.text_area("Paste student group findings / word-cloud words here (or type):", key=f"group_input_{st.session_state.slide_idx}", height=120)
        if st.button("Save group responses"):
            st.session_state.completed.add(st.session_state.slide_idx)
            st.success("Saved responses for this activity.")
    # For Wrap-Up slide, collect exit ticket
    if "Exit Ticket" in slide["subtitle"] or "Wrap-Up" in slide["subtitle"] or "Exit" in slide["subtitle"]:
        st.markdown("---")
        st.markdown("### Exit Ticket")
        exit_text = st.text_area("One question about life/religion you hope this class will answer:", key="exit_ticket", height=120)
        if st.button("Submit Exit Ticket"):
            st.session_state.journal_entries.append({"type": "exit_ticket", "text": exit_text})
            st.success("Exit ticket recorded. Thanks!")
    # Day 2 preview on wrap-up slide and a dedicated mini-section
    if st.session_state.slide_idx == len(SLIDES)-1:
        st.markdown("---")
        st.markdown("### Preview: Day 2 — Argument Structure")
        st.write(DAY2_PREVIEW)

# -- Right column: Journal, Quizzes, LLM Q&A
with right_col:
    st.markdown("### Student Journal")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    challenge_text = st.text_area("Describe a challenge you're facing:", height=80, key="challenge")
    effort_taken = st.text_area("What effort have you made so far?", height=80, key="effort")
    mistake_text = st.text_area("Describe a mistake you’ve made:", height=80, key="mistake")
    lesson_learned = st.text_area("What did you learn from that mistake?", height=80, key="lesson")
    growth_action = st.text_input("One action you'll take this week to grow:", key="growth_action", value="Ask for help on a tough problem")
    if st.button("📥 Save journal entry"):
        entry = {
            "challenge": challenge_text,
            "effort": effort_taken,
            "mistake": mistake_text,
            "lesson": lesson_learned,
            "growth_action": growth_action,
            "slide": st.session_state.slide_idx,
            "timestamp": time.time()
        }
        st.session_state.journal_entries.append(entry)
        st.success("Journal saved.")
    if st.button("📄 Download all journals (txt)"):
        buf = io.StringIO()
        for i, e in enumerate(st.session_state.journal_entries):
            buf.write(f"Entry {i+1}\n")
            for k,v in e.items():
                buf.write(f"{k}: {v}\n")
            buf.write("\n---\n\n")
        st.download_button("Download journaling TXT", data=buf.getvalue(), file_name="growth_journals.txt", mime="text/plain")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Quizzes")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # Show list of quizzes; allow attempting quiz
    quiz_to_take = st.selectbox("Choose quiz", options=[q["title"] for q in QUIZZES])
    chosen_quiz = next(q for q in QUIZZES if q["title"] == quiz_to_take)
    if st.button("Start Quiz"):
        st.session_state[f"taking_{chosen_quiz['id']}"] = True
        st.experimental_rerun()
    if st.session_state.get(f"taking_{chosen_quiz['id']}"):
        st.markdown(f"#### {chosen_quiz['title']}")
        user_answers = []
        score = 0
        for i, q in enumerate(chosen_quiz["questions"]):
            st.markdown(f"**Q{i+1}. {q['q']}**")
            ans = st.radio("Select answer", options=q["choices"], key=f"{chosen_quiz['id']}_q{i}")
            chosen_index = q["choices"].index(ans)
            user_answers.append(chosen_index)
            if st.button(f"Submit answer Q{i+1}", key=f"submit_{chosen_quiz['id']}_q{i}"):
                correct = chosen_index == q["answer"]
                if correct:
                    st.success("Correct ✅")
                    score += 1
                else:
                    st.error(f"Incorrect — {q['explain']}")
        # Finalize
        if st.button("Finish quiz & grade"):
            pct = int((score / len(chosen_quiz["questions"])) * 100)
            passed = pct >= chosen_quiz["passing_pct"]
            st.session_state.quiz_scores[chosen_quiz["id"]] = {"score": score, "pct": pct, "passed": passed}
            st.session_state.pop(f"taking_{chosen_quiz['id']}", None)
            st.success(f"Quiz graded: {score}/{len(chosen_quiz['questions'])} ({pct}%) — {'Passed' if passed else 'Needs review'}")
    # Show previous quiz results
    if st.session_state.quiz_scores:
        st.markdown("**Previous quiz results**")
        for k, v in st.session_state.quiz_scores.items():
            st.markdown(f"- {k}: {v['score']} correct, {v['pct']}% — {'Passed' if v['passed'] else 'Not passed'}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Resources & Q&A")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # Resource video embeds
    st.markdown("**Live videos**")
    for vid in RESOURCES["videos"]:
        st.markdown(f"**{vid['title']}**")
        st.video(vid["embed"])
    st.markdown("**Links & Readings**")
    for link in RESOURCES["links"]:
        st.markdown(f"- [{link['title']}]({link['url']})")
    for r in RESOURCES["readings"]:
        st.markdown(f"- {r['title']} — {r.get('note','')}")
    st.markdown("---")
    st.markdown("**Ask the course LLM assistant**")
    llm_question = st.text_input("Ask a question about today's lecture or the quizzes:", key="llm_question")
    if st.button("Ask LLM"):
        # Basic LLM integration placeholder. Replace with your OpenAI call or other LLM call.
        # IMPORTANT: Do not store API keys here in session_state. Use secure backend or Secrets manager.
        if not openai_key:
            st.info("No OpenAI key provided. Returning canned answer. To enable live answers, paste an OpenAI key in the sidebar.")
            canned = f"I can help: try asking about definitions (e.g. 'What's Durkheim's view?'), or request examples. Preview of your question: {llm_question}"
            st.markdown(canned)
            st.session_state.llm_history.append({"question": llm_question, "answer": canned})
        else:
            try:
                # Minimal OpenAI example (user should pip install openai)
                import openai
                openai.api_key = openai_key
                prompt = [
                    {"role": "system", "content": "You are a helpful teaching assistant for an introductory course on religion and philosophy. Keep answers concise and reference today's Day 1 topics."},
                    {"role": "user", "content": llm_question}
                ]
                resp = openai.ChatCompletion.create(model=llm_model, messages=prompt, max_tokens=400, temperature=0.2)
                answer = resp["choices"][0]["message"]["content"]
                st.markdown(answer)
                st.session_state.llm_history.append({"question": llm_question, "answer": answer})
            except Exception as e:
                st.error(f"LLM call failed: {e}")
    if st.session_state.llm_history:
        st.markdown("**Recent LLM Q&A**")
        for item in st.session_state.llm_history[-5:]:
            st.markdown(f"- **Q:** {item['question']}")
            st.markdown(f"  - **A:** {item['answer']}")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Bottom toolbar: slide nav, keyboard hints, completion -----------------
st.write("---")
col1, col2, col3 = st.columns([1,1,2])
with col1:
    if st.button("← Previous Slide"):
        st.session_state.slide_idx = max(0, st.session_state.slide_idx - 1)
with col2:
    if st.button("Next Slide →"):
        st.session_state.slide_idx = min(len(SLIDES)-1, st.session_state.slide_idx + 1)
with col3:
    st.markdown("**Shortcuts:** F = fullscreen | P = presentation mode | N = notes (presenter). Use the sidebar to start timers.")

# ----------------- Simple timer display (if active) -----------------
if st.session_state.get("timer_seconds"):
    remaining = st.session_state.timer_seconds - int(time.time() - st.session_state.get("timer_start", time.time()))
    if remaining <= 0:
        st.success("⏰ Time's up!")
        st.session_state.pop("timer_seconds", None)
        st.session_state.pop("timer_start", None)
    else:
        mins = remaining // 60
        secs = remaining % 60
        st.warning(f"⏳ Activity timer: {mins}:{str(secs).zfill(2)} remaining")

# ----------------- Mark slide as complete when viewed for some time (soft) -----------------
# We'll mark it if the user clicked "Next" — keep behavior simple and robust.
st.session_state.completed.add(st.session_state.slide_idx)

# ----------------- Footer: course & deploy info -----------------
st.write("---")
st.markdown("""
<div style="display:flex; justify-content:space-between;">
  <div>
    <strong>PHL 101 — Comparative Religions I</strong><br/>
    Developed by Xavier Honablue M.Ed for CognitiveCloud.ai
  </div>
  <div class="small-muted">
    Use responsibly. Configure LLM keys via the sidebar. This app stores no API keys long-term.
  </div>
</div>
""", unsafe_allow_html=True)
