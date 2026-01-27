from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.company_repo import CompanyRepository
from app.services.company_service import CompanyService
from app.schemas.company import CompanyProfileRead

router = APIRouter(prefix="/companies", tags=["companies"])

service = CompanyService(CompanyRepository())

@router.get("", response_model=list[CompanyProfileRead])
def list_companies(db: Session = Depends(get_db)):
    return service.list_companies(db)

@router.get("/{company_id}", response_model=CompanyProfileRead)
def get_company(company_id: str, db: Session = Depends(get_db)):
    return service.get_company_or_404(db, company_id)
