# Lavora — Pernyataan Masalah

## 1. Nama dan Deskripsi Aplikasi

**Lavora** adalah sistem manajemen laundry yang dirancang untuk membantu usaha laundry dalam mengelola pesanan pelanggan, menghitung biaya layanan, memantau proses pencucian, mencatat pembayaran, serta mengelola informasi pengambilan dan pengantaran pakaian. Sistem ini memiliki tiga jenis pengguna, yaitu pelanggan (*Customer*), staf laundry (*Laundry Staff*), dan pemilik laundry (*Laundry Owner*). Setiap pengguna memiliki hak akses sesuai dengan peran dan tanggung jawabnya.

Lavora menyediakan pilihan pembayaran online dan offline untuk layanan laundry serta pilihan pengambilan pakaian secara mandiri atau menggunakan jasa pengiriman eksternal, seperti Gojek atau layanan kurir lainnya. Untuk pengiriman eksternal, proses pemesanan kurir dan pembayaran ongkos kirim dilakukan melalui platform penyedia jasa tersebut, bukan melalui Lavora.

## 2. Pernyataan Masalah

Usaha laundry skala kecil sering kali mengelola kegiatan operasional menggunakan nota tulis tangan, perhitungan biaya secara manual, dan komunikasi melalui aplikasi pesan seperti WhatsApp. Cara tersebut dapat menyulitkan pemilik atau staf dalam mengatur pesanan pelanggan, memantau proses pencucian, serta menjaga keakuratan catatan pembayaran. Ketika jumlah pesanan meningkat, risiko kehilangan nota, kesalahan perhitungan biaya, dan tertukarnya pakaian pelanggan juga semakin besar.

Pelanggan juga dapat mengalami kesulitan untuk mengetahui perkembangan pesanan, termasuk apakah pakaian masih dalam proses pencucian atau sudah siap diambil. Selain itu, pelanggan yang membutuhkan layanan pengantaran harus mengatur pengiriman melalui penyedia jasa eksternal secara terpisah. Tanpa pencatatan metode pengambilan dan informasi pengiriman yang terorganisasi, pelanggan maupun staf dapat mengalami kesulitan dalam memastikan bagaimana pakaian akan diterima pelanggan.

Komunikasi mengenai perubahan status pesanan juga dapat menambah beban kerja staf apabila harus disampaikan secara manual kepada setiap pelanggan. Oleh karena itu, diperlukan mekanisme notifikasi agar pelanggan dapat memperoleh informasi mengenai perkembangan pesanan tanpa harus selalu menghubungi staf laundry.

Lavora dikembangkan untuk membantu mengatasi permasalahan tersebut melalui sistem terpusat yang dapat mengelola pesanan laundry, menghitung biaya layanan, memantau status pencucian, mencatat pembayaran, mengelola informasi metode pengambilan atau pengantaran, serta memberikan notifikasi perubahan status pesanan. Dengan adanya sistem ini, pelanggan dapat memantau pesanan mereka, sedangkan staf dan pemilik laundry dapat mengelola operasional secara lebih terorganisasi tanpa harus mengelola sistem pengiriman eksternal secara langsung.

## 3. Target Pengguna dan Aktor

### 3.1 Pelanggan (*Customer*)

Pelanggan menggunakan Lavora untuk:
- Membuat akun secara mandiri dan login ke sistem.
- Membuat dan melihat pesanan laundry miliknya.
- Memantau perkembangan dan status pesanan.
- Melihat rincian biaya layanan laundry.
- Memilih metode pembayaran online atau offline yang tersedia untuk layanan laundry.
- Memilih pengambilan sendiri atau menggunakan jasa pengiriman eksternal.
- Melihat informasi metode pengambilan dan menerima notifikasi perubahan status pesanan.

### 3.2 Staf Laundry (*Laundry Staff*)

Staf laundry menggunakan Lavora untuk:
- Login menggunakan akun dengan hak akses staf.
- Melihat dan mengelola pesanan pelanggan sesuai dengan hak aksesnya.
- Memperbarui status proses pencucian.
- Mencatat pembayaran offline dan memperbarui status pembayaran sesuai prosedur yang berlaku.
- Menyiapkan pesanan untuk diambil pelanggan atau diserahkan kepada layanan pengiriman eksternal.
- Mencatat informasi pengiriman yang diperlukan dalam pesanan.

