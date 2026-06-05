# main.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "http://127.0.0.1:5000"
