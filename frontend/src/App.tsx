import { useEffect, useMemo, useState } from "react";
import "./App.css";

type Company = {
  company_id: string;
  legal_entity_name: string;
};

type Period = "Q1" | "Q2" | "Q3" | "Annual";

const API_BASE = "http://localhost:8000";

export default function App() {
  const periods = useMemo(() => ["Q1", "Q2", "Q3", "Annual"] as const, []);

  const [companies, setCompanies] = useState<Company[]>([]);
  const [companyId, setCompanyId] = useState<string>("");
  const [period, setPeriod] = useState<Period>("Q1");

  const [isLoadingCompanies, setIsLoadingCompanies] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string>("");

  const [output, setOutput] = useState<any>(null);

  useEffect(() => {
    let cancelled = false;

    async function loadCompanies() {
      setIsLoadingCompanies(true);
      setError("");

      try {
        const res = await fetch(`${API_BASE}/api/companies`);
        if (!res.ok) {
          throw new Error(`GET /api/companies failed (${res.status})`);
        }

        const data: Company[] = await res.json();
        if (cancelled) return;

        setCompanies(data);

        if (data.length > 0) {
          setCompanyId(data[0].company_id);
        } else {
          setCompanyId("");
        }
      } catch (e: any) {
        if (cancelled) return;
        setError(e?.message ?? "Failed to load companies.");
      } finally {
        if (!cancelled) setIsLoadingCompanies(false);
      }
    }

    loadCompanies();
    return () => {
      cancelled = true;
    };
  }, []);

  async function onGenerate() {
    if (!companyId) {
      setError("Please select a company.");
      return;
    }

    setIsGenerating(true);
    setError("");
    setOutput(null);

    try {
      const res = await fetch(`${API_BASE}/api/output/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          company_id: companyId,
          period,
        }),
      });

      if (!res.ok) {
        const text = await res.text().catch(() => "");
        throw new Error(
          `POST /api/output/generate failed (${res.status})${text ? `: ${text}` : ""}`
        );
      }

      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setError(e?.message ?? "Failed to generate output.");
    } finally {
      setIsGenerating(false);
    }
  }

  return (
    <div className="page">
      <div className="shell">
        <header className="header">
          <div className="badge">Assignment 2</div>
          <h1 className="title">Company Profile Manager &amp; Input Validator</h1>
        </header>

        <main className="panel">
          <div className="questionBlock">
            <div className="qTop">
              <div className="qNumber">Question 1</div>
              <div className="qPrompt">Which company are you preparing the report for?</div>
            </div>

            <select
              className="select"
              value={companyId}
              onChange={(e) => setCompanyId(e.target.value)}
              disabled={isLoadingCompanies || companies.length === 0}
            >
              {isLoadingCompanies ? (
                <option value="">Loading companies...</option>
              ) : companies.length === 0 ? (
                <option value="">No companies found</option>
              ) : (
                companies.map((c) => (
                  <option key={c.company_id} value={c.company_id}>
                    {c.legal_entity_name}
                  </option>
                ))
              )}
            </select>
          </div>

          <div className="questionBlock">
            <div className="qTop">
              <div className="qNumber">Question 2</div>
              <div className="qPrompt">What financial period are we reporting?</div>
            </div>

            <select
              className="select"
              value={period}
              onChange={(e) => setPeriod(e.target.value as Period)}
              disabled={isGenerating}
            >
              {periods.map((p) => (
                <option key={p} value={p}>
                  {p}
                </option>
              ))}
            </select>
          </div>

          {error && (
            <div className="error" role="alert">
              <div className="errorTitle">Something went wrong</div>
              <div className="errorMsg">{error}</div>
            </div>
          )}

          <div className="actions">
            <button
              className="button"
              onClick={onGenerate}
              disabled={isGenerating || isLoadingCompanies || !companyId}
            >
              {isGenerating ? "Generating..." : "Generate output"}
            </button>

          </div>

          {output && (
            <div className="output">
              <div className="outputHeader">
                <div className="outputTitle">Output Preview</div>
              </div>
              <pre className="outputPre">{JSON.stringify(output, null, 2)}</pre>
            </div>
          )}
        </main>

      </div>
    </div>
  );
}
