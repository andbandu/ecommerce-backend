from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.category import schemas, crud
from database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

# 1. Read All Categories
@router.get("/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.read_categories(db=db)

# 2. Create Category
@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# 3. Read Single Category
@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.read_category(db=db, category_id=category_id)
    
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
        
    return db_category

# 4. Update Category
@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    updated_category = crud.update_category(db=db, category_id=category_id, category=category)
    
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
        
    return updated_category

# 5. Delete Category
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(db=db, category_id=category_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
        
    return {"message": "Category deleted successfully"}