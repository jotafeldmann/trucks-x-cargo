from unittest import TestCase
from functools import partial
from json import dumps

from main import main, load_data, output_routes, output_columns_title
from tests.fixtures.load_fixtures import cargos_fixture_generator, trucks_fixture_generator


def receive_return(a=None, b=None, c=None):
    return a, b, c


def receive_return_single(value):
    return value


class TestMain(TestCase):
    def setUp(self):
        self.load_data = partial(load_data,
                                 get_trucks_data=trucks_fixture_generator,
                                 get_cargos_data=cargos_fixture_generator)
        self.output_routes = output_routes
        self.output_columns_title = output_columns_title

    def test_main(self):
        title = self.output_columns_title(output=receive_return_single)
        routes = dumps(
            main(
                load_data=self.load_data,
                output_routes=output_routes,
                output_columns_title=self.output_columns_title,
                output=receive_return))
        expected_title = "Cargo, Truck Company, Distance (km)"
        expected_routes = dumps([
            [["Light bulbs, ", "Viking Products Of Austin Incustin, ", 190.0]],
            [["Recyclables, ", "Ricardo Juradoacramento, ", 173.0]],
            [["Apples, ", "Kjellberg'S Carpet Oneuffalo, ", 65.0]],
            [["Wood, ", "Wisebuys Stores Incouverneur, ", 263.0]],
            [["Cell phones, ", "Paul J Krez Companyorton Grove, ", 65.0]],
            [["Wood, ", "Gary Lee Wilcoxpencer, ", 348.0]],
            [["Oranges, ", "Fish-Bones Towingew York, ", 260.0]]
        ])
        self.assertEqual(title, expected_title)
        self.assertEqual(routes, expected_routes)
