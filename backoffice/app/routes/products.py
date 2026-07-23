from fastapi import APIRouter, Query

from app.services.product_service import (
    search_products as search_products_service,
    get_product as get_product_service,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/search")
async def search_products(
    query: str = Query("", description="Product name or identifier")
):
    """
    Search products from the Product MCP Server.
    """
    return await search_products_service(query)


@router.get("/{product_id}")
async def get_product(product_id: str):
    """
    Get product details from the Product MCP Server.
    """
    return await get_product_service(product_id)
