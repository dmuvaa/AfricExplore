#!/usr/bin/python3

"""Imports and Blueprint Setup"""
import json
from flask import Blueprint, render_template, current_app

bp = Blueprint('destinations', __name__)

"""Helper function to load destinations data"""
def load_destinations():
    with current_app.open_resource('static/destinations_data.json', 'r') as f:
        return json.load(f)

"""Home Page Route"""
@bp.route('/')
def index():
    destinations = load_destinations()
    return render_template('index.html', destinations=destinations)

"""Destinations Page Route"""
@bp.route('/destinations', methods=['GET'])
def list_destinations():
    destinations_data = load_destinations()
    return render_template('destination_list.html', destinations=destinations_data)
