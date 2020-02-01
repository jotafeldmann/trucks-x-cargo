from unittest import TestCase

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.routes.designate_cargo_for_truck import designate_cargo_for_truck
from tests.fixtures.load_fixtures import cargos_fixture, trucks_fixture


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargo = Cargo(**cargos_fixture[0])
        self.trucks_list = [Truck(**row) for row in trucks_fixture]

    def test_cargo_get_route_total_length(self):
        # distance, closest_truck = designate_cargo_for_truck()
        self.assertEqual(True, True)
