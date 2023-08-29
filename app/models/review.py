#!/usr/bin/python3

from AfricExplore.app import db

class Review(db.Model):
    """creates a class"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
