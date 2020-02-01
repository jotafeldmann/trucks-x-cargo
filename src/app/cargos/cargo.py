from dataclasses import dataclass
from utils.geolocation import GeoPoint, get_distance


@dataclass
class Cargo:
    product: str
    origin_city: str
    origin_state: str
    origin_location: GeoPoint
    destination_city: str
    destination_state: str
    destination_location: GeoPoint

    def __init__(
        self,
        product,
        origin_city,
        origin_state,
        origin_latitude,
        origin_longitude,
        destination_city,
        destination_state,
        destination_latitude,
        destination_longitude
    ):
        self.product = product
        self.origin_city = origin_city
        self.origin_state = origin_state
        self.origin_location = GeoPoint(origin_latitude, origin_longitude)
        self.destination_city = destination_city
        self.destination_state = destination_state
        self.destination_location = GeoPoint(destination_latitude, destination_longitude)

    def __hash__(self):
        return hash((self.destination_location, self.origin_location))

    def get_route_total_length(self):
        return get_distance(self.origin_location, self.destination_location)
