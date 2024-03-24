from fastapi import HTTPException
from ..data.data_loader import load_trips_data

def search_trips(city: str):
    trips = load_trips_data()
    filtered_trips = [trip for trip in trips if trip.city.lower() == city.lower()]
    if not filtered_trips:
        raise HTTPException(status_code=404, detail="No trips found for the given city.")
    
    
    fastest_trip = min(filtered_trips, key=lambda x: x.duration)
    
    cheapest_trip = min(filtered_trips, key=lambda x: x.price_econ)
    
    response = {}
    
    response['fastest'] = fastest_trip
    response['cheapest'] = cheapest_trip
    
    
    return response