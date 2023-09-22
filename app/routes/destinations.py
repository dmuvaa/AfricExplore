#!/usr/bin/python3

"""Imports and Blueprint Setup"""
from flask import request, Blueprint, render_template, current_app, jsonify, flash, redirect, url_for
import requests
import json
from app.api_utils import fetch_booking_data
from app.forms import BookingForm, ContactForm

bp = Blueprint('destinations', __name__)

BOOKING_ENDPOINT_URL = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"
url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"

headers = {
    "X-RapidAPI-Key": "389115d71amsha0f2499a7b9e437p1046f9jsn29ce7c7f65ee",
    "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
}
querystring = {
    "offset": "0",
    "arrival_date": "2023-09-20",
    "departure_date": "2023-09-23",
    "guest_qty": "1",
    "dest_ids": "-2258110",
    "room_qty": "1",
    "search_type": "city",
    "children_qty": "2",
    "children_age": "5,7",
    "search_id": "none",
    "price_filter_currencycode": "USD",
    "order_by": "popularity",
    "languagecode": "en-us",
    "travel_purpose": "leisure"
}

cities = {
    "Nairobi": "-2258072",
    "Nakuru": "-2258197",
    "Naivasha": "-2258110",
    "Mombasa": "-2256513",
    "Cape Town": "-1217214",
    "Cairo": "-290692"
}

def fetch_data_from_api():

    response = {}
    if response is not None:
        response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def load_destinations_from_local():
    with current_app.open_resource('static/destinations_data.json', 'r') as f:
        return json.load(f)

def load_destinations():
    booking_data = fetch_booking_data(BOOKING_ENDPOINT_URL)
    if booking_data and 'listings' in booking_data:
        return booking_data['listings']
    return load_destinations_from_local()

@bp.route('/', methods=['GET', 'POST'])
def index():
    destinations = load_destinations()
    form = BookingForm()
    return render_template('index.html', destinations=destinations, form=form)

@bp.route('/book', methods=['GET', 'POST'])
def book():
    form = BookingForm()
    listings = []

    if form.validate_on_submit():
        city = form.city.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        guests = form.guests.data
        children = form.children.data

        api_endpoint = f"{BOOKING_ENDPOINT_URL}?dest_ids={city}&checkin_date={start_date}&checkout_date={end_date}&adults_number={guests}&children_number={children}"
        response_data = fetch_booking_data(api_endpoint)
        if response_data and 'listings' in response_data:
            listings = response_data['listings']

    return render_template('book.html', form=form, listings=listings)

@bp.route('/destinations', methods=['GET'])
def list_destinations():
    destinations_data = load_destinations()
    return render_template('destination_list.html', destinations=destinations_data)

@bp.route('/get_properties', methods=['GET'])
def get_properties():
    # date = request.form.get()
    form = BookingForm()
    data = fetch_data_from_api()
    result = data["result"]
    return render_template('dest.html', result=result, form=form)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        
        flash('Thanks for contacting us. We will get back to you soon!', 'success')
        return redirect(url_for('destinations.index'))  # or wherever you'd like to redirect to after successful form submission
    return render_template('contact.html', form=form)