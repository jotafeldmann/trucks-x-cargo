from utils.input import get_trucks_data, get_cargos_data
from models.truck import Truck

rows = get_trucks_data()

truckList = [[Truck(**row)] for row in rows]

print(truckList[0])