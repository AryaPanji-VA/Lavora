# D6. Test Case Design


| ID   | Title | Type | Preconditions | Input / Steps | Expected Result |
|-----------------------|-------|------|---------------|---------------|-----------------|
| TC-01 | Hitung biaya cucian regular berat bulat | Common | Sistem siap menerima input tarif | Berat cucian 3 kg dengan layanan regular | Total biaya Rp18.000 |
| TC-02 | Hitung biaya cucian regular berat desimal | Common | Sistem siap menerima input tarif | Berat cucian 2,5 kg dengan layanan regular | Total biaya Rp15.000 |
| TC-03 | Hitung biaya cucian express berat bulat | Common | Sistem siap menerima input tarif | Berat cucian 2 kg dengan layanan express | Total biaya Rp20.000 |
| TC-04 | Hitung biaya cucian express berat desimal | Common | Sistem siap menerima input tarif | Berat cucian 1,5 kg dengan layanan express | Total biaya Rp15.000 |
| TC-05 | Penulisan jenis layanan huruf kapital dan spasi | Common | Sistem siap menerima input tarif | Berat cucian 2 kg, jenis layanan ditulis " Express " dengan huruf kapital dan spasi | Total biaya Rp20.000 (huruf kapital dan spasi diabaikan) |
| TC-06 | Cucian di bawah berat minimum (0,5 kg) | Edge | Sistem menerapkan aturan minimum charge 1 kg | Berat cucian 0,5 kg dengan layanan regular | Total biaya Rp6.000 (dihitung sebagai berat minimum 1 kg) |
| TC-07 | Cucian tepat pada batas minimum (1 kg) | Edge | Sistem menerapkan batas ambang | Berat cucian 1 kg dengan layanan regular | Total biaya Rp6.000 |
| TC-08 | Input berat bernilai nol atau negatif | Edge | Validasi input aktif | Berat cucian -1,5 kg dengan layanan regular | Sistem menolak input dan menampilkan pesan "Berat cucian harus lebih besar dari 0" |
| TC-09 | Jenis layanan tidak terdaftar | Edge | Validasi input aktif | Berat cucian 3 kg dengan jenis layanan "super fast" yang tidak tersedia | Sistem menolak input dan menampilkan pesan "Jenis layanan tidak valid" |
| TC-10 | Tipe data berat cucian bukan numerik | Edge | Validasi tipe data aktif | Berat cucian diisi dengan tulisan "tiga kg" dan layanan regular | Sistem menolak input dan menampilkan pesan "Berat harus berupa angka" |

### Mengapa Memilih Edge Cases Ini?

Kasus edge dipilih untuk menguji kondisi khusus yang berpotensi menyebabkan kesalahan dalam perhitungan biaya laundry. Pengujian mencakup berat cucian di bawah batas minimum, tepat pada batas minimum, serta berat nol atau negatif untuk memastikan validasi berat berjalan dengan benar. Selain itu, jenis layanan yang tidak valid dan input berat berupa teks diuji untuk memastikan sistem dapat menolak input yang tidak sesuai. Pengujian variasi huruf kapital dan spasi juga dilakukan untuk memastikan sistem tetap mengenali jenis layanan yang valid meskipun format penulisannya berbeda.
