from fastapi import FastAPI

from app.routes import auth
from app.routes import admin
from app.routes import stock
from app.routes import products
from app.database import Base, engine
from app.models import User, Branch, Stock

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(stock.router)
app.include_router(products.router)
