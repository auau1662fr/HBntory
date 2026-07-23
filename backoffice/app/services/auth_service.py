from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.security.password import verify_password
from app.security.jwt import create_access_token


def login(db: Session, username: str, password: str):
    """
    Authenticate a user and return a JWT access token.
    """

    # Rechercher l'utilisateur
    user = db.query(User).filter(
        User.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    # Vérifier le soft delete
    if user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is deleted."
        )

    # Vérifier que le compte est actif
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is inactive."
        )

    # Vérifier le mot de passe
    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    # Créer le JWT
    token = create_access_token(
        {
            "sub": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
