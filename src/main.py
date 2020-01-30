#!/usr/bin/python3.8

import argparse
from app.models.cargo import Cargo
from app.models.truck import Truck
from app.routes.routes import get_routes_local, get_routes_remote
from utils.geolocation import PROVIDER_KEY_NAME
from utils.input import get_trucks_data, get_cargos_data

def parse_arguments():
    parser = argparse.ArgumentParser("make run")
    parser.add_argument("--remote", required=False, help="Use Google Routes provider to calculate distances, please set env var {}".format(PROVIDER_KEY_NAME))
    return parser.parse_args()

def load_data():
    trucks = [Truck(**row) for row in get_trucks_data()]
    cargos = [Cargo(**row) for row in get_cargos_data()]
    return trucks, cargos

def print_routes(routes):
    print('Cargo, Truck Company, Distance (km)')
    [[print(route.cargo.product + ', ', route.closest_truck.company + ', ', route.distance)] for route in routes]

def main():
    args = parse_arguments()
    get_routes = get_routes_remote if args.remote else get_routes_local
    trucks, cargos = load_data()
    routes = get_routes(trucks, cargos)
    print_routes(routes)

if __name__ == "__main__":
    main()
