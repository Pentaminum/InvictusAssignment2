from sqlalchemy.orm import Session
from app.models.company_profile import CompanyProfile

class CompanyRepository:
    def list_companies(self, db: Session) -> list[CompanyProfile]:
        return (
            db.query(CompanyProfile)
            .order_by(CompanyProfile.legal_entity_name.asc())
            .all()
        )

    def get(self, db: Session, company_id: str) -> CompanyProfile | None:
        return db.query(CompanyProfile).filter(CompanyProfile.company_id == company_id).first()
