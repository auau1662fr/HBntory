from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    branch_id: int | None = None


class PasswordUpdate(BaseModel):
    password: str


class BranchUpdate(BaseModel):
    branch_id: int


class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    branch_id: int | None

    class Config:
        from_attributes = True
