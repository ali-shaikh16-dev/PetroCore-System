import Model
import pytest
from Database.db_connect import engine, SessionLocal, Base


@pytest.fixture(scope="function")
def get_db():
    Base.metadata.create_all(bind=engine)  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

