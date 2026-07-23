from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Stock


def list_products(db: Session, branch_id: int):
    """
    Return all products available in a branch.
    """

    return (
        db.query(Stock)
        .filter(Stock.branch_id == branch_id)
        .all()
    )


def get_quantity(db: Session, branch_id: int, product_id: str):
    """
    Return the quantity of a product in a branch.
    """

    stock = (
        db.query(Stock)
        .filter(
            Stock.branch_id == branch_id,
            Stock.product_id == product_id
        )
        .first()
    )

    if stock is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found in this branch."
        )

    return stock


def add_stock(db: Session, branch_id: int, product_id: str, quantity: int):
    """
    Add stock to a branch.
    """

    stock = (
        db.query(Stock)
        .filter(
            Stock.branch_id == branch_id,
            Stock.product_id == product_id
        )
        .first()
    )

    if stock:
        stock.quantity += quantity

    else:
        stock = Stock(
            branch_id=branch_id,
            product_id=product_id,
            quantity=quantity
        )

        db.add(stock)

    db.commit()
    db.refresh(stock)

    return stock


def remove_stock(db: Session, branch_id: int, product_id: str, quantity: int):
    """
    Remove stock from a branch.
    """

    stock = (
        db.query(Stock)
        .filter(
            Stock.branch_id == branch_id,
            Stock.product_id == product_id
        )
        .first()
    )

    if stock is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found."
        )

    if stock.quantity < quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough stock."
        )

    stock.quantity -= quantity

    db.commit()
    db.refresh(stock)

    return stock
