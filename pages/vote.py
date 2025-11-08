import streamlit as st
import sqlite3

# steup Database connection 
def get_db_connection():
    conn = sqlite3.connect('voting.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get candidates list 
def get_candidates():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, name FROM candidates")
    candidates = c.fetchall()
    conn.close()
    return candidates

# Check if voter has already voted
def has_already_voted(username):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT has_voted FROM voters WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    # evaluates to True only when a row was returned and its first (has_voted) column equals 1.
    return result and result[0] == 1 

# Record vote( increment candidate vote and set has_voted to 1)
def record_vote(username, candidate_id):
    conn = get_db_connection()
    c = conn.cursor()

    # Update candidate votes
    c.execute("UPDATE candidates SET votes = votes + 1 WHERE id=?", (candidate_id,))
    # Mark voter as voted
    c.execute("UPDATE voters SET has_voted = 1 WHERE username=?", (username,))
    conn.commit()
    conn.close()

# --- Streamlit App ---
st.title("🗳️ Cast Your Vote")
# check if user accessing voting page without loggin in 
if "username" not in st.session_state:
    st.warning("Please log in first.")
    st.stop()
# greet user
username = st.session_state["username"]
st.write(f"Welcome, **{username}**")

# Check if already voted
if has_already_voted(username):
    st.info("You have already voted. Thank you!")
else:
    # Getting all candidates for voting
    candidates = get_candidates()
    options = [f"{c['id']}: {c['name']}" for c in candidates]
    choice = st.radio("Select your candidate:", options)
    
    # submitting vote 
    if st.button("Submit Vote"):
        candidate_id = int(choice.split(":")[0])
        record_vote(username, candidate_id)
        st.success("Your vote has been recorded successfully!")
        
if st.button("View Results"):
    st.switch_page("pages/results.py")
