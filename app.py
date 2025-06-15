import streamlit as st

# Page setup
st.set_page_config(page_title="Investor Persona Profiler", layout="centered")

# Custom style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Libre Baskerville', serif;
        background-color: #f9f9f9;
        color: #2e2e2e;
    }

    .stButton>button {
        background-color: #2d4059;
        color: white;
        border-radius: 12px;
        font-size: 16px;
        padding: 0.6em 1.2em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4d6d8a;
        transform: scale(1.02);
    }

    .stRadio > div {
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("🧭 Investor Persona Profiler")
st.markdown("""
Welcome to a personalized investment assessment tool.  
Answer the following questions to discover your **investment personality** and receive custom insights.  
""")

# Questionnaire setup
questions = [
    {
        "question": "What is your primary investment objective?",
        "options": ["Preserve capital", "Generate income", "Grow capital moderately", "Maximize long-term growth"]
    },
    {
        "question": "What is your investment time horizon?",
        "options": ["Less than 3 years", "3–5 years", "6–10 years", "More than 10 years"]
    },
    {
        "question": "How would you react if your investment dropped by 15% in a year?",
        "options": ["Sell everything", "Reduce investment", "Stay invested", "Buy more at lower prices"]
    },
    {
        "question": "How much investment experience do you have?",
        "options": ["None", "Basic (savings, GICs)", "Moderate (funds, ETFs)", "Advanced (stocks, options)"]
    },
    {
        "question": "What portion of your total savings do you plan to invest?",
        "options": ["Less than 10%", "10–25%", "25–50%", "Over 50%"]
    },
    {
        "question": "How important is liquidity to you?",
        "options": ["Very important", "Somewhat important", "Neutral", "Not important at all"]
    },
    {
        "question": "What type of return are you expecting?",
        "options": ["1–3% annually", "3–6% annually", "6–10% annually", "10%+ annually"]
    },
    {
        "question": "Are you financially dependent on this investment?",
        "options": ["Yes, completely", "Somewhat", "Not really", "Not at all"]
    }
]

# Score and responses
total_score = 0
for idx, q in enumerate(questions):
    response = st.radio(f"**{q['question']}**", q["options"], key=f"q{idx}")
    total_score += q["options"].index(response)

# Profile logic
if st.button("🎯 Get My Investor Profile"):
    if total_score <= 7:
        profile = "🛡️ Capital Preserver"
        desc = "You prioritize security and minimal risk. Your portfolio might include GICs, bonds, and savings accounts."
    elif total_score <= 14:
        profile = "💰 Income Seeker"
        desc = "You aim for steady income with controlled risk. Expect dividend-paying stocks and fixed income instruments."
    elif total_score <= 21:
        profile = "⚖️ Balanced Investor"
        desc = "You're open to moderate risk for long-term growth. Your portfolio likely blends equities and fixed income."
    else:
        profile = "🚀 Growth-Oriented Investor"
        desc = "You thrive on long-term opportunities and high-return assets. Equities, international markets, and innovation sectors suit you."

    st.subheader(f"Your Investor Profile: {profile}")
    st.write(desc)
    st.success("Use this insight to guide your next investment conversation.")
    st.balloons()
