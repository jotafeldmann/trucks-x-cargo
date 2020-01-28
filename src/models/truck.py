from dataclasses import dataclass
from utils.geolocation import GeoPoint

@dataclass
class Truck:
    company: str
    city: str
    state: str
    location: GeoPoint

    def __init__(self, company, city, state, latitude, longitude):
        self.company = company
        self.city = city
        self.state = state
        self.location = GeoPoint(latitude, longitude)
        