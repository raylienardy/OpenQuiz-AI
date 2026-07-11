function Home() {
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
          <div className="card-indicator yellow"></div>
          <div className="card-content">
            <h2>Backend Status</h2>
            <p>Checking connection...</p>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Home;
