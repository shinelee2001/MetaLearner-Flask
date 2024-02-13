from flask import Flask
from routes.main_routes import main_bp
from routes.fileConv_routes import fileConvert_bp
from routes.error_routes import error_bp
from routes.externalNotes_routes import externalNotes_bp

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(main_bp)
app.register_blueprint(fileConvert_bp)
app.register_blueprint(error_bp)
app.register_blueprint(externalNotes_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
