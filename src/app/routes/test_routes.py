from unittest import TestCase

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.routes.routes import _get_routes_sorted_map
from tests.utils.utils import get_cargos_fixture, get_trucks_fixture, get_closest_trucks_for_cargo

trucks_list = [Truck(**row) for row in get_trucks_fixture()]
cargos_list = [Cargo(**row) for row in get_cargos_fixture()]


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargos_list = cargos_list
        self.trucks_list = trucks_list

    def test_sorted_map_algorithm(self):
        routes = [route for route in _get_routes_sorted_map(trucks_list, cargos_list)]
        # self.assertEqual(routes, False)
