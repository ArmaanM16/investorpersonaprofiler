import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Investor Persona Profiler", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Quicksand', sans-serif;
        background-color: #fffefc;
        color: #2c3e50;
        font-size: 18px;
    }

    h1, h2, h3 {
        color: #2d4059;
    }

    .stButton>button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 0.6em 1.4em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f65f5f;
        transform: scale(1.05);
    }

    .stRadio > div {
        padding-bottom: 14px;
    }

    .stRadio label {
        font-size: 17px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧭 Investor Persona Profiler")
st.markdown("Answer 15 thoughtful and fun questions to discover your **investor personality** and receive tailored  **ETF recommendations** with a visual chart!")

# Load the rest of the code from previously defined final_app_code

questions = [
    {"question": "What is your primary investment objective?",
     "options": ["Preserve capital", "Generate income", "Grow capital moderately", "Maximize long-term growth"]},
    {"question": "What is your investment time horizon?",
     "options": ["Less than 3 years", "3–5 years", "6–10 years", "More than 10 years"]},
    {"question": "How would you react if your investment dropped by 15% in a year?",
     "options": ["Sell everything", "Reduce investment", "Stay invested", "Buy more at lower prices"]},
    {"question": "How much investment experience do you have?",
     "options": ["None", "Basic (savings, GICs)", "Moderate (funds, ETFs)", "Advanced (stocks, options)"]},
    {"question": "What portion of your total savings do you plan to invest?",
     "options": ["Less than 10%", "10–25%", "25–50%", "Over 50%"]},
    {"question": "How important is liquidity to you?",
     "options": ["Very important", "Somewhat important", "Neutral", "Not important at all"]},
    {"question": "What type of return are you expecting?",
     "options": ["1–3% annually", "3–6% annually", "6–10% annually", "10%+ annually"]},
    {"question": "Are you financially dependent on this investment?",
     "options": ["Yes, completely", "Somewhat", "Not really", "Not at all"]},
    {"question": "How do you feel about market volatility?",
     "options": ["Very uncomfortable", "Uncomfortable", "Neutral", "Comfortable"]},
    {"question": "How frequently do you plan to review your investments?",
     "options": ["Rarely", "Annually", "Quarterly", "Monthly"]},
    {"question": "How would you describe your current financial situation?",
     "options": ["Unstable", "Stable", "Comfortable", "Very secure"]},
    {"question": "Which of the following best describes your attitude toward financial loss?",
     "options": ["Avoid at all costs", "Tolerate minor losses", "Accept moderate losses", "Willing to risk significant losses"]},
    {"question": "Do you prefer guaranteed returns over potentially higher gains?",
     "options": ["Always", "Usually", "Sometimes", "Rarely"]},
    {"question": "How diversified is your current investment portfolio?",
     "options": ["Not at all", "Slightly diversified", "Moderately diversified", "Highly diversified"]},
    {"question": "What level of financial knowledge do you possess?",
     "options": ["Basic", "Intermediate", "Advanced", "Expert"]}
]

score = 0
for i, q in enumerate(questions):
    response = st.radio(f"**{q['question']}**", q["options"], key=f"q{i}")
    score += q["options"].index(response)

if st.button("🎯 Get My Investor Profile"):
    if score <= 15:
        profile = "🛡️ Capital Preserver"
        desc = "You prefer stability over returns. Conservative investments like bonds and GICs suit your style."
        etfs = ["VSB - Vanguard Short-Term Bond ETF", "ZAG - BMO Aggregate Bond Index ETF"]
        chart = "Capital_Preserver_chart.png"
    elif score <= 30:
        profile = "💰 Income Seeker"
        desc = "You look for consistent income while managing risk. Dividend stocks and bond ETFs work well for you."
        etfs = ["VDY - Vanguard Canadian High Dividend Yield", "XDV - iShares Dividend Index ETF"]
        chart = "Income_Seeker_chart.png"
    elif score <= 45:
        profile = "⚖️ Balanced Investor"
        desc = "You accept moderate risk to achieve growth. A 60/40 blend of equities and bonds is ideal."
        etfs = ["VBAL - Vanguard Balanced ETF", "XBAL - iShares Core Balanced ETF"]
        chart = "Balanced_Investor_chart.png"
    else:
        profile = "🚀 Growth-Oriented Investor"
        desc = "You seek high returns and are comfortable with risk. Equities, tech, and global ETFs are your go-to."
        etfs = ["VFV - Vanguard S&P 500 ETF", "XQQ - iShares NASDAQ 100 ETF", "VEQT - Vanguard All Equity ETF"]
        chart = "Growth-Oriented_Investor_chart.png"

    st.subheader(f"Your Investor Profile: {profile}")
    st.markdown(desc)
    st.markdown("**Recommended ETFs:**")
    for etf in etfs:
        st.markdown(f"- {etf}")

    st.image(chart, caption="Suggested Asset Allocation", use_container_width=True)
    st.success("Use these results to guide conversations with financial advisors or plan your portfolio.")
