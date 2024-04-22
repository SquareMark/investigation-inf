from pydantic import BaseModel

class Item(BaseModel):
    name: str

# core/database.py
class Profile(BaseModel):
    name: str
    age: int
    email: str
    phone_number: str