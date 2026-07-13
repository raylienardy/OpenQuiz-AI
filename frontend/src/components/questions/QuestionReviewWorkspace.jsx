import { useState, useMemo, useCallback } from "react";
import QuestionSearch from "./QuestionSearch";
import QuestionFilter from "./QuestionFilter";
import QuestionSort from "./QuestionSort";
import QuestionPagination from "./QuestionPagination";
import QuestionList from "./QuestionList";
import QuestionEmpty from "./QuestionEmpty";
import QuestionToolbar from "./QuestionToolbar";

const DIFFICULTY_ORDER = { easy: 1, medium: 2, hard: 3 };

export default function QuestionReviewWorkspace({ questions, onRegenerate }) {
  const [searchTerm, setSearchTerm] = useState("");
  const [filterType, setFilterType] = useState("");
  const [sortOption, setSortOption] = useState("default");
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);

  // Dapatkan tipe unik dari data untuk filter
  const types = useMemo(() => {
    if (!questions) return [];
    const uniqueTypes = [...new Set(questions.map((q) => q.type))];
    return uniqueTypes;
  }, [questions]);

  // Filter
  const filteredQuestions = useMemo(() => {
    if (!questions) return [];
    let result = [...questions];
    // Search
    if (searchTerm.trim() !== "") {
      const term = searchTerm.toLowerCase();
      result = result.filter(
        (q) =>
          q.question.toLowerCase().includes(term) ||
          (q.explanation && q.explanation.toLowerCase().includes(term)) ||
          (q.answer && q.answer.toLowerCase().includes(term)) ||
          q.type.toLowerCase().includes(term),
      );
    }
    // Filter by type
    if (filterType) {
      result = result.filter((q) => q.type === filterType);
    }
    return result;
  }, [questions, searchTerm, filterType]);

  // Sort
  const sortedQuestions = useMemo(() => {
    const arr = [...filteredQuestions];
    if (sortOption === "question_asc") {
      arr.sort((a, b) => a.question.localeCompare(b.question));
    } else if (sortOption === "question_desc") {
      arr.sort((a, b) => b.question.localeCompare(a.question));
    } else if (sortOption === "type_asc") {
      arr.sort((a, b) => a.type.localeCompare(b.type));
    } else if (sortOption === "type_desc") {
      arr.sort((a, b) => b.type.localeCompare(a.type));
    } else if (sortOption === "difficulty_asc") {
      arr.sort(
        (a, b) =>
          (DIFFICULTY_ORDER[a.difficulty] || 0) -
          (DIFFICULTY_ORDER[b.difficulty] || 0),
      );
    } else if (sortOption === "difficulty_desc") {
      arr.sort(
        (a, b) =>
          (DIFFICULTY_ORDER[b.difficulty] || 0) -
          (DIFFICULTY_ORDER[a.difficulty] || 0),
      );
    }
    // default: keep original order
    return arr;
  }, [filteredQuestions, sortOption]);

  // Pagination
  const totalPages = Math.ceil(sortedQuestions.length / pageSize);
  const visibleQuestions = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return sortedQuestions.slice(start, start + pageSize);
  }, [sortedQuestions, currentPage, pageSize]);

  // Reset page saat filter/search berubah
  const handleSearchChange = useCallback((val) => {
    setSearchTerm(val);
    setCurrentPage(1);
  }, []);
  const handleFilterChange = useCallback((val) => {
    setFilterType(val);
    setCurrentPage(1);
  }, []);
  const handleSortChange = useCallback((val) => {
    setSortOption(val);
    setCurrentPage(1);
  }, []);

  return (
    <div className="question-review-workspace">
      <div className="workspace-toolbar">
        <div className="workspace-controls">
          <QuestionSearch value={searchTerm} onChange={handleSearchChange} />
          <QuestionFilter
            value={filterType}
            onChange={handleFilterChange}
            types={types}
          />
          <QuestionSort value={sortOption} onChange={handleSortChange} />
        </div>
        <QuestionToolbar questions={questions} onRegenerate={onRegenerate} />
      </div>

      {visibleQuestions.length > 0 ? (
        <>
          <QuestionList questions={visibleQuestions} />
          <QuestionPagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={setCurrentPage}
            pageSize={pageSize}
            onPageSizeChange={(size) => {
              setPageSize(size);
              setCurrentPage(1);
            }}
          />
        </>
      ) : (
        <QuestionEmpty />
      )}
    </div>
  );
}
