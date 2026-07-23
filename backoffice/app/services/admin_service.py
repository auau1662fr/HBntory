from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.security.password import hash_password


def list_users(db: Session):
    """
    Return all non-deleted users.
    """

    return (
        db.query(User)
        .filter(User.is_deleted == False)
        .all()
    )


def create_user(
    db: Session,
    username: str,
    password: str,
    role: str,
    branch_id: int | None
):
    """
    Create a new user.
    """

    existing = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )

    user = User(
        username=username,
        password_hash=hash_password(password),
        role=role,
        branch_id=branch_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def change_password(
    db: Session,
    user_id: int,
    new_password: str
):
    """
    Change a user's password.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    user.password_hash = hash_password(new_password)

    db.commit()

    return {"message": "Password updated."}


def change_branch(
    db: Session,
    user_id: int,
    branch_id: int
):
    """
    Assign a user to another branch.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    user.branch_id = branch_id

    db.commit()

    return {"message": "Branch updated."}


def soft_delete_user(
    db: Session,
    user_id: int
):
    """
    Soft delete a user.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    user.is_deleted = True
    user.is_active = False

    db.commit()

    return {"message": "User deleted."}
