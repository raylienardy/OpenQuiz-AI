# Mock Provider (Quick Guide)

Mock provider adalah AI client bawaan yang mengembalikan respons tetap tanpa perlu koneksi internet atau API key. Cocok untuk pengembangan frontend, pengujian, dan kerja offline.

## Aktivasi

Cukup atur variabel berikut di `backend/.env`:

```env
AI_PROVIDER=mock
```

Tidak perlu variabel lain. Backend akan langsung menggunakan MockClient.

## Verifikasi

Jalankan backend, lalu akses endpoint uji:

```bash
curl http://localhost:8000/ai/test
```

Respons yang diharapkan:

```json
{
  "success": true,
  "provider": "mock",
  "model": "mock-model",
  "response": "{\n  \"questions\": [...] }"
}
```

## Kapan Digunakan

- **Frontend development** – antarmuka bisa langsung dibangun tanpa menunggu AI sungguhan.
- **Offline** – tidak ada internet? Tetap bisa coding.
- **Tes otomatis** – output selalu sama, memudahkan penulisan unit test.
- **Kuota habis** – ketika provider lain mencapai batas free tier, Mock tetap jalan.

## Perilaku

- `initialize()` – selalu berhasil.
- `generate()` – mengembalikan JSON soal pilihan ganda statis.
- `health_check()` – selalu `true`.
- Tidak ada panggilan jaringan, tidak ada penundaan.

## Kustomisasi (Masa Depan)

Ke depan, Mock dapat dikonfigurasi untuk simulasi:

- `MOCK_DELAY_MS` – tambah jeda buatan.
- `MOCK_FAIL_RATE` – persentase kegagalan acak.
- `MOCK_INVALID_JSON` – menguji penanganan respons rusak.

Untuk detail arsitektur dan rencana pengembangan, lihat [mock-provider.md](mock-provider.md).
