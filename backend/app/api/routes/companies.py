from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_company_service
from app.schemas.company_profile import CompanyProfileRead
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["companies"])

@router.get("", response_model=list[CompanyProfileRead])
def list_companies(
    db: Session = Depends(get_db),
    service: CompanyService = Depends(get_company_service),
):
    return service.list_companies(db)

