# D3. Diagram Use Case

Diagram use case ini menggambarkan seluruh sistem Lavora: siapa saja penggunanya dan apa yang dapat mereka lakukan. Use case diberi label modul (`[M01]` sampai `[M07]`) agar mudah dicocokkan dengan pembagian modul pada D2.

## Diagram

![Use Case Diagram Lavora](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Use%20Case%20Diagram/use%20case%20lavora.png)

**File sumber:** [use case lavora.puml](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Use%20Case%20Diagram/use%20case%20lavora.puml) (PlantUML)

## Aktor

| Aktor | Peran dalam sistem |
|---|---|
| Pelanggan (Customer) | Mendaftar, membuat dan membatalkan pesanan, memantau status, dan melihat notifikasi |
| Staf Laundry (Laundry Staff) | Menimbang cucian, memperbarui status, mencatat pembayaran offline, dan mencatat serah terima |
| Pemilik Laundry (Laundry Owner) | Menyetujui akun staf, mengelola tarif, serta memantau status, pembayaran, dan operasional |

## Daftar Use Case per Modul

| Modul | Use Case | Aktor |
|---|---|---|
| M01 Autentikasi dan Pengaturan Hak Akses | Registrasi Akun Mandiri | Pelanggan |
| | Otentikasi / Login | Pelanggan, Staf Laundry, Pemilik Laundry |
| | Setujui Akun Staf | Pemilik Laundry |
| M02 Pengelolaan Pesanan | Membuat Pesanan Laundry | Pelanggan |
| | Membatalkan Pesanan | Pelanggan (melalui relasi extend) |
| | Lihat Rincian & Riwayat Pesanan | Pelanggan |
| M03 Perhitungan Harga dan Biaya | Input Berat & Hitung Biaya | Staf Laundry |
| | Kelola Tarif Layanan | Pemilik Laundry |
| M04 Pelacakan Status Laundry | Lacak Status Cucian | Pelanggan, Pemilik Laundry |
| | Perbarui Status Laundry | Staf Laundry |
| M05 Payment Management | Catat Pembayaran Offline | Staf Laundry |
| | Awasi Pembayaran & Operasional | Pemilik Laundry |
| M06 Pengelolaan Pengambilan dan Pengantaran | Pilih Metode Ambil / Antar | Pelanggan (melalui relasi include) |
| | Catat Serah Terima Cucian | Staf Laundry |
| | Serah Terima ke Kurir Eksternal | Staf Laundry (melalui relasi extend) |
| M07 Customer Notification | Lihat Notifikasi Pesanan | Pelanggan |
| | Kirim Notifikasi Perubahan Status | Sistem (melalui relasi include) |

Total: **17 use case**.

## Relasi Include dan Extend

### `<<include>>`

| Use case utama | Use case yang di-include | Alasan |
|---|---|---|
| Membuat Pesanan Laundry | Pilih Metode Ambil / Antar | Setiap pesanan harus memiliki metode penyerahan yang jelas, sehingga langkah ini selalu terjadi saat pesanan dibuat |
| Perbarui Status Laundry | Kirim Notifikasi Perubahan Status | Setiap perubahan status selalu memicu notifikasi otomatis kepada pelanggan |

### `<<extend>>`

| Use case tambahan | Use case utama | Kondisi |
|---|---|---|
| Membatalkan Pesanan | Membuat Pesanan Laundry | Hanya terjadi jika pelanggan memutuskan membatalkan pesanan sebelum cucian diproses |
| Serah Terima ke Kurir Eksternal | Catat Serah Terima Cucian | Hanya terjadi jika pelanggan memilih pengantaran dengan kurir eksternal |

## Pemenuhan Ketentuan D3

- [x] Satu diagram use case yang mencakup seluruh sistem
- [x] Semua aktor dari D1 muncul (Pelanggan, Staf Laundry, Pemilik Laundry)
- [x] Minimal 8 use case (ada 17)
- [x] Minimal satu relasi `<<include>>` atau `<<extend>>` (ada 2 include dan 2 extend)
- [x] Use case diberi label per modul (`[M01]` sampai `[M07]`)
