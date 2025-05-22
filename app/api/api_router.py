from fastapi import APIRouter

from .routes import (
    hello
)

router = APIRouter()

router.include_router(hello.app_router, tags=["hello"], prefix="/hello")