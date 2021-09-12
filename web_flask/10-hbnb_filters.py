#!/usr/bin/python3
""" Flask web application.

"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ This function start an application in an address URL
    '/hbnb_filters'.
    Return: An Html page with the states, cities and amenity.

    """
    states = storage.all(State).values()
    amenity = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html", states=states, amenity=amenity)


@app.teardown_appcontext
def teardown(error):
    """ This method after each request you must remove
    the current SQLAlchemy Session.

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
