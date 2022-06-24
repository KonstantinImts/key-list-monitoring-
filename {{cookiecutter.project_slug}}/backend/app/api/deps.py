from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ..models.auth import User
from ..services.auth import AuthService


oath2_scheme = OAuth2PasswordBearer(
    tokenUrl='/auth/sign-in',
)


def get_current_user(token: str = Depends(oath2_scheme)) -> User:
    return AuthService.validate_token(token)


# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user
