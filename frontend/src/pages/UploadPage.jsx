import { useState } from "react";
import UploadCard from "../components/UploadCard";
import QuestionReviewWorkspace from "../components/questions/QuestionReviewWorkspace"; // ganti
import { uploadFile } from "../services/uploadService";
import { generateQuestions } from "../services/questionService";
import { validateFile } from "../utils/validateFile";
import "./UploadPage.css";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadState, setUploadState] = useState("idle");
  const [uploadResult, setUploadResult] = useState(null);
  const [uploadError, setUploadError] = useState("");
  const [validationError, setValidationError] = useState(null);
  const [generationState, setGenerationState] = useState("idle");
  const [generatedQuestions, setGeneratedQuestions] = useState(null);
  const [generationError, setGenerationError] = useState("");

  const handleFileSelect = (file) => {
    const error = validateFile(file);
    setSelectedFile(file);
    setValidationError(error);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    resetGeneration();
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    resetGeneration();
  };

  const resetGeneration = () => {
    setGenerationState("idle");
    setGeneratedQuestions(null);
    setGenerationError("");
  };

  const handleUpload = async () => {
    if (!selectedFile || validationError) return;
    setUploadState("uploading");
    setUploadError("");
    setUploadResult(null);
    resetGeneration();

    try {
      const data = await uploadFile(selectedFile);
      setUploadState("success");
      setUploadResult(data.data);
    } catch (error) {
      setUploadState("error");
      if (error.response) {
        setUploadError(
          error.response.data?.detail || "Upload failed due to server error.",
        );
      } else if (error.request) {
        setUploadError(
          "Unable to reach the server. Please check your connection.",
        );
      } else {
        setUploadError("An unexpected error occurred.");
      }
    }
  };

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
      const data = await generateQuestions(payload);
      // data.data.questions adalah array pertanyaan yang sudah divalidasi
      setGenerationState("success");
      setGeneratedQuestions(data.data.questions);
    } catch (error) {
      setGenerationState("error");
      setGenerationError(
        error.response?.data?.detail ||
          "Failed to generate questions. Please try again.",
      );
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    resetGeneration();
  };

  return (
    <div className="upload-page-container">
      <div className="upload-header">
        <h1>Upload Learning Material</h1>
        <p>
          Upload your PDF, DOCX, or TXT file to generate AI-powered questions.
        </p>
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
            <QuestionReviewWorkspace
              questions={generatedQuestions}
              onRegenerate={handleGenerate}
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
