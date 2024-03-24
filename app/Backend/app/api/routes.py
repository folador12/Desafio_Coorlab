from fastapi import APIRouter
from ..services.trip_service import search_trips

router = APIRouter()

@router.get("/search")
def read_trips(city: str):
    return search_trips(city)