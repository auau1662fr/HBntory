from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users")
def list_users():
    pass


@router.post("/users")
def create_user():
    pass


@router.patch("/users/{user_id}/password")
def change_password(user_id: int):
    pass


@router.patch("/users/{user_id}/branch")
def change_branch(user_id: int):
    pass


@router.delete("/users/{user_id}")
def soft_delete_user(user_id: int):
    pass
