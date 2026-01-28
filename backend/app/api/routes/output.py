import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.company_repo import CompanyRepository
from app.schemas.output import OutputRequest, OutputResponse
from app.services.output_service import OutputService

router = APIRouter(prefix="/output", tags=["output"])

service = OutputService(CompanyRepository())

@router.post(
        "/generate",
        response_model=OutputResponse,
        response_model_exclude_none=True,
             )
def generate_output(payload: OutputRequest, db: Session = Depends(get_db)):
    return service.build_output(db, payload.company_id, payload.period)
