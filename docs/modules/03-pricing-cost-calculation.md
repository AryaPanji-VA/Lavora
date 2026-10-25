# Modul : Pricing & Cost Calculation

**Tanggung Jawab :**  
Modul ini bertanggung jawab menghitung total biaya layanan laundry berdasarkan berat cucian dan tarif per kilogram yang telah ditentukan oleh pemilik laundry. Modul ini juga memastikan perhitungan harga dilakukan secara akurat dan hasilnya dapat digunakan dalam pencatatan pesanan pelanggan.

**Data :**
- Berat Cucian (`weight_kg`)
- Tarif per Kilogram (`price_per_kg`)
- Total Harga (`total_price`)

**Aturan :**
- Berat cucian harus berupa angka yang valid dan lebih besar dari nol.
- Tarif per kilogram ditentukan dan dikelola oleh pemilik laundry.
- Sistem menghitung total harga berdasarkan berat cucian dikalikan tarif per kilogram.
- Tarif yang digunakan dalam perhitungan harus sesuai dengan tarif yang berlaku.
- Jika berat cucian atau tarif tidak valid, sistem harus menolak perhitungan dan memberikan pesan kesalahan.
- Total harga yang dihasilkan digunakan sebagai rincian biaya pada pesanan pelanggan.
- Pelanggan dapat melihat rincian harga, sedangkan staf menggunakan hasil perhitungan untuk membantu pencatatan pesanan.
- Perubahan tarif hanya dapat dilakukan oleh pemilik laundry sesuai dengan hak akses yang ditentukan.

**Hubungan antar Modul :**
- `02-order-management.md` : menerima hasil perhitungan total harga untuk disimpan sebagai bagian dari data pesanan laundry.
- `05-payment-management.md` : menggunakan total harga yang tercatat pada pesanan sebagai dasar pencatatan pembayaran pelanggan.
- `01-authentication-access-control.md` : memastikan hak akses pengguna sesuai dengan perannya, terutama ketika pemilik laundry mengelola tarif layanan.

**Alasan Pengelompokan :**  
Fitur pengelolaan tarif, validasi berat cucian, dan perhitungan total harga memiliki tujuan yang sama, yaitu memastikan biaya layanan laundry dihitung secara akurat dan konsisten. 
Oleh karena itu, fitur-fitur tersebut dikelompokkan dalam satu modul agar proses perhitungan harga terpusat, mudah dikelola oleh pemilik laundry, dan dapat diuji melalui fungsi `calculate_price(weight_kg, price_per_kg)`.
