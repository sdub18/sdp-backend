import os
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://" + os.getenv('POSTGRES_USER') + ":" + os.getenv('POSTGRES_PASSWORD') + "@db:5432/" + os.getenv('POSTGRES_DB')

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()