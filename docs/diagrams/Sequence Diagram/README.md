# Dokumentasi Sequence Diagram Lavora

Dokumen ini menjelaskan tiga sequence diagram utama pada sistem Lavora: login dan pembuatan pesanan, pemrosesan laundry dan pembaruan status, serta pembayaran dan serah terima pesanan. Setiap diagram menunjukkan urutan interaksi antara aktor, antarmuka Lavora, modul yang terlibat, dan database bila digunakan.

## Daftar Sequence Diagram

| ID | Skenario | Aktor utama | Modul yang terlibat | File diagram |
|---|---|---|---|---|
| SD1 | Login dan Pembuatan Pesanan | Pelanggan | M01, M02, M03 | [PNG](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/sd1-login-pemesanan.png) · [PlantUML](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/sd1-login-pemesanan.puml) |
| SD2 | Pemrosesan Laundry dan Pembaruan Status | Staf Laundry | M01, M02, M04, M07 | [PNG](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/SD2-Pemrosesan%20Laundry%20dan%20Pembaruan%20Status.png) · [PlantUML](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/SD2-Pemrosesan%20Laundry%20dan%20Pembaruan%20Status.puml) |
| SD3 | Pembayaran dan Serah Terima Pesanan | Pelanggan dan Staf Laundry | M01, M02, M04, M05, M06, M07 | [PNG](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/SD3%20-%20Pembayaran%20dan%20Serah%20Terima%20Pesanan.png) · [PlantUML](https://github.com/AryaPanji-VA/Lavora/blob/main/docs/diagrams/Sequence%20Diagram/SD3%20-%20Pembayaran%20dan%20Serah%20Terima%20Pesanan.puml) |

---

## SD1 — Login dan Pembuatan Pesanan Lavora

### Tujuan dan alasan penting

SD1 menjelaskan bagaimana pelanggan masuk ke sistem Lavora dan membuat pesanan laundry. Skenario ini penting karena autentikasi memastikan pesanan dibuat oleh pengguna yang memiliki akses, sedangkan perhitungan biaya dan penyimpanan pesanan memastikan pelanggan menerima ringkasan pesanan dengan total biaya yang sesuai.

### Aktor dan modul

- **Aktor:** Pelanggan.
- **M01 — Autentikasi dan Hak Akses:** memeriksa akun pelanggan dan memverifikasi sesi sebelum pesanan diproses.
- **M02 — Pengelolaan Pesanan:** menerima detail pesanan, meminta perhitungan biaya, dan menyimpan pesanan.
- **M03 — Perhitungan Biaya:** mengambil harga layanan dari database dan menghitung total biaya.
- **Database:** menyimpan data akun, harga layanan, dan pesanan.

### Alur utama

1. Pelanggan membuka halaman login dan Lavora menampilkan formulir login.
2. Pelanggan memasukkan email dan password. Antarmuka mengirimkan data login ke M01.
3. M01 memeriksa akun ke database dan menerima hasil pemeriksaan.
4. Jika akun valid, sistem menampilkan halaman utama. Jika tidak valid, sistem menampilkan pesan kesalahan.
5. Pelanggan mengisi detail pesanan dan antarmuka meneruskan detail tersebut ke M02.
6. M02 meminta M01 memverifikasi sesi pelanggan.
7. Jika sesi valid, M02 meminta M03 menghitung biaya. M03 mengambil harga layanan dari database dan mengembalikan total biaya.
8. M02 menyimpan pesanan ke database.
9. Jika penyimpanan berhasil, antarmuka menampilkan ringkasan pesanan kepada pelanggan.

### Alur alternatif

- **Akun tidak valid:** M01 mengembalikan hasil login gagal dan antarmuka menampilkan pesan kesalahan.
- **Sesi pelanggan tidak valid:** M01 menolak hak akses; pesanan tidak diproses dan pelanggan diminta login kembali.
- **Penyimpanan pesanan gagal:** database mengembalikan kegagalan, lalu antarmuka menampilkan pesan bahwa pesanan gagal dibuat.

### Hasil yang diharapkan

Jika seluruh proses berhasil, pesanan tersimpan dan pelanggan dapat melihat ringkasan pesanan beserta total biaya. Perhitungan biaya dilakukan pada saat pembuatan pesanan; SD3 menggunakan total biaya yang sudah tersimpan untuk proses pembayaran.

---

## SD2 — Pemrosesan Laundry dan Pembaruan Status

### Tujuan dan alasan penting

SD2 menjelaskan bagaimana staf laundry melihat pesanan masuk, memproses pakaian, dan memperbarui status pengerjaan. Skenario ini penting agar perkembangan laundry tercatat dan pelanggan memperoleh informasi status terbaru melalui notifikasi Lavora.

### Aktor dan modul

- **Aktor:** Staf Laundry.
- **M01 — Autentikasi dan Pengaturan Hak Akses:** memverifikasi akun staf saat login dan memeriksa hak akses ketika status diperbarui.
- **M02 — Pengelolaan Pesanan:** menyediakan daftar pesanan masuk dan detail pesanan.
- **M04 — Pelacakan Status Laundry:** menangani pembaruan status dan pencatatan riwayat status.
- **M07 — Pengelolaan Notifikasi Pelanggan:** memproses notifikasi perubahan status.
- **Antarmuka Lavora:** menjadi perantara interaksi staf dengan modul-modul sistem.

### Alur utama

1. Staf login melalui antarmuka Lavora. Data kredensial dikirim ke M01 untuk diverifikasi.
2. Setelah akun dinyatakan valid dengan peran staf, staf membuka daftar pesanan masuk.
3. Antarmuka meminta M02 mengambil daftar pesanan, lalu daftar tersebut ditampilkan kepada staf.
4. Staf memilih salah satu pesanan. M02 mengambil dan mengembalikan detail pesanan.
5. Staf memproses pakaian sesuai pesanan.
6. Setelah proses dimulai, staf mengubah status, misalnya dari **Menunggu Diproses** menjadi **Sedang Dicuci**.
7. Antarmuka mengirim permintaan pembaruan status ke M04.
8. M04 meminta M01 memverifikasi hak akses sesi staf.
9. Jika hak akses valid, M04 menyimpan status dan mencatat riwayat perubahan.
10. M04 meminta M07 membuat notifikasi berdasarkan ID pesanan dan status baru.
11. Setelah status berhasil diperbarui, antarmuka menampilkan status terbaru kepada staf.

### Alur alternatif

- **Hak akses tidak valid:** M04 menerima hasil verifikasi yang menolak akses, lalu antarmuka menampilkan pesan bahwa staf tidak memiliki akses.
- **Penyimpanan status gagal:** M04 mengembalikan informasi kegagalan dan antarmuka menampilkan pesan error.
- **Pembaruan berhasil:** status disimpan dan notifikasi perubahan status diproses oleh M07.

### Hasil yang diharapkan

Status laundry dan riwayatnya tercatat, lalu informasi status terbaru tersedia bagi proses notifikasi. Diagram ini berfokus pada pemrosesan laundry dan perubahan status, bukan pada pembayaran atau serah terima.

---

## SD3 — Pembayaran dan Serah Terima Pesanan

### Tujuan dan alasan penting

SD3 menjelaskan proses setelah laundry selesai, mulai dari pemberian informasi kepada pelanggan, pencatatan pembayaran, hingga pencatatan serah terima atau metode pengantaran. Skenario ini penting untuk memastikan pembayaran tercatat dan perubahan status pesanan dapat ditelusuri sebelum pesanan diserahkan atau disiapkan untuk pengantaran.

### Aktor dan modul

- **Aktor:** Pelanggan dan Staf Laundry.
- **M01 — Autentikasi dan Pengaturan Hak Akses:** memvalidasi akses pelanggan sebelum proses pembayaran.
- **M02 — Pengelolaan Pesanan:** mengambil detail pesanan dan total biaya yang sudah tersimpan.
- **M04 — Pelacakan Status Laundry:** memperbarui status laundry dan status pesanan.
- **M05 — Pengelolaan Pembayaran:** mencatat pembayaran dan mengembalikan hasil pencatatan.
- **M06 — Pengelolaan Pengambilan dan Pengantaran:** mencatat metode pengambilan atau pengantaran.
- **M07 — Pengelolaan Notifikasi Pelanggan:** memproses informasi laundry selesai dan informasi status terbaru.
- **Database:** menyimpan status laundry, data pembayaran, metode serah terima, dan perubahan status pesanan.

### Alur utama

1. Staf menandai laundry selesai melalui antarmuka Lavora.
2. Antarmuka meneruskan pembaruan ke M04. M04 menyimpan status ke database.
3. Setelah status tersimpan, M04 meminta M07 memproses notifikasi laundry selesai kepada pelanggan.
4. Pelanggan melakukan pembayaran melalui antarmuka Lavora.
5. M01 memvalidasi hak akses pelanggan.
6. M02 mengambil total biaya dari data pesanan yang telah tersimpan. SD3 tidak menghitung ulang biaya; perhitungan dilakukan di SD1 melalui M03.
7. Antarmuka mengirim permintaan pencatatan pembayaran ke M05.
8. Jika pembayaran berhasil dicatat, sistem memberikan konfirmasi pembayaran.
9. Staf memproses serah terima. Antarmuka mengirim pilihan pengambilan atau pengantaran ke M06.
10. M06 menyimpan metode serah terima ke database.
11. M06 meminta M04 memperbarui status pesanan. M04 menyimpan status terbaru dan meminta M07 memproses notifikasi.
12. Pelanggan menerima informasi status terbaru.

### Alur alternatif

- **Pembayaran gagal dicatat:** M05 mengembalikan hasil gagal, lalu antarmuka menampilkan pesan kesalahan kepada pelanggan. Alur serah terima tidak dilanjutkan dalam cabang ini.
- **Pembayaran berhasil dicatat:** sistem melanjutkan proses pencatatan serah terima, pembaruan status pesanan, dan pemrosesan notifikasi.

### Hasil yang diharapkan

Pembayaran tercatat, metode serah terima tersimpan, status pesanan diperbarui, dan pelanggan menerima informasi terbaru. Pengantaran oleh kurir eksternal tidak berarti Lavora terintegrasi langsung dengan sistem kurir; diagram ini hanya mencakup pencatatan metode dan informasi serah terima.

---

## Ringkasan keterlibatan modul

| Modul | SD1 | SD2 | SD3 |
|---|:---:|:---:|:---:|
| M01 — Autentikasi dan Pengaturan Hak Akses | ✓ | ✓ | ✓ |
| M02 — Pengelolaan Pesanan | ✓ | ✓ | ✓ |
| M03 — Perhitungan Harga dan Biaya | ✓ | — | — |
| M04 — Pelacakan Status Laundry | — | ✓ | ✓ |
| M05 — Pengelolaan Pembayaran | — | — | ✓ |
| M06 — Pengelolaan Pengambilan dan Pengantaran | — | — | ✓ |
| M07 — Pengelolaan Notifikasi Pelanggan | — | ✓ | ✓ |

Tanda centang menunjukkan bahwa modul terlibat dalam skenario tersebut, bukan berarti seluruh fungsi modul harus berjalan di setiap diagram.

## Catatan konsistensi

- SD1 menetapkan dan menyimpan total biaya pesanan; SD3 menggunakan total biaya tersebut untuk pembayaran.
- SD2 berfokus pada pemrosesan laundry dan pembaruan status, sedangkan SD3 berfokus pada pembayaran dan serah terima.
- Notifikasi merupakan bagian dari M07 dan diproses sesuai peristiwa yang relevan.
- Pembayaran online dalam ruang lingkup Lavora bersifat konseptual dan bukan integrasi payment gateway nyata.
- Operasional kurir eksternal berada di luar integrasi langsung Lavora.

