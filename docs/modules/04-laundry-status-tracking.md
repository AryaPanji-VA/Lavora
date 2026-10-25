# Modul 4: Laundry Status Tracking

**Tanggung Jawab:**

Modul ini bertanggung jawab mengelola dan memantau perkembangan proses laundry pelanggan. Modul ini memungkinkan staf laundry memperbarui status pesanan, sedangkan pelanggan dapat melihat perkembangan pesanan mereka.

**Data:**
- ID Pesanan (`order_id`)
- Status Laundry (`laundry_status`)
- Waktu Pembaruan Status (`updated_at`)
- ID Pengguna yang Memperbarui Status (`updated_by`)
- Status Sebelumnya (`previous_status`)

**Aturan:**
- Setiap pesanan harus memiliki ID pesanan yang valid agar status laundry dapat dilacak.
- Pelanggan hanya dapat melihat status pesanan miliknya sendiri.
- Staf laundry dan pemilik laundry memiliki hak akses untuk memperbarui status laundry.
- Status laundry harus sesuai dengan kondisi pengerjaan pesanan.
- Setiap perubahan status harus disimpan agar informasi pesanan selalu terbaru.
- Jika ID pesanan tidak ditemukan, sistem harus menampilkan pesan kesalahan.
- Sistem harus menolak pembaruan status oleh pengguna yang tidak memiliki hak akses.
- Perubahan status harus mengikuti alur proses laundry yang telah ditentukan oleh sistem.
- Informasi status harus diperbarui sesuai kondisi pesanan yang sebenarnya.

**Hubungan antar Modul:**
- `01-authentication-access-control.md`: Memverifikasi identitas dan hak akses pengguna sebelum melakukan pembaruan status laundry.
- `02-order-management.md`: Menyediakan data dan ID pesanan yang digunakan untuk melacak perkembangan laundry.
- `06-customer-notification.md`: Menggunakan informasi perubahan status untuk memberikan notifikasi kepada pelanggan.

**Alasan Pengelompokan:**

Fitur melihat status pesanan, memperbarui status pengerjaan cucian, memvalidasi ID pesanan, dan mencatat perubahan status memiliki tujuan yang sama, yaitu memantau perkembangan proses laundry. 
Oleh karena itu, fitur-fitur tersebut dikelompokkan dalam satu modul agar pelanggan dapat mengetahui perkembangan pesanan dan staf laundry dapat mengelola proses laundry secara terstruktur.
