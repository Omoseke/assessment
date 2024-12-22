# routes/user.py
from fastapi import APIRouter, HTTPException
from app.models import User
from app.db import users

router = APIRouter()

@router.post("/users/")
def create_user(user: User):
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return user

@router.get("/users/{user_id}")
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
