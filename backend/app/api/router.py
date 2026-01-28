from fastapi import APIRouter
from app.api.routes.health import router as health_router
from app.api.routes.companies import router as companies_router
from app.api.routes.output import router as output_router

api_router = APIRouter(prefix="/api")

api_router.include_router(health_router)
api_router.include_router(companies_router)
api_router.include_router(output_router)
