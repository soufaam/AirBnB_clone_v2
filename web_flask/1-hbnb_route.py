#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask, request


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
