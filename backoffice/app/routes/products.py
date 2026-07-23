from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/search")
def search_products():
    pass


@router.get("/{product_id}")
def get_product(product_id: str):
    pass
