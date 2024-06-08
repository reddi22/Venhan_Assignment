import sqlite3

def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)')
    conn.commit()
    conn.close()

def insert_student(name: str, grade: float):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    query = 'INSERT INTO students (name, grade) VALUES (?, ?)'
    cursor.execute(query, (name, grade))
    conn.commit()
    conn.close()

def display_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")

# Create the table if it doesn't exist
create_table()

# Insert new students
insert_student('Raju', 9.2)
insert_student('Balu', 7.75)
insert_student('Manoj', 8.5)

# Display all students
display_students()