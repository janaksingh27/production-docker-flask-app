import os
from flask import Flask

app = Flask(__name__)

APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello Janak from Docker!")

@app.route("/")
def home():
    return APP_MESSAGE

app.run(host="0.0.0.0", port=5000)
