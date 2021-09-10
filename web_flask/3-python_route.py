#!/usr/bin/python3
""" Flask web application.

"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ This function start an application in an address URL '/'.
    Return: Hello HBNB!.

    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ This function start an application in an address URL '/hbnb'.
    Return: HBNB.

    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ This function start an application in an address URL '/c/<text>'.
    The 'text' variable, is a variable that is passed from browser together with the URL.
    Return: C and the value of the 'text' variable.

    """
    without_underscore = escape(text).replace('_', ' ')
    return "C {}".format(without_underscore)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyhton_is_cool(text='is cool'):
    """ This function start an application in an address URL '/python' and '/python/<text>'.
    The 'text' variable, is a variable that is passed from browser together with the URL.
    Return: Python and the value of the 'text' variable.

    """
    without_underscore = escape(text).replace('_', ' ')
    return "Python {}".format(without_underscore)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
