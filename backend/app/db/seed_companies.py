#run once to seed the database with example companies
from app.db.session import SessionLocal
from app.models.company_profile import Company_profile
from app.repositories.company_repo import CompanyRepository

def seed():
    db = SessionLocal()
    repo = CompanyRepository()

    companies = [
        Company_profile(
            company_id="CMP-ALP-001",
            legal_entity_name="Alpine Resource Technologies Ltd.",
            legal_address="1200 Burrard Street, Suite 1800, Vancouver, BC, V6Z 2C7, Canada",
            jurisdiction="Canada",
            ticker_symbol="TSX:ART",
            stock_exchange="TSX",
            industry="Mining Technology & Services",
            currency_of_reporting="CAD",
            fiscal_year_end_date="2024-12-31",
            incorporation_date="2015-06-18",
            style_guide_reference="style_guides/alpine_fs_style_v1.pdf",
        ),
        Company_profile(
            company_id="CMP-NVX-002",
            legal_entity_name="Novex Health Systems Inc.",
            legal_address="455 Market Street, Floor 22, San Francisco, CA 94105, USA",
            jurisdiction="United States",
            ticker_symbol="NASDAQ:NVHX",
            stock_exchange="NASDAQ",
            industry="Healthcare Technology",
            currency_of_reporting="USD",
            fiscal_year_end_date="2024-09-30",
            incorporation_date="2012-02-10",
            style_guide_reference="style_guides/novex_reporting_standard_2024.docx",
        ),
        Company_profile(
            company_id="CMP-STR-003",
            legal_entity_name="Stratos Retail Group Corp.",
            legal_address="88 Orchard Road, #15-02, Singapore 238841",
            jurisdiction="Singapore",
            ticker_symbol="SGX:STR",
            stock_exchange="SGX",
            industry="Consumer Retail",
            currency_of_reporting="SGD",
            fiscal_year_end_date="2024-03-31",
            incorporation_date="2008-11-05",
            style_guide_reference="style_guides/stratos_group_ifrs_style.xml",
        ),
    ]

    repo.upsert_many(db, companies)
    db.close()

if __name__ == "__main__":
    seed()
