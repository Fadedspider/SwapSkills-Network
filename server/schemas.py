from pydantic import BaseModel, EmailStr

# Input format for login
class UserLogin(BaseModel):
    email: str
    password: str

# Output format for token
class Token(BaseModel):
    access_token: str
    token_type: str

# Input format for registration
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserProfileOut(BaseModel):
    id: int
    email: str
    name: str | None = None
    location: str | None = None
    availability: str | None = None
    is_public: bool | None = True
    profile_photo_url: str | None = None

    class Config:
        orm_mode = True

class UserProfileUpdate(BaseModel):
    name: str | None = None
    location: str | None = None
    availability: str | None = None
    is_public: bool | None = True
    profile_photo_url: str | None = None
