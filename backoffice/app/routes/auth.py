from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import LoginRequest, Token
from app.services.auth_service import login as login_user
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=Token)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Authenticate a user and return a JWT token.
    """

    return login_user(
        db,
        request.username,
        request.password
    )


@router.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    """
    Return the authenticated user's information.
    """

    return {
        "id": current_user.id,
        "username": current_user.username,
        "role": current_user.role,
        "branch_id": current_user.branch_id
    }
