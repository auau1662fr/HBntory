from fastapi import FastAPI

from app.database import Base, engine

from app.models.user import User
from app.models.branch import Branch
from app.models.stock import Stock

app = FastAPI()

Base.metadata.create_all(bind=engine)
