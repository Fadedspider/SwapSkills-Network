from models import Base
from db import engine

# This creates all tables defined by Base subclasses (i.e., User)
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
