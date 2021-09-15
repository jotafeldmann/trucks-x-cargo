import os
import requests
from dataclasses import dataclass
from scipy.spatial import KDTree
from geopy.distance import distance
from utils.config import config, PROVIDER_KEY_NAME

EARTH_CIRCUMFERENCE_KM = 40000
EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS = EARTH_CIRCUMFERENCE_KM
PRECISION_DECIMALS_FOR_KM = 0


@dataclass
class GeoPoint:
    latitude: float
    longitude: float

    def __init__(self, latitude=0, longitude=0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __hash__(self):
        return hash((self.latitude, self.longitude))


def _precision(value, decimals=PRECISION_DECIMALS_FOR_KM):
    return round(value, decimals)


def _convert_meters_to_km(value):
    return int(value) / 1000


def _get_distance_by_harvesine(geo_point_1, geo_point_2):
    return _precision(distance((geo_point_1.latitude, geo_point_1.longitude),
                               (geo_point_2.latitude, geo_point_2.longitude)).km)


def _fetch_distance_from_provider(geo_point_1, geo_point_2):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    key = os.environ[PROVIDER_KEY_NAME]
    try:
        request = requests.get('{}?units=metric&origins={},{}&destinations={},{}&key={}' .format(
            url, geo_point_1.latitude, geo_point_1.longitude,
            geo_point_2.latitude, geo_point_2.longitude, key))
        json = request.json()
        return _precision(_convert_meters_to_km(
            json.get('rows')[0].get('elements')[0].get('distance').get('value')))
    except ValueError as err:
        print(err)
        print('Using get_distance')
        return get_distance(geo_point_1, geo_point_2)


class GeoPointList(KDTree):
    pass


get_distance = _fetch_distance_from_provider if config.options.remote else _get_distance_by_harvesine
