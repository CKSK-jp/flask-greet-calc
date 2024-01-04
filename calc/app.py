from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add", methods=["GET"])
def add_me():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    answer = add(a, b)
    return f"{answer}"


@app.route("/sub", methods=["GET"])
def sub_me():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    answer = sub(a, b)
    return f"{answer}"


@app.route("/mult", methods=["GET"])
def mult_me():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    answer = mult(a, b)
    return f"{answer}"


@app.route("/div", methods=["GET"])
def divide_me():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    answer = div(a, b)
    return f"{answer}"


operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>", methods=["GET"])
def math_me(oper):
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    answer = operations[oper](a, b)
    return f"{answer}"
