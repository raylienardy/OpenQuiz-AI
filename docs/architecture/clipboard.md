# Clipboard & Ekspor Dasar

Sistem ekspor terdiri dari lapisan formatter dan utilitas clipboard:

- **Formatter** (`utils/export/`): fungsi murni yang mengubah array pertanyaan menjadi string JSON, Markdown, atau teks biasa.
- **Clipboard** (`utils/export/clipboard.js`): menyalin teks ke clipboard dengan fallback.
- **Toolbar** memanggil formatter lalu `copyToClipboard()`.

Ke depan, formatter yang sama akan digunakan untuk ekspor PDF, DOCX, CSV, dll.
