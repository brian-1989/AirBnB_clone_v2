#!/usr/bin/python3
""" Flask web application.

"""

from flask import Flask, render_template, escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ This function start an application in an address URL
    '/states/<id>'.
    The 'id' variable, is a variable that is passed from browser
    together with the URL.
    Return: An Html page with the states.

    """
    if id:
        states_id = storage.all(State).values()
        cities_id = storage.all(City).values()
        for i in cities_id:
            if escape(id) == i.state_id:
                my_flag = True
                return render_template(
                    "9-states.html",
                    states_id=states_id,
                    cities_id=cities_id, id=escape(id), my_flag=my_flag)
        my_flag = False
        return render_template("9-states.html", id=my_flag)
    else:
        states = storage.all(State).values()
        return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(error):
    """ This method after each request you must remove
    the current SQLAlchemy Session.

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
