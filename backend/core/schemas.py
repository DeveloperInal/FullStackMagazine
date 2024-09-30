from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Card_UC_Data(BaseModel):
    id: int
    title: str
    price: int
    image_url: str

    class Config:
        from_attributes = True

class User_By_Product(BaseModel):
    tg_id: int
    card_title: str
    by_product_date: Optional[datetime]
    promocode: str
    price: int

    class Config:
        from_attributes = True
class Promocod_Data(BaseModel):
    promocode: str
    title: str
