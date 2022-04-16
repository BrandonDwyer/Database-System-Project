from crypt import methods
import flask
from flask_sqlalchemy import SQLAlchemy 

DATABASE_URL='postgresql://ngbexfifdiceji:5179e9ccb52690e4437b859807e2153eaf4883811a9d1ce9c886af128eafc583@ec2-52-203-118-49.compute-1.amazonaws.com:5432/d7kmt662gm8rel'

app = flask.Flask(__name__)
# Point SQLAlchemy to your Heroku database
db_url = DATABASE_URL

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = b"I am a secret key!"  # don't defraud my app ok?



db = SQLAlchemy(app)

from models import Driver, Vehicle, Employee, UpcomingEvents

@app.route("/")
def home():
        return flask.render_template("home.html")

@app.route("/drivers")
def driver():
        return flask.render_template("drivers.html")

@app.route("/drivers", methods=['GET','POST'])
def driver_post():
    Id = flask.request.form.get("ID")
    name = flask.request.form.get("name")
    birth = flask.request.form.get("birth")
    vehicle_Used = flask.request.form.get("vehicle_Used")
    country = flask.request.form.get("country")
    record = Driver(ID=Id, name=name, birth=birth, 
    vehicle_Used=vehicle_Used, country=country)
    db.session.add(record)
    db.session.commit()
    

    return flask.render_template("drivers.html")


@app.route("/vehicles")
def vehicle():
        return flask.render_template("vehicles.html")

@app.route("/vehicles", methods=['GET','POST'])
def vehicle_post():
    Id = flask.request.form.get("vehicleID")
    make = flask.request.form.get("car_make")
    model = flask.request.form.get("car_model")
    year = flask.request.form.get("car_year")
    color = flask.request.form.get("car_color")
    record2 = Vehicle(vehicleID=Id, make=make, model=model, 
    year=year, color=color)
    db.session.add(record2)
    db.session.commit()
    
    return flask.render_template("vehicles.html")


@app.route("/upcomingEvents", methods=["GET", "POST"])
def upcomingEvents():
        return flask.render_template("upcomingEvents.html", query=UpcomingEvents.query.order_by(UpcomingEvents.event_date.asc())
)

@app.route("/lessons", methods=["GET", "POST"])
def lessons():
        return flask.render_template("lessons.html", query=Employee.query.filter_by(instructor=True).all())