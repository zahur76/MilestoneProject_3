import os
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from flask_pymongo import flask_Pymongo 
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def all_items():
    return "Hello world"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


