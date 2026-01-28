import { useEffect, useMemo, useState } from "react";
import "./App.css";

import type { CompanyListItem, Period, OutputResponse } from "./api/types";
import { listCompanies } from "./api/companies";
import { generateOutput } from "./api/output";

import ErrorBanner from "./components/ErrorBanner";
import OutputPreview from "./components/OutputPreview";

const API_BASE = "http://localhost:8000";

export default function App() {
  const periods = useMemo(() => ["Q1", "Q2", "Q3", "Annual"] as const, []);

  const [companies, setCompanies] = useState<CompanyListItem[]>([]);
  const [companyId, setCompanyId] = useState<string>("");
  const [period, setPeriod] = useState<Period>("Q1");

  const [isLoadingCompanies, setIsLoadingCompanies] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string>("");

  const [output, setOutput] = useState<OutputResponse | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function loadCompanies() {
      setIsLoadingCompanies(true);
      setError("");

      try {
        const data = await listCompanies(API_BASE);
        if (cancelled) return;

        setCompanies(data);
        setCompanyId(data.length > 0 ? data[0].company_id : "");
      } catch (e: any) {
        if (!cancelled) setError(e?.message ?? "Failed to load companies.");
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
      const data = await generateOutput(API_BASE, { company_id: companyId, period });
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

          {error && <ErrorBanner message={error} />}

          <div className="actions">
            <button
              className="button"
              onClick={onGenerate}
              disabled={isGenerating || isLoadingCompanies || !companyId}
            >
              {isGenerating ? "Generating..." : "Generate output"}
            </button>
          </div>

          {output && <OutputPreview output={output} />}
        </main>
      </div>
    </div>
  );
}
