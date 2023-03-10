from fastapi.routing import APIRouter

from fission_project_template.web.api import demo_app, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(demo_app.router, prefix="/demo", tags=["demo"])
