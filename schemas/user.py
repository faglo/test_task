from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    name: str
    spent_money: int
    gems: List[str]

class User(UserBase):
    id: int
