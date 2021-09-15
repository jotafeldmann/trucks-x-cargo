from unittest import TestCase

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.routes.designate_cargo_for_truck import designate_cargo_for_truck
from tests.utils.utils import get_cargos_fixture, get_trucks_fixture, get_closest_trucks_for_cargo

trucks_list = [Truck(**row) for row in get_trucks_fixture()]
cargos = [Cargo(**row) for row in get_cargos_fixture()]
closest_trucks = get_closest_trucks_for_cargo(trucks_list, cargos[0])


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargo = cargos[0]
        self.trucks_list = trucks_list
        self.closest_trucks = closest_trucks
        self.trucks_designated_map = {}

    def test_cargo_get_route_total_length(self):
        distance, closest_truck = designate_cargo_for_truck(
            self.cargo, closest_trucks, trucks_designated_map=self.trucks_designated_map)
        self.assertEqual(closest_truck.company, 'Viking Products Of Austin Incustin')
        self.assertEqual(distance, 190)

    def test_cargo_get_route_total_length_for_max_cargos_equal_to_1(self):
        trucks_designated_map = {}
        cargo_1 = cargos[2]
        closest_trucks = get_closest_trucks_for_cargo(trucks_list, cargo_1)
        distance_1, closest_truck_1 = designate_cargo_for_truck(
            cargo_1, closest_trucks, trucks_designated_map=trucks_designated_map, max_cargos_per_truck=1)
        self.assertEqual(closest_truck_1.company, 'Kjellberg\'S Carpet Oneuffalo')
        self.assertEqual(distance_1, 65)

        cargo_2 = cargos[2]
        closest_trucks = get_closest_trucks_for_cargo(trucks_list, cargo_2)
        distance_2, closest_truck_2 = designate_cargo_for_truck(
            cargo_2, closest_trucks, trucks_designated_map=trucks_designated_map, max_cargos_per_truck=1)
        self.assertEqual(closest_truck_2.company, 'Wisebuys Stores Incouverneur')
        self.assertEqual(distance_2, 140)

    def test_cargo_get_route_total_length_for_max_cargos_equal_to_2(self):
        trucks_designated_map = {}
        cargo_1 = cargos[2]
        closest_trucks = get_closest_trucks_for_cargo(trucks_list, cargo_1)
        distance_1, closest_truck_1 = designate_cargo_for_truck(
            cargo_1, closest_trucks, trucks_designated_map=trucks_designated_map, max_cargos_per_truck=2)
        self.assertEqual(closest_truck_1.company, 'Kjellberg\'S Carpet Oneuffalo')
        self.assertEqual(distance_1, 65)

        cargo_2 = cargos[3]
        closest_trucks = get_closest_trucks_for_cargo(trucks_list, cargo_2)
        distance_2, closest_truck_2 = designate_cargo_for_truck(
            cargo_2, closest_trucks, trucks_designated_map=trucks_designated_map, max_cargos_per_truck=2)
        self.assertEqual(closest_truck_2.company, 'Kjellberg\'S Carpet Oneuffalo')
        self.assertEqual(distance_2, 241)
