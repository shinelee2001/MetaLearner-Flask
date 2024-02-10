from flask import Flask
from main_routes import main_bp

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
