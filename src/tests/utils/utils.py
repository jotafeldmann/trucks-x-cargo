from sortedcontainers import SortedDict

from utils.input import get_trucks_data, get_cargos_data
from utils.geolocation import _get_distance_by_harvesine


def get_trucks_fixture_generator():
    return get_trucks_data()


def get_cargos_fixture_generator():
    return get_cargos_data()


def get_trucks_fixture():
    trucks_fixture = [row for row in get_trucks_fixture_generator()]
    return trucks_fixture


def get_cargos_fixture():
    cargos_fixture = [row for row in get_cargos_fixture_generator()]
    return cargos_fixture


def get_closest_trucks_for_cargo(trucks_list, cargo, get_distance=_get_distance_by_harvesine):
    closest_trucks_sorted = SortedDict()

    for truck in trucks_list:
        cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)
        closest_trucks_sorted[cargo_distance_to_truck] = truck

    return closest_trucks_sorted
