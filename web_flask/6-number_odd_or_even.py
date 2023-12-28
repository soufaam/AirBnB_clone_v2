#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask, redirect, url_for, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
