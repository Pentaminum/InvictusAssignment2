import { apiRequest } from "./client";
import type { CompanyListItem } from "./types";

export function listCompanies(apiBase: string) {
  return apiRequest<CompanyListItem[]>(`${apiBase}/api/companies`);
}
