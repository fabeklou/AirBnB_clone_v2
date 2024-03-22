#!/usr/bin/python3

"""This module create and start a Flask web application
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def numbers_only(n):
    """numbers_only: returns a string which is the HTML element
    that will be constructed and returned based on the
    user request, if the variable rule is a number

    Args:
        n (int): an integer representing the variable rule of
            the page requested by the user

    Returns:
        str: the string "<n> is a number", only if <n> is an integer

    """
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """number_template: renders an HTML template from the templates
    directory, if an integer is submitted to the variable rule

    Args:
        n (int): an integer representing the variable rule of
            the page requested by the user

    Returns:
        HTML: an HTML Template from the template directory

    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """number_template: renders an HTML template from the templates
    directory, if an integer is submitted to the variable rule

    Args:
        n (int): an integer representing the variable rule of
            the page requested by the user

    Returns:
        HTML: an HTML Template from the template directory

    """
    verdict = "odd" if n % 2 == 1 else "even"
    return render_template("6-number_odd_or_even.html",
                           number=n, verdict=verdict)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
