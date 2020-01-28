from dataclasses import dataclass
from models.cargo import Cargo
from models.truck import Truck

@dataclass
class ShortestRoute:
    cargo: Cargo
    closest_truck: Truck
    distance: float