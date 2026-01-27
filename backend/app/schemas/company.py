from pydantic import BaseModel, Field

class CompanyProfileBase(BaseModel):
    company_id: str = Field(min_length=1)
    legal_entity_name: str
    legal_address: str
    jurisdiction: str
    ticker_symbol: str | None = None
    stock_exchange: str | None = None
    industry: str | None = None
    currency_of_reporting: str = Field(min_length=3, max_length=3)
    fiscal_year_end_date: str = Field(
        pattern=r"\d{4}-\d{2}-\d{2}",
        description="YYYY-MM-DD"
    )
    incorporation_date: str = Field(
        pattern=r"\d{4}-\d{2}-\d{2}",
        description="YYYY-MM-DD"
    )
    style_guide_reference: str | None = None


class CompanyProfileRead(CompanyProfileBase):
    class Config:
        from_attributes = True
