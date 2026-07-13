# Prompt Pipeline

`PromptBuilder` mengonversi `QuestionRequest` menjadi prompt terstruktur. Template dipecah menjadi fungsi-fungsi kecil di `prompt_templates.py` untuk kemudahan penyesuaian.

Alur:

1. System prompt (peran AI)
2. Instruksi tugas (jenis soal)
3. Jumlah soal
4. Tingkat kesulitan
5. Bahasa
6. Teks sumber
7. Aturan format output (JSON)

Versi prompt dilacak (`PROMPT_VERSION`) dan disertakan dalam metadata.
