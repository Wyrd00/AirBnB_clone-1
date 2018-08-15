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
    city_in_state = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        states = storage.all("State")
        states = list(states.values())
        for city in states:
            city_in_state.append(city.name)
    else:
        states = storage.all(State)
        states = states.values()
        city_in_state = states.cities()

    return render_template("8-cities_by_states.html", states=states,
                           city_in_state=city)


@app.teardown_appcontext
def tear_down(exception):
    """
        tear down
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
