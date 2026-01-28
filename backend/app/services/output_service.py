import calendar
from datetime import date
from sqlalchemy.orm import Session

from app.repositories.company_repo import CompanyRepository
from app.schemas.company_profile import CompanyProfileRead
from app.schemas.output import Period, OutputResponse
from app.core.errors import NotFoundError

class OutputService:
    def __init__(self, repo: CompanyRepository):
            self.repo = repo

    def add_months(self, dt: date, months: int) -> date:
        # months can be negative
        y = dt.year + (dt.month - 1 + months) // 12
        m = (dt.month - 1 + months) % 12 + 1
        last_day = calendar.monthrange(y, m)[1]
        d = min(dt.day, last_day)
        return date(y, m, d)


    def build_output(self, db: Session, company_id: str, period: Period) -> OutputResponse:
        company = self.repo.get(db, company_id)
        if not company:
            raise NotFoundError(f"Company '{company_id}' not found")

        # 1) ORM -> Pydantic
        company_read = CompanyProfileRead.model_validate(company)

        # 2) parse ISO to date
        fy_end = date.fromisoformat(company_read.fiscal_year_end_date)

        # 3) report_type / quarter / reporting_period_end calculation
        if period == Period.ANNUAL:
            report_type = "Annual"
            quarter = None
            reporting_period_end = fy_end
        else:
            report_type = "Interim"
            quarter = period.value
            months_back = {"Q1": -9, "Q2": -6, "Q3": -3}[quarter]
            reporting_period_end = self.add_months(fy_end, months_back)

        # 4) output format
        year_end_str = fy_end.strftime("%B %d").replace(" 0", " ")
        reporting_end_str = reporting_period_end.strftime("%B %d, %Y").replace(" 0", " ")

        # 5) add new fields
        return OutputResponse(
            **company_read.model_dump(),
            report_type=report_type,
            quarter=quarter,
            year_end=year_end_str,
            reporting_period_end=reporting_end_str,
        )
