import math
from functools import partial
from sortedcontainers import SortedDict

from app.cargos.cargo import Cargo
from app.routes.designate_cargo_for_truck import designate_cargo_for_truck
from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.shortest_route import ShortestRoute
from utils.geolocation import get_distance, fetch_distance_from_provider, EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS

def _get_routes_with_sorted_order_and_max_cargo_per_truck(trucks: [Truck], cargos: [Cargo], max_cargos_per_truck=1, get_distance=get_distance) -> [ShortestRoute]:

    trucks_designated = {}

    for cargo in cargos:
        closest_trucks_map = SortedDict()
        cargo_truck_to_pick = 0

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_map[cargo_distance_to_truck] = truck
        
        distance, closest_truck = designate_cargo_for_truck(cargo, closest_trucks_map, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)

def _get_routes_with_kdtree_and_max_cargo_per_truck(trucks: TruckList, cargos: [Cargo], max_cargos_per_truck=1, get_distance=get_distance) -> [ShortestRoute]:

    for cargo in cargos:
        closest_trucks_map = SortedDict()
        cargo_truck_to_pick = 0

        closest_truck = trucks.get_closest_truck_to_location(location=cargo.origin_location)
        distance = get_distance(cargo.origin_location, closest_truck.location)
        closest_trucks_map[distance] = closest_truck
        
        # distance, closest_truck = designate_cargo_for_truck(cargo, closest_trucks_map, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)

_get_routes_algorithm = _get_routes_with_kdtree_and_max_cargo_per_truck
get_routes_local = _get_routes_algorithm
get_routes_remote = partial(_get_routes_algorithm, get_distance=fetch_distance_from_provider)