import csv


def readTrucks():
    with open('./../input/trucks.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            truck, city, state, lat, lon = row
            print(city)

def readCargo():
    with open('./../input/cargo.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            product, origin_city, origin_state, origin_lat, origin_lon, destination_city, destination_state, destination_lat, destination_lon = row
            print(product)

readCargo()