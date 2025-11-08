# 🗳️ Simple Voting System for Class Representatives

A secure and user-friendly web-based **voting system** built with **Streamlit** and **SQLite**.  
It allows students to log in, cast their votes once, and view live results — while the admin manages voters and candidates efficiently.

🔗 **Live App:** [https://votingsystem-se.streamlit.app/](https://votingsystem-se.streamlit.app/)

---

## **Project Overview**

Manual voting during class elections is often slow, error-prone, and difficult to manage.  
This project automates the process with a simple, secure system that ensures:
- One vote per student.
- Easy management for the admin.
- Real-time display of results.

---

## **Features**

### For Students
- Secure login using credentials.
- View list of candidates.
- Vote once per election.
- See confirmation after voting.

### For Admin
- Login access for managing the election.
- Add, remove, or reset voters and candidates.
- View live voting statistics.

### Additional
- Real-time results display using Streamlit charts.
- Simple SQLite database for storage.
- Clean, responsive Streamlit interface.

---

## **Tech Stack**

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| Library Used | `streamlit`, `sqlite3` |

---

## **Project Structure**
```text
voting_system/
├── app.py            # Login page (main entry)
├── pages/
│   ├── vote.py       # Student voting page
│   ├── admin.py      # Admin dashboard
│   └── results.py    # Live results page
├── setup_database.py # Creates tables & inserts sample data
└── voting.db         # SQLite database
```

## How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/AbhinavMsh/VotingSystem.git
```

2. Navigate to the project directory
```bash
cd VotingSystem
```

3. Create a virtual environment (optional)
```bash
python -m venv venv
```

4. Activate the virtual environment

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

5. Install dependencies
```bash
pip install -r requirements.txt
```

6. Run the application
```bash
python home.py
```

7. Open your browser and visit:
```
http://localhost:5000
```

## 🔐 Default Credentials

| Role    | Username   | Password  |
|---------|------------|-----------|
| Admin   | admin      | admin123  |
| Student | Abhinav    | 1234      |

## 📚 Future Enhancements

- Add OTP or email-based authentication.
- Generate downloadable election reports (CSV / PDF).
- Role-based access management with finer permissions.
- Cloud database integration (Postgres / Firestore) for scalability.
- Audit logs and tamper-evident vote history.
- Support for multiple simultaneous elections and scheduling.
- Improved accessibility and responsive UI refinements.

## 👨‍💻 Author

Abhinav Masih  
📧 masih.abhinav@icloud.com

🌐 Live Streamlit App: https://votingsystem-se.streamlit.app/
