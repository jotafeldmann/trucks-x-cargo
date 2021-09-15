from unittest import TestCase

from app.trucks.truck import Truck
from app.trucks.truck_list import TruckList
from tests.utils.utils import get_trucks_fixture
from utils.geolocation import GeoPoint

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

    def test_get_closest_trucks_to_location(self):
        truck_1 = trucks[0]
        self.trucks_list.append(truck_1)

        truck_2 = trucks[1]
        self.trucks_list.append(truck_2)

        result_1 = self.trucks_list.get_closest_trucks_to_location(truck_1.location)
        distance, truck = result_1[0]

        self.assertEqual(len(self.trucks_list), 2)
        self.assertEqual(len(result_1), 2)
        self.assertEqual(distance, 0)
        self.assertEqual(truck, truck_1)

        result_2 = self.trucks_list.get_closest_trucks_to_location(GeoPoint(8, 7))
        distance, truck = result_2[0]

        self.assertEqual(distance, 9934)
        self.assertEqual(truck, truck_1)
        self.assertEqual(result_2[1], (12707, truck_2))
