from unittest import TestCase

from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from app.routes.designate_cargo_for_truck import designate_cargo_for_truck
from tests.utils.utils import get_cargos_fixture, get_trucks_fixture, get_closest_trucks_for_cargo

trucks = [Truck(**row) for row in get_trucks_fixture()]


class TestTruckList(TestCase):
    def setUp(self):
        self.trucks_list = TruckList()

    def test_truck_list_append(self):
        truck = trucks[0]
        self.trucks_list.append(truck)
        self.assertEqual(self.trucks_list[0], truck)
        self.assertEqual(len(self.trucks_list), 1)
        self.assertEqual(self.trucks_list.geo_points_list[0], [truck.location.latitude, truck.location.longitude])
        self.assertEqual(len(self.trucks_list.geo_points_list), 1)
