from app import db

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicleID = db.Column(db.Integer,primary_key=True)
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    color = db.Column(db.String(80))

class Driver(db.Model):
    __tablename__ = 'driver'
    ID = db.Column(db.Integer, primary_key=True)
    birth = db.Column(db.String(80))
    name = db.Column(db.String(80))
    vehicle_Used = db.Column(db.Integer, db.ForeignKey("vehicle.vehicleID"))
    country = db.Column(db.String(80))

class Country(db.Model):
    __tablename__ = 'country'
    country_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80))

class UpcomingEvents(db.Model):
    __tablename__ = 'upcoming_events'
    event_ID = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.String(80))
    employeeID = db.Column(db.Integer, db.ForeignKey("employee.ID"))
    event_Name = db.Column(db.String(80))
    Track_location_ID = db.Column(db.Integer, db.ForeignKey("location.track_location_id"))

class Race(db.Model):
    __tablename__ = 'race'
    race_id = db.Column(db.Integer, primary_key=True)
    race_date = db.Column(db.String(80))
    event_id = db.Column(db.Integer, db.ForeignKey("upcoming_events.event_ID"))
    driverID = db.Column(db.Integer, db.ForeignKey("driver.ID"))
    vehicle_ID = db.Column(db.Integer, db.ForeignKey("vehicle.vehicleID"))
    track_location_ID = db.Column(db.Integer, db.ForeignKey("location.track_location_id"))

class Employee(db.Model):
    __tablename__ = 'employee'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    instructor = db.Column(db.Boolean)
    SSN = db.Column(db.Integer)

class Location(db.Model):
    __tablename__ = 'location'
    track_location_id = db.Column(db.Integer, primary_key = True)
    Track = db.Column(db.String(80))
    Location = db.Column(db.String(80))
	
db.create_all()

