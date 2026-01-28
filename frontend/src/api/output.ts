import { apiRequest } from "./client";
import type { OutputRequest, OutputResponse } from "./types";

export function generateOutput(apiBase: string, payload: OutputRequest) {
  return apiRequest<OutputResponse>(`${apiBase}/api/output/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}
