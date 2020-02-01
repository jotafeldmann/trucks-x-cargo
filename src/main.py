#!/usr/bin/python3.8

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.routes import get_routes
from time import time
from utils.config import config
from utils.input import get_trucks_data, get_cargos_data

DEFAULT_OUTPUT = print


def output_columns_title(output):
    return output("Cargo, Truck Company, Distance (km)")


def load_data(get_trucks_data=get_trucks_data, get_cargos_data=get_cargos_data):
    trucks = TruckList()
    [trucks.append(Truck(**row)) for row in get_trucks_data()]
    cargos = [Cargo(**row) for row in get_cargos_data()]
    return trucks, cargos


def output_routes(routes, output):
    return [[output(route.cargo.product + ', ', route.closest_truck.company + ', ', route.distance)]
            for route in routes]


def main(
        load_data=load_data,
        get_routes=get_routes,
        output_routes=output_routes,
        output_columns_title=output_columns_title,
        output=DEFAULT_OUTPUT):
    trucks, cargos = load_data()
    routes = get_routes(trucks, cargos)
    output_columns_title(output=output)
    return output_routes(routes, output=output)


if __name__ == "__main__":
    start = time()
    config.start()
    main()
    end = time()
    if config.options.debug:
        print("Time to complete: {} seconds".format(round(end - start, 4)))
