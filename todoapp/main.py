# Create database.
from fastapi import FastAPI, Depends, HTTPException , Path 
#what is dependency injection, implmented by Depends import above?
import models
from models import Todos
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status


app= FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/",status_code=status.HTTP_200_OK)
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()

@app.get("/todos/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int=Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    return HTTPException(status_code=404, detail='Todo not found')