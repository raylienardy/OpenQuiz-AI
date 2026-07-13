export default function QuestionCard({ question, index }) {
  return (
    <div className="question-card">
      <div className="question-header">
        <span className="question-number">Question {index + 1}</span>
        <span className="question-type-badge">{question.type}</span>
      </div>
      <p className="question-text">{question.question}</p>

      {question.type === "multiple_choice" && question.choices && (
        <div className="choices-list">
          {question.choices.map((choice, i) => (
            <div
              key={i}
              className={`choice-item ${choice.label === question.answer ? "correct" : ""}`}
            >
              <span className="choice-label">{choice.label}.</span>
              <span className="choice-text">{choice.text}</span>
            </div>
          ))}
        </div>
      )}

      {question.type === "true_false" && (
        <div className="choices-list">
          <div
            className={`choice-item ${question.answer?.toUpperCase() === "TRUE" ? "correct" : ""}`}
          >
            True
          </div>
          <div
            className={`choice-item ${question.answer?.toUpperCase() === "FALSE" ? "correct" : ""}`}
          >
            False
          </div>
        </div>
      )}

      <div className="answer-section">
        <strong>Answer:</strong> {question.answer}
      </div>

      {question.explanation && (
        <div className="explanation-section">
          <strong>Explanation:</strong> {question.explanation}
        </div>
      )}
    </div>
  );
}
