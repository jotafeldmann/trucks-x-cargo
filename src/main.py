#!/usr/bin/python3.8

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.routes import get_routes
from utils.config import config
from utils.input import get_trucks_data, get_cargos_data



def load_data():
    trucks = TruckList()
    [trucks.append(Truck(**row)) for row in get_trucks_data()]
    cargos = [Cargo(**row) for row in get_cargos_data()]
    return trucks, cargos

def print_routes(routes):
    print('Cargo, Truck Company, Distance (km)')
    [[print(route.cargo.product + ', ', route.closest_truck.company + ', ', route.distance)] for route in routes]

def main():
    config.start()
    trucks, cargos = load_data()
    routes = get_routes(trucks, cargos)
    print_routes(routes)

if __name__ == "__main__":
    main()
