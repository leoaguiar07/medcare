# views.py
from django.shortcuts import render
import os
import requests

def get_coordinates(address):
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    print(url)
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None, None

def google_maps_link(address):
    
        latitude, longitude = get_coordinates(address)
        if latitude is not None and longitude is not None:
            maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
            return ('google_maps_link.html', {'maps_link': maps_link})
        else:
            error_message = "Não foi possível encontrar as coordenadas para o endereço fornecido."
            return ('google_maps_link.html', {'error_message': error_message})
        
    # return ('google_maps_link.html')
