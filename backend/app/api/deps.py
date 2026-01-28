from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.company_repo import CompanyRepository
from app.services.company_service import CompanyService
from app.services.output_service import OutputService


# ---- Repos ----
def get_company_repo() -> CompanyRepository:
    return CompanyRepository()


# ---- Services ----
def get_company_service(
    repo: CompanyRepository = Depends(get_company_repo),
) -> CompanyService:
    return CompanyService(repo)


def get_output_service(
    repo: CompanyRepository = Depends(get_company_repo),
) -> OutputService:
    return OutputService(repo)
