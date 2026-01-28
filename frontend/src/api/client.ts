import type { ApiErrorBody } from "./types";

async function parseApiError(res: Response): Promise<string> {
  try {
    const data = (await res.json()) as ApiErrorBody;
    const msg = data?.error?.message;
    if (msg) return msg;
  } catch {
    // ignore
  }

  try {
    const text = await res.text();
    if (text) return text;
  } catch {
    // ignore
  }

  return `Request failed (${res.status})`;
}

export async function apiRequest<T>(input: RequestInfo, init?: RequestInit): Promise<T> {
  const res = await fetch(input, init);
  if (!res.ok) {
    const msg = await parseApiError(res);
    throw new Error(msg);
  }
  return (await res.json()) as T;
}
