import os
import random
import sqlite3
import string

from flask import Flask, jsonify, redirect, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def hashed():
    let = string.ascii_uppercase + string.ascii_lowercase
    dig = string.digits
    hash = random.choices(let, k=1) + random.choices(let + dig, k=5)
    return "".join(hash)


@app.route("/_short", methods=["POST"])
def shorten():
    conn = get_db_connection()
    if "url" in request.json:
        url = request.json["url"]
    else:
        return jsonify({"error": "Please enter a URL"}), 400

    if "shorten" in request.json:
        shorten = request.json["shorten"]
        if conn.execute(
            "SELECT url FROM urls WHERE shorten = (?)",
            (shorten,),
        ).fetchone():
            return jsonify({"error": "This address is already taken!"}), 400
    else:
        shorten = hashed()
        while conn.execute(
            "SELECT url FROM urls WHERE shorten = (?)",
            (shorten,),
        ).fetchone():
            shorten = hashed()

    conn.execute(
        "INSERT INTO urls (shorten, url) VALUES (?, ?)", (shorten, url)
    )
    conn.commit()
    conn.close()
    return (
        jsonify({"shorten": request.host_url + shorten}),
        201,
    )


@app.route("/<shorten>")
def url_redirect(shorten):
    conn = get_db_connection()
    request = conn.execute(
        "SELECT url, count FROM urls WHERE shorten = (?)",
        (shorten,),
    ).fetchone()
    if request:
        conn.execute(
            "UPDATE urls SET count = (?) WHERE shorten = (?)",
            (request["count"] + 1, shorten),
        )
        conn.commit()
        conn.close()
        return redirect(request["url"])
    return jsonify({"error": "Invalid URL"}), 404

def create_app(foo):
    app = Flask(__name__)
    app.config['foo'] = foo
    print('Passed item: ', app.config['foo'])
    return app


if __name__ == "__main__":
    host = os.environ.get("HOST", "localhost")
    app.run(host=host, port=8000)
