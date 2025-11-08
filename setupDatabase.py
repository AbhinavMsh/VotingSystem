import sqlite3

# connect or create the database
conn = sqlite3.connect("voting.db")
c = conn.cursor()

# --- Insert sample data ---
# Admin
# Voters
students = [
    [24150002, "Swayam", "1234"],
    [24150003, "Akarshi", "1234"],
    [24150004, "Shreenath", "1234"],
    [24150005, "Akshar", "1234"],
    [24150006, "Soumya", "1234"],
    [24150007, "Archit", "1234"],
    [24150008, "Aditya Z", "1234"],
    [24150009, "Vedant", "1234"],
    [24150010, "Sadichha", "1234"],
    [24150011, "Ayush P", "1234"],
    [24150012, "Om S", "1234"],
    [24150013, "Siddhant", "1234"],
    [24150014, "Yash", "1234"],
    [24150015, "Nishita", "1234"],
    [24150016, "Sayali", "1234"],
    [24150017, "Durvesh", "1234"],
    [24150030, "Chandan", "1234"],
    [24150031, "Abhinav", "1234"],
    [24150032, "Siddhi", "1234"],
    [24150033, "Anushka", "1234"],
    [24150034, "Lavkush", "1234"],
    [24150035, "Kshitij", "1234"],
    [24150036, "Atharv SS", "1234"],
    [24150038, "Aksh", "1234"],
    [24150039, "Arnav", "1234"],
    [24150040, "Shreya S", "1234"],
    [24150041, "Raunak", "1234"],
    [24150042, "Ayush M", "1234"],
    [24150043, "Sakshi P", "1234"],
    [24150046, "Sharvari", "1234"],
    [24150048, "Kapil", "1234"],
    [24150052, "Shravanee", "1234"],
    [24150054, "Aditya G", "1234"],
    [24150058, "Vipul", "1234"],
    [24150066, "K Abhinav", "1234"],
    [24150070, "Dinesh", "1234"],
    [24150096, "Santhu", "1234"],
    [24150097, "Atharva K", "1234"],
    [24150098, "Siddesh", "1234"],
    [24150099, "Atharva S", "1234"],
    [24150100, "Prajwal", "1234"],
    [24150101, "Harsh", "1234"],
    [24150102, "Shreya C", "1234"],
    [24150103, "Anaisha", "1234"],
    [24150104, "Yogesh", "1234"],
    [24150105, "Om B", "1234"],
    [24150106, "Sakshi G", "1234"],
    [24150107, "Satyam", "1234"],
    [24150108, "Santosh", "1234"],
    [24150111, "Rozan", "1234"],
    [24150115, "Raja", "1234"],
    [24150116, "Dashrath", "1234"],
    [24150119, "Allen", "1234"],
    [24150124, "Sanchay", "1234"],
    [24150126, "Reyansh", "1234"],
    [24150128, "Bhushan", "1234"],
    [24150131, "Pavan", "1234"],
    [24150143, "Prasanna", "1234"],
    [24150146, "Tejas", "1234"],
    [24150148, "Aditya P", "1234"]
]



c.executemany("INSERT OR IGNORE INTO voters (id, username, password) VALUES (?, ?, ?)", students)

conn.commit()
conn.close()

print("✅ Database setup complete!")
