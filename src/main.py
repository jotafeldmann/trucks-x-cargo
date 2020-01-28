from utils.input import get_trucks_data, get_cargos_data
from models.truck import Truck
from models.cargo import Cargo

truck_rows = get_trucks_data()
trucks = [[Truck(**row)] for row in truck_rows]

cargo_rows = get_cargos_data()
cargos = [[Cargo(**row)] for row in cargo_rows]

print(cargos[0])

