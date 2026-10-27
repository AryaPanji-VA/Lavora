# D3 — Use Case Diagram

Dokumen ini menjelaskan use case diagram Lavora: siapa aktornya, use case apa saja yang dimodelkan, dan alasan di balik setiap relasi `<<include>>` dan `<<extend>>`.

- **Source:** [`diagrams/Use Case Diagram/use case lavora.puml`](diagrams/Use%20Case%20Diagram/use%20case%20lavora.puml)
- **Hasil render:** [`diagrams/Use Case Diagram/use case lavora.png`](diagrams/Use%20Case%20Diagram/use%20case%20lavora.png)

## 1. Aktor

Tiga aktor pada diagram berasal langsung dari [`problem-statement.md`](problem-statement.md) bagian 3.

| Aktor | Tipe | Ringkasan hak akses |
|---|---|---|
| Pelanggan (*Customer*) | Primer | Registrasi, login, membuat dan membatalkan pesanan, melihat riwayat, memantau status, memilih metode ambil/antar, menerima notifikasi |
| Staf Laundry (*Laundry Staff*) | Primer | Login, input berat dan hitung biaya, memperbarui status cucian, mencatat pembayaran offline, mencatat serah terima |
| Pemilik Laundry (*Laundry Owner*) | Primer | Login, mengelola tarif, menyetujui akun staf, mengawasi pesanan dan pembayaran |

Tidak ada aktor admin terpisah: fungsi administrasi dijalankan oleh Pemilik Laundry.

## 2. Daftar Use Case

Total **17 use case**, dikelompokkan per modul.

| ID | Use Case | Modul | Aktor utama |
|---|---|---|---|
| UC1 | Registrasi Akun Mandiri | M01 | Pelanggan |
| UC2 | Otentikasi / Login | M01 | Pelanggan, Staf, Pemilik |
| UC14 | Setujui Akun Staf | M01 | Pemilik |
| UC3 | Membuat Pesanan Laundry | M02 | Pelanggan |
| UC5 | Lihat Rincian & Riwayat Pesanan | M02 | Pelanggan |
| UC16 | Membatalkan Pesanan | M02 | Pelanggan |
| UC8 | Input Berat & Hitung Biaya | M03 | Staf |
| UC13 | Kelola Tarif Layanan | M03 | Pemilik |
| UC6 | Lacak Status Cucian | M04 | Pelanggan, Pemilik |
| UC9 | Perbarui Status Laundry | M04 | Staf |
| UC11 | Catat Pembayaran Offline | M05 | Staf |
| UC15 | Awasi Pembayaran & Operasional | M05 | Pemilik |
| UC4 | Pilih Metode Ambil / Antar | M06 | Pelanggan (via UC3) |
| UC12 | Catat Serah Terima Cucian | M06 | Staf |
| UC17 | Serah Terima ke Kurir Eksternal | M06 | Staf (via UC12) |
| UC7 | Lihat Notifikasi Pesanan | M07 | Pelanggan |
| UC10 | Kirim Notifikasi Perubahan Status | M07 | Sistem (via UC9) |

## 3. Relasi `<<include>>`

| Relasi | Arah | Alasan |
|---|---|---|
| UC3 → UC4 | Membuat Pesanan **include** Pilih Metode Ambil/Antar | Setiap pesanan wajib punya metode pengambilan. Pelanggan tidak bisa menyimpan pesanan tanpa memilih ambil sendiri atau dikirim, jadi langkah ini selalu dieksekusi — bukan opsional. |
| UC9 → UC10 | Perbarui Status **include** Kirim Notifikasi | Setiap perubahan status wajib memicu notifikasi ke pelanggan. Ini aturan sistem, bukan keputusan staf, sehingga selalu ikut berjalan. |

## 4. Relasi `<<extend>>`

Panah `<<extend>>` selalu mengarah **dari use case tambahan ke use case dasar**, karena use case tambahan yang memperluas, bukan sebaliknya.

| Relasi | Arah | Kondisi perluasan |
|---|---|---|
| UC16 → UC3 | Membatalkan Pesanan **extend** Membuat Pesanan | Pembatalan hanya terjadi pada kondisi tertentu: pesanan belum masuk proses pencucian. Kalau pesanan berjalan normal, UC16 tidak pernah dieksekusi. |
| UC17 → UC12 | Serah Terima ke Kurir **extend** Catat Serah Terima | Serah terima ke kurir hanya terjadi kalau pelanggan memilih pengiriman eksternal. Kalau pelanggan mengambil sendiri, alurnya berhenti di UC12. |

## 5. Catatan desain

**Login adalah prasyarat, bukan `<<include>>`.** UC2 tidak di-include oleh use case lain. Kalau login di-include ke setiap use case, artinya pengguna diminta login ulang setiap kali klik — itu salah secara semantik. Login cukup dimodelkan sebagai satu use case berdiri sendiri yang menghubungkan ketiga aktor.

**Batas ruang lingkup dijaga.** UC17 hanya mencatat serah terima ke kurir eksternal. Memesan kurir, melacak posisi kurir, dan membayar ongkos kirim tetap di luar ruang lingkup (lihat [`problem-statement.md`](problem-statement.md) bagian 4.2). Begitu juga UC10: notifikasi dikirim melalui mekanisme internal Lavora, bukan integrasi WhatsApp.

## Ringkasan

Lavora punya tiga aktor (Pelanggan, Staf, Pemilik) dan tujuh modul, dengan 17 use case yang semuanya bisa dilacak ke modul asalnya. Ada dua relasi `<<include>>` untuk langkah yang wajib selalu jalan (pilih metode pengambilan dan kirim notifikasi) dan dua relasi `<<extend>>` untuk langkah yang hanya jalan pada kondisi tertentu (pembatalan pesanan dan serah terima ke kurir). Login sengaja dimodelkan sebagai use case terpisah, bukan include, karena login adalah prasyarat satu kali, bukan langkah yang diulang di setiap aksi.
