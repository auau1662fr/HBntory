import os
from dotenv import load_dotenv

# Charge les variables du fichier .env
load_dotenv()

# Database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./hbntory.db"
)

# JWT
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change_this_secret_key"
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
