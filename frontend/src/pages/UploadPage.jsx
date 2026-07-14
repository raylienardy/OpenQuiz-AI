import { useState, useEffect, useMemo } from "react";
import UploadCard from "../components/UploadCard";
import QuestionReviewWorkspace from "../components/questions/QuestionReviewWorkspace";
import QuestionAnalyticsPanel from "../components/questions/QuestionAnalyticsPanel";
import AIMetadataPanel from "../components/questions/AIMetadataPanel";
import AIPipelineInspector from "../components/debug/AIPipelineInspector";
import DeveloperToolbar from "../components/debug/DeveloperToolbar";
import LoadingMessage from "../components/feedback/LoadingMessage";
import RetryCard from "../components/feedback/RetryCard";
import EmptyState from "../components/feedback/EmptyState";
import SuccessState from "../components/feedback/SuccessState";
import { uploadFile } from "../services/uploadService";
import { generateQuestions } from "../services/questionService";
import { validateFile } from "../utils/validateFile";
import "./UploadPage.css";
import { createSession } from "../session/generationSession";
import ExportPreview from "../components/export/ExportPreview";
import GenerationSessionPanel from "../components/session/GenerationSessionPanel";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadState, setUploadState] = useState("idle");
  const [uploadResult, setUploadResult] = useState(null);
  const [uploadError, setUploadError] = useState(null);
  const [validationError, setValidationError] = useState(null);
  const [generationState, setGenerationState] = useState("idle");
  const [generatedQuestions, setGeneratedQuestions] = useState(null);
  const [generationMeta, setGenerationMeta] = useState(null);
  const [debugData, setDebugData] = useState(null);
  const [devMode, setDevMode] = useState(
    () => localStorage.getItem("devMode") === "true",
  );
  // state tambahan
  const [showExportPreview, setShowExportPreview] = useState(false);
  const [exportPreviewData, setExportPreviewData] = useState(null);

  // fungsi untuk mengambil preview
  const handlePreviewExport = async (format = "pdf") => {
    if (!generatedQuestions) return;
    try {
      const response = await fetch("http://localhost:8000/export/preview", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          questions: generatedQuestions,
          format: format,
          metadata: generationMeta,
        }),
      });
      const preview = await response.json();
      setExportPreviewData(preview);
      setShowExportPreview(true);
    } catch (error) {
      console.error("Failed to load preview:", error);
    }
  };

  const handleDownload = async () => {
    window.open(`/api/export/download?format=pdf&...`, "_blank");
  };

  // Bentuk session object secara memoized dari metadata dan questions
  const generationSession = useMemo(() => {
    if (generationState !== "success" || !generationMeta || !generatedQuestions)
      return null;
    return createSession({
      provider: generationMeta.provider,
      model: generationMeta.model,
      generationTime: generationMeta.latency_seconds,
      questionCount: generatedQuestions.length,
      language: "id", // bisa dari state, untuk sementara hardcode
      difficulty: "medium",
      questionType: "multiple_choice",
      promptVersion: generationMeta.prompt_version,
      schemaVersion: generationMeta.schema_version,
      status: "completed",
    });
  }, [generationState, generationMeta, generatedQuestions]);

  useEffect(() => {
    localStorage.setItem("devMode", devMode);
  }, [devMode]);

  const handleFileSelect = (file) => {
    const error = validateFile(file);
    setSelectedFile(file);
    setValidationError(error);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError(null);
    resetGeneration();
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError(null);
    resetGeneration();
  };

  const resetGeneration = () => {
    setGenerationState("idle");
    setGeneratedQuestions(null);
    setGenerationMeta(null);
    setDebugData(null);
  };

  const handleUpload = async () => {
    if (!selectedFile || validationError) return;
    setUploadState("uploading");
    setUploadError(null);
    setUploadResult(null);
    resetGeneration();

    try {
      const data = await uploadFile(selectedFile);
      setUploadState("success");
      setUploadResult(data.data);
    } catch (error) {
      setUploadState("error");
      setUploadError(error);
    }
  };

  const handleGenerate = async () => {
    if (!uploadResult || !uploadResult.text) return;
    setGenerationState("generating");
    setUploadError(null);
    try {
      const payload = {
        text: uploadResult.text,
        question_type: "multiple_choice",
        number_of_questions: 5,
        difficulty: "medium",
        language: "id",
      };
      const response = await generateQuestions(payload, devMode);
      setGenerationState("success");
      setGeneratedQuestions(response.data.questions);
      setGenerationMeta(response.metadata);
      setDebugData(response.debug || null);
    } catch (error) {
      setGenerationState("error");
      setUploadError(error); // kita gunakan RetryCard untuk menampilkan
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError(null);
    resetGeneration();
  };

  return (
    <div className="upload-page-container">
      <div className="upload-header">
        <h1>Upload Learning Material</h1>
        <p>
          Upload your PDF, DOCX, or TXT file to generate AI-powered questions.
        </p>
        <DeveloperToolbar devMode={devMode} onToggle={setDevMode} />
      </div>

      <div className="upload-section">
        <UploadCard
          file={selectedFile}
          onFileSelect={handleFileSelect}
          onRemove={handleRemoveFile}
          onUpload={handleUpload}
          uploadState={uploadState}
          uploadResult={uploadResult}
          uploadError={uploadError}
          validationError={validationError}
          onReset={handleReset}
        />
      </div>

      {/* Status upload */}
      {uploadState === "uploading" && <LoadingMessage stage="upload" />}
      {uploadState === "error" && (
        <RetryCard error={uploadError} onRetry={handleUpload} />
      )}

      {/* Tombol generate dan status generasi */}
      {uploadState === "success" && uploadResult && uploadResult.text && (
        <div className="generation-section">
          <button
            className="generate-btn"
            onClick={handleGenerate}
            disabled={generationState === "generating"}
          >
            {generationState === "generating"
              ? "Generating..."
              : "Generate Questions"}
          </button>

          {generationState === "generating" && (
            <LoadingMessage stage="generating" />
          )}
          {generationState === "error" && (
            <RetryCard error={uploadError} onRetry={handleGenerate} />
          )}

          {generationState === "success" && generatedQuestions && (
            <>
              <SuccessState message="Questions generated successfully!" />

              {/* Session Panel */}
              <GenerationSessionPanel session={generationSession} />

              <AIPipelineInspector debugData={debugData} isOpen={devMode} />
              <QuestionAnalyticsPanel
                questions={generatedQuestions}
                provider={generationMeta?.provider}
                model={generationMeta?.model}
              />
              <AIMetadataPanel metadata={generationMeta} />
              <QuestionReviewWorkspace
                questions={generatedQuestions}
                onRegenerate={handleGenerate}
              />
              {/* TOMBOL EXPORT PDF & MODAL PREVIEW */}
              <div style={{ marginTop: "1rem" }}>
                <button onClick={() => handlePreviewExport("pdf")}>
                  📄 Export PDF
                </button>
              </div>

              {showExportPreview && exportPreviewData && (
                <div
                  className="modal-overlay"
                  onClick={() => setShowExportPreview(false)}
                >
                  <div
                    className="modal-content"
                    onClick={(e) => e.stopPropagation()}
                  >
                    <ExportPreview
                      previewData={exportPreviewData}
                      onDownload={handleDownload}
                    />
                    <button onClick={() => setShowExportPreview(false)}>
                      Close
                    </button>
                  </div>
                </div>
              )}
            </>
          )}

          {generationState === "idle" && !generatedQuestions && (
            <EmptyState
              title="Ready to generate"
              description="Click the button above to create AI-powered questions."
            />
          )}
        </div>
      )}

      <div className="supported-info">
        <p>
          Supported formats: <strong>PDF</strong>, <strong>DOCX</strong>,{" "}
          <strong>TXT</strong>
        </p>
        <p>
          Maximum file size: <strong>20 MB</strong>
        </p>
      </div>
    </div>
  );
}
