from pydantic import BaseModel

# Input format for login
class UserLogin(BaseModel):
    email: str
    password: str

# Output format for token
class Token(BaseModel):
    access_token: str
    token_type: str
