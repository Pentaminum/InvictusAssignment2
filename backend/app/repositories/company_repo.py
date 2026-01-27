from sqlalchemy.orm import Session
from app.models.company_profile import Company_profile

class CompanyRepository:
    def list_companies(self, db: Session) -> list[Company_profile]:
        return (
            db.query(Company_profile)
            .order_by(Company_profile.legal_entity_name.asc())
            .all()
        )

    def get(self, db: Session, company_id: str) -> Company_profile | None:
        return db.query(Company_profile).filter(Company_profile.company_id == company_id).first()

    def upsert_many(self, db: Session, companies: list[Company_profile]) -> None:
        # for seeding: if exists, update, if not, insert
        for c in companies:
            existing = self.get(db, c.company_id)
            if existing:
                existing.legal_entity_name = c.legal_entity_name
                existing.legal_address = c.legal_address
                existing.jurisdiction = c.jurisdiction
                existing.ticker_symbol = c.ticker_symbol
                existing.stock_exchange = c.stock_exchange
                existing.industry = c.industry
                existing.currency_of_reporting = c.currency_of_reporting
                existing.fiscal_year_end_date = c.fiscal_year_end_date
                existing.incorporation_date = c.incorporation_date
                existing.style_guide_reference = c.style_guide_reference
            else:
                db.add(c)
        db.commit()
