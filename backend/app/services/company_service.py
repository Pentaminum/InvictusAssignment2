from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.company_repo import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    def list_companies(self, db: Session):
        return self.repo.list_companies(db)

    def get_company(self, db: Session, company_id: str):
        return self.repo.get(db, company_id)
