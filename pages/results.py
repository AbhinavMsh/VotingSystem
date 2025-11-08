import streamlit as st
import sqlite3
import pandas as pd

# --- Database connection helper ---
def get_db_connection():
    conn = sqlite3.connect('voting.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Fetch and display results ---
def show_results():
    conn = get_db_connection()
    try:
        cur = conn.execute("SELECT id, name, votes FROM candidates")
        rows = cur.fetchall()
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return
    finally:
        conn.close()

    if not rows:
        st.info("No candidates found.")
        return

    results = [{"id": r["id"], "name": r["name"], "votes": r["votes"]} for r in rows]
    results = sorted(results, key=lambda x: x["votes"], reverse=True)

    st.header("Election Results")
    df = pd.DataFrame(results)
    df["id"] = df["id"].astype(str)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Run when the page is loaded
show_results()