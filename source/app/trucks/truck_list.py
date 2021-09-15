from dataclasses import dataclass
from app.trucks.truck import Truck
from utils.geolocation import GeoPoint, GeoPointList, get_distance

# TODO: update GeoPointList for each list operation


@dataclass
class TruckList(list):
    truck_list: [Truck]
    geo_points_list: []

    def __init__(self, geo=GeoPointList, get_distance=get_distance):
        self.truck_list = []
        self.geo_points_list = []
        self._geo = geo
        super().__init__()

    def get_closest_trucks_to_location(self, location: GeoPoint) -> (float, Truck):
        _, indexes = self._geo(self.geo_points_list).query(
            [location.latitude, location.longitude], len(self.truck_list))
        return [(get_distance(location, self.truck_list[index].location),
                 self.truck_list[index]) for index in indexes]

    def append(self, truck: Truck):
        self.truck_list.append(truck)
        self.geo_points_list.append([truck.location.latitude, truck.location.longitude])
        return super().append(truck)
