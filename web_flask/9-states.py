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
def all_states(id=None):
    """ This function use storage for fetching data from
        the storage engine: FileStorage or DBStorage.
        If <id> is not specified display all states, otherwise
        """
    if id is None:
        is_state = storage.all(State).values()
        return render_template('9-states.html', states=is_state)
    else:
        for element in storage.all(State).values():
            if element.id == id:
                return render_template('9-states.html', states_id=element)
        # last return for "not found!" -> evite TypeError
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown(error):
    """ This method after each request you must remove
    the current SQLAlchemy Session.

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
