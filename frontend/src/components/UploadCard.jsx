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
  onReset,
}) {
  const isIdle = uploadState === "idle";
  const isUploading = uploadState === "uploading";
  const isSuccess = uploadState === "success";
  const isError = uploadState === "error";

  return (
    <div className="upload-card">
      {/* Tampilan dropzone atau file terpilih (hanya saat idle atau belum ada file yang dipilih) */}
      {!file && isIdle && <FileDropzone onFileSelect={onFileSelect} />}

      {/* Tampilan file terpilih saat idle, uploading, error (tidak saat success) */}
      {file && !isSuccess && (
        <SelectedFile file={file} onRemove={!isUploading ? onRemove : null} />
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

      {/* Error */}
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

      {/* Tombol Upload (muncul hanya saat idle dengan file terpilih) */}
      {file && isIdle && (
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
