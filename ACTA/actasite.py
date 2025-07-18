from flask import Flask

app = Flask(__name__)
from flask import request, redirect, url_for, render_template

# ...existing code...

@app.route("/")
def home():
    return render_template("index.html")

# ...existing code...