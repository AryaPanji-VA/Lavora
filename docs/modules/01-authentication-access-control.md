# Modul 1 — Autentikasi dan Pengaturan Hak Akses

## 1. Gambaran Umum

**ID Modul:** M01

Modul ini bertanggung jawab untuk memverifikasi identitas pengguna dan mengatur hak akses berdasarkan peran dalam sistem Lavora. Modul ini memastikan bahwa pelanggan, staf laundry, dan pemilik laundry hanya dapat mengakses fitur sesuai tanggung jawabnya.

## 2. Tujuan

- Memungkinkan pengguna masuk dan keluar dari sistem.
- Memfasilitasi pendaftaran akun pelanggan.
- Mengatur hak akses berdasarkan peran pengguna.
- Memastikan akun staf memperoleh persetujuan pemilik sebelum mendapatkan hak akses staf.

## 3. Aktor

- **Pelanggan:** mendaftar, masuk, dan mengakses fitur pelanggan.
- **Staf Laundry:** masuk dan mengakses fitur operasional sesuai hak aksesnya.
- **Pemilik Laundry:** masuk, menyetujui akun staf, dan menetapkan hak aksesnya.

Akun pemilik disiapkan melalui konfigurasi awal sistem, bukan melalui pendaftaran publik.

## 4. Fitur Utama

### 4.1 Pendaftaran Pelanggan
Sistem memungkinkan pelanggan membuat akun dan memvalidasi informasi yang diperlukan untuk mencegah akun duplikat.

### 4.2 Masuk dan Keluar Sistem
Sistem memverifikasi informasi akun sebelum memberikan akses. Pengguna dapat keluar untuk mengakhiri sesi aktif.

### 4.3 Persetujuan Akun Staf
Akun yang mengajukan akses sebagai staf harus disetujui oleh pemilik sebelum memperoleh hak akses staf.

### 4.4 Pengaturan Hak Akses
Sistem membatasi akses fitur berdasarkan peran:
- Pelanggan hanya dapat mengakses pesanan miliknya.
- Staf dapat menjalankan fungsi operasional yang diizinkan.
- Pemilik dapat mengakses fungsi pengelolaan dan pengawasan sesuai perannya.

## 5. Aturan Bisnis

1. Pengguna harus masuk sebelum mengakses fitur yang memerlukan autentikasi.
2. Pelanggan dapat mendaftar secara mandiri.
3. Akun staf harus disetujui oleh pemilik sebelum mendapatkan hak akses staf.
4. Akun pemilik dibuat melalui konfigurasi awal sistem.
5. Pengguna hanya dapat mengakses fitur sesuai perannya.
6. Pelanggan tidak boleh melihat atau mengubah pesanan milik pelanggan lain.

## 6. Masukan dan Keluaran

| Masukan | Keluaran |
|---|---|
| Data pendaftaran pelanggan | Akun berhasil dibuat atau pesan kesalahan |
| Informasi akun untuk masuk | Hasil verifikasi dan akses jika berhasil |
| Persetujuan pemilik atas akun staf | Hak akses staf diberikan |
| Permintaan keluar | Sesi pengguna diakhiri |

## 7. Ketergantungan dengan Modul Lain

- [Modul 2 — Pengelolaan Pesanan](02-order-management.md): menyediakan identitas pengguna dan pembatasan akses saat pesanan dibuat atau dilihat.

Modul lain dapat menerapkan pemeriksaan hak akses sesuai kebutuhannya, tetapi tidak semuanya menjadi ketergantungan langsung modul ini.