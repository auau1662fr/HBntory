from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    UniqueConstraint,
    CheckConstraint
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)

    branch_id = Column(
        Integer,
        ForeignKey("branches.id"),
        nullable=False
    )

    product_id = Column(
        String(100),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    __table_args__ = (
        UniqueConstraint(
            "branch_id",
            "product_id",
            name="uq_branch_product"
        ),

        CheckConstraint(
            "quantity >= 0",
            name="check_quantity_positive"
        )
    )


    branch = relationship(
        "Branch",
        back_populates="stock_items"
    )
