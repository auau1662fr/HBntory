import httpx

from app.config import PRODUCT_API_URL


async def list_products():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{PRODUCT_API_URL}/products"
        )

    return response.json()
