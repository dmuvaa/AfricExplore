#!/usr/bin/python3

"""Imports and Blueprint Setup"""
import json
from flask import Blueprint, render_template, current_app
from app.api_utils import fetch_airbnb_data
from app.api_utils import fetch_airbnb_languages
from app.forms import BookingForm



bp = Blueprint('destinations', __name__)

"""Helper function to load destinations data from local JSON"""
def load_destinations_from_local():
    with current_app.open_resource('static/destinations_data.json', 'r') as f:
        return json.load(f)

"""Helper function to load destinations data from Airbnb or fallback to local JSON"""
def load_destinations():
    AIRBNB_ENDPOINT_URL = "https://api.airbnb.com/v2/listings"  # Hypothetical URL

    # Try fetching from Airbnb API first
    airbnb_data = fetch_airbnb_data(AIRBNB_ENDPOINT_URL)

    if airbnb_data and 'listings' in airbnb_data:
        return airbnb_data['listings']
    
    # If the API call fails, fall back to the local data
    return load_destinations_from_local()

"""Home Page Route"""
@bp.route('/', methods = ['GET', 'POST'])
def index():
    destinations = load_destinations()
    form = BookingForm()
    return render_template('index.html', destinations=destinations, form=form)

"""Destinations Page Route"""
@bp.route('/destinations', methods=['GET'])
def list_destinations():
    destinations_data = load_destinations()
    return render_template('destination_list.html', destinations=destinations_data)

@bp.route('/languages')
def get_languages():
    languages_data = fetch_airbnb_languages()
    if languages_data:
        return render_template('languages.html', languages=languages_data)
    else:
        return "Error fetching data", 500