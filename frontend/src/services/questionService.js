import api from "./api";

/**
 * Mengirim teks ke backend untuk menghasilkan pertanyaan.
 * @param {object} payload - { text, question_type, number_of_questions, difficulty, language, additional_instruction }
 * @returns {Promise<object>} - response dari backend
 */
export async function generateQuestions(payload) {
  const response = await api.post("/questions/generate", payload);
  return response.data;
}
