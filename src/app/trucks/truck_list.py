from dataclasses import dataclass
from app.trucks.truck import Truck
from utils.geolocation import GeoPoint, GeoPointList

# TODO: update GeoPointList for each list operation

@dataclass
class TruckList(list):
    truck_list: [Truck]
    _truck_locations_list: GeoPointList

    def __init__(self, iterable = []):
        self.truck_list = iterable
        super().__init__(iterable)
    
    def get_closest_truck_to_location(self, location: GeoPoint) -> (float, Truck):
        index = self._truck_locations_list.query(location)
        return self.truck_list[index]

    def append(self, value):
        self.truck_list.append(value)
        self._truck_locations_list = self._generate_geo_points(self.truck_list)
        return super().append(value)
    
    @staticmethod
    def _generate_geo_points(truck_list: [Truck]) -> GeoPointList:
        if (len(truck_list)):
            return GeoPointList([[truck.location.latitude, truck.location.longitude] for truck in truck_list ])
        return GeoPointList([])

    

        