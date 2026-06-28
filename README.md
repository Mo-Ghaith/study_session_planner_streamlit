# AI Study Session Planner

A reusable Streamlit productivity app that creates structured study plans based on:

- Study topic
- Available time
- Current level
- Learning goal
- Focus area
- Energy level
- Output style

## How to run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Go to Streamlit Community Cloud.
4. Click `New app`.
5. Select your repository.
6. Set the main file path to `app.py`.
7. Click `Deploy`.
8. Copy the public Streamlit app URL.

## Suggested Udacity Short Description

My app is an AI Study Session Planner that creates a focused study plan based on the user's topic, available time, current level, and learning goal. I built it to make studying more organized, repeatable, and easier to manage when learning technical topics in a limited time.

## Suggested Udacity Reflection

Compared to a chatbot, the app feels more structured and reusable because the input fields guide the user and the output widgets give consistent results every time. In a chatbot, I would need to rewrite the prompt each time, but the app makes the process faster and easier to share.

## Rubric Note

If your Udacity rubric specifically asks for a PartyRock public app link, a Streamlit link may not be accepted unless the reviewer allows alternatives.
