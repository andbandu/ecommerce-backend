from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.category import schemas, crud
from database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.read_categories(db)

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(category, db)

@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.read_category(category_id, db)

@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.update_category(category_id, category, db)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete_category(category_id, db)
