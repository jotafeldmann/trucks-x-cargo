from sortedcontainers import SortedDict

from app.cargos.cargo import Cargo
from app.routes.designate_cargo_for_truck import designate_cargo_for_truck
from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.shortest_route import ShortestRoute
from utils.geolocation import get_distance
from utils.config import config

MAX_CARGOS_PER_TRUCK = 1


def _get_routes_sorted_map(
        trucks: [Truck],
        cargos: [Cargo],
        max_cargos_per_truck=MAX_CARGOS_PER_TRUCK,
        get_distance=get_distance) -> [ShortestRoute]:

    for cargo in cargos:
        cargo_truck_to_pick = 0
        closest_trucks_sorted = SortedDict()

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
            closest_trucks_sorted[cargo_distance_to_truck] = truck

        distance, closest_truck = designate_cargo_for_truck(
            cargo, closest_trucks_sorted, cargo_truck_to_pick, max_cargos_per_truck)

        yield ShortestRoute(cargo, closest_truck, distance)


def _get_routes_kdtree(
        trucks: TruckList,
        cargos: [Cargo],
        max_cargos_per_truck=MAX_CARGOS_PER_TRUCK,
        get_distance=get_distance) -> [ShortestRoute]:

    def lambda_get_closest_truck(map, index):
        return map[index]

    for cargo in cargos:
        cargo_truck_to_pick = 0
        closest_trucks_sorted = trucks.get_closest_trucks_to_location(
            location=cargo.origin_location)
        distance, closest_truck = designate_cargo_for_truck(
            cargo, closest_trucks_sorted, cargo_truck_to_pick, max_cargos_per_truck,
            lambda_get_closest_truck=lambda_get_closest_truck)

        yield ShortestRoute(cargo, closest_truck, distance)


get_routes = _get_routes_kdtree if config.options.algorithm else _get_routes_sorted_map
