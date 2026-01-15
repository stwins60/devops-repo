from fastapi import APIRouter, HTTPException
from app.models import User, UserCreate
from datetime import datetime
from typing import List

router = APIRouter()

# In-memory database
users_db = {}
user_id_counter = 1

@router.get("/users", response_model=List[User])
async def get_users():
    return list(users_db.values())

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.post("/users", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    global user_id_counter
    new_user = User(
        id=user_id_counter,
        name=user.name,
        email=user.email,
        created_at=datetime.now()
    )
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    return new_user

@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
