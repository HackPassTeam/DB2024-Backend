from fastapi import APIRouter

from . import (
    token,
    registration,
    me,
    identification,
    utm,
    educational_materials,
    tags
)

router = APIRouter(prefix='/v1')

router.include_router(token.router)
router.include_router(registration.router)
router.include_router(me.router)
router.include_router(identification.router)
router.include_router(utm.router)
router.include_router(educational_materials.router)
router.include_router(tags.router)
