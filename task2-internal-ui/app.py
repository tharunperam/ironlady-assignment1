import streamlit as st
import sqlite3

# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect("learners.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS learners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    program TEXT,
    status TEXT
)
""")
conn.close()

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Iron Lady | Internal Dashboard",
    page_icon="📊",
    layout="centered"
)

# ---------- HEADER ----------
st.title("📊 Iron Lady – Internal Learner Management")
st.write("Internal dashboard to manage learner enrollments")

st.divider()

# ---------- CREATE ----------
st.subheader("➕ Add New Learner")

with st.form("add_form"):
    name = st.text_input("Learner Name")
    program = st.selectbox(
        "Program",
        ["Career Transition", "Leadership Program", "Entrepreneurship Program", "Skill Development"]
    )
    status = st.selectbox(
        "Status",
        ["Enrolled", "In Progress", "Completed"]
    )

    submit = st.form_submit_button("Add Learner")

    if submit:
        conn = get_db()
        conn.execute(
            "INSERT INTO learners (name, program, status) VALUES (?, ?, ?)",
            (name, program, status)
        )
        conn.commit()
        conn.close()
        st.success("Learner added successfully")

st.divider()

# ---------- READ ----------
st.subheader("📋 Learner Records")

conn = get_db()
learners = conn.execute("SELECT * FROM learners").fetchall()
conn.close()

if learners:
    for learner in learners:
        with st.expander(f"👩‍🎓 {learner['name']} - {learner['program']}"):
            st.write(f"**Status:** {learner['status']}")

            col1, col2 = st.columns(2)

            # ---------- UPDATE ----------
            with col1:
                new_status = st.selectbox(
                    "Update Status",
                    ["Enrolled", "In Progress", "Completed"],
                    key=f"status_{learner['id']}"
                )
                if st.button("Update", key=f"update_{learner['id']}"):
                    conn = get_db()
                    conn.execute(
                        "UPDATE learners SET status=? WHERE id=?",
                        (new_status, learner['id'])
                    )
                    conn.commit()
                    conn.close()
                    st.success("Status updated")

            # ---------- DELETE ----------
            with col2:
                if st.button("Delete", key=f"delete_{learner['id']}"):
                    conn = get_db()
                    conn.execute(
                        "DELETE FROM learners WHERE id=?",
                        (learner['id'],)
                    )
                    conn.commit()
                    conn.close()
                    st.warning("Learner deleted")
else:
    st.info("No learners found")

st.divider()
st.caption("© Iron Lady | Task 2 – Internal Business Automation")