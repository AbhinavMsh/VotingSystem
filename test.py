import sqlite3

conn = sqlite3.connect("voting.db")
c = conn.cursor()

print("Admins:", c.execute("SELECT * FROM admin").fetchall())
print("Voters:", c.execute("SELECT * FROM voters").fetchall())
print("Candidates:", c.execute("SELECT * FROM candidates").fetchall())