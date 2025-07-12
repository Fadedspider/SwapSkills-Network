from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from server.config.db import get_db            
from server.models import User                 
from server.schemas import UserLogin, Token
from server.utils import verify_password, create_jwt_token

auth_router = APIRouter()

@auth_router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_jwt_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
