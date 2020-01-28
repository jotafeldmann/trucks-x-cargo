from dataclasses import dataclass
from geopy.distance import distance
import requests
import os

EARTH_CIRCUMFERENCE_KM = 40000
EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS = EARTH_CIRCUMFERENCE_KM

@dataclass
class GeoPoint:
    latitude: float
    longitude: float

    def __init__(self, latitude=0, longitude=0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
    
    def __hash__(self):
        return hash((self.latitude, self.longitude))

def get_distance(geo_point_1, geo_point_2):
    return distance((geo_point_1.latitude, geo_point_1.longitude), (geo_point_2.latitude, geo_point_2.longitude)).km

def fetch_distance_from_provider(geo_point_1, geo_point_2):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    key = os.environ['GOOGLE_API_KEY']
    try:
        request = requests.get('{}?units=metric&origins={},{}&destinations={},{}&key={}'
            .format(url, geo_point_1.latitude, geo_point_1.longitude, geo_point_2.latitude, geo_point_2.longitude, key))
        json = request.json()
        return json.get('rows')[0].get('elements')[0].get('distance').get('value')
    except ValueError as err:
        print(err)
        print('Using get_distance')
        return get_distance(geo_point_1, geo_point_2)

