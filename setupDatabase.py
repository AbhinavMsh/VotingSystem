import sqlite3

# connect or create the database
conn = sqlite3.connect("voting.db")
c = conn.cursor()

# --- Insert sample data ---
# Admin
# Voters
voters = [
    [24150031, "Abhinav", "1234"],
    [24150032, "Aditya", "1234"],
    [24150033, "Allen", "1234"],
    [24150034, "Ayush", "1234"],
    [24150035, "Chandan", "1234"],
    [24150036, "Om", "1234"],
    [24150037, "Sanchay", "1234"],
    [24150038, "Shreya", "1234"],
    [24150039, "Sid", "1234"]
]


c.executemany("INSERT OR IGNORE INTO voters (id, username, password) VALUES (?, ?, ?)", voters)

conn.commit()
conn.close()

print("✅ Database setup complete!")
