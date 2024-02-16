from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
import os, subprocess

UPLOAD_FOLDER = "C:\\Users\\LG\\Desktop\\1_4_7_14\\uploads"

externalNotes_bp = Blueprint(
    "externalNotes", __name__, template_folder="../templates/externalNotesTemplates"
)


def check_for_webshells():
    try:
        detector = "C:\\Users\\LG\\Desktop\\1_4_7_14\\webshell_detector\\detector.exe"
        result = subprocess.run(
            [detector], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except Exception as e:
        print(f"Detector did not run successfully: {e}")

def get_uploaded_files():
    files = os.listdir(UPLOAD_FOLDER)
    return files


@externalNotes_bp.route("/externalNotes")
def externalNotes():
    result = check_for_webshells()
    files = get_uploaded_files()
    return render_template("uploads.html", result=result, files=files)


@externalNotes_bp.route("/externalNotes/save", methods=["POST"])
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

@externalNotes_bp.route("/externalNotes/uploads/<filename>")
def load_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)