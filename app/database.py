from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://admin:Piyushrai%40123@postgres:5432/coding_platform"
# DATABASE_URL = "postgresql://admin:Piyushrai%40123@localhost:5432/coding_platform"
# DATABASE_URL = "postgresql://postgres:Piyushrai@123@localhost:5432/coding_platform"
# DATABASE_URL = "postgresql://admin:Piyushrai123@localhost:5432/coding_platform"
# 
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    db_host = os.getenv("DB_HOST", "postgres")
    DATABASE_URL = f"postgresql://admin:Piyushrai123@{db_host}:5432/coding_platform"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()