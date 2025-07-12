from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.config.db import get_db
from server.models import User
from server.utils import get_current_user
from server.schemas import UserProfileOut
from server.schemas import UserProfileUpdate

profile_router = APIRouter()

@profile_router.get("/profile/me", response_model=UserProfileOut)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return current_user

@profile_router.put("/profile", response_model=UserProfileOut)
def update_my_profile(
    updated_data: UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    for field, value in updated_data.dict(exclude_unset=True).items():
        setattr(current_user, field, value)

    db.commit()
    db.refresh(current_user)
    return current_user
