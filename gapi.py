import requests
from bs4 import BeautifulSoup
import json

My_location = []

def coord_banks(lat, lng):
    global My_location
    My_location = [lat, lng]
    Banks = []
    URLt = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=2000&type=bank&language=ru&key=AIzaSyA4TW4MaPG_YUkCrUWJypsFIgO1OGre6m8'
    URL = URLt.format(lat, lng)
    inf_banks_location = json.loads(requests.get(URL).content)['results']
    for bank in inf_banks_location:
        Banks.append([bank['name'], bank['geometry']['location']['lat'], bank['geometry']['location']['lng']])
    return Banks

def sortByDist(Bank):
    return ((Bank[1] - float(My_location[0])) ** 2 + (Bank[2] - float(My_location[1])) ** 2)
    

def nearest_10(lat, lng):
    Banks = coord_banks(lat, lng)
    Banks.sort(key=sortByDist)
    return Banks[:10]

    
