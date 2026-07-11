import FileDropzone from "./FileDropzone";
import SelectedFile from "./SelectedFile";

export default function UploadCard({
  file,
  onFileSelect,
  onRemove,
  onUpload,
  uploadState,
  uploadResult,
  uploadError,
  validationError,
  onReset,
}) {
  const isIdle = uploadState === "idle";
  const isUploading = uploadState === "uploading";
  const isSuccess = uploadState === "success";
  const isError = uploadState === "error";

  const isFileValid = file && !validationError;

  return (
    <div className="upload-card">
      {/* Tampilan dropzone saat belum ada file */}
      {!file && isIdle && <FileDropzone onFileSelect={onFileSelect} />}

      {/* Tampilan file terpilih + status validasi saat idle, uploading, error (kecuali success) */}
      {file && !isSuccess && (
        <>
          <SelectedFile file={file} onRemove={!isUploading ? onRemove : null} />
          {isIdle && validationError && (
            <div className="validation-message error">
              <span className="validation-icon">⚠️</span>
              <p>{validationError}</p>
            </div>
          )}
          {isIdle && isFileValid && (
            <div className="validation-message success">
              <span className="validation-icon">✅</span>
              <p>Ready to upload</p>
            </div>
          )}
        </>
      )}

      {/* Loading spinner */}
      {isUploading && (
        <div className="upload-status">
          <div className="spinner"></div>
          <p>Uploading... Please wait.</p>
        </div>
      )}

      {/* Success */}
      {isSuccess && uploadResult && (
        <div className="upload-status success">
          <span className="status-icon">✅</span>
          <h3>Upload Successful</h3>
          <div className="result-details">
            <p>
              <strong>Filename:</strong> {uploadResult.filename}
            </p>
            <p>
              <strong>Size:</strong>{" "}
              {(uploadResult.size / (1024 * 1024)).toFixed(2)} MB
            </p>
            <p>
              <strong>Type:</strong> {uploadResult.content_type}
            </p>
          </div>
          <button className="reset-btn" onClick={onReset}>
            Upload Another File
          </button>
        </div>
      )}

      {/* Error (dari backend/network) */}
      {isError && (
        <div className="upload-status error">
          <span className="status-icon">❌</span>
          <h3>Upload Failed</h3>
          <p className="error-message">{uploadError}</p>
          {file && (
            <button className="retry-btn" onClick={onUpload}>
              Try Again
            </button>
          )}
        </div>
      )}

      {/* Tombol Upload hanya jika idle, file valid, dan tidak ada error validasi */}
      {file && isIdle && isFileValid && (
        <>
          <button className="upload-btn active" onClick={onUpload}>
            Upload
          </button>
          <p className="upload-hint">Click to upload the selected file.</p>
        </>
      )}
    </div>
  );
}
