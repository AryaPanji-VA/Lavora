# Lavora — Pernyataan Masalah

## 1. Nama dan Deskripsi Aplikasi

**Lavora** adalah sistem manajemen laundry yang dirancang untuk membantu usaha laundry dalam mengelola pesanan pelanggan, menghitung biaya layanan, memantau proses pencucian, mencatat pembayaran, dan memberikan notifikasi mengenai perubahan status pesanan. Sistem ini memiliki tiga jenis pengguna, yaitu pelanggan, staf laundry, dan pemilik laundry. Setiap pengguna memiliki hak akses yang berbeda sesuai dengan peran dan tanggung jawabnya.

## 2. Pernyataan Masalah

Usaha laundry skala kecil sering kali mengelola kegiatan operasional menggunakan nota tulis tangan, perhitungan biaya secara manual, dan komunikasi melalui aplikasi pesan seperti WhatsApp. Cara tersebut dapat menyulitkan pemilik atau staf dalam mengatur pesanan pelanggan, memantau proses pencucian, serta menjaga keakuratan catatan pembayaran. Ketika jumlah pesanan meningkat, risiko kehilangan nota, kesalahan perhitungan biaya, dan tertukarnya pakaian pelanggan juga semakin besar.

Pelanggan juga sering mengalami kesulitan untuk mengetahui apakah pakaian mereka masih dalam proses pencucian, sudah siap diambil, atau telah selesai diproses. Pelanggan perlu menghubungi staf laundry secara langsung untuk menanyakan perkembangan pesanan. Hal ini menambah beban komunikasi staf dan membuat proses pelayanan menjadi kurang efisien.

Lavora dikembangkan untuk mengatasi permasalahan tersebut melalui sistem terpusat yang dapat digunakan untuk mengelola pesanan laundry, menghitung biaya layanan, memperbarui status pencucian, mencatat pembayaran, dan memberikan notifikasi ketika status pesanan berubah. Dengan mengintegrasikan proses tersebut ke dalam satu sistem, Lavora diharapkan dapat mengurangi kesalahan pencatatan manual dan meningkatkan komunikasi antara pelanggan dengan pihak laundry.

## 3. Target Pengguna dan Aktor

### 3.1 Pelanggan (Customer)

Pelanggan menggunakan Lavora untuk:
- Membuat akun secara mandiri dan login ke sistem.
- Membuat dan melihat pesanan laundry miliknya.
- Memantau perkembangan dan status pesanan.
- Melihat biaya layanan dan status pembayaran.
- Menerima notifikasi mengenai perubahan status pesanan.

### 3.2 Staf Laundry (Laundry Staff)

Staf laundry menggunakan Lavora untuk:
- Login menggunakan akun yang telah dibuat atau disetujui oleh pemilik laundry.
- Melihat dan mengelola pesanan pelanggan sesuai hak aksesnya.
- Memperbarui status proses pencucian.
- Mencatat pembayaran pelanggan.
- Membantu operasional laundry melalui sistem yang terpusat.

### 3.3 Pemilik Laundry (Laundry Owner)

Pemilik laundry menggunakan Lavora untuk:
- Login ke sistem menggunakan akun pemilik.
- Mengelola harga layanan laundry.
- Membuat atau menyetujui akun staf serta mengatur hak aksesnya.
- Melihat dan memantau seluruh pesanan laundry.
- Mengawasi proses operasional dan pencatatan pembayaran.

Dalam Lavora, pemilik laundry juga menjalankan fungsi administrasi sistem sehingga tidak diperlukan aktor admin yang terpisah.

## 4. Ruang Lingkup Proyek

### 4.1 Fitur yang Termasuk

Fitur yang termasuk dalam ruang lingkup Lavora adalah:
- Registrasi mandiri dan autentikasi akun pelanggan.
- Login untuk pelanggan, staf, dan pemilik laundry.
- Pengaturan hak akses berdasarkan peran pengguna.
- Pembuatan dan pengelolaan pesanan laundry.
- Perhitungan biaya layanan laundry.
- Pemantauan dan pembaruan status pencucian.
- Pencatatan pembayaran dan pengelolaan status pembayaran.
- Notifikasi kepada pelanggan mengenai perubahan status pesanan.
- Pengelolaan harga layanan dan akun staf oleh pemilik laundry.

### 4.2 Fitur yang Tidak Termasuk

Fitur berikut tidak termasuk dalam ruang lingkup proyek Lavora saat ini:
- Pemrosesan pembayaran daring melalui bank, dompet digital, atau layanan gerbang pembayaran.
- Pelacakan pengiriman secara langsung dan pengelolaan kurir.
- Pengelolaan persediaan deterjen, kemasan, dan perlengkapan laundry lainnya.
- Pelaporan keuangan, akuntansi, dan analisis bisnis tingkat lanjut.
- Integrasi dengan platform pesan eksternal seperti WhatsApp untuk mengirim notifikasi secara otomatis.

## 5. Tujuan Proyek

Tujuan Lavora adalah menunjukkan bagaimana sistem manajemen laundry terpusat dapat mendukung kebutuhan operasional dasar suatu usaha laundry. Sistem ini diharapkan dapat membantu pelanggan memantau pesanan, membantu staf menjalankan kegiatan operasional, serta membantu pemilik mengelola layanan dan mengawasi kegiatan laundry.

Proyek ini berfokus pada pendokumentasian kebutuhan sistem, penentuan modul beserta ketergantungannya, pemodelan interaksi utama pengguna, penyusunan kasus pengujian, serta implementasi satu fungsi sederhana yang dilengkapi pengujian unit sesuai dengan ketentuan Ujian Akhir Semester mata kuliah Software Development Fundamentals.
