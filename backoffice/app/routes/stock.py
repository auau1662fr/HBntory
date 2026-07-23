from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_user

from app.schemas.stock import (
    StockUpdate,
    StockResponse,
    StockItem
)

from app.services.stock_service import (
    list_products,
    get_quantity,
    add_stock,
    remove_stock
)

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)


@router.get("/products", response_model=list[StockItem])
def get_products(
    db: Session = Depends(get_db),
    current_user=Depends(require_user)
):
    """
    List all products in the current user's branch.
    """

    return list_products(
        db,
        current_user.branch_id
    )


@router.get("/quantity/{product_id}", response_model=StockResponse)
def quantity(
    product_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(require_user)
):
    """
    Return the quantity of one product.
    """

    return get_quantity(
        db,
        current_user.branch_id,
        product_id
    )


@router.post("/add", response_model=StockResponse)
def add(
    request: StockUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_user)
):
    """
    Add stock.
    """

    return add_stock(
        db,
        current_user.branch_id,
        request.product_id,
        request.quantity
    )


@router.post("/remove", response_model=StockResponse)
def remove(
    request: StockUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_user)
):
    """
    Remove stock.
    """

    return remove_stock(
        db,
        current_user.branch_id,
        request.product_id,
        request.quantity
    )
