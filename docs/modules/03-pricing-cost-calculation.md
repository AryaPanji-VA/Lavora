# Modul 3 — Perhitungan Harga dan Biaya

## 1. Gambaran Umum

**ID Modul:** M03

Modul ini bertanggung jawab untuk menghitung biaya layanan laundry berdasarkan berat cucian dan tarif per kilogram yang ditetapkan oleh pemilik laundry. Modul ini mengelompokkan pengaturan tarif dan perhitungan biaya karena keduanya berkaitan langsung dengan penentuan harga pesanan. Modul ini memastikan pelanggan dapat mengetahui biaya laundry berdasarkan data pesanan yang dimasukkan ke dalam sistem Lavora.

## 2. Tujuan

- Memungkinkan pemilik laundry menetapkan tarif layanan laundry.
- Memfasilitasi staf laundry dalam memasukkan dan memeriksa berat cucian.
- Menghitung total biaya laundry berdasarkan berat cucian dan tarif yang berlaku.
- Memungkinkan pelanggan melihat biaya pesanan laundry.

## 3. Aktor

- **Pelanggan:** melihat biaya pesanan laundry.
- **Staf Laundry:** memasukkan dan memeriksa berat cucian untuk perhitungan biaya.
- **Pemilik Laundry (Admin):** menetapkan dan mengelola tarif layanan laundry.

## 4. Fitur Utama

### 4.1 Pengaturan Tarif Laundry

Sistem memungkinkan pemilik laundry menetapkan tarif layanan per kilogram yang digunakan sebagai dasar perhitungan biaya pesanan.

### 4.2 Penginputan Berat Cucian

Setelah cucian diterima, staf laundry menimbang cucian dan memasukkan berat aktualnya ke dalam sistem. Berat aktual tersebut digunakan sebagai dasar perhitungan biaya sesuai tarif layanan yang berlaku.

### 4.3 Perhitungan Total Biaya

Sistem menghitung total biaya laundry berdasarkan berat aktual cucian yang telah dimasukkan staf dan tarif per kilogram untuk layanan yang dipilih. Hasil perhitungan digunakan sebagai total biaya pesanan dalam M02 agar biaya yang tercatat sesuai dengan data pesanan.

Rumus perhitungan:

Total Biaya = Berat Aktual Cucian × Tarif per Kilogram

### 4.4 Informasi Biaya Pesanan

Sistem menampilkan informasi biaya laundry kepada pelanggan agar pelanggan dapat mengetahui biaya pesanan yang tercatat dalam sistem.

## 5. Aturan Bisnis

1. Tarif layanan laundry ditetapkan oleh pemilik laundry.
2. Berat cucian digunakan sebagai dasar perhitungan biaya laundry.
3. Total biaya dihitung berdasarkan berat cucian dikalikan tarif per kilogram yang berlaku.
4. Perhitungan biaya harus menggunakan data berat dan tarif yang sesuai dengan pesanan.
5. Pelanggan hanya dapat melihat informasi biaya dari pesanan miliknya.
6. Pengelolaan tarif hanya dapat dilakukan oleh pengguna yang memiliki hak akses pemilik laundry.

## 6. Ketergantungan dengan Modul Lain

- [Modul 1 — Autentikasi dan Pengaturan Hak Akses](01-authentication-access-control.md): menyediakan identitas pengguna dan pembatasan hak akses untuk pengelolaan tarif serta informasi biaya.
- [Modul 2 — Pengelolaan Pesanan](02-order-management.md): menyediakan data pesanan yang diperlukan dalam proses perhitungan dan penyimpanan biaya laundry.

Modul ini mendukung proses pengelolaan pesanan dengan menyediakan perhitungan biaya berdasarkan berat cucian dan tarif yang berlaku.
