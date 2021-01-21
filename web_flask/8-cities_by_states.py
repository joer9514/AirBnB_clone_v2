#!/usr/bin/python3
"""Flask"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """  Function that display a HTML page """
    # Fetch in a list of all the values available in a given dictionary
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states"""
    res = []
    storage.reload()

    for v in storage.all("State").values():
        res.append([v.id, v.name])

    return render_template("8-cities_by_states.html", states=res)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request you must remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
