from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Show welcome page"""
    return "<p>welcome</p>"


@app.route("/welcome/home")
def open_home():
    """Show home page"""
    return "<p>welcome home</p>"


@app.route("/welcome/back")
def open_back():
    """Show back page"""
    return "<p>welcome back</p>"
