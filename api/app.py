from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/data.db")

CLASSES = ["Year 1", "Year 2", "Year 3", "Year 4"]

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, timeout=5, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE,
            name TEXT NOT NULL,
            class TEXT NOT NULL
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)
        conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_student', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        sid = request.form['student_id']
        name = request.form['name']
        cls = request.form['class']

        try:
            with get_db_connection() as conn:
                existing = conn.execute(
                    "SELECT * FROM students WHERE student_id=?", (sid,)
                ).fetchone()
                if existing:
                    return render_template('error.html', message=f"Student ID '{sid}' already exists!")

                conn.execute(
                    "INSERT INTO students (student_id, name, class) VALUES (?, ?, ?)",
                    (sid, name, cls)
                )
                conn.commit()
            return redirect('/')
        except sqlite3.OperationalError as e:
            return render_template('error.html', message=str(e))

    return render_template('new_student.html', classes=CLASSES)

@app.route('/select_class/<action>')
def select_class(action):
    return render_template('select_class.html', classes=CLASSES, action=action)

@app.route('/attendance/<cls>', methods=['GET', 'POST'])
def attendance(cls):
    with get_db_connection() as conn:
        students = conn.execute(
            "SELECT * FROM students WHERE class=?", (cls,)
        ).fetchall()

    if request.method == 'POST':
        chosen_date = request.form['date']
        try:
            with get_db_connection() as conn:
                for student in students:
                    status = request.form.get(f"status_{student['student_id']}", "Absent")

                    existing = conn.execute(
                        "SELECT * FROM attendance WHERE student_id=? AND date=?",
                        (student['student_id'], chosen_date)
                    ).fetchone()

                    if existing:
                        conn.execute(
                            "UPDATE attendance SET status=? WHERE student_id=? AND date=?",
                            (status, student['student_id'], chosen_date)
                        )
                    else:
                        conn.execute(
                            "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                            (student['student_id'], chosen_date, status)
                        )
                conn.commit()
            return redirect('/')
        except sqlite3.OperationalError as e:
            return render_template('error.html', message=str(e))

    return render_template('attendance.html', students=students, cls=cls, today=date.today())

@app.route('/records/<cls>', methods=['GET', 'POST'])
def records(cls):
    chosen_date = None
    if request.method == 'POST':
        chosen_date = request.form.get('date')

    with get_db_connection() as conn:
        if chosen_date:
            rec = conn.execute("""
                SELECT s.student_id, s.name, a.status
                FROM students s
                LEFT JOIN attendance a
                ON s.student_id = a.student_id AND a.date = ?
                WHERE s.class = ?
                ORDER BY s.name
            """, (chosen_date, cls)).fetchall()

            rec_list = list(rec)

            if rec_list and all(r['status'] is None for r in rec_list):
                return render_template('not_found.html')
        else:
            rec = conn.execute("""
                SELECT s.student_id, s.name, NULL AS status
                FROM students s
                WHERE s.class = ?
                ORDER BY s.name
            """, (cls,)).fetchall()
            rec_list = list(rec)

    return render_template(
        'records.html',
        records=rec_list,
        cls=cls,
        chosen_date=chosen_date
    )

@app.route('/remove/<cls>', methods=['GET', 'POST'])
def remove_student(cls):
    with get_db_connection() as conn:
        students = conn.execute(
            "SELECT * FROM students WHERE class=?", (cls,)
        ).fetchall()

    if request.method == 'POST':
        sid = request.form['student_id']
        try:
            with get_db_connection() as conn:
                conn.execute("DELETE FROM students WHERE student_id=?", (sid,))
                conn.commit()
            return redirect('/')
        except sqlite3.OperationalError as e:
            return render_template('error.html', message=str(e))

    return render_template('remove_student.html', students=students, cls=cls)

