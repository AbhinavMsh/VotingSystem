import streamlit as st
import sqlite3
st.set_page_config(page_title="Class Representative Voting System")

def check_login(username, password, role):
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()
      
    #conn.cursor() returns a sqlite3.Cursor which provides methods like:
    #execute(sql, params) — run a query or statement
    #fetchone(), fetchall(), fetchmany(n) — get results
    #close() — release cursor resources
    
    
    try:
        if role == "Admin":
            c.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
        else:
            c.execute("SELECT * FROM voters WHERE username=? AND password=?", (username, password))
        # Select * returns every column from the matched row
        result = c.fetchone() # to get the matched user record (if any) for the provided username/password (type - tuple)
    finally:
        c.close()
        conn.close()
    return result

st.title("Class Representative Voting System")

role = st.radio("Login as:", ["Student", "Admin"])
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"): # as st.button return true, adding if makes it like a submit button
    user = check_login(username, password, role)

    if user:
        # Storing username and role in session state
        st.session_state["username"] = username
        st.session_state["role"] = role

        st.success(f"Welcome, {username}!")
        if role == "Admin":
            st.switch_page("pages/admin.py")
        else:
            st.switch_page("pages/vote.py")
    else:
        st.error("Invalid credentials")
