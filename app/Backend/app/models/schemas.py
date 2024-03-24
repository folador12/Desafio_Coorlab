from pydantic import BaseModel

class TripSchema(BaseModel):
    id: int
    name: str
    price_confort: float
    price_econ: float
    city: str
    duration: float
    seat: str
    bed: str