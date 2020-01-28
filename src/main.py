from utils.input import get_trucks_data, get_cargos_data
from app.models.truck import Truck
from app.models.cargo import Cargo
from app.routes.routes import get_routes

def load_data():
    trucks = [Truck(**row) for row in get_trucks_data()]
    cargos = [Cargo(**row) for row in get_cargos_data()]
    return trucks, cargos

def print_routes(routes):
    print('Cargo, Truck Company, Distance')
    [[print(route.cargo.product + ', ', route.closest_truck.company + ', ', route.distance)] for route in routes]

def main():
    trucks, cargos = load_data()
    routes = get_routes(trucks, cargos)
    print_routes(routes)

if __name__ == "__main__":
    main()
