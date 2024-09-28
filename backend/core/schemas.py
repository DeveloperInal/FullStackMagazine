from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Card_UC_Data(BaseModel):
    id: int
    title: str
    price: int
    description: str

    class Config:
        from_attributes = True

class User_By_Product(BaseModel):
    tg_id: int
    card_title: str
    by_product_date: Optional[datetime]

    class Config:
        from_attributes = True
class Promocod_Data(BaseModel):
    promocod: str

    class Config:
        from_attributes = True