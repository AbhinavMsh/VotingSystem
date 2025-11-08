import streamlit as st
import sqlite3

# --- Database connection helper ---
def get_db_connection():
    conn = sqlite3.connect('voting.db')
    conn.row_factory = sqlite3.Row
    return conn
# not logged in warning 
st.title("Admin Panel")
if "username" not in st.session_state:
    st.warning("Please log in first.")
    st.stop()
# not admin warning 
role = st.session_state.get("role")
if role != "Admin":
    st.warning("Not an Admin!")
    st.stop()
# options
choice = st.radio("Settings",["Add Voter", "Remove Voter", 
                     "Add Candidate", "Remove Candidate"], horizontal=True)

if choice == "Add Voter":
    id = st.text_input("",placeholder="ID")
    username = st.text_input("",placeholder="Username")
    password = st.text_input("",placeholder="Password", type="password")
    hasVoted = 0

    conn = get_db_connection()
    c = conn.cursor()

    if st.button("Submit"):
        if not id or not username or not password:
            st.warning("Please fill all fields")
        else:
            try:
                c.execute(
                    "INSERT INTO voters (id, username, password, has_voted) VALUES (?, ?, ?, ?)",
                    (id, username, password, hasVoted)
                )
                conn.commit()
                st.success("Voter added successfully.")
            except sqlite3.IntegrityError:
                st.error("A voter with that ID already exists.")
            finally:
                conn.close()


elif choice == "Remove Voter":
    id = st.text_input("", placeholder="ID")

    if st.button("Search"):
        conn = get_db_connection()
        c = conn.cursor()

        c.execute("SELECT * FROM voters WHERE id=?", (id,))
        result = c.fetchone()

        if result:
            st.session_state["search_result"] = dict(result)
            st.success("Voter found.")
        else:
            st.info("No voter found with that ID.")
            st.session_state.pop("search_result", None)
        conn.close()

    # Show result if present
    if "search_result" in st.session_state:
        st.write(st.session_state["search_result"])

        if st.button("Remove Voter"):
            conn = get_db_connection()
            c = conn.cursor()
            try:
                c.execute("DELETE FROM voters WHERE id = ?", (id,))
                conn.commit()
                st.success("Voter removed successfully.")
                st.session_state.pop("search_result", None)
            except sqlite3.Error as e:
                st.error(f"Error removing voter: {e}")
            finally:
                conn.close()



elif choice == "Add Candidate":
    id = st.text_input("",placeholder="ID")
    username = st.text_input("",placeholder="Username")
    votes=0

    conn = get_db_connection()
    c = conn.cursor()

    if st.button("Submit"):
        if not id or not username:
            st.warning("Please fill all fields")
        else:
            try:
                c.execute(
                    "INSERT INTO candidates (id, name, votes) VALUES (?, ?, ?)",
                    (id, username, votes)
                )
                conn.commit()
                st.success("Candidate added successfully.")
            except sqlite3.IntegrityError:
                st.error("A candidate with that ID already exists.")
            finally:
                conn.close()

elif choice == "Remove Candidate":
    id = st.text_input("", placeholder="ID")

    if st.button("Search"):
        conn = get_db_connection()
        c = conn.cursor()

        c.execute("SELECT * FROM candidates WHERE id=?", (id,))
        result = c.fetchone()

        if result:
            st.session_state["search_result"] = dict(result)
            st.success("Candidate found.")
        else:
            st.info("No Candidate found with that ID.")
            st.session_state.pop("search_result", None)
        conn.close()

    # Show result if present
    if "search_result" in st.session_state:
        st.write(st.session_state["search_result"])

        if st.button("Remove Candidate"):
            conn = get_db_connection()
            c = conn.cursor()
            try:
                c.execute("DELETE FROM Candidates WHERE id = ?", (id,))
                conn.commit()
                st.success("Candidate removed successfully.")
                st.session_state.pop("search_result", None)
                
            except sqlite3.Error as e:
                st.error(f"Error removing Candidate: {e}")
            finally:
                conn.close()
