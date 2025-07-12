from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace these values with your actual credentials
DB_USER = "postgres"         # or your custom user
DB_PASSWORD = "kaustubh" # the password you set
DB_NAME = "swapskills"
DB_HOST = "localhost"
DB_PORT = "5432"

# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = f"postgresql://postgres:{DB_PASSWORD}@db.vaqytztdyddmjurvdcnr.supabase.co:5432/postgres"

# Set up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
