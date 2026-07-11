import { useHealthCheck } from "../hooks/useHealthCheck";

function Home() {
  const { isLoading, isConnected, status, message } = useHealthCheck();

  return (
    <main className="container">
      <div className="hero">
        <h1 className="title">OpenQuiz AI</h1>
        <p className="subtitle">
          AI-powered question generation from your learning materials.
        </p>
      </div>

      <div className="status-grid">
        <div className="card">
          <div className="card-indicator green"></div>
          <div className="card-content">
            <h2>System Ready</h2>
            <p>The frontend is loaded and ready.</p>
          </div>
        </div>

        <div className="card">
          <div
            className="card-indicator"
            style={{
              backgroundColor: isLoading
                ? "#ffc107"
                : isConnected
                  ? "#198754"
                  : "#dc3545",
            }}
          ></div>
          <div className="card-content">
            <h2>Backend Status</h2>
            {isLoading && <p>Checking backend...</p>}
            {!isLoading && isConnected && (
              <>
                <p>🟢 Backend Connected</p>
                <p className="detail">Status: {status}</p>
                <p className="detail">Message: {message}</p>
              </>
            )}
            {!isLoading && !isConnected && (
              <>
                <p>🔴 Backend Offline</p>
                <p className="detail">Unable to connect to backend.</p>
              </>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}

export default Home;
