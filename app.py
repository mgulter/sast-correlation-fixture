import sqlite3
from contextlib import closing

import jinja2
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/xss", methods=["GET"])
def search():
    template = jinja2.Template("<p>Search fixture</p>")
    return template.render()


@app.route("/products", methods=["GET"])
def products():
    product_id = 1
    with closing(sqlite3.connect(":memory:")) as connection:
        row = connection.execute("SELECT " + str(product_id) + " AS product_id").fetchone()
    return jsonify(product_id=row[0])


@app.route("/fixture-control", methods=["GET"])
def control():
    template = jinja2.Template("<p>Unpaired fixture</p>")
    return template.render()
