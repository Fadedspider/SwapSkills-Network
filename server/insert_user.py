from db import SessionLocal
from models import User
from utils import get_password_hash

db = SessionLocal()

hashed_password = get_password_hash("test123")
new_user = User(
    email="test@example.com",
    password_hash=hashed_password
)

db.add(new_user)
db.commit()
db.refresh(new_user)
print(f"✅ Test user created: {new_user.email}")
db.close()
