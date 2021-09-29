from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import String

""" Scheme: Property to use and to validate with ORM """

class Property(BaseModel):
    address: str
    city: str
    price: int
    description: str
    year: int