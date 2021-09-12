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
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ This function start an application in an address URL
    '/states/<id>'.
    The 'id' variable, is a variable that is passed from browser
    together with the URL.
    Return: An Html page with the states.

    """
    states_with_id = storage.all(State).values()
    for i in states_with_id:
        if escape(id) == i.id:
            my_flag = True
            return render_template(
                "9-states.html",
                states_with_id=states_with_id, id=escape(id), my_flag=my_flag)
    my_flag = False
    return render_template("9-states.html", id=my_flag)


@app.teardown_appcontext
def teardown(error):
    """ This method after each request you must remove
    the current SQLAlchemy Session.

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
