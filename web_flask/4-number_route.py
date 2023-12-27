#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text """
    return (f"C {text.replace('_', ' ')}")


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pycool(text):
    """display “C ” followed by the value of the text """
    return (f"Python {text.replace('_', ' ')}")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return (f"{n} is a number")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)