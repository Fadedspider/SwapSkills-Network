from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from server.config.db import get_db          
from server.models import User                 
from server.schemas import UserLogin, Token, UserRegister
from server.utils import verify_password, create_jwt_token, get_password_hash

auth_router = APIRouter()

@auth_router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_jwt_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/register", response_model=Token)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    # Check if email is already taken
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = get_password_hash(user_data.password)

    # Create new user
    new_user = User(email=user_data.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return JWT token
    access_token = create_jwt_token(data={"sub": str(new_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}