# Modul 5: Manajemen Pembayaran

**Tanggung jawab:** Mengelola metode dan status pembayaran layanan laundry, baik online maupun offline, dengan alur online dimodelkan secara konseptual tanpa integrasi payment gateway. Pemilik laundry mengawasi pencatatan pembayaran.

**Fitur utama:**
- Pelanggan memilih metode pembayaran (online atau offline) untuk pesanannya
- Pelanggan melihat rincian biaya layanan dan status pembayaran pesanannya
- Staf laundry mencatat pembayaran offline dan memperbarui status pembayaran
- Status pembayaran (Belum Bayar atau Lunas)
- Pemilik laundry melihat dan mengawasi catatan pembayaran seluruh pesanan
- Riwayat pembayaran per pesanan, termasuk siapa yang mencatat
- Validasi pembayaran (pesanan yang sudah lunas tidak bisa dicatat lagi, jumlah harus sesuai tagihan)

**Bergantung pada:** Autentikasi dan Kontrol Akses (pelanggan hanya melihat pesanannya sendiri, hanya staf yang boleh mencatat, pemilik boleh mengawasi), Manajemen Pesanan (pembayaran melekat pada pesanan), Perhitungan Harga (sumber jumlah tagihan)

**Di luar cakupan:**
- Integrasi langsung dengan bank, dompet digital, atau payment gateway
- Pemrosesan dan pencatatan otomatis pembayaran ongkos kirim eksternal (ongkos kirim dibayar pelanggan langsung ke penyedia jasa pengiriman)
