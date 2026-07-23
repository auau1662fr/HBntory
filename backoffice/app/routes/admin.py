from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_admin

from app.schemas.user import (
    UserCreate,
    UserResponse,
    PasswordUpdate,
    BranchUpdate
)

from app.services.admin_service import (
    list_users,
    create_user,
    change_password,
    change_branch,
    soft_delete_user
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return list_users(db)


@router.post("/users", response_model=UserResponse)
def create_new_user(
    request: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return create_user(
        db,
        request.username,
        request.password,
        request.role,
        request.branch_id
    )


@router.patch("/users/{user_id}/password")
def update_password(
    user_id: int,
    request: PasswordUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return change_password(
        db,
        user_id,
        request.password
    )


@router.patch("/users/{user_id}/branch")
def update_branch(
    user_id: int,
    request: BranchUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return change_branch(
        db,
        user_id,
        request.branch_id
    )


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return soft_delete_user(
        db,
        user_id
    )
