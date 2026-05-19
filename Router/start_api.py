from Database.db_connect import Base , engine
from fastapi import FastAPI , APIRouter

router = APIRouter()

@router.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)