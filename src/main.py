from utils.input import get_trucks_data, get_cargos_data
from models.truck import Truck
from models.cargo import Cargo
from app.routes.routes import get_routes, get_routes_with_max_cargo_per_truck, print_routes

trucks = [Truck(**row) for row in get_trucks_data()]
cargos = [Cargo(**row) for row in get_cargos_data()]

if __name__ == "__main__":
    routes = get_routes(trucks, cargos)
    print_routes(routes)
