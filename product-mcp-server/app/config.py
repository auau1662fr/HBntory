import os

from dotenv import load_dotenv

load_dotenv()

PRODUCT_API_URL = os.getenv("PRODUCT_API_URL")

if not PRODUCT_API_URL:
    raise RuntimeError("PRODUCT_API_URL is not defined.")
