import { useState } from "react";
import UploadCard from "../components/UploadCard";
import { uploadFile } from "../services/uploadService";
import { validateFile } from "../utils/validateFile";
import "./UploadPage.css";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadState, setUploadState] = useState("idle"); // idle | uploading | success | error
  const [uploadResult, setUploadResult] = useState(null);
  const [uploadError, setUploadError] = useState("");
  const [validationError, setValidationError] = useState(null); // client-side validation

  const handleFileSelect = (file) => {
    // Validasi di sisi klien segera setelah file dipilih
    const error = validateFile(file);
    setSelectedFile(file);
    setValidationError(error);

    // Reset upload state ketika file baru dipilih
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
  };

  const handleUpload = async () => {
    // Jangan upload jika validasi gagal (seharusnya tombol sudah disabled, tapi double-check)
    if (!selectedFile || validationError) return;

    setUploadState("uploading");
    setUploadError("");
    setUploadResult(null);

    try {
      const data = await uploadFile(selectedFile);
      setUploadState("success");
      setUploadResult(data.file);
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

  const handleReset = () => {
    setSelectedFile(null);
    setValidationError(null);
    setUploadState("idle");
    setUploadResult(null);
    setUploadError("");
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
