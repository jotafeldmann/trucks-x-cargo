from sortedcontainers import SortedDict

def designate_cargo_for_truck(cargo, closest_trucks_map = SortedDict(), cargo_truck_to_pick = 0, max_cargos_per_truck = 1, trucks_designated_map = {}):
    distance, closest_truck = closest_trucks_map.peekitem(cargo_truck_to_pick)

    if trucks_designated_map.get(closest_truck):

        if len(trucks_designated_map[closest_truck].get('cargos').keys()) == max_cargos_per_truck:
            # TODO: work with imutable maps (new maps for each iteration)
            return designate_cargo_for_truck(cargo, closest_trucks_map, cargo_truck_to_pick + 1, max_cargos_per_truck, trucks_designated_map)
        
        trucks_designated_map[closest_truck].get('cargos').setdefault(cargo, distance)
    else:
        trucks_designated_map[closest_truck] = { 'cargos': { cargo: distance } }

    return distance, closest_truck