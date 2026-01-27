from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Company_profile(Base):
    __tablename__ = "company_profile"

    company_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    legal_entity_name: Mapped[str] = mapped_column(String, nullable=False) #full company name
    legal_address: Mapped[str] = mapped_column(String, nullable=False) #address
    jurisdiction: Mapped[str] = mapped_column(String, nullable=False) #country/region of registration
    ticker_symbol: Mapped[str] = mapped_column(String, nullable=True) #e.g. TSX:ABC
    stock_exchange: Mapped[str] = mapped_column(String, nullable=True) #e.g. TSX, NASDAQ
    industry: Mapped[str] = mapped_column(String, nullable=True) #e.g. Mining Technology & Services, Healthcare Technology, Consumer Retail
    currency_of_reporting: Mapped[str] = mapped_column(String, nullable=False) #e.g. CAD, USD
    fiscal_year_end_date: Mapped[str] = mapped_column(String, nullable=False) #stored as ISO date (YYYY-MM-DD)
    incorporation_date: Mapped[str] = mapped_column(String, nullable=False) #stored as ISO date (YYYY-MM-DD)
    style_guide_reference: Mapped[str] = mapped_column(String, nullable=True) #links to another table or file
