from fastapi import APIRouter, FastAPI

from .system_health.router import router as health_router

main_router = APIRouter(prefix='/api')


main_router.include_router(health_router)

app = FastAPI()
app.include_router(main_router)
