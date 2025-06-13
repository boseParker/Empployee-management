import sqlite3

def connect():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            job_title TEXT,
            department TEXT,
            salary REAL
        )
    """)
    
    conn.commit()
    conn.close()
