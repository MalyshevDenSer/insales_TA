from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_user", response_model=schemas.MainResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="There is no user with such ID")
    game = crud.get_the_game(db)
    response = {
        'user': {
            'name': db_user.name,
            'id': db_user.id,
            'stage_1': db_user.stage_1,
            'stage_2': db_user.stage_2,
        },
        'game': {
            'stage_number': game.stage_number,
            'despcription': game.despcription,
            'ending_date': game.ending_date,
        }
    }
    return response


@app.get("/get_game", response_model=schemas.Game)
def read_user(db: Session = Depends(get_db)):
    game = crud.get_the_game(db)
    return game


@app.put("/edit_user")
def edit_user(user: schemas.UserEdit, db: Session = Depends(get_db)):
    if not crud.get_user_by_id(db, user.id):
        raise HTTPException(status_code=400, detail="There is no user with such ID")
    db_user = crud.edit_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail='Something went wrong')
    return db_user

@app.post("/add_user", response_model=schemas.UserInfo)
def add_user(user: schemas.BaseUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)
