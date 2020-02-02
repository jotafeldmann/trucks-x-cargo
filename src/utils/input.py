import csv

from app.trucks.truck import Truck
from app.cargos.cargo import Cargo

from utils.config import config
from utils.get_class_arguments import get_class_arguments_order

FILES_PATH_DEFAULT = './../input'

truck_fields_order = get_class_arguments_order(Truck)
cargo_fields_order = get_class_arguments_order(Cargo)


def _read_file(path, fields_order=None, skipHeader=True):
    with open(path) as file:
        reader = csv.DictReader(file, fieldnames=fields_order)

        if skipHeader:
            next(reader, None)

        for row in reader:
            yield row


_files_to_read = {
    'trucks': {
        'path': config.options.trucks_csv if config.options.trucks_csv else '{}/trucks.csv'.format(FILES_PATH_DEFAULT),
        'fields_order': truck_fields_order
    },
    'cargos': {
        'path': config.options.cargos_csv if config.options.cargos_csv else '{}/cargo.csv'.format(FILES_PATH_DEFAULT),
        'fields_order': cargo_fields_order
    }
}


def get_trucks_data():
    return _read_file(**_files_to_read.get('trucks'))


def get_cargos_data():
    return _read_file(**_files_to_read.get('cargos'))
