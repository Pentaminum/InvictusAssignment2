from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.company_repo import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    def list_companies(self, db: Session):
        return self.repo.list_companies(db)

    def get_company_or_404(self, db: Session, company_id: str):
        company = self.repo.get(db, company_id)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        return company
