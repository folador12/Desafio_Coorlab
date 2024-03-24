import json

from ..models.schemas import TripSchema

def load_trips_data():
    with open("app/data/data.json", "r") as file:
        data = json.load(file)["transport"]
    for item in data:
        item['duration'] = float(item['duration'].replace('h', ''))
        item['price_confort'] = float(item['price_confort'].replace('R$ ', '').replace(',', '.'))
        item['price_econ'] = float(item['price_econ'].replace('R$ ', '').replace(',', '.'))
    return [TripSchema(**item) for item in data]