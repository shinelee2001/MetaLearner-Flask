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


def get_course_names():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course FROM study")
    course_names = cursor.fetchall()
    conn.close()
    return course_names


def fetch_sorted_study_data():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT content_type, content, saved_date, course FROM study ORDER BY saved_date"
    )
    data = cursor.fetchall()
    conn.close()
    return data


@study_bp.route("/")
def index():
    study_data = fetch_sorted_study_data()
    course_names = get_course_names()

    # Sort the data where date diff is max 3
    current_date = datetime.now().date()
    date_diff_one = []
    for entry in study_data:
        saved_date = entry[2].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 1:
            date_diff_one.append(entry)

    date_diff_four = []
    for entry in study_data:
        saved_date = entry[2].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 4 and diff > 1:
            date_diff_four.append(entry)

    data_by_date = [date_diff_one, date_diff_four]

    return render_template(
        "index.html",
        study_data=study_data,
        course_names=course_names,
        data_by_date=data_by_date,
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
    return redirect(url_for("study.index"))
