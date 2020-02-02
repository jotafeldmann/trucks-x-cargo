from unittest import TestCase

from app.cargos.cargo import Cargo
from tests.utils.utils import cargos_fixture


class TestCargoModel(TestCase):
    def setUp(self):
        self.cargo = Cargo(**cargos_fixture[0])

    def test_cargo_get_route_total_length(self):
        distance = self.cargo.get_route_total_length()
        self.assertEqual(distance, 812.0)
