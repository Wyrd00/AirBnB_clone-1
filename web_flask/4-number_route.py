#!/usr/bin/python3
'''
    Starts a Flask web application
'''
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """
        display Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
        display HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """
        display “C ” followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return "C is {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_route(text="is_cool"):
    """
        display “Python ”, followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def n_route(n):
    """
        display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
