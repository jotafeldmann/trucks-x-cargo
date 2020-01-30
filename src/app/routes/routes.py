import math
from functools import partial
from sortedcontainers import SortedDict

from app.models.cargo import Cargo
from app.models.truck import Truck
from app.routes.shortest_route import ShortestRoute
from utils.geolocation import get_distance, fetch_distance_from_provider, EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS, GeoList

def _designate_cargo_for_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick = 0, max_cargos_per_truck = 1):
    distance, closest_truck = closest_trucks_list.peekitem(cargo_truck_to_pick)

    if trucks_designated.get(closest_truck):

        if len(trucks_designated[closest_truck].get('cargos').keys()) == max_cargos_per_truck:
            return _designate_cargo_for_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick + 1)
        
        trucks_designated[closest_truck].get('cargos').setdefault(cargo, distance)
    else:
        trucks_designated[closest_truck] = { 'cargos': { cargo: distance } }

    return distance, closest_truck

def _get_routes_with_sorted_order_and_max_cargo_per_truck(trucks: [Truck], cargos: [Cargo], max_cargos_per_truck=1, get_distance=get_distance) -> [ShortestRoute]:

    trucks_designated = {}

    for cargo in cargos:
        closest_trucks_list = SortedDict()
        cargo_truck_to_pick = 0

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = _designate_cargo_for_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)

def _get_routes_with_kdtree_and_max_cargo_per_truck(trucks: [Truck], cargos: [Cargo], max_cargos_per_truck=1, get_distance=get_distance) -> [ShortestRoute]:

    trucks_designated = {}
    g = GeoList([[truck.location.latitude, truck.location.longitude] for truck in trucks  ])
    latitude = cargos[0].origin_location.latitude
    longitude = cargos[0].origin_location.longitude
    print(trucks[g.query([ latitude, longitude ])[1]])
    exit()

    for cargo in cargos:
        closest_trucks_list = SortedDict()
        cargo_truck_to_pick = 0

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_list[cargo_distance_to_truck] = truck
        
        distance, closest_truck = _designate_cargo_for_truck_from_list(cargo, trucks_designated, closest_trucks_list, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)

_get_routes_algorithm = _get_routes_with_kdtree_and_max_cargo_per_truck
get_routes_local = _get_routes_algorithm
get_routes_remote = partial(_get_routes_algorithm, get_distance=fetch_distance_from_provider)