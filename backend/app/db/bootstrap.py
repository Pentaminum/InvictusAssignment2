import json
from pathlib import Path

from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.models.company_profile import Company_profile


def bootstrap_db() -> None:
    # 1) Create tables
    Base.metadata.create_all(bind=engine)

    # 2) Seed if empty
    db = SessionLocal()
    try:
        has_any = db.query(Company_profile).first() is not None
        if has_any:
            return

        seed_path = Path(__file__).parent / "seed_data" / "companies.json"
        data = json.loads(seed_path.read_text(encoding="utf-8"))

        db.add_all([Company_profile(**row) for row in data])
        db.commit()
    finally:
        db.close()
