import FileDropzone from "./FileDropzone";
import SelectedFile from "./SelectedFile";
import LoadingSpinner from "./feedback/LoadingSpinner";
import ProgressBar from "./feedback/ProgressBar";
import UploadResult from "./feedback/UploadResult";
import UploadError from "./feedback/UploadError";

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

  return (
    <div className="upload-card">
      {/* Idle: dropzone */}
      {!file && isIdle && <FileDropzone onFileSelect={onFileSelect} />}

      {/* File selected, not success yet (idle, uploading, error) */}
      {file && !isSuccess && (
        <>
          <SelectedFile file={file} onRemove={isUploading ? null : onRemove} />
          {/* Validasi */}
          {isIdle && validationError && (
            <div className="validation-message error">
              <span className="validation-icon">⚠️</span>
              <p>{validationError}</p>
            </div>
          )}
          {isIdle && !validationError && (
            <div className="validation-message success">
              <span className="validation-icon">✅</span>
              <p>Ready to upload</p>
            </div>
          )}
        </>
      )}

      {/* Uploading state */}
      {isUploading && (
        <div className="upload-feedback">
          <LoadingSpinner size={36} />
          <ProgressBar indeterminate />
          <p className="uploading-text">Uploading... Please wait.</p>
        </div>
      )}

      {/* Success */}
      {isSuccess && uploadResult && (
        <UploadResult fileInfo={uploadResult} onReset={onReset} />
      )}

      {/* Error */}
      {isError && (
        <UploadError
          message={uploadError || "An unexpected error occurred."}
          onRetry={file ? onUpload : null}
        />
      )}

      {/* Tombol Upload (idle, file valid) */}
      {file && isIdle && !validationError && (
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
