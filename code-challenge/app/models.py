from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime) 
    updated_at = db.Column(db.DateTime)  

    # Define the one-to-many relationship with HeroPowers
    powers = db.relationship('Hero_Power', back_populates='hero', lazy=True)


    #Define the one-to-many relationship with HeroPowers
    powers = db.relationship('Hero_Power', back_populates='hero', lazy=True)

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

     # Define the one-to-many relationship with HeroPowers
    heroes = db.relationship('Hero_Power', back_populates='power', lazy=True)


class Hero_Power(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    # Define the many-to-one relationship with Hero
    hero = db.relationship('Hero', back_populates='powers',lazy=True)

     # Define the many-to-one relationship with Power
    power = db.relationship('Power', back_populates='heroes',lazy=True)

 