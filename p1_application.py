import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def login():
    headline = "My Book Review"
    return render_template("p1_login.html", headline=headline)


@app.route("/books")
def books():
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("p1_index.html", books=isbn)
