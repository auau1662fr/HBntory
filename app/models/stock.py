from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)

    branch_id = Column(Integer, ForeignKey("branches.id"))
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    branch = relationship("Branch", back_populates="stock_items")
