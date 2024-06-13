from datetime import datetime
from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    in_diet = db.Column(db.Boolean, default=True)
