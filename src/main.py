import math
from utils.input import get_trucks_data, get_cargos_data
from models.truck import Truck
from models.cargo import Cargo
from utils.geolocation import get_distance, EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS

truck_rows = get_trucks_data()
trucks = [Truck(**row) for row in truck_rows]

cargo_rows = get_cargos_data()
cargos = [Cargo(**row) for row in cargo_rows]

def get_routes(trucks, cargos):
    for cargo in cargos:
        cargo_closest_truck = None
        cargo_closest_truck_distance = EARTH_MAX_DISTANCE_BETWEEN_TWO_POINTS

        for truck in trucks:
            cargo_distance_to_truck = get_distance(cargo.origin_location, truck.location)

            if cargo_distance_to_truck < cargo_closest_truck_distance:
                cargo_closest_truck = truck
                cargo_closest_truck_distance = cargo_distance_to_truck

        yield cargo, cargo_closest_truck, cargo_closest_truck_distance


def print_routes(routes):
    print('Product, Truck Company, Distance')
    [[print(cargo.product + ', ', truck.company + ', ', distance)] for (cargo, truck, distance) in routes]

if __name__ == "__main__":
    routes = get_routes(trucks, cargos)
    print_routes(routes)
