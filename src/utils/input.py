import csv

def _read_file(path, fields_order=None, skipHeader=True):
    with open(path) as file:
        reader = csv.DictReader(file, fieldnames=fields_order)

        if skipHeader:
            next(reader, None)
            
        for row in reader:
            yield row

_files_to_read = {
    'trucks': {
        'path': './../input/trucks.csv',
        'fields_order': ['company', 'city', 'state', 'latitude', 'longitude']
    },
    'cargos': {
        'path': './../input/cargo.csv',
        'fields_order': ['product', 'origin_city', 'origin_state', 'origin_latitude', 'origin_longitude', 'destination_city', 'destination_state', 'destination_latitude', 'destination_longitude']
    }
}

def get_trucks_data():
    return _read_file(**_files_to_read.get('trucks'))

def get_cargos_data():
    return _read_file(**_files_to_read.get('cargos'))
