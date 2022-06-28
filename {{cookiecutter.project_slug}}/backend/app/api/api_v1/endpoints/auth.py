from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ....models.auth import Token, User, UserCreate
from ....services.auth import AuthService
from ...deps import get_current_user


router = APIRouter()


@router.post('/sign-up', response_model=Token)
def sign_up(
    user_data: UserCreate = Depends(),
    service: AuthService = Depends(),
):
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token, name='sign-in')
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
):
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )


@router.get("/me", response_model=User)
def get_current_user(current_user: User = Depends(get_current_user)):
    return current_user
