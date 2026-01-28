export type CompanyProfile = {
    company_id: string;
    legal_entity_name: string;
    legal_address: string;
    jurisdiction: string;
    ticker_symbol?: string | null;
    stock_exchange?: string | null;
    industry?: string | null;
    currency_of_reporting: string;
    fiscal_year_end_date: string; // "YYYY-MM-DD"
    incorporation_date: string;   // "YYYY-MM-DD"
    style_guide_reference?: string | null;
  };
  
  export type CompanyListItem = Pick<CompanyProfile, "company_id" | "legal_entity_name">;
  
  export type Period = "Q1" | "Q2" | "Q3" | "Annual";
  
  export type OutputRequest = {
    company_id: string;
    period: Period;
  };
  
  export type OutputResponse = CompanyProfile & {
    report_type: string;             // "Annual" | "Interim"
    reporting_period_end: string;    // "June 30, 2024"
    year_end: string;                // "December 31"
    quarter?: string | null;         // "Q1" | "Q2" | "Q3" | null
  };
  
  export type ApiErrorBody = {
    error?: {
      code?: string;
      message?: string;
    };
  };
