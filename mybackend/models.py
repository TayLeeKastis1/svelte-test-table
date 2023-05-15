'''
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Exchange(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    currency: str = Field(...)
    name: str = Field(...)
    buy: str = Field(...)
    sell: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "currency": "ZAR",
                "name": "South African Rands",
                "buy": "1.34578",
                "sell": "1.34578"
            }
        }

class ExchangeUpdate(BaseModel):
    currency: Optional[str]
    name: Optional[str]
    buy: Optional[str]
    sell: Optional[str]


    class Config:
        schema_extra = {
            "example": {
                "currency": "ZAR",
                "name": "South African Rands",
                "buy": "1.34578",
                "sell": "1.34578"
            }
        }
        '''