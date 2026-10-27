# Modul 2 — Pengelolaan Pesanan

## 1. Gambaran Umum

**ID Modul:** M02

Modul ini bertanggung jawab untuk mengelola pesanan laundry pelanggan, mulai dari pembuatan pesanan hingga penyimpanan detail layanan dan pakaian yang akan dicuci. Fitur pembuatan, pencatatan, dan pengelolaan pesanan dikelompokkan dalam satu modul karena semuanya berfokus pada siklus pengelolaan pesanan laundry pelanggan.

## 2. Tujuan

- Memungkinkan pelanggan membuat pesanan laundry.
- Memudahkan staf mengelola pesanan yang masuk.
- Menyimpan detail pesanan agar mengurangi kesalahan pencatatan.
- Memastikan setiap pesanan terhubung dengan pelanggan yang benar.

## 3. Aktor

- **Pelanggan:** membuat dan melihat pesanan miliknya.
- **Staf Laundry:** melihat dan mengelola pesanan yang masuk.
- **Pemilik Laundry:** memantau pesanan yang tercatat dalam sistem.

## 4. Fitur Utama

### 4.1 Pembuatan Pesanan
Pelanggan dapat membuat pesanan dengan mengisi detail layanan laundry dan informasi pakaian yang diperlukan.

### 4.2 Pengelolaan Detail Pesanan
Sistem menyimpan informasi pesanan, seperti jenis layanan, berat atau jumlah pakaian, dan catatan khusus jika diperlukan.

### 4.3 Melihat Detail Pesanan
Pelanggan dapat melihat detail pesanan miliknya, sedangkan staf dan pemilik dapat mengakses informasi pesanan sesuai hak aksesnya.

### 4.4 Pengelolaan Pesanan oleh Staf
Staf dapat memeriksa pesanan yang masuk dan memperbarui detail pesanan apabila diperlukan sesuai kewenangannya.

## 5. Aturan Modul

1. Pelanggan harus masuk ke sistem sebelum membuat pesanan.
2. Setiap pesanan harus terhubung dengan satu pelanggan.
3. Sistem harus menyimpan detail layanan dan pakaian untuk setiap pesanan.
4. Pelanggan hanya dapat melihat pesanan miliknya sendiri.
5. Perubahan detail pesanan hanya dapat dilakukan oleh pengguna yang memiliki hak akses.
6. Perhitungan biaya dan pembaruan status mengikuti fungsi modul terkait.

## 6. Ketergantungan dengan Modul Lain

- **[Modul 1 — Autentikasi dan Pengaturan Hak Akses:](01-authentication-access-control.md)** memverifikasi identitas pengguna dan memastikan akses pesanan sesuai perannya.
- **[Modul 3 — Perhitungan Biaya:](03-pricing-cost-calculation.md)** menghitung biaya berdasarkan detail layanan dan pakaian dalam pesanan.
- **[Modul 4 — Pelacakan Status Laundry:](04-laundry-status-tracking.md)** mengelola status pengerjaan pesanan.
- **[Modul 6 — Pengelolaan Pengambilan dan Pengantaran:](06-pickup-delivery-management.md)** mengelola pilihan pengambilan atau pengantaran untuk pesanan yang dibuat.

