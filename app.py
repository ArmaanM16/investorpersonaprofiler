import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Investor Persona Profiler", layout="centered")

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
    </style>
""", unsafe_allow_html=True)

st.title("🧭 Investor Persona Profiler")
st.markdown("Answer 15 thoughtful questions to discover your investor personality and get tailored ETF suggestions.")

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
    elif score <= 30:
        profile = "💰 Income Seeker"
        desc = "You look for consistent income while managing risk. Dividend stocks and bond ETFs work well for you."
        etfs = ["VDY - Vanguard Canadian High Dividend Yield", "XDV - iShares Dividend Index ETF"]
    elif score <= 45:
        profile = "⚖️ Balanced Investor"
        desc = "You accept moderate risk to achieve growth. A 60/40 blend of equities and bonds is ideal."
        etfs = ["VBAL - Vanguard Balanced ETF", "XBAL - iShares Core Balanced ETF"]
    else:
        profile = "🚀 Growth-Oriented Investor"
        desc = "You seek high returns and are comfortable with risk. Equities, tech, and global ETFs are your go-to."
        etfs = ["VFV - Vanguard S&P 500 ETF", "XQQ - iShares NASDAQ 100 ETF", "VEQT - Vanguard All Equity ETF"]

    st.subheader(f"Your Investor Profile: {profile}")
    st.markdown(desc)
    st.markdown("**Recommended ETFs:**")
    for etf in etfs:
        st.markdown(f"- {etf}")

    # Show chart
    profiles = ['Capital Preserver', 'Income Seeker', 'Balanced', 'Growth']
    ranges = [15, 30, 45, 60]
    fig, ax = plt.subplots()
    ax.bar(profiles, ranges, color=['#6c757d', '#17a2b8', '#ffc107', '#28a745'])
    ax.set_ylabel('Score Threshold')
    ax.set_title('Investor Profile Score Ranges')
    st.pyplot(fig)

    st.success("Use these results to guide conversations with financial advisors or plan your portfolio.")

