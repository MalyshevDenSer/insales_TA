from pydantic import BaseModel
from datetime import date
from typing import Optional


class BaseUser(BaseModel):
    name: str


class UserInfo(BaseModel):
    id: int
    stage_1: bool
    stage_2: bool

    class Config:
        orm_mode = True


class UserEdit(BaseModel):
    id: int
    name: Optional[str] = None
    stage_1: Optional[bool] = None
    stage_2: Optional[bool] = None

    class Config:
        orm_mode = True


class Game(BaseModel):
    stage_number: int
    despcription: str
    ending_date: date

    class Config:
        orm_mode = True


class MainResponse(BaseModel):
    user: UserInfo
    game: Game

    class Config:
        orm_mode = True

