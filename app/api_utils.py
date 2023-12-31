import requests
from flask import current_app

def fetch_booking_data(url):
    headers = {
        "X-RapidAPI-Key": current_app.config['RAPIDAPI_KEY'],
        "X-RapidAPI-Host": current_app.config['RAPIDAPI_HOST']
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_listings(city=None, start_date=None, end_date=None, guests=1):
    # Define the endpoint URL and any necessary parameters.
    url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"
    params = {
        "city": city,
        "start_date": start_date,
        "end_date": end_date,
        "guests": guests,
    }
    
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN"
    }
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
