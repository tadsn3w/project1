import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    headline = "My hello website"
    return render_template("p1_index.html", headline=headline, new_year=new_year)


@app.route("/bye")
def bye():
    headline = "Sayonara"
    return render_template("p1_index.html", headline=headline)
