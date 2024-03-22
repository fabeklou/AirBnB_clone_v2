#!/usr/bin/python3

"""This module create and start a Flask web application
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """home: returns the string < Hello HBNB! >,
    when the user request the home/landing page

    Returns:
        str: the "Hello HBNB!" string to be rendered as HTML
            element

    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hbnb: returns the string < HBNB >,
    when the user request the /hbnb page

    Returns:
        str: the "HBNB" string to be rendered as HTML
            element

    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """c_is_fun returns: a string which is the HTML element
    that will be constructed and returned based on the
    user request

    Args:
        text (str): a string representing the variable rule of
        the page requested by the user

    Returns:
        str: C followed by the name of the page requested

    """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is_cool"):
    """python_is_cool: returns a string which is the HTML element
    that will be constructed and returned based on the
    user request

    Args:
        text (str): a string representing the variable rule of
            the page requested by the user and set to "is cool"
            by default

    Returns:
        str: Python followed by the name of the page requested

    """
    return "Python {}".format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(port=5000)
