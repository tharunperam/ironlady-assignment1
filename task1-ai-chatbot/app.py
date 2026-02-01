import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Iron Lady | AI Program Advisor",
    page_icon="👩‍💼",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
    color: #b0125b;
}
.sub-title {
    font-size: 18px;
    color: #444;
}
.card {
    background-color: #f9f1f5;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}
.footer {
    text-align: center;
    color: #888;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-title">👩‍💼 Iron Lady – AI Program Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Helping women choose the right career & leadership programs</div>', unsafe_allow_html=True)
st.write("")

# ---------- SIDEBAR ----------
st.sidebar.title("📌 Quick Guidance")
option = st.sidebar.radio(
    "What are you looking for?",
    (
        "Career Switch",
        "Leadership Growth",
        "Entrepreneurship",
        "Student / Fresher",
        "Program Fees",
        "Program Duration"
    )
)

# ---------- RESPONSE LOGIC ----------
def get_response(text):
    text = text.lower().strip()

    if "career" in text or "switch" in text:
        return """
<h3>🌱 Career Transition Program</h3>
✔ Designed for women planning a career change<br>
✔ Skill development + confidence building<br>
✔ Guided mentorship and structured learning
"""

    elif "leadership" in text or "manager" in text or "lead" in text:
        return """
<h3>👑 Women Leadership Program</h3>
✔ Leadership mindset & communication<br>
✔ Decision-making and confidence<br>
✔ Ideal for working professionals
"""

    elif "business" in text or "startup" in text or "entrepreneur" in text:
        return """
<h3>🚀 Women Entrepreneurship Program</h3>
✔ Business fundamentals<br>
✔ Idea validation & execution<br>
✔ Mentorship from industry experts
"""

    elif "student" in text or "fresher" in text or "graduate" in text:
        return """
<h3>🎓 Skill Development Program</h3>
✔ Industry-ready skills<br>
✔ Career guidance<br>
✔ Best for students and freshers
"""

    elif "fee" in text or "cost" in text or "price" in text:
        return """
<h3>💰 Program Fees</h3>
✔ Fees vary depending on the program<br>
✔ Flexible payment options available<br>
✔ Contact Iron Lady support for exact details
"""

    elif "duration" in text or "weeks" in text or "time" in text:
        return """
<h3>⏳ Program Duration</h3>
✔ Typically 6–12 weeks<br>
✔ Live sessions + self-paced learning
"""

    return """
<h3>⚠️ Not Related to Iron Lady Programs</h3>
I am designed to help with Iron Lady’s career and learning programs for women.<br><br>

✔ Career switching<br>
✔ Leadership growth<br>
✔ Entrepreneurship guidance<br>
✔ Student & fresher programs<br><br>

Please ask a question related to career development or program guidance.
"""
# ---------- USER INPUT ----------
st.write("### 💬 Ask the Advisor")
user_input = st.text_input("Type your career goal or question:")

# ---------- DISPLAY RESPONSE ----------

# Priority: Text input > Sidebar
if user_input.strip():
    st.markdown("**🧠 Interpreting your typed input...**")
    response = get_response(user_input)

else:
    st.markdown(f"**📌 Based on your selection: {option}**")
    response = get_response(option)

st.markdown(f'<div class="card">{response}</div>', unsafe_allow_html=True)
# ---------- FOOTER ----------
st.markdown('<div class="footer">© Iron Lady | AI & Technology Intern Assignment</div>', unsafe_allow_html=True)