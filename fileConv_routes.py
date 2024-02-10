from flask import Blueprint, render_template, request
from DB_handler import create_db_table
from datetime import datetime
import pandas as pd
import sqlite3

fileConvert_bp = main_bp = Blueprint("fileConvert", __name__)


@fileConvert_bp.route("/preview", methods=["POST"])
def preview():
    create_db_table()

    saved_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = request.files["file"]
    dataFrame = pd.read_excel(file)

    dataFrame.rename(
        columns={
            "Course": "course",
            "Content Type": "content_type",
            "Title": "title",
            "Content": "content",
        },
        inplace=True,
    )
    dataFrame["saved_date"] = saved_date

    """
    conn = sqlite3.connect("NOTES.db")
    dataFrame.to_sql("NOTES", conn, if_exists="append", index=False)
    """

    return render_template("excelPreview.html", notes=dataFrame)
