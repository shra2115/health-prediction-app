import sqlite3

def create_table():
    conn = sqlite3.connect("patients.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,dob TEXT,email TEXT,
    glucose REAL,haemoglobin REAL,
    cholesterol REAL,remarks TEXT)''')
    conn.commit()
    conn.close()

def add_patient(name,dob,email,glucose,haemoglobin,cholesterol,remarks):
    conn = sqlite3.connect("patients.db")
    conn.execute('INSERT INTO patients(name,dob,email,glucose,haemoglobin,cholesterol,remarks) VALUES(?,?,?,?,?,?,?)',
                 (name,dob,email,glucose,haemoglobin,cholesterol,remarks))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect("patients.db")
    data = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return data

def delete_patient(pid):
    conn = sqlite3.connect("patients.db")
    conn.execute("DELETE FROM patients WHERE id=?", (pid,))
    conn.commit()
    conn.close()
