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

    for cargo in cargos:
        closest_trucks_list = SortedDict()

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = closest_trucks_list.peekitem(0)
        yield ShortestRoute(cargo, closest_truck, distance)

def designate_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick = 0, max_cargos_per_truck = 1):
    distance, closest_truck = closest_trucks_list.peekitem(cargo_truck_to_pick)

    if trucks_designated.get(closest_truck):

        if len(trucks_designated[closest_truck].get('cargos').keys()) == max_cargos_per_truck:
            return designate_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick + 1)
        
        trucks_designated[closest_truck].get('cargos').setdefault(cargo, distance)
    else:
        trucks_designated.setdefault(closest_truck, { 'cargos' : {
            cargo: distance
        } })

    return distance, closest_truck

def _get_routes_with_sorted_list_and_max_cargo_per_truck(trucks: [Truck], cargos: [Cargo], max_cargos_per_truck=1) -> [ShortestRoute]:

    trucks_designated = {}

    for cargo in cargos:
        closest_trucks_list = SortedDict()
        cargo_truck_to_pick = 0

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = designate_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)

    
    print('\nCounting companies and cargos')
    for t in trucks_designated:
        print(t.company, len(trucks_designated[t].get('cargos').keys()))
    
    

get_routes = _get_routes_with_sorted_list_and_max_cargo_per_truck