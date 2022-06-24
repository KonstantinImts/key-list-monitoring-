from typing import List

from fastapi import APIRouter, Depends

from ....api import deps
from ....models.auth import User
from ....services.users import UserService


router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/', response_model=List[User])
def get_users(
    service: UserService = Depends(),
    user: User = Depends(deps.get_current_user),
):
    return service.get_list()
