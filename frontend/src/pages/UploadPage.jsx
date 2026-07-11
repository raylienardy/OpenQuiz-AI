import { useState } from "react";
import UploadCard from "../components/UploadCard";
import "./UploadPage.css";

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileSelect = (file) => {
    setSelectedFile(file);
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
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
        />
      </div>

      <div className="supported-info">
        <p>
          Supported formats: <strong>PDF</strong>, <strong>DOCX</strong>,{" "}
          <strong>TXT</strong>
        </p>
        <p>
          Maximum file size: <strong>10 MB</strong>
        </p>
      </div>
    </div>
  );
}
