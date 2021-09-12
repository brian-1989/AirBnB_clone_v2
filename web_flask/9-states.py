#!/usr/bin/python3
""" Flask web application.

"""

from flask import Flask, render_template, escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ This function start an application in an address URL
    '/states'.
    Return: An Html page with the states.

    """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<param>", strict_slashes=False)
def states_id(param):
        for state in storage.all(State).values():
            if state.id == param:
                return render_template("9-states.html", state_id=state)
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown(error):
    """ This method after each request you must remove
    the current SQLAlchemy Session.

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
