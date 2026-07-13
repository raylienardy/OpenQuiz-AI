import { useState } from "react";

export default function QuestionToolbar({ questions, onRegenerate }) {
  const [copyJsonFeedback, setCopyJsonFeedback] = useState(false);
  const [copyTextFeedback, setCopyTextFeedback] = useState(false);

  const handleCopyJson = async () => {
    const json = JSON.stringify({ questions }, null, 2);
    try {
      await navigator.clipboard.writeText(json);
      setCopyJsonFeedback(true);
      setTimeout(() => setCopyJsonFeedback(false), 2000);
    } catch {
      // fallback
      const textarea = document.createElement("textarea");
      textarea.value = json;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      setCopyJsonFeedback(true);
      setTimeout(() => setCopyJsonFeedback(false), 2000);
    }
  };

  const handleCopyText = async () => {
    let text = "";
    questions.forEach((q, idx) => {
      text += `Question ${idx + 1}\n${q.question}\n`;
      if (q.choices) {
        q.choices.forEach((c) => {
          text += `${c.label}. ${c.text}\n`;
        });
      }
      text += `Answer: ${q.answer}\n`;
      if (q.explanation) text += `Explanation: ${q.explanation}\n`;
      text += "\n";
    });
    try {
      await navigator.clipboard.writeText(text);
      setCopyTextFeedback(true);
      setTimeout(() => setCopyTextFeedback(false), 2000);
    } catch {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      setCopyTextFeedback(true);
      setTimeout(() => setCopyTextFeedback(false), 2000);
    }
  };

  const handleDownloadJson = () => {
    const json = JSON.stringify({ questions }, null, 2);
    const blob = new Blob([json], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "questions.json";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="question-toolbar">
      <button onClick={onRegenerate} className="toolbar-btn">
        🔄 Regenerate
      </button>
      <button onClick={handleCopyJson} className="toolbar-btn">
        {copyJsonFeedback ? "✅ Copied JSON" : "📋 Copy JSON"}
      </button>
      <button onClick={handleCopyText} className="toolbar-btn">
        {copyTextFeedback ? "✅ Copied Text" : "📝 Copy Questions"}
      </button>
      <button onClick={handleDownloadJson} className="toolbar-btn">
        💾 Download JSON
      </button>
    </div>
  );
}
