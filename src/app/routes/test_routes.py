from unittest import TestCase

from app.cargos.cargo import Cargo
from app.trucks.truck import Truck
from app.routes.routes import _get_routes_sorted_map
from tests.utils.utils import get_cargos_fixture, get_trucks_fixture

trucks_list = [Truck(**row) for row in get_trucks_fixture()]
cargos_list = [Cargo(**row) for row in get_cargos_fixture()]


class TestDesignateCargoForTruck(TestCase):
    def setUp(self):
        self.cargos_list = cargos_list
        self.trucks_list = trucks_list

    def test_sorted_map_algorithm(self):
        routes = [route for route in _get_routes_sorted_map(trucks_list, cargos_list)]
        result_routes = routes.__str__()
        expected_routes = """\
[ShortestRoute(cargo=Cargo(product='Light bulbs', origin_city='Sikeston', origin_state='MO', \
origin_location=GeoPoint(latitude=36.876719, longitude=-89.5878579), destination_city='Grapevine', \
destination_state='TX', destination_location=GeoPoint(latitude=32.9342919, longitude=-97.0780654)), \
closest_truck=Truck(company='Viking Products Of Austin Incustin', city='Fort Campbell', state='TN', \
location=GeoPoint(latitude=36.6634467, longitude=-87.47739020000002)), distance=190.0),\
 ShortestRoute(cargo=Cargo(product='Recyclables', origin_city='Christiansburg', origin_state='VA', \
origin_location=GeoPoint(latitude=37.1298517, longitude=-80.4089389), destination_city='Apopka', \
destination_state='FL', destination_location=GeoPoint(latitude=28.6934076, longitude=-81.5322149)), \
closest_truck=Truck(company='Ricardo Juradoacramento', city='Covesville', state='VA', \
location=GeoPoint(latitude=37.8901411, longitude=-78.70474010000001)), distance=173.0),\
 ShortestRoute(cargo=Cargo(product='Apples', origin_city='Columbus', origin_state='OH', \
origin_location=GeoPoint(latitude=39.9611755, longitude=-82.99879419999999), destination_city='Woodland', \
destination_state='CA', destination_location=GeoPoint(latitude=38.67851570000001, longitude=-121.7732971)), \
closest_truck=Truck(company="Kjellberg'S Carpet Oneuffalo", city='Mount Vernon', state='OH', \
location=GeoPoint(latitude=40.3933956, longitude=-82.4857181)), distance=65.0),\
 ShortestRoute(cargo=Cargo(product='Wood', origin_city='Hebron', origin_state='KY', \
origin_location=GeoPoint(latitude=39.0661472, longitude=-84.70318879999999), destination_city='Jefferson', \
destination_state='LA', destination_location=GeoPoint(latitude=29.96603709999999, longitude=-90.1531298)), \
closest_truck=Truck(company='Wisebuys Stores Incouverneur', city='Washington', state='WV', \
location=GeoPoint(latitude=39.244853, longitude=-81.6637765)), distance=263.0),\
 ShortestRoute(cargo=Cargo(product='Cell phones', origin_city='Hickory', origin_state='NC', \
origin_location=GeoPoint(latitude=35.7344538, longitude=-81.3444573), destination_city='La Pine', \
destination_state='OR', destination_location=GeoPoint(latitude=43.67039949999999, longitude=-121.503636)), \
closest_truck=Truck(company='Paul J Krez Companyorton Grove', city='Forest City', state='NC', \
location=GeoPoint(latitude=35.3340108, longitude=-81.8651028)), distance=65.0),\
 ShortestRoute(cargo=Cargo(product='Wood', origin_city='Northfield', origin_state='MN', \
origin_location=GeoPoint(latitude=44.4582983, longitude=-93.161604), destination_city='Waukegan', \
destination_state='IL', destination_location=GeoPoint(latitude=42.3636331, longitude=-87.84479379999999)), \
closest_truck=Truck(company='Gary Lee Wilcoxpencer', city='Eagle River', state='WI', \
location=GeoPoint(latitude=45.9171763, longitude=-89.2442988)), distance=348.0),\
 ShortestRoute(cargo=Cargo(product='Oranges', origin_city='Fort Madison', origin_state='IA', \
origin_location=GeoPoint(latitude=40.6297634, longitude=-91.31453499999999), destination_city='Ottawa', \
destination_state='IL', destination_location=GeoPoint(latitude=41.3455892, longitude=-88.8425769)), \
closest_truck=Truck(company='Fish-Bones Towingew York', city='Monroe', state='WI', \
location=GeoPoint(latitude=42.60111939999999, longitude=-89.6384532)), distance=260.0)]"""
        self.assertEqual(result_routes, expected_routes)
