from fastapi import APIRouter

from .endpoints.auth import router as auth_router
from .endpoints.users import router as users_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(users_router)