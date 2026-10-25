# Modul 4 — Pelacakan Status Laundry

## 1. Gambaran Umum

**ID Modul:** M04

Modul ini bertanggung jawab untuk mengelola informasi status pesanan laundry agar pelanggan dapat mengetahui perkembangan pesanan mereka. Modul ini mengelompokkan pembaruan status dan pemantauan pesanan karena keduanya berkaitan dengan penyampaian informasi mengenai kondisi pesanan selama proses layanan laundry. Modul ini memastikan informasi status pesanan dapat diperbarui oleh pengguna yang berwenang dan dilihat oleh pelanggan sesuai hak aksesnya.

## 2. Tujuan

- Memungkinkan staf laundry memperbarui status pesanan.
- Memfasilitasi pemilik laundry dalam memantau dan memperbarui status pesanan sesuai hak aksesnya.
- Memungkinkan pelanggan melihat perkembangan pesanan laundry.
- Memastikan informasi status yang ditampilkan sesuai dengan data pesanan dalam sistem Lavora.

## 3. Aktor

- **Pelanggan:** melihat status dan perkembangan pesanan laundry miliknya.
- **Staf Laundry:** memperbarui status pesanan sesuai tugas operasionalnya.
- **Pemilik Laundry (Admin):** memantau dan memperbarui status pesanan sesuai hak aksesnya.

## 4. Fitur Utama

### 4.1 Pembaruan Status Pesanan

Sistem memungkinkan staf laundry dan pemilik laundry memperbarui informasi status pesanan sesuai hak akses masing-masing.

### 4.2 Pemantauan Status Pesanan

Sistem menyediakan informasi status pesanan agar staf dan pemilik laundry dapat memantau perkembangan pesanan yang dikelola.

### 4.3 Informasi Status untuk Pelanggan

Sistem memungkinkan pelanggan melihat status terkini dari pesanan laundry miliknya melalui sistem Lavora.

### 4.4 Penyimpanan Informasi Status

Sistem menyimpan informasi status pesanan yang diperbarui agar informasi perkembangan pesanan dapat ditampilkan secara konsisten kepada pengguna yang memiliki hak akses.

## 5. Aturan Bisnis

1. Pengguna harus masuk sebelum mengakses fitur pelacakan status yang memerlukan autentikasi.
2. Pembaruan status pesanan hanya dapat dilakukan oleh staf laundry atau pemilik laundry yang memiliki hak akses.
3. Pelanggan hanya dapat melihat status pesanan miliknya sendiri.
4. Informasi status yang ditampilkan harus sesuai dengan data pesanan yang tersimpan dalam sistem.
5. Pembaruan status harus merujuk pada pesanan yang benar.
6. Pengguna hanya dapat melakukan tindakan terkait status pesanan sesuai dengan perannya dalam sistem.

## 6. Ketergantungan dengan Modul Lain

- [Modul 1 — Autentikasi dan Pengaturan Hak Akses](01-authentication-access-control.md): menyediakan identitas pengguna dan pembatasan hak akses untuk melihat serta memperbarui status pesanan.
- [Modul 2 — Pengelolaan Pesanan](02-order-management.md): menyediakan data pesanan yang diperlukan untuk menampilkan dan memperbarui informasi status laundry.

Modul ini mendukung pengelolaan pesanan dengan menyediakan informasi perkembangan status yang dapat dipantau oleh pengguna sesuai hak aksesnya.
