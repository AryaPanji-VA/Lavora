# Modul 6 — Pengelolaan Pengambilan dan Pengantaran

## 1. Gambaran Umum

**ID Modul:** M06

Modul ini bertanggung jawab untuk mencatat metode pengambilan atau pengantaran laundry yang dipilih pelanggan serta mengelola informasi yang diperlukan untuk proses tersebut. Fitur pengambilan mandiri dan pencatatan pengantaran dikelompokkan dalam satu modul karena keduanya berkaitan dengan proses penyerahan laundry kepada pelanggan setelah proses pengerjaan selesai.

Sistem Lavora hanya mengelola informasi pengambilan dan pengantaran laundry. Untuk pengantaran menggunakan layanan eksternal seperti Gojek, pemesanan kurir, pelacakan perjalanan, dan pembayaran ongkos kirim dilakukan di luar sistem Lavora.

## 2. Tujuan

- Memungkinkan pelanggan memilih metode pengambilan atau pengantaran laundry.
- Mencatat informasi yang diperlukan untuk proses pengambilan atau pengantaran.
- Membantu staf mengetahui metode penyerahan laundry untuk setiap pesanan.
- Memastikan informasi penyerahan laundry tercatat dengan jelas.

## 3. Aktor

- **Pelanggan:** memilih metode pengambilan atau pengantaran serta memberikan informasi yang diperlukan.
- **Staf Laundry:** melihat informasi penyerahan dan mencatat penyerahan laundry sesuai prosedur.
- **Pemilik Laundry:** memantau informasi pengambilan dan pengantaran pesanan.

Kurir dari layanan eksternal bukan aktor dalam sistem Lavora karena tidak menggunakan atau mengakses sistem.

## 4. Fitur Utama

### 4.1 Pemilihan Metode Penyerahan

Sistem memungkinkan pelanggan memilih salah satu metode penyerahan laundry:
- **Ambil sendiri:** pelanggan mengambil laundry langsung di tempat laundry.
- **Pengantaran eksternal:** pelanggan menggunakan layanan pengantaran pihak ketiga di luar sistem Lavora.

### 4.2 Pencatatan Informasi Pengambilan

Sistem menyimpan informasi yang diperlukan untuk proses pengambilan mandiri, termasuk pesanan terkait dan status penyerahannya.

### 4.3 Pencatatan Informasi Pengantaran

Untuk metode pengantaran eksternal, sistem mencatat informasi yang diperlukan, seperti metode pengantaran dan catatan penyerahan jika tersedia. Pelanggan melakukan pemesanan layanan kurir melalui aplikasi penyedia layanan secara terpisah.

### 4.4 Pembaruan Status Penyerahan

Staf dapat memperbarui status penyerahan laundry sesuai proses yang berlangsung. Untuk pengantaran eksternal, staf dapat mencatat ketika laundry telah diserahkan kepada kurir.

Lavora tidak melacak perjalanan kurir atau memperkirakan waktu kedatangan kurir.

### 4.5 Melihat Informasi Penyerahan

Pelanggan dapat melihat metode penyerahan dan status terkait pesanan miliknya. Staf dan pemilik dapat melihat informasi sesuai hak akses masing-masing.

## 5. Aturan Bisnis

1. Setiap pesanan harus memiliki metode penyerahan yang jelas sebelum proses penyerahan dilakukan.
2. Pelanggan dapat memilih pengambilan mandiri atau pengantaran menggunakan layanan eksternal.
3. Informasi pengambilan atau pengantaran harus terhubung dengan pesanan yang sesuai.
4. Laundry hanya dapat diserahkan setelah memenuhi ketentuan status pengerjaan yang berlaku.
5. Staf hanya dapat memperbarui informasi penyerahan sesuai hak aksesnya.
6. Pelanggan hanya dapat melihat informasi penyerahan untuk pesanan miliknya sendiri.
7. Pemesanan kurir, pelacakan perjalanan, dan pembayaran ongkos kirim layanan eksternal dilakukan di luar sistem Lavora.
8. Status penyerahan kepada kurir dicatat oleh staf berdasarkan proses penyerahan yang sebenarnya.

## 6. Ketergantungan dengan Modul Lain

- **[Modul 1 — Autentikasi dan Pengaturan Hak Akses:](01-authentication-access-control.md)** memastikan pengguna hanya dapat mengakses informasi sesuai perannya.
- **[Modul 2 — Pengelolaan Pesanan:](02-order-management.md)** menyediakan data pesanan yang membutuhkan pengambilan atau pengantaran.
- **[Modul 4 — Pelacakan Status Laundry:](04-laundry-status-tracking.md)** menyediakan informasi status pengerjaan untuk menentukan kesiapan laundry diserahkan.
