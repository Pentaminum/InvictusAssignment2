from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_output_service
from app.schemas.output import OutputRequest, OutputResponse
from app.services.output_service import OutputService

router = APIRouter(prefix="/output", tags=["output"])

@router.post(
    "/generate",
    response_model=OutputResponse,
    response_model_exclude_none=True,
)
def generate_output(
    payload: OutputRequest,
    db: Session = Depends(get_db),
    service: OutputService = Depends(get_output_service),
):
    return service.build_output(db, payload.company_id, payload.period)
