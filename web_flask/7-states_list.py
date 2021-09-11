#!/usr/bin/python3
""" Flask web application.

"""

from flask import Flask, render_template
from ..models import storage
from ..models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
@app.teardown_appcontext
def states_list():
    """ This function start an application in an address URL
    '/states_list'.
    Return: An Html page with the states.

    """
    storage.close()
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
