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


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargos_list = cargos_list
        self.trucks_list = trucks_list

    def test_sorted_map_algorithm(self):
        routes = [route for route in _get_routes_sorted_map(trucks_list, cargos_list)]

        self.assertEqual(get_route_values(routes[0]),
                         ("Light bulbs", "Viking Products Of Austin Incustin", 190.0))

        self.assertEqual(get_route_values(routes[1]),
                         ("Recyclables", "Ricardo Juradoacramento", 173.0))

        self.assertEqual(get_route_values(routes[2]),
                         ("Apples", "Kjellberg'S Carpet Oneuffalo", 65.0))

        self.assertEqual(get_route_values(routes[3]),
                         ("Wood", "Wisebuys Stores Incouverneur", 263.0))

        self.assertEqual(get_route_values(routes[4]),
                         ("Cell phones", "Paul J Krez Companyorton Grove", 65.0))

        self.assertEqual(get_route_values(routes[5]),
                         ("Wood", "Gary Lee Wilcoxpencer", 348.0))

        self.assertEqual(get_route_values(routes[6]),
                         ("Oranges", "Fish-Bones Towingew York", 260.0))

    def test_kdtree_algorithm(self):
        trucks_list = TruckList()
        [trucks_list.append(Truck(**row)) for row in get_trucks_fixture()]
        routes = [route for route in _get_routes_kdtree(trucks_list, cargos_list)]
        result_routes = routes.__str__()

        # self.assertEqual(result_routes, expected_routes)