### 3.3 Pemilik Laundry (*Laundry Owner/Admin*)

Pemilik laundry menggunakan Lavora untuk:
- Login ke sistem menggunakan akun pemilik.
- Mengelola harga layanan laundry.
- Membuat atau menyetujui akun staf serta mengatur hak aksesnya.
- Melihat dan memantau seluruh pesanan laundry.
- Mengawasi pencatatan pembayaran dan proses operasional.
- Mengelola pengaturan layanan laundry.

Dalam Lavora, pemilik laundry juga menjalankan fungsi administrasi sistem sehingga tidak diperlukan aktor admin yang terpisah.

## 4. Ruang Lingkup Proyek

### 4.1 Fitur yang Termasuk

Fitur yang termasuk dalam ruang lingkup Lavora adalah:
- Registrasi mandiri pelanggan dan autentikasi pengguna.
- Login dan pengaturan hak akses berdasarkan peran pelanggan, staf, dan pemilik.
- Pembuatan dan pengelolaan pesanan laundry.
- Perhitungan biaya layanan laundry berdasarkan ketentuan harga yang ditetapkan.
- Pemantauan dan pembaruan status pencucian.
- Pencatatan pembayaran serta pengelolaan status pembayaran layanan laundry.
- Dukungan alur pembayaran online dan offline secara konseptual.
- Pemilihan metode pengambilan sendiri atau pengiriman eksternal.
- Pencatatan informasi metode dan status pengiriman secara manual jika diperlukan.
- Pengiriman notifikasi kepada pelanggan mengenai perubahan status pesanan.
- Pengelolaan pengaturan notifikasi yang relevan dengan proses pesanan.

### 4.2 Fitur yang Tidak Termasuk

Fitur berikut tidak termasuk dalam ruang lingkup proyek Lavora saat ini:
- Integrasi langsung dengan bank, dompet digital, atau penyedia *payment gateway* untuk memproses transaksi online secara otomatis.
- Integrasi API dengan Gojek atau penyedia jasa pengiriman eksternal lainnya.
- Pengelolaan akun, penugasan, dan operasional kurir eksternal.
- Pelacakan lokasi kurir menggunakan GPS secara real-time.
- Optimasi rute pengiriman atau penentuan kurir secara otomatis.
- Pemesanan kurir eksternal secara langsung melalui Lavora.
- Pemrosesan dan pencatatan otomatis pembayaran ongkos kirim eksternal.
- Pengelolaan persediaan perlengkapan laundry.
- Pelaporan keuangan, akuntansi, dan analisis bisnis tingkat lanjut.
- Integrasi otomatis dengan platform pesan eksternal seperti WhatsApp.

Ongkos kirim eksternal dibayarkan oleh pelanggan melalui platform penyedia jasa pengiriman. Lavora berfokus pada pencatatan pesanan laundry dan informasi metode pengiriman yang relevan, bukan pada transaksi atau operasional jasa pengiriman tersebut.

Notifikasi dalam ruang lingkup proyek berfokus pada pemberian informasi perubahan status pesanan melalui mekanisme yang dirancang dalam sistem. Integrasi otomatis dengan layanan pesan eksternal tidak termasuk dalam ruang lingkup.

## 5. Tujuan Proyek

Tujuan Lavora adalah membantu meningkatkan keteraturan operasional usaha laundry melalui sistem manajemen yang terpusat. Sistem ini diharapkan dapat membantu pelanggan dalam membuat dan memantau pesanan, membantu staf dalam mengelola pesanan dan pembayaran, serta membantu pemilik dalam mengawasi operasional dan pengaturan layanan. Selain itu, mekanisme notifikasi diharapkan dapat mempermudah penyampaian informasi mengenai perkembangan pesanan kepada pelanggan.

Proyek ini berfokus pada pendokumentasian kebutuhan sistem, pembagian modul beserta ketergantungannya, pemodelan interaksi pengguna melalui diagram, penyusunan kasus pengujian, serta implementasi satu fungsi sederhana yang dilengkapi pengujian unit sesuai dengan ketentuan Ujian Akhir Semester mata kuliah Software Development Fundamentals.
