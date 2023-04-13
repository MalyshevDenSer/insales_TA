from sqlalchemy.orm import Session
import caching
from schemas import BaseUser, UserEdit
import models


def get_the_game(db):
    return caching.get_game_guery(db)


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_game_db_cache(game, db: Session):
    db_game = db.query(models.Game).filter(models.Game.stage_number == game.stage_number).first()
    if db_game:
        for var, value in vars(game).items():
            setattr(db_game, var, value) if value else None
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        caching.update_cache(db)
    return db_game


def edit_user(db: Session, user: UserEdit):
    updated_info = user.__dict__.items()
    for key, value in updated_info:
        if value is not None and key != 'id':
            db.query(models.User).filter(models.User.id == user.id).update({key: value})
    db.commit()
    return


def create_user(db: Session, user: BaseUser):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
