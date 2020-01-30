from dataclasses import dataclass
from utils.geolocation import GeoPoint, GeoList

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

    def __hash__(self):
        return hash((self.company, self.city, self.state, hash(self.location)))
        