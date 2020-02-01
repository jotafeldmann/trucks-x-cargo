from unittest import TestCase
from functools import partial
from json import dumps

from main import main, load_data, output_routes
from tests.fixtures.load_fixtures import cargos_fixture_generator, trucks_fixture_generator


def receive_return(*value):
    return value


class TestMain(TestCase):
    def setUp(self):
        self.load_data = partial(load_data,
                                 get_trucks_data=trucks_fixture_generator,
                                 get_cargos_data=cargos_fixture_generator)
        self.output_routes = partial(output_routes, output=receive_return)

    def test_main(self):

        routes = dumps(main(load_data=self.load_data, output_routes=self.output_routes))
        expected_routes = dumps([
            [["Light bulbs, ", "Viking Products Of Austin Incustin, ", 190.0]],
            [["Recyclables, ", "Ricardo Juradoacramento, ", 173.0]],
            [["Apples, ", "Kjellberg'S Carpet Oneuffalo, ", 65.0]],
            [["Wood, ", "Wisebuys Stores Incouverneur, ", 263.0]],
            [["Cell phones, ", "Paul J Krez Companyorton Grove, ", 65.0]],
            [["Wood, ", "Gary Lee Wilcoxpencer, ", 348.0]],
            [["Oranges, ", "Fish-Bones Towingew York, ", 260.0]]
        ])
        self.assertEqual(routes, expected_routes)
