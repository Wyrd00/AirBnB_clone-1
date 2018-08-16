#!/usr/bin/python3
'''
    Starts a Flask web application
'''
from models import storage
from models.state import State
from os import getenv
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """
        display HTML with States
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        states = storage.all("State")
    else:
        states = storage.all(State)
    states = states.values()

    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states")
def cities_by_states():
    """
        display HTML with cities in States
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        states = storage.all("State")
        states = list(states.values())
    else:
        states = storage.all(State)
        states = states.values()

    return render_template("8-cities_by_states.html", states=states)


@app.route("/states")
def states():
    """
        display HTML with states
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        states = storage.all("State")
    else:
        states = storage.all(State)
    state_a = states.values()

    return render_template("9-states.html", state_a=state_a)


@app.route("/states/<id>")
def states_id(id):
    """
        display HTML with states id
    """
    single_state = None

    if getenv("HBNB_TYPE_STORAGE") == "db":
        state_b = storage.all("State").values()
    else:
        state_b = storage.all(State).values()

    for state in state_b:
        if state.id == id:
            single_state = state
    state_b = single_state

    return render_template("9-states.html", state_b=state_b)


@app.teardown_appcontext
def tear_down(exception):
    """
        tear down
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
