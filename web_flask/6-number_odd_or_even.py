#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes=False

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

@app.route("/python/<text>", defaults={"text": "is cool"})
def python_route(text):
    """
        display “Python ”, followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return "Python is {}".format(text)

@app.route("/number/<int:n>")
def n_route(n):
    """
        display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>")
def template_n_route(n):
    """
         display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>")
def even_odd(n):
    """

    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
