

from fastapi import HTTPException

from app.category import schemas, models
from sqlalchemy.orm import Session

from database import get_db


def read_categories(db: Session = get_db):
    categories = db.query(models.Category).all()
    return categories

def create_category(category: schemas.CategoryCreate, db: Session = get_db):
    db_category = models.Category(**category.model_dump())  
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def read_category(category_id: int, db: Session = get_db):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    return db_category

def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = get_db):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        update_data = category.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
                setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

