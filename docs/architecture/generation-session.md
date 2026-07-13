# Sesi Generasi

Setiap kali pengguna menghasilkan pertanyaan, sebuah objek sesi dibuat di frontend. Objek ini menyimpan metadata penting seperti:

- Waktu generasi
- Provider dan model
- Latency
- Jumlah pertanyaan
- Versi prompt/skema
- Status (completed/failed)

Sesi hanya bertahan selama sesi browser (state React). Di masa depan, sesi dapat digunakan untuk riwayat, perbandingan, atau ekspor.

**Implementasi:** `frontend/src/session/generationSession.js` menyediakan `createSession()`, `updateSession()`, dan `clearSession()`.
