import FileDropzone from "./FileDropzone";
import SelectedFile from "./SelectedFile";

export default function UploadCard({ file, onFileSelect, onRemove }) {
  return (
    <div className="upload-card">
      {!file ? (
        <FileDropzone onFileSelect={onFileSelect} />
      ) : (
        <SelectedFile file={file} onRemove={onRemove} />
      )}

      <button className="upload-btn" disabled>
        Upload
      </button>
      <p className="upload-hint">
        Upload feature will be enabled in the next update.
      </p>
    </div>
  );
}
