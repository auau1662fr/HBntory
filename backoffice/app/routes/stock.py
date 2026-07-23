from fastapi import APIRouter

router = APIRouter(prefix="/stock", tags=["Stock"])


@router.get("/products")
def list_products():
    pass


@router.get("/quantity/{product_id}")
def get_quantity(product_id: str):
    pass


@router.post("/add")
def add_stock():
    pass


@router.post("/remove")
def remove_stock():
    pass
