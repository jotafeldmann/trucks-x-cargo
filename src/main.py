from utils.input import get_trucks_data, get_cargos_data
from models.truck import Truck
from models.cargo import Cargo
from app.routes.routes import get_routes, print_routes

def load_data():
    trucks = [Truck(**row) for row in get_trucks_data()]
    cargos = [Cargo(**row) for row in get_cargos_data()]
    return trucks, cargos

def main():
    trucks, cargos = load_data()
    routes = get_routes(trucks, cargos)
    print_routes(routes)

if __name__ == "__main__":
    main()
