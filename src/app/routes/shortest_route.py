from dataclasses import dataclass
from app.models.cargo import Cargo
from app.models.truck import Truck

@dataclass
class ShortestRoute:
    cargo: Cargo
    closest_truck: Truck
    distance: float