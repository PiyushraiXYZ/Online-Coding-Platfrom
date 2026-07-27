import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
from app.routes import router
from app.database import engine, SessionLocal
from app.models import Base, Problem
from app.migrate_problems import migrate_problems

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def init_db():
    for _ in range(20):
        try:
            Base.metadata.create_all(bind=engine)
            with SessionLocal() as db:
                if db.query(Problem).count() == 0:
                    migrate_problems(db)
            return
        except OperationalError:
            time.sleep(2)

    raise RuntimeError("Database is not ready. Please check PostgreSQL container.")


init_db()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "API Running"}