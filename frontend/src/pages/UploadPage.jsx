import { useState } from "react";
import UploadCard from "../components/UploadCard";
import QuestionReviewWorkspace from "../components/questions/QuestionReviewWorkspace"; // ganti
import { uploadFile } from "../services/uploadService";
import { generateQuestions } from "../services/questionService";
import { validateFile } from "../utils/validateFile";
import "./UploadPage.css";
import QuestionAnalyticsPanel from "../components/questions/QuestionAnalyticsPanel";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadState, setUploadState] = useState("idle");
  const [uploadResult, setUploadResult] = useState(null);
  const [uploadError, setUploadError] = useState("");
  const [validationError, setValidationError] = useState(null);
  const [generationState, setGenerationState] = useState("idle");
  const [generatedQuestions, setGeneratedQuestions] = useState(null);
  const [generationError, setGenerationError] = useState("");
  const [generationMeta, setGenerationMeta] = useState(null);
  const [devMode, setDevMode] = useState(
    () => localStorage.getItem("devMode") === "true",
  );
  const [debugData, setDebugData] = useState(null);

  useEffect(() => {
    localStorage.setItem("devMode", devMode);
  }, [devMode]);

  const handleGenerate = async () => {
    if (!uploadResult || !uploadResult.text) return;
    setGenerationState("generating");
    setGenerationError("");
    try {
      const payload = {
        text: uploadResult.text,
        question_type: "multiple_choice",
        number_of_questions: 5,
        difficulty: "medium",
        language: "id",
      };
      // Tambahkan debug param jika devMode
      const response = await generateQuestions(payload, devMode);
      setGenerationState("success");
      setGeneratedQuestions(response.data.questions);
      setGenerationMeta(response.metadata);
      setDebugData(response.debug || null);
    } catch (error) {
      setGenerationState("error");
      const msg = error.response?.data?.detail || "Generation failed.";
      setGenerationError(msg);
      setDebugData(error.response?.data?.debug || null); // debug info mungkin ada di error response
    }
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

          {generationState === "generating" && <QuestionLoading />}
          {generationState === "error" && (
            <div className="error-message">❌ {generationError}</div>
          )}

          {generationState === "success" && generatedQuestions && (
            <>
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
            </>
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
