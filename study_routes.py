from flask import Blueprint, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime

study_bp = Blueprint("study", __name__)


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

@study_bp.route("/")
def index():
    study_data = fetch_study_data()
    course_names = get_course_names()
    return render_template(
        "index.html", study_data=study_data, course_names=course_names
    )
    
@study_bp.route("/save", methods=["POST"])
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