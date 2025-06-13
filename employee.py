import sqlite3

def add_employee(name, email, job_title, department, salary):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees (name, email, job_title, department, salary) VALUES (?, ?, ?, ?, ?)",
                       (name, email, job_title, department, salary))
        conn.commit()
    except sqlite3.IntegrityError:
        print(" Email already exists!")
    conn.close()

def get_all_employees():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_employee_by_name(name):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE LOWER(name) = LOWER(?)", (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_employee(emp_id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()

def update_employee(emp_id, name, email, job_title, department, salary):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE employees SET name=?, email=?, job_title=?, department=?, salary=?
        WHERE id=?
    """, (name, email, job_title, department, salary, emp_id))
    conn.commit()
    conn.close()


def get_employee_by_id(emp_id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    data = cursor.fetchone()
    conn.close()
    return data
