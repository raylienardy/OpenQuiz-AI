import { useState } from "react";
import UploadCard from "../components/UploadCard";
import { uploadFile } from "../services/uploadService";
import { generateQuestions } from "../services/questionService";
import { validateFile } from "../utils/validateFile";
import "./UploadPage.css";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadState, setUploadState] = useState("idle"); // idle | uploading | success | error
  const [uploadResult, setUploadResult] = useState(null);
  const [uploadError, setUploadError] = useState("");
  const [validationError, setValidationError] = useState(null);
  const [generationState, setGenerationState] = useState("idle"); // idle | generating | success | error
  const [generatedText, setGeneratedText] = useState("");

  const handleFileSelect = (file) => {
    const error = validateFile(file);
    setSelectedFile(file);
    setValidationError(error);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    setGenerationState("idle");
    setGeneratedText("");
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    setGenerationState("idle");
    setGeneratedText("");
  };

  const handleUpload = async () => {
    if (!selectedFile || validationError) return;
    setUploadState("uploading");
    setUploadError("");
    setUploadResult(null);
    setGenerationState("idle");
    setGeneratedText("");

    try {
      const data = await uploadFile(selectedFile);
      setUploadState("success");
      setUploadResult(data.data); // data.data berisi text, filename, dll.
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
    try {
      const payload = {
        text: uploadResult.text,
        question_type: "multiple_choice", // default, bisa dibuat pilihan nanti
        number_of_questions: 5,
        difficulty: "medium",
        language: "id",
      };
      const data = await generateQuestions(payload);
      setGenerationState("success");
      setGeneratedText(data.raw_response);
    } catch (error) {
      setGenerationState("error");
      setGeneratedText(error.response?.data?.detail || "Generation failed.");
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
    setGenerationState("idle");
    setGeneratedText("");
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

      {/* Tombol Generate tampil setelah upload sukses dan teks tersedia */}
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
            <div className="loading-spinner">⏳ Generating questions...</div>
          )}
          {generationState === "success" && (
            <div className="generated-content">
              <h3>Generated Output (Raw)</h3>
              <pre className="raw-response">{generatedText}</pre>
            </div>
          )}
          {generationState === "error" && (
            <div className="error-message">❌ {generatedText}</div>
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
