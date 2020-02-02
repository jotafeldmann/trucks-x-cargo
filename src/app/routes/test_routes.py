from unittest import TestCase

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.routes import _get_routes_sorted_map, _get_routes_kdtree
from tests.utils.utils import get_cargos_fixture, get_trucks_fixture

trucks_list = [Truck(**row) for row in get_trucks_fixture()]
cargos_list = [Cargo(**row) for row in get_cargos_fixture()]


def get_route_values(route):
    product = route.cargo.product
    truck = route.closest_truck.company
    distance = route.distance
    return product, truck, distance


sorted_map_expected_routes = [
    ("Light bulbs", "Viking Products Of Austin Incustin", 190.0),
    ("Recyclables", "Ricardo Juradoacramento", 173.0),
    ("Apples", "Kjellberg'S Carpet Oneuffalo", 65.0),
    ("Wood", "Wisebuys Stores Incouverneur", 263.0),
    ("Cell phones", "Paul J Krez Companyorton Grove", 65.0),
    ("Wood", "Gary Lee Wilcoxpencer", 348.0),
    ("Oranges", "Fish-Bones Towingew York", 260.0)
]

kdtree_expected_routes = [
    ("Light bulbs", "Viking Products Of Austin Incustin", 190.0),
    ("Recyclables", "Ricardo Juradoacramento", 173.0),
    ("Apples", "Kjellberg'S Carpet Oneuffalo", 65.0),
    ("Wood", "Ibrahim Chimandalpharetta", 304.0),
    ("Cell phones", "Paul J Krez Companyorton Grove", 65.0),
    ("Wood", "Fish-Bones Towingew York", 352.0),
    ("Oranges", "Edmon'S Unique Furniture & Stone Gallery Inc.Os Angeles", 297.0)
]


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargos_list = cargos_list
        self.trucks_list = trucks_list

    def test_sorted_map_algorithm(self):
        routes = [route for route in _get_routes_sorted_map(trucks_list, cargos_list)]

        self.assertEqual(get_route_values(routes[0]), sorted_map_expected_routes[0])
        self.assertEqual(get_route_values(routes[1]), sorted_map_expected_routes[1])
        self.assertEqual(get_route_values(routes[2]), sorted_map_expected_routes[2])
        self.assertEqual(get_route_values(routes[3]), sorted_map_expected_routes[3])
        self.assertEqual(get_route_values(routes[4]), sorted_map_expected_routes[4])
        self.assertEqual(get_route_values(routes[5]), sorted_map_expected_routes[5])
        self.assertEqual(get_route_values(routes[6]), sorted_map_expected_routes[6])

    def test_kdtree_algorithm(self):
        trucks_list = TruckList()
        [trucks_list.append(Truck(**row)) for row in get_trucks_fixture()]
        routes = [route for route in _get_routes_kdtree(trucks_list, cargos_list)]

        self.assertEqual(get_route_values(routes[0]), kdtree_expected_routes[0])
        self.assertEqual(get_route_values(routes[1]), kdtree_expected_routes[1])
        self.assertEqual(get_route_values(routes[2]), kdtree_expected_routes[2])
        self.assertEqual(get_route_values(routes[3]), kdtree_expected_routes[3])
        self.assertEqual(get_route_values(routes[4]), kdtree_expected_routes[4])
        self.assertEqual(get_route_values(routes[5]), kdtree_expected_routes[5])
        self.assertEqual(get_route_values(routes[6]), kdtree_expected_routes[6])
