from fastapi import HTTPException, status


def require_admin(user):
    """
    Allow access only to administrators.
    """

    if user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required."
        )

    return True


def require_common_user(user):
    """
    Allow access only to common users.
    """

    if user.role != "USER":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Common user access required."
        )

    return True


def check_branch_access(user, branch_id):
    """
    A common user can only access their assigned branch.
    """

    if user.role == "ADMIN":
        return True

    if user.branch_id != branch_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this branch."
        )

    return True
