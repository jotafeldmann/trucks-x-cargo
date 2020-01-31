from dataclasses import dataclass
from app.cargos.cargo import Cargo
from app.trucks.truck import Truck

@dataclass
class ShortestRoute:
    cargo: Cargo
    closest_truck: Truck
    distance: float