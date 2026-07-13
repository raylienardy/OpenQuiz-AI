export default function QuestionCard({
  question,
  index,
  isSelected,
  onSelect,
}) {
  return (
    <div
      className={`question-card ${isSelected ? "selected" : ""}`}
      onClick={() => onSelect(question, index)}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "Enter") onSelect(question, index);
      }}
    >
      <div className="question-header">
        <span className="question-number">Q{index + 1}</span>
        <span className="question-type-badge">
          {question.type.replace("_", " ")}
        </span>
        {question.difficulty && (
          <span className="question-difficulty">{question.difficulty}</span>
        )}
      </div>
      <p className="question-text">
        {question.question.substring(0, 100)}
        {question.question.length > 100 ? "..." : ""}
      </p>
      <div className="question-answer-indicator">Answer: {question.answer}</div>
    </div>
  );
}
