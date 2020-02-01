from utils.input import get_trucks_data, get_cargos_data

trucks_fixture_generator = get_trucks_data
cargos_fixture_generator = get_cargos_data

trucks_fixture = [row for row in trucks_fixture_generator()]
cargos_fixture = [row for row in cargos_fixture_generator()]
