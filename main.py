from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import app.category.models as models, app.category.schemas as schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

from app.category import router as category_router

app = FastAPI(title="E-commerce Backend API"            , version="1.0.0")

app.include_router(category_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

