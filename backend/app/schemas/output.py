from enum import Enum
from pydantic import BaseModel, Field
from app.schemas.company_profile import CompanyProfileRead


class Period(str, Enum):
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    ANNUAL = "Annual"


class OutputRequest(BaseModel):
    company_id: str
    period: Period

class OutputResponse(CompanyProfileRead):
    # all fields from CompanyProfileRead + fields below
    report_type: str
    quarter: str | None = None # None if Annual
    year_end: str              # "December 31"
    reporting_period_end: str  # "June 30, 2024"