from flask import Flask
from study_routes import study_bp

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(study_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
