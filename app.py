from datetime import datetime
from html import escape

import streamlit as st


st.set_page_config(
    page_title="AI Study Session Planner",
    page_icon=":books:",
    layout="wide",
)

st.markdown(
    """
<style>
.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}
.subtitle {
    font-size: 1.05rem;
    color: #5f6368;
    margin-bottom: 1.4rem;
}
.card {
    padding: 1rem 1.2rem;
    border-radius: 8px;
    border: 1px solid #e3e5e8;
    background: #fafafa;
    margin-bottom: 1rem;
}
.small-muted {
    color: #6f747a;
    font-size: 0.9rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">AI Study Session Planner</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Create a focused, repeatable study plan based on your topic, time, level, and goal.</div>',
    unsafe_allow_html=True,
)


def split_session_time(time_minutes):
    """Return section lengths that always add up to the available time."""
    warmup = max(5, round(time_minutes * 0.10))
    review = max(5, round(time_minutes * 0.15))
    remaining = time_minutes - warmup - review
    learn = max(10, round(remaining * 0.55))
    practice = time_minutes - warmup - review - learn
    return warmup, learn, practice, review


def build_plan(topic, time_minutes, level, goal, focus_area, energy, output_style):
    time_minutes = int(time_minutes)
    warmup, learn, practice, review = split_session_time(time_minutes)

    if level == "Beginner":
        depth = "focus on simple definitions, examples, and basic use cases"
        difficulty = "easy to medium"
    elif level == "Intermediate":
        depth = "connect concepts together and practice realistic scenarios"
        difficulty = "medium"
    else:
        depth = "focus on edge cases, trade-offs, and exam-style reasoning"
        difficulty = "medium to advanced"

    if energy == "Low":
        pace = "Use a gentle pace, more breaks, and avoid heavy memorization."
    elif energy == "Medium":
        pace = "Use a balanced pace with short breaks between sections."
    else:
        pace = "Use an intensive pace and spend more time on active recall."

    plan = [
        (
            "Warm-up",
            warmup,
            f"Write what you already know about {topic}. List 3 questions you want answered.",
        ),
        (
            "Focused learning",
            learn,
            f"Study {topic} and {depth}. Focus especially on: {focus_area}.",
        ),
        (
            "Practice",
            practice,
            f"Solve {difficulty} practice questions related to {goal}. Explain each answer in your own words.",
        ),
        (
            "Review and next step",
            review,
            "Summarize the session in 5 bullet points and decide the next topic to study.",
        ),
    ]

    concepts = [
        f"Core definitions and purpose of {topic}",
        f"Main components, services, or steps involved in {topic}",
        f"Common real-world use cases related to {focus_area}",
        "Typical mistakes or confusing points beginners face",
        f"How {topic} connects to the final goal: {goal}",
    ]

    questions = [
        f"What problem does {topic} solve?",
        f"What are the most important parts of {topic}?",
        f"Give one real-world example where {topic} would be useful.",
        f"What is one common mistake people make when learning {topic}?",
        f"How would you explain {topic} to a beginner in two sentences?",
    ]

    if output_style == "Exam-focused":
        questions.extend(
            [
                f"Which scenario would best fit {topic}, and why?",
                f"What answer choice would be wrong for {topic}, and why?",
            ]
        )
    elif output_style == "Project-focused":
        questions.extend(
            [
                f"How can you apply {topic} in a small practical project?",
                f"What would be the first step to build something using {topic}?",
            ]
        )
    else:
        questions.extend(
            [
                f"What is one thing about {topic} you still do not understand?",
                "What should you review tomorrow to keep the knowledge fresh?",
            ]
        )

    return plan, concepts, questions, pace


with st.sidebar:
    st.header("Session Inputs")
    topic = st.text_input("Study topic", value="AWS AI services")
    time_minutes = st.slider("Available study time", 30, 240, 90, 15)
    level = st.selectbox("Current level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_area(
        "Learning goal",
        value="Understand which AWS AI service fits each business use case.",
    )
    focus_area = st.text_input(
        "Focus area",
        value="sentiment analysis, recommendations, document processing, and chatbots",
    )
    energy = st.selectbox("Energy level today", ["Low", "Medium", "High"], index=1)
    output_style = st.selectbox(
        "Output style",
        ["Balanced", "Exam-focused", "Project-focused"],
    )
    generate = st.button("Generate Study Plan", type="primary")

topic = topic.strip() or "your topic"
goal = goal.strip() or "your learning goal"
focus_area = focus_area.strip() or "your focus area"

if generate:
    plan, concepts, questions, pace = build_plan(
        topic,
        time_minutes,
        level,
        goal,
        focus_area,
        energy,
        output_style,
    )

    st.success("Your study session plan is ready.")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("Step-by-step Study Plan")
        for title, minutes, action in plan:
            st.markdown(
                f"""
                <div class="card">
                    <b>{escape(title)}</b> - {minutes} minutes<br>
                    <span>{escape(action)}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.subheader("Mini Checklist")
        st.checkbox("I understand the main idea.")
        st.checkbox("I can explain it without looking.")
        st.checkbox("I solved practice questions.")
        st.checkbox("I wrote what to study next.")

    with col2:
        st.subheader("Key Concepts")
        for item in concepts:
            st.write(f"- {item}")

        st.subheader("Practice Questions")
        for index, question in enumerate(questions, 1):
            st.write(f"{index}. {question}")

        st.subheader("Study Advice")
        st.info(pace)

    st.divider()
    st.subheader("Copyable Summary")
    summary = f"""Study Topic: {topic}
Available Time: {time_minutes} minutes
Current Level: {level}
Goal: {goal}
Focus Area: {focus_area}
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Recommended approach:
{pace}

Next action:
Start with a short warm-up, study the core concepts, practice questions, then summarize what you learned."""
    st.code(summary, language="text")

else:
    st.info("Fill in the inputs from the sidebar, then click Generate Study Plan.")
    st.markdown(
        """
**Example use:**

Topic: AWS AI services

Goal: Choose the correct AWS service for each business scenario

Focus area: Amazon Comprehend, SageMaker AI, Bedrock, Lex, Polly, Transcribe, Kendra
"""
    )

st.markdown("---")
st.markdown(
    '<p class="small-muted">Built as a reusable AI-style productivity app for structured study planning.</p>',
    unsafe_allow_html=True,
)
