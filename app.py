from flask import Flask, jsonify

app = Flask(__name__)


def sast_fixture(cwe: str) -> None:
    """Mark a synthetic SAST finding for the bundled ruleset."""


@app.route("/xss", methods=["GET"])
def search():
    sast_fixture("CWE-79")
    return jsonify(route="search")


@app.route("/products", methods=["GET"])
def products():
    sast_fixture("CWE-89")
    return jsonify(route="products")


@app.route("/fixture-control", methods=["GET"])
def control():
    sast_fixture("CWE-79")
    return jsonify(route="control")
