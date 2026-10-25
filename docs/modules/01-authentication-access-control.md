# Modul 1 — Autentikasi dan Pengaturan Hak Akses

## 1. Gambaran Umum Modul

**Nama Modul:** Autentikasi dan Pengaturan Hak Akses

**ID Modul:** M01

**Deskripsi:**

Modul Autentikasi dan Pengaturan Hak Akses bertanggung jawab untuk memverifikasi identitas pengguna dan mengatur hak akses berdasarkan peran masing-masing pengguna dalam sistem Lavora. Modul ini memastikan bahwa pelanggan, staf laundry, dan pemilik laundry hanya dapat mengakses fitur yang sesuai dengan tanggung jawab mereka.

## 2. Tujuan Modul

Modul ini bertujuan untuk:
- Memungkinkan pengguna masuk ke sistem menggunakan akun yang terdaftar.
- Memfasilitasi pendaftaran akun pelanggan secara mandiri.
- Memastikan akun staf mendapatkan persetujuan pemilik sebelum memperoleh hak akses staf.
- Memverifikasi identitas pengguna sebelum memberikan akses ke fitur yang dilindungi.
- Membatasi akses fitur berdasarkan peran pengguna.
- Menyediakan fitur keluar dari akun untuk mengakhiri sesi pengguna.

## 3. Aktor

### 3.1 Pelanggan

- Mendaftarkan akun secara mandiri.
- Masuk ke sistem menggunakan informasi akun yang terdaftar.
- Mengakses fitur yang diperuntukkan bagi pelanggan.

### 3.2 Staf Laundry

- Masuk menggunakan akun staf yang telah disetujui oleh pemilik laundry.
- Mengakses fitur operasional laundry sesuai dengan hak aksesnya.

### 3.3 Pemilik Laundry

- Masuk menggunakan akun pemilik yang disiapkan melalui konfigurasi awal sistem.
- Menyetujui pendaftaran akun staf dan menetapkan hak aksesnya.
- Mengakses fitur pengelolaan dan pengawasan sesuai tanggung jawabnya.

## 4. Fitur Utama

### 4.1 Pendaftaran Akun Pelanggan

Sistem memungkinkan pelanggan membuat akun dengan mengisi informasi yang diperlukan. Sistem memvalidasi data pendaftaran dan mencegah penggunaan identitas akun yang sudah terdaftar, seperti alamat email yang sama.

### 4.2 Masuk ke Sistem

Sistem memverifikasi informasi akun yang dimasukkan pengguna. Jika informasi tersebut valid dan status akun memenuhi persyaratan, sistem memberikan akses sesuai dengan peran pengguna.

### 4.3 Persetujuan Akun Staf

Akun yang mengajukan akses sebagai staf tidak langsung memperoleh hak akses staf. Pemilik laundry harus menyetujui akun tersebut dan menetapkan perannya sebelum akun dapat mengakses fitur operasional staf.

### 4.4 Pengaturan Hak Akses Berdasarkan Peran

Sistem membatasi akses fitur berdasarkan peran pengguna:
- **Pelanggan:** melihat dan mengelola pesanan miliknya sendiri serta mengakses informasi yang berkaitan dengan pesanan tersebut.
- **Staf Laundry:** menjalankan kegiatan operasional yang diizinkan untuk peran staf.
- **Pemilik Laundry:** mengakses fitur pengelolaan dan pengawasan sesuai tanggung jawabnya.

### 4.5 Pengelolaan Sesi dan Keluar dari Akun

Sistem mempertahankan sesi pengguna selama pengguna masuk ke sistem. Pengguna dapat keluar dari akun untuk mengakhiri sesi sehingga sesi tersebut tidak dapat digunakan kembali untuk mengakses fitur yang dilindungi.

## 5. Aturan Bisnis

1. Pengguna harus masuk ke sistem sebelum mengakses fitur yang memerlukan autentikasi.
2. Pelanggan dapat mendaftarkan akun secara mandiri.
3. Akun yang belum mendapatkan persetujuan tidak boleh memperoleh hak akses staf.
4. Hanya pemilik laundry yang berwenang menyetujui akun staf dan menetapkan perannya.
5. Akun pemilik disiapkan melalui konfigurasi awal sistem dan tidak dapat dibuat melalui pendaftaran publik sebagai pemilik.
6. Pengguna hanya dapat mengakses fitur yang sesuai dengan perannya.
7. Pelanggan hanya dapat melihat dan mengelola pesanan miliknya sendiri.
8. Staf hanya dapat menjalankan tindakan yang diizinkan untuk peran staf.
9. Pemilik memiliki hak akses pengelolaan sesuai tanggung jawabnya.
10. Keluar dari akun harus mengakhiri sesi pengguna yang sedang aktif.

## 6. Masukan dan Keluaran

| Masukan | Keluaran |
|---|---|
| Data pendaftaran pelanggan | Akun berhasil dibuat atau pesan kesalahan validasi |
| Informasi akun untuk masuk | Hasil verifikasi dan akses ke sistem jika berhasil |
| Status persetujuan akun staf | Hak akses staf aktif atau tetap tidak aktif |
| Peran pengguna | Hak akses sesuai dengan peran |
| Permintaan keluar dari akun | Sesi pengguna berakhir |

## 7. Ketergantungan dengan Modul Lain

- **[Modul 02 Pengelolaan Pesanan:](02-order-management.md)** menyediakan pembatasan akses agar pelanggan hanya dapat mengakses pesanan miliknya.
- **[Modul 03 Perhitungan Biaya:](03-pricing-cost-calculation.md)** memastikan akses terhadap informasi dan fitur terkait biaya sesuai dengan hak akses pengguna.
- **[Modul 04 Pelacakan Status Laundry:](04-laundry-status-tracking.md)** memastikan pembaruan status hanya dapat dilakukan oleh pengguna yang berwenang.
- **[Modul 05 Pengelolaan Pembayaran:](05-payment-management.md)** membatasi akses terhadap pencatatan dan informasi pembayaran berdasarkan peran.
- **[Modul 06 Pengelolaan Pengambilan dan Pengantaran:](06-pickup-delivery-management.md)** membatasi akses terhadap informasi pengambilan dan pengiriman berdasarkan peran.
- **[Modul 07 Pengelolaan Notifikasi:](07-customer-notification.md)** menggunakan informasi pengguna dan pesanan untuk menentukan penerima notifikasi.

## 8. Batasan Modul

Modul ini tidak bertanggung jawab atas:
- Pengelolaan detail pesanan laundry.
- Perhitungan biaya layanan.
- Pencatatan dan pengelolaan pembayaran.
- Pembaruan status pencucian.
- Pengelolaan informasi pengambilan dan pengantaran.
- Pengiriman notifikasi kepada pelanggan.

Fungsi-fungsi tersebut menjadi tanggung jawab modul Lavora lainnya.
