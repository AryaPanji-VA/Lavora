# Modul 5 — Payment Management

## 1. Gambaran Umum
**ID Modul:** M05

**Tanggung jawab:** Modul ini bertanggung jawab untuk mengelola metode dan status pembayaran layanan laundry, baik online maupun offline. Alur pembayaran online dimodelkan secara konseptual tanpa integrasi dengan bank, dompet digital, atau payment gateway.

**Alasan pengelompokan:** Fitur memilih metode pembayaran, melihat rincian biaya dan status pembayaran, mencatat pembayaran offline, memvalidasi pembayaran, dan menyimpan riwayat pembayaran memiliki tujuan yang sama, yaitu mengelola pembayaran layanan laundry. Fitur-fitur tersebut dipisah dari perhitungan biaya karena menghitung biaya menghasilkan angka, sedangkan pembayaran mencatat apakah angka itu sudah dibayar. Dengan satu modul khusus, pelanggan dapat mengetahui status pembayarannya, staf dapat mencatat pembayaran secara akurat, dan pemilik dapat mengawasi pencatatannya.

## 2. Tujuan
- Memungkinkan pelanggan memilih metode pembayaran online atau offline.
- Memungkinkan pelanggan melihat rincian biaya layanan dan status pembayaran pesanannya.
- Memungkinkan staf laundry mencatat pembayaran offline dan memperbarui status pembayaran.
- Memungkinkan pemilik laundry mengawasi pencatatan pembayaran.

## 3. Aktor
- **Pelanggan:** memilih metode pembayaran serta melihat biaya dan status pembayaran pesanannya.
- **Staf Laundry:** mencatat pembayaran offline dan memperbarui status pembayaran.
- **Pemilik Laundry:** melihat dan mengawasi catatan pembayaran seluruh pesanan.

## 4. Fitur Utama

### 4.1 Pemilihan Metode Pembayaran
Pelanggan dapat memilih metode pembayaran online atau offline untuk pesanannya.

### 4.2 Informasi Biaya dan Status Pembayaran
Sistem menampilkan rincian biaya layanan dan status pembayaran (Belum Bayar atau Lunas) kepada pelanggan.

### 4.3 Pencatatan Pembayaran
Staf laundry mencatat pembayaran offline dan memperbarui status pembayaran sesuai prosedur yang berlaku. Sistem memvalidasi pembayaran sebelum dicatat.

### 4.4 Pengawasan Pembayaran
Pemilik laundry dapat melihat catatan pembayaran seluruh pesanan untuk mengawasi proses pencatatan.

### 4.5 Riwayat Pembayaran
Sistem menyimpan riwayat pembayaran setiap pesanan, termasuk staf yang mencatatnya.

## 5. Aturan Modul
- Setiap pembayaran harus terkait dengan satu pesanan yang valid.
- Jumlah tagihan berasal dari hasil perhitungan biaya layanan.
- Hanya staf laundry yang dapat mencatat pembayaran offline dan memperbarui status pembayaran.
- Pesanan yang sudah berstatus Lunas tidak dapat dicatat pembayarannya lagi.
- Jumlah pembayaran yang dicatat harus sesuai dengan tagihan.
- Pelanggan hanya dapat melihat pembayaran pesanan miliknya sendiri.
- Pemilik laundry dapat melihat seluruh catatan pembayaran.
- Ongkos kirim eksternal dibayar pelanggan langsung ke penyedia jasa pengiriman dan tidak dicatat dalam modul ini.

## 6. Ketergantungan dengan Modul Lain
- **[Modul 1 — Authentication & Access Control:](01-authentication-access-control.md)** memastikan hanya staf yang dapat mencatat pembayaran, pemilik dapat mengawasi, dan pelanggan hanya melihat pesanannya sendiri.
- **[Modul 2 — Order Management:](02-order-management.md)** menyediakan data dan ID pesanan yang menjadi dasar pencatatan pembayaran.
- **[Modul 3 — Pricing & Cost Calculation:](03-pricing-cost-calculation.md)** menyediakan jumlah tagihan layanan laundry.
