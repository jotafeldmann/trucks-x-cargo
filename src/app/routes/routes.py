import math
from sortedcontainers import SortedDict
from dataclasses import dataclass

from models.truck import Truck
from models.cargo import Cargo
from utils.geolocation import get_distance, EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS

@dataclass
class ShortestRoute:
    cargo: Cargo
    closest_truck: Truck
    distance: float

def print_routes(routes: [ShortestRoute]) -> None:
    print('Product, Truck Company, Distance')
    [[print(route.cargo.product + ', ', route.closest_truck.company + ', ', route.distance)] for route in routes]

def _get_routes_simple(trucks: [Truck], cargos: [Cargo]) -> [ShortestRoute]:
    for cargo in cargos:
        closest_truck = None
        distance = EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)

            if cargo_distance_to_truck < distance:
                closest_truck = truck
                distance = cargo_distance_to_truck

        yield ShortestRoute(cargo, closest_truck, distance)

def _get_routes_simple_with_sorted_list(trucks: [Truck], cargos: [Cargo]) -> [ShortestRoute]:

    trucks_designated = {}

    for cargo in cargos:
        closest_trucks_list = SortedDict()

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = closest_trucks_list.peekitem(0)
        yield ShortestRoute(cargo, closest_truck, distance)

def _get_routes_with_sorted_list_and_max_cargo_per_truck(trucks: [Truck], cargos: [Cargo], max_cargos=1) -> [ShortestRoute]:

    trucks_designated = {}

    for cargo in cargos:
        closest_trucks_list = SortedDict()

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = closest_trucks_list.peekitem(0)
        yield ShortestRoute(cargo, closest_truck, distance)

get_routes = _get_routes_with_sorted_list_and_max_cargo_per_truck