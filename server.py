from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/add_user", response_model=schemas.UserInfo, status_code=201)
def create_user(user: schemas.BaseUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="This name is already registered")
    return crud.create_user(db=db, user=user)


@app.get("/get_user_and_game", response_model=schemas.MainResponse, status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="There is no user with such ID")
    db_game = crud.get_the_game(db)
    if not crud.get_the_game(db):
        raise HTTPException(status_code=400, detail=f"There is no game at all")
    response = {'user': vars(db_user), 'game': vars(db_game)}
    for key in response:
        response[key].pop('_sa_instance_state')
    return response


@app.put("/edit_user", status_code=200)
def edit_user(user: schemas.UserEdit, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user.id)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"There is no user with ID={user.id}")
    if crud.get_user_by_name(db, user.name):
        raise HTTPException(status_code=400, detail=f"This name is already registered")
    updated_db_user = crud.edit_user(db, user, db_user)
    if not updated_db_user:
        raise HTTPException(status_code=400, detail='Something went wrong')
    return updated_db_user


@app.get("/get_game", status_code=200)
def get_game(db: Session = Depends(get_db)):
    game = crud.get_the_game(db)
    return game


@app.post("/update_game", response_model=schemas.Game, status_code=200)
def update_game(game: schemas.GameEdit, db: Session = Depends(get_db)):
    db_game = crud.get_the_game(db)
    if not db_game:
        raise HTTPException(status_code=400, detail=f"There is no game at all")
    elif game.stage_number != db_game.stage_number:
        raise HTTPException(status_code=400, detail=f"There is no game with stage_number={game.stage_number}")
    updated_game = crud.update_game_db_and_cache(db, game, db_game)
    if not updated_game:
        raise HTTPException(status_code=400, detail=f"The game was not updated, something went wrong")
    return updated_game


@app.post("/add_the_game", response_model=schemas.Game, status_code=201)
def create_game(game: schemas.Game, db: Session = Depends(get_db)):
    db_game = crud.get_the_game(db)
    if db_game:
        raise HTTPException(status_code=400, detail="There is already one game")
    new_game = crud.create_game(db, game)
    crud.update_game_db_and_cache(db, game, new_game)
    return new_game
