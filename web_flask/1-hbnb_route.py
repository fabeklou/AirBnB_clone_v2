#!/usr/bin/python3

"""This module create and start a Flask web application
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """home: returns the string "Hello HBNB!",
    when the user request the landing page

    Returns:
        str: the "Hello HBNB!" string to be rendered as HTML
            element

    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hbnb: returns the string "HBNB",
    when the user request the /hbnb page

    Returns:
        str: the "HBNB" string to be rendered as an HTML
            element

    """
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000)
