# D4 — Sequence Diagrams

Tiga sequence diagram, masing-masing mewakili satu skenario berbeda: alur masuk dan pemesanan, alur operasional harian di sisi staf, dan alur uang serta barang berpindah tangan.

Setiap diagram punya minimal satu fragment `alt` untuk menunjukkan percabangan kondisi, lengkap dengan return message (`-->`) pada setiap pemanggilan.

| Kode | Skenario | Source | Render |
|---|---|---|---|
| SD1 | Login dan Pembuatan Pesanan | [`sd1-login-pemesanan.puml`](diagrams/Sequence%20Diagram/sd1-login-pemesanan.puml) | [`sd1-login-pemesanan.png`](diagrams/Sequence%20Diagram/sd1-login-pemesanan.png) |
| SD2 | Pemrosesan Laundry dan Pembaruan Status | [`SD2-Pemrosesan Laundry dan Pembaruan Status.puml`](diagrams/Sequence%20Diagram/SD2-Pemrosesan%20Laundry%20dan%20Pembaruan%20Status.puml) | [`SD2-Pemrosesan Laundry dan Pembaruan Status.png`](diagrams/Sequence%20Diagram/SD2-Pemrosesan%20Laundry%20dan%20Pembaruan%20Status.png) |
| SD3 | Pembayaran dan Serah Terima Pesanan | [`SD3 - Pembayaran dan Serah Terima Pesanan.puml`](diagrams/Sequence%20Diagram/SD3%20-%20Pembayaran%20dan%20Serah%20Terima%20Pesanan.puml) | [`SD3 - Pembayaran dan Serah Terima Pesanan.png`](diagrams/Sequence%20Diagram/SD3%20-%20Pembayaran%20dan%20Serah%20Terima%20Pesanan.png) |

## SD1 — Login dan Pembuatan Pesanan

**Kenapa skenario ini penting:** ini pintu masuk seluruh sistem dan alur yang paling sering dipakai pelanggan. Diagram ini memperlihatkan bahwa pesanan tidak bisa disimpan sebelum sesi diverifikasi, dan bahwa total biaya dihitung modul M03 *sebelum* pesanan ditulis ke database — bukan setelahnya. Kalau urutan ini terbalik, pelanggan bisa menerima pesanan dengan harga kosong atau salah.

**Lifeline:** Pelanggan, Halaman Lavora (UI), M01 Autentikasi, M02 Pengelolaan Pesanan, M03 Perhitungan Biaya, Database.

**Alur:** pelanggan membuka halaman login → UI mengirim kredensial ke M01 → M01 memeriksa akun ke database. Setelah login, pelanggan mengisi detail pesanan → M02 memverifikasi sesi ke M01 → M02 meminta perhitungan biaya ke M03 → M03 mengambil tarif dari database → pesanan disimpan.

**Fragment `alt`:**
1. `alt Akun valid` / `else Akun tidak valid` — login berhasil masuk halaman utama, atau gagal dengan pesan kesalahan.
2. `alt Sesi valid` / `else Sesi tidak valid` — kalau sesi kedaluwarsa, M02 menolak memproses dan UI meminta login kembali.
3. `alt Pesanan berhasil disimpan` / `else Penyimpanan gagal` — dibedakan agar kegagalan database tidak dilaporkan sebagai pesanan sukses.

## SD2 — Pemrosesan Laundry dan Pembaruan Status

**Kenapa skenario ini penting:** ini inti pekerjaan harian staf, dan satu aksi staf memicu dua efek sekaligus — status pesanan berubah *dan* pelanggan otomatis dapat notifikasi. Justru di sinilah nilai Lavora dibanding nota tulis tangan: pelanggan tidak perlu lagi menghubungi staf untuk menanyakan perkembangan cucian. Diagram ini juga menunjukkan bahwa hak akses staf diverifikasi ulang di sisi modul, bukan hanya disembunyikan di tampilan.

**Lifeline:** Staf Laundry, Antarmuka Lavora, M01 Autentikasi, M02 Pengelolaan Pesanan, M04 Pelacakan Status, M07 Customer Notification.

**Alur:** staf login → membuka daftar pesanan masuk → memilih satu pesanan → mengubah status (Menunggu Diproses → Sedang Dicuci) → M04 memverifikasi hak akses ke M01 → status disimpan beserta riwayatnya → M07 membuat notifikasi untuk pelanggan.

**Fragment `alt`:** tiga cabang — `hak akses valid dan status tersimpan`, `hak akses tidak valid`, dan `penyimpanan status gagal`. Percabangan ketiga sengaja dipisah dari yang kedua supaya kegagalan teknis tidak tertukar dengan penolakan akses.

## SD3 — Pembayaran dan Serah Terima Pesanan

**Kenapa skenario ini penting:** di titik inilah uang dan barang berpindah pada saat yang sama, jadi ini skenario paling berisiko rugi. Kalau status pembayaran tercatat tapi cucian tidak tercatat diserahkan (atau sebaliknya), laundry kehilangan bukti dan rawan sengketa dengan pelanggan. Diagram ini memaksa keduanya tercatat berurutan dalam satu alur, dan memastikan serah terima hanya diproses setelah pembayaran berhasil.

**Lifeline:** Pelanggan, Staf Laundry, Halaman Lavora, M01 Autentikasi, M02 Pengelolaan Pesanan, M04 Status Laundry, M05 Pembayaran, M06 Serah Terima, M07 Notifikasi, Database.

**Alur:** staf menyelesaikan cucian → M04 memperbarui status → M07 mengirim notifikasi "laundry selesai" ke pelanggan. Pelanggan membayar → akses divalidasi M01 → total biaya diambil dari M02 → M05 mencatat pembayaran → staf memproses serah terima → M06 menyimpan metode serah terima → status pesanan diperbarui → notifikasi terakhir dikirim.

**Fragment `alt`:** `alt Pembayaran berhasil` / `else Pembayaran gagal`. Blok serah terima berada **di dalam** cabang berhasil, sehingga pesanan tidak mungkin diserahkan sebelum pembayaran tercatat.

## Ringkasan

Tiga diagram ini menutup tiga titik kritis: masuknya pengguna dan pesanan (SD1), berjalannya operasional harian dan notifikasi otomatis (SD2), serta pertukaran uang dan barang (SD3). Semuanya memakai lifeline yang konsisten — aktor, antarmuka, modul terkait, dan database — dan masing-masing punya minimal satu `alt` yang membedakan jalur sukses dari kegagalan.
