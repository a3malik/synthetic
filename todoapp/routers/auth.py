from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class CreateUserRequest(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    role: str


@router.post("/auth",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        email=create_user_request.email,
        role=create_user_request.role,
        is_active=True  # Default value
    )
    db.add(create_user_model)
    db.commit()
