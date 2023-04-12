from sqlalchemy.orm import Session

import models
from schemas import BaseUser, UserEdit


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_the_game(db: Session):
    return db.query(models.Game).filter().first()


def edit_user(db: Session, user: UserEdit):
    updated_info = user.__dict__.items()
    for key, value in updated_info:
        if value is not None and key != 'id':
            db.query(models.User).filter(models.User.id == user.id).update({key: value})
    db.commit()
    return get_user_by_id(db, user.id)


def create_user(db: Session, user: BaseUser):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
