from http import HTTPStatus

from fastapi import APIRouter

from .health_schemas import HealthResponse

router = APIRouter(prefix='/health', tags=['Monitoring'])


@router.get(
    '/health',
    tags=['Monitoring'],
    response_model=HealthResponse,
    status_code=HTTPStatus.OK,
)
async def health_check():
    """Verifica se o servidor está de pé."""
    return {'status': 'alive', 'version': '0.1.0', 'service': 'TycheHound'}
