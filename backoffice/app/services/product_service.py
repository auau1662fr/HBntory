import httpx
from fastapi import HTTPException

# Adresse de ton Product MCP Server
MCP_SERVER_URL = "http://localhost:8001"


async def search_products(query: str = ""):
    """
    Search products in the MCP Product Server.
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{MCP_SERVER_URL}/products",
                params={"query": query}
            )

        response.raise_for_status()
        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Product MCP Server is unavailable."
        )

    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=response.status_code,
            detail="Unable to retrieve products."
        )


async def get_product(product_id: str):
    """
    Get one product from the MCP Product Server.
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{MCP_SERVER_URL}/products/{product_id}"
            )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        response.raise_for_status()
        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Product MCP Server is unavailable."
        )

    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=response.status_code,
            detail="Unable to retrieve product."
        )
