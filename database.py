from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True, unique=True)
    password = db.Column(db.String(100), nullable=True, unique=True)

class TrackerInput(db.Model):   
    # __tablename__ = 'tracker_input' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    Average_Income = db.Column(db.Float,nullable=False)
    Ad_Spend_per_Car = db.Column(db.Float,nullable=False)
    Sales_to_Income_Ratio = db.Column(db.Float,nullable=False)
    result =db.Column(db.Integer,nullable=False)
