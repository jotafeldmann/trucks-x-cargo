from dataclasses import dataclass
from utils.geolocation import GeoPoint

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
        