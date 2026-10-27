# Modul 7 — Customer Notification

## 1. Gambaran Umum
**ID Modul:** M07

**Tanggung jawab:** Modul ini bertanggung jawab untuk memberi tahu pelanggan mengenai perubahan status pesanan melalui mekanisme yang dirancang dalam sistem, sehingga pelanggan tidak perlu menghubungi staf laundry untuk menanyakan perkembangan pesanan.

**Alasan pengelompokan:** Fitur mengirim notifikasi perubahan status, menampilkan daftar notifikasi, menandai notifikasi sudah dibaca, dan mengatur jenis notifikasi memiliki tujuan yang sama, yaitu menyampaikan informasi perkembangan pesanan kepada pelanggan. Fitur-fitur tersebut dipisah karena tugasnya hanya menyampaikan informasi dari perubahan di modul lain, sehingga cara dan jenis notifikasi dapat diubah tanpa menyentuh logika pesanan atau status.

## 2. Tujuan
- Memberi tahu pelanggan ketika status pesanan berubah.
- Memberi tahu pelanggan ketika cucian siap diambil atau sudah diserahkan untuk pengantaran.
- Memungkinkan pelanggan melihat dan mengatur notifikasi pesanannya.

## 3. Aktor
- **Pelanggan:** menerima, melihat, dan mengatur notifikasi.
- **Staf Laundry:** memicu notifikasi secara tidak langsung saat memperbarui status pesanan.

## 4. Fitur Utama

### 4.1 Notifikasi Perubahan Status
Sistem membuat notifikasi secara otomatis ketika staf laundry memperbarui status pesanan.

### 4.2 Notifikasi Pengambilan atau Pengantaran
Sistem memberi notifikasi khusus ketika cucian siap diambil atau sudah diserahkan kepada layanan pengiriman eksternal.

### 4.3 Daftar Notifikasi
Pelanggan dapat melihat daftar notifikasi di akunnya dan menandai notifikasi sebagai sudah dibaca.

### 4.4 Pengaturan Notifikasi
Pelanggan dapat memilih jenis notifikasi pesanan yang ingin diterima.

## 5. Aturan Bisnis
- Notifikasi dibuat otomatis ketika status pesanan berubah.
- Notifikasi hanya dikirim kepada pelanggan pemilik pesanan.
- Pelanggan hanya dapat melihat notifikasi miliknya sendiri.
- Notifikasi disampaikan melalui mekanisme dalam sistem, bukan melalui platform pesan eksternal seperti WhatsApp.
- Pengaturan notifikasi hanya memengaruhi notifikasi milik pelanggan yang bersangkutan.

## 6. Ketergantungan dengan Modul Lain
- **[Modul 4 — Laundry Status Tracking:](04-laundry-status-tracking.md)** menyediakan informasi perubahan status yang menjadi pemicu notifikasi.
- **[Modul 2 — Order Management:](02-order-management.md)** menyediakan data pesanan, metode pengambilan, dan pelanggan penerima notifikasi.
- **[Modul 1 — Authentication & Access Control:](01-authentication-access-control.md)** memastikan notifikasi hanya tampil di akun pelanggan yang bersangkutan.
