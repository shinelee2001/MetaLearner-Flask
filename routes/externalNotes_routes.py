from flask import Blueprint, render_template, request, redirect, url_for, flash
import os

UPLOAD_FOLDER = "C:\\Users\\LG\\Desktop\\1_4_7_14\\uploads"

externalNotes_bp = Blueprint(
    "externalNotes", __name__, template_folder="../templates/externalNotesTemplates"
)


def check_for_webshells():
    try:
        os.system(
            r"C:\\Users\\LG\\Desktop\\1_4_7_14\\websell_detector\\detector"
            + " > output.txt"
        )
        with open("output.txt", "r", encoding="utf-8") as file:
            output = file.read()
        print(output)
    except Exception as e:
        print(f"Error executing detector: {e}")


@externalNotes_bp.route("/externalNotes")
def externalNotes():
    result = check_for_webshells()
    return render_template("uploads.html", result=result)


@externalNotes_bp.route("/externalNotes/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part", "error")
            return redirect(url_for("externalNotes.externalNotes"))

        file = request.files["file"]
        if file.filename == "":
            flash("No selected file", "error")
            return redirect(url_for("externalNotes.externalNotes"))

        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        flash("File uploaded successfully", "info")

        return redirect(url_for("externalNotes.externalNotes"))

    return render_template("uploads.html")
