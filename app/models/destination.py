#!/usr/bin/python3

"""import modules"""


from AfricExplore.app import db

class Destination(db.Model):
    """create a class that inherits from table in database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=True)
