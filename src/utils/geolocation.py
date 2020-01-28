from dataclasses import dataclass

@dataclass
class GeoPoint:
    latitude: float
    longitude: float

    def __init__(self, latitude=0, longitude=0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)