import sqlite3

def create_db_table():
    conn = sqlite3.connect("NOTES.db")
    cursor = conn.cursor()
    # Create table if it does not exist
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS NOTES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course TEXT,
                content_type TEXT,
                title TEXT,
                content TEXT,
                saved_date DATETIME
            )
        """
    )
    conn.commit()
    conn.close()


def get_course_names():
    conn = sqlite3.connect("NOTES.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course FROM NOTES")
    course_names = cursor.fetchall()
    conn.close()
    return course_names


def fetch_sorted_notes_data():
    conn = sqlite3.connect("NOTES.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT content_type, title, content, saved_date, course FROM NOTES ORDER BY saved_date"
    )
    data = cursor.fetchall()
    conn.close()
    return data