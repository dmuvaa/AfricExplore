import requests

url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"

querystring = {"offset":"0","arrival_date":"2023-09-15","departure_date":"2023-09-18","guest_qty":"5","dest_ids":"-2258072","room_qty":"5","search_type":"city","children_qty":"2","search_id":"none","price_filter_currencycode":"USD","order_by":"popularity","languagecode":"en-us","travel_purpose":"leisure","categories_filter":"5"}

headers = {
	"X-RapidAPI-Key": "389115d71amsha0f2499a7b9e437p1046f9jsn29ce7c7f65ee",
	"X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())