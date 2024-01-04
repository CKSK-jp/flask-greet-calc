from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add", methods=["GET"])
def add_me():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    answer = add(int(a), int(b))
    return f"{answer}"


@app.route("/sub", methods=["GET"])
def sub_me():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    answer = sub(int(a), int(b))
    return f"{answer}"


@app.route("/mult", methods=["GET"])
def mult_me():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    answer = mult(int(a), int(b))
    return f"{answer}"


@app.route("/div", methods=["GET"])
def divide_me():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    answer = div(int(a), int(b))
    return f"{answer}"


@app.route("/math/<oper>", methods=["GET"])
def check_all(oper):
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    if oper == "add":
        answer = add(int(a), int(b))
    elif oper == "sub":
        answer = sub(int(a), int(b))
    elif oper == "mult":
        answer = mult(int(a), int(b))
    elif oper == "div":
        answer = div(int(a), int(b))
    else:
        return "Invalid operation"
    return f"{answer}"
