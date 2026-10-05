from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)  # අනිවාර්ය field එකක්
    description = Column(String, nullable=True)
    parent_id = Column(Integer, nullable=True)
    product_count = Column(Integer, default=0)
    order = Column(Integer, default=0)
    status = Column(Boolean, default=True)          # status එක boolean නිසා
    color = Column(String, nullable=True)
    image = Column(String, nullable=True)