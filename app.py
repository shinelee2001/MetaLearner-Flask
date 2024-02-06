from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def create_db_table():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    # Create table if it does not exist
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS study (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course TEXT,
                content_type TEXT,
                content TEXT,
                saved_date DATETIME
            )
        """
    )
    conn.commit()
    conn.close()


def fetch_study_data():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content_type, content, saved_date, course FROM study")
    data = cursor.fetchall()
    conn.close()
    return data


def get_course_names():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course FROM study")
    course_names = cursor.fetchall()
    conn.close()
    return course_names


@app.route("/")
def index():
    study_data = fetch_study_data()
    course_names = get_course_names()
    return render_template(
        "index.html", study_data=study_data, course_names=course_names
    )


@app.route("/save", methods=["POST"])
def save():
    create_db_table()

    course = request.form.get("course")
    content_type = request.form.get("contentType")
    content = request.form.get("content")
    saved_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if course == "None" or course == "Select The Course":
        flash("Select the course!", "error")
        return redirect(url_for("index"))

    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO study (course, content_type, content, saved_date) VALUES (?, ?, ?, ?)",
        (course, content_type, content, saved_date),
    )
    conn.commit()
    conn.close()

    flash("Saved Successfully!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
