from sortedcontainers import SortedDict
from app.trucks.truck import Truck


def _get_closest_truck_from_dict(closest_trucks_sorted: SortedDict, cargo_truck_to_pick):
    return closest_trucks_sorted.peekitem(cargo_truck_to_pick)


def _is_truck_already_designated(trucks_designated_map, closest_truck):
    return trucks_designated_map.get(closest_truck)


def _is_truck_already_designated_for_max_cargos(
        trucks_designated_map, closest_truck, max_cargos_per_truck):
    if not _is_truck_already_designated(trucks_designated_map, closest_truck):
        return False
    return len(trucks_designated_map[closest_truck].get('cargos').keys()) == max_cargos_per_truck


def _set_cargo_for_truck(trucks_designated_map, closest_truck, cargo, distance):
    # TODO: find just one way to set
    # For now we are just EAFP (https://docs.python.org/3/glossary.html)
    try:
        trucks_designated_map[closest_truck].get('cargos').setdefault(cargo, distance)
    except KeyError:
        trucks_designated_map[closest_truck] = {'cargos': {cargo: distance}}


def designate_cargo_for_truck(
        cargo,
        closest_trucks_sorted=SortedDict(),
        cargo_truck_to_pick=0,
        max_cargos_per_truck=1,
        trucks_designated_map={},
        lambda_get_closest_truck=_get_closest_truck_from_dict) -> (float, Truck):
    distance, closest_truck = lambda_get_closest_truck(closest_trucks_sorted, cargo_truck_to_pick)

    if _is_truck_already_designated_for_max_cargos(
            trucks_designated_map, closest_truck, max_cargos_per_truck):
        # TODO: work with imutable maps (new maps for each iteration)
        return designate_cargo_for_truck(
            cargo,
            closest_trucks_sorted,
            cargo_truck_to_pick + 1,
            max_cargos_per_truck,
            trucks_designated_map,
            lambda_get_closest_truck)

    _set_cargo_for_truck(trucks_designated_map, closest_truck, cargo, distance)

    return (distance, closest_truck)
