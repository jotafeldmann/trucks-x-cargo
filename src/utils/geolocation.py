from dataclasses import dataclass
from geopy.distance import distance

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
