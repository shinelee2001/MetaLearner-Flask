from flask import Blueprint, render_template, request, redirect, flash, url_for
from datetime import datetime
from DB_handler import create_db_table, get_course_names, fetch_sorted_notes_data
import sqlite3

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    create_db_table()
    notes_data = fetch_sorted_notes_data()
    course_names = get_course_names()

    ########################################
    # Sort the data by the date difference #
    ########################################
    current_date = datetime.now().date()
    date_diff_one = []
    for note in notes_data:
        saved_date = note[3].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 1:
            date_diff_one.append(note)

    date_diff_four = []
    for note in notes_data:
        saved_date = note[3].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 4 and diff > 1:
            date_diff_four.append(note)

    date_diff_seven = []
    for note in notes_data:
        saved_date = note[3].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 7 and diff > 4:
            date_diff_seven.append(note)

    date_diff_fourteen = []
    for note in notes_data:
        saved_date = note[3].split()[0]
        saved_datetime = datetime.strptime(saved_date, "%Y-%m-%d").date()
        diff = (current_date - saved_datetime).days
        if diff <= 14 and diff > 7:
            date_diff_fourteen.append(note)

    return render_template(
        "index.html",
        notes_data=notes_data,
        course_names=course_names,
        date_diff_one=date_diff_one,
        date_diff_four=date_diff_four,
        date_diff_seven=date_diff_seven,
        date_diff_fourteen=date_diff_fourteen,
    )


@main_bp.route("/save", methods=["POST"])
def save():
    create_db_table()
    
    course = request.form.get("course")
    content_type = request.form.get("contentType")
    title = request.form.get("title")
    content = request.form.get("content")
    saved_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if course == "None" or course == "Select The Course":
        flash("Select the course!", "error")
        return redirect(url_for("main.index"))

    conn = sqlite3.connect("NOTES.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO NOTES (course, content_type, title, content, saved_date) VALUES (?, ?, ?, ?, ?)",
        (course, content_type, title, content, saved_date),
    )
    conn.commit()
    conn.close()

    flash("Saved Successfully!", "success")
    return redirect(url_for("main.index"))
