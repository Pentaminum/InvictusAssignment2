import type { OutputResponse } from "../api/types";
import { downloadJson } from "../utils/download";

type Props = {
  output: OutputResponse;
};

function safeFilenamePart(s: string) {
  return s.replace(/[^a-zA-Z0-9_-]+/g, "_").slice(0, 60);
}

export default function OutputPreview({ output }: Props) {
  const filename = `output_${safeFilenamePart(output.company_id)}_${safeFilenamePart(
    output.report_type
  )}_${safeFilenamePart(output.quarter ?? "Annual")}.json`;

  return (
    <div className="output">
      <div className="outputHeader">
        <div className="outputTitle">Output Preview</div>

        {/* this component renders only if output was successfully generated*/}
        <button
          className="button"
          onClick={() => downloadJson(filename, output)}
          style={{ marginLeft: "auto" }}
        >
          Download JSON
        </button>
      </div>

      <pre className="outputPre">{JSON.stringify(output, null, 2)}</pre>
    </div>
  );
}
