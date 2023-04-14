from pydantic import BaseModel
from datetime import date
from typing import Optional


class BaseUser(BaseModel):
    name: str


class UserInfo(BaseUser):
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
    description: str
    ending_date: date

    class Config:
        orm_mode = True


class GameEdit(BaseModel):
    stage_number: int
    description: Optional[str] = None
    ending_date: Optional[date] = None


class MainResponse(BaseModel):
    user: UserInfo
    game: Game

    class Config:
        orm_mode = True
