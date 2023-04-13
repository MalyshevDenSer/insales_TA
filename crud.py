from sqlalchemy.orm import Session
import caching
from schemas import BaseUser
import models


def create_user(db: Session, user: BaseUser):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def edit_user(db: Session, user, db_user):
    for key, value in vars(user).items():
        if key != 'id' and value is not None:
            setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    return user


def get_the_game(db):
    return caching.get_game_guery(db)


def update_game_db_and_cache(db: Session, game, db_game):
    if db_game:
        for var, value in vars(game).items():
            if value is not None:
                setattr(db_game, var, value)
        db.add(db_game)
        db.commit()
        caching.update_cache(db)
    return db_game
