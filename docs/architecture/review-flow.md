# Alur Review Pertanyaan

Alur lengkap dari unggahan hingga peninjauan pertanyaan:

1. **Upload & Ekstraksi**  
   File (PDF/DOCX/TXT) diunggah → teks diekstraksi dan dibersihkan.

2. **Prompt Builder**  
   `QuestionRequest` dikonversi menjadi prompt AI yang terstruktur.

3. **Provider AI**  
   Prompt dikirim ke provider (Groq/Gemini/Mock) melalui `AIService`.

4. **Parser JSON**  
   Respons mentah AI diurai menjadi objek `QuestionResponse`.

5. **Validator**  
   `QuestionResponse` diperiksa struktur dan konsistensinya.

6. **Review Workspace**  
   Pertanyaan ditampilkan dengan pencarian, filter, urutkan, dan paginasi.

7. **Panel Detail**  
   Informasi lengkap satu pertanyaan ditampilkan saat dipilih.

8. **Panel Analitik**  
   Statistik jumlah, tipe, kesulitan, bahasa, dan provider.

9. **Metadata AI & Sesi**  
   Metadata provider, latency, versi prompt dicatat dan ditampilkan.

10. **Clipboard & Ekspor (dasar)**  
    Salin sebagai JSON, Markdown, atau hanya teks pertanyaan; unduh JSON.

Diagram alur (ASCII):
Upload → Ekstraksi → Prompt Builder → Provider AI → Parser → Validator → Review Workspace → Detail/Analitik/Metadata
