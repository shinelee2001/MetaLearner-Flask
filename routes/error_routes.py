from flask import Blueprint, render_template

error_bp = Blueprint("error", __name__, template_folder="../templates/errorTemplates")

@error_bp.app_errorhandler(404)
def page_note_found(error):
    return render_template('404.html'), 404