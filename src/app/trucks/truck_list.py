from dataclasses import dataclass
from app.trucks.truck import Truck
from utils.geolocation import GeoPoint, GeoPointList

@dataclass
class TruckList(list):
    truck_list: [Truck]
    _truck_locations_list: GeoPointList

    def __init__(self, iterable):
        self.truck_list = iterable
        self._truck_locations_list = self._generate_geo_points(self.truck_list)
        super().__init__(iterable)

    @staticmethod
    def _generate_geo_points(truck_list: [Truck]) -> GeoPointList:
        return GeoPointList([[truck.location.latitude, truck.location.longitude] for truck in truck_list ])
    
    def get_closest_truck_to_location(self, location: GeoPoint) -> (distance: float, truck: Truck):
        latitude = location.latitude
        longitude = location.longitude
        distance, index = self._truck_locations_list.query([ latitude, longitude ])
        return distance, self.truck_list[index]

    # TODO: update GeoPointList for each list operation

        