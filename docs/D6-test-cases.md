# D6 — Test Case Design

Dokumen ini merangkum desain test case untuk **satu skenario**, yaitu perhitungan biaya laundry pada SD1 (Login dan Pembuatan Pesanan). Fungsi yang diuji adalah `calculate_laundry_cost` di [`../src/pricing.py`](../src/pricing.py).

- **Implementasi unit test (D7):** [`../test/test_pricing.py`](../test/test_pricing.py)
- **Dokumen asal test case:** [`../test/Test_Case_Design.md`](../test/Test_Case_Design.md)
- **Bukti test lulus:** [`../test/screenshot-2026-10-27_19-55-03.png`](../test/screenshot-2026-10-27_19-55-03.png)

## 1. Aturan bisnis yang diuji

| Aturan | Nilai |
|---|---|
| Tarif layanan `regular` | Rp6.000 per kg |
| Tarif layanan `express` | Rp10.000 per kg |
| Minimum charge | Berat di bawah 1 kg tetap dihitung 1 kg |
| Berat tidak valid | ≤ 0 ditolak dengan `ValueError` |
| Jenis layanan tidak dikenal | Ditolak dengan `ValueError` |
| Tipe data berat salah | Ditolak dengan `TypeError` |
| Penulisan jenis layanan | Tidak peka huruf besar/kecil dan spasi di ujung |

## 2. Tabel test case

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|---|---|---|---|---|---|
| TC-01 | Hitung biaya cucian regular berat bulat | Common | Sistem siap menerima input tarif | Berat cucian 3 kg, layanan `regular` | Total biaya Rp18.000 |
| TC-02 | Hitung biaya cucian regular berat desimal | Common | Sistem siap menerima input tarif | Berat cucian 2,5 kg, layanan `regular` | Total biaya Rp15.000 |
| TC-03 | Hitung biaya cucian express berat bulat | Common | Sistem siap menerima input tarif | Berat cucian 2 kg, layanan `express` | Total biaya Rp20.000 |
| TC-04 | Hitung biaya cucian express berat desimal | Common | Sistem siap menerima input tarif | Berat cucian 1,5 kg, layanan `express` | Total biaya Rp15.000 |
| TC-05 | Penulisan jenis layanan huruf kapital dan spasi | Common | Sistem siap menerima input tarif | Berat cucian 2 kg, jenis layanan ditulis `" Express "` | Total biaya Rp20.000 (kapital dan spasi diabaikan) |
| TC-06 | Cucian di bawah berat minimum (0,5 kg) | Edge | Sistem menerapkan minimum charge 1 kg | Berat cucian 0,5 kg, layanan `regular` | Total biaya Rp6.000 (dihitung sebagai berat minimum 1 kg) |
| TC-07 | Cucian tepat pada batas minimum (1 kg) | Edge | Sistem menerapkan batas ambang | Berat cucian 1 kg, layanan `regular` | Total biaya Rp6.000 |
| TC-08 | Input berat bernilai nol atau negatif | Edge | Validasi input aktif | Berat cucian 0 kg dan -1,5 kg, layanan `regular` | Sistem menolak input dengan `ValueError` "Berat cucian harus lebih besar dari 0" |
| TC-09 | Jenis layanan tidak terdaftar | Edge | Validasi input aktif | Berat cucian 3 kg, jenis layanan `"super fast"` | Sistem menolak input dengan `ValueError` "Jenis layanan tidak valid" |
| TC-10 | Tipe data berat cucian bukan numerik | Edge | Validasi tipe data aktif | Berat cucian diisi `"tiga kg"` dan `True` | Sistem menolak input dengan `TypeError` "Berat harus berupa angka" |

**Komposisi:** 5 common case (TC-01 s/d TC-05) dan 5 edge case (TC-06 s/d TC-10).

## 3. Cara memilih edge case

Edge case dipilih dengan mencari titik di mana aturan bisnis berubah perilaku, bukan sekadar menambah variasi input. Batas minimum charge diuji dari dua sisi — 0,5 kg di bawah batas dan tepat 1 kg di batas — karena kesalahan yang paling sering terjadi adalah salah memakai operator pembanding, sehingga 0,9 kg bisa ikut tertagih penuh atau 1 kg justru dianggap di bawah minimum. Input tidak valid diambil dari tiga kategori yang dampaknya berbeda: berat nol atau negatif yang lolos validasi logika, jenis layanan tidak terdaftar yang berpotensi menimbulkan `KeyError` saat tarif dicari, dan tipe data salah seperti teks yang bisa membuat perhitungan menghasilkan nilai palsu. Nilai boolean `True` sengaja diuji karena di Python `True` dianggap `int` sehingga bisa lolos pengecekan tipe biasa dan menghasilkan biaya yang tidak masuk akal. Terakhir, variasi penulisan `" Express "` diuji karena input pengguna sering membawa spasi dan huruf kapital, dan normalisasi yang terlewat akan menolak input yang sebenarnya sah.

## 4. Pemetaan test case ke unit test D7

| ID | Fungsi test di `test_pricing.py` |
|---|---|
| TC-01 | `test_regular_integer_weight` |
| TC-02 | `test_regular_decimal_weight` |
| TC-03 | `test_express_integer_weight` |
| TC-04 | `test_express_decimal_weight` |
| TC-05 | `test_case_insensitive_and_whitespace` |
| TC-06 | `test_minimum_weight_threshold` |
| TC-07 | `test_exact_minimum_weight` |
| TC-08 | `test_zero_or_negative_weight` |
| TC-09 | `test_invalid_service_type` |
| TC-10 | `test_invalid_data_type` |

Setiap test case di tabel ini punya satu fungsi test yang sesuai, dan seluruhnya lulus dengan `python3 -m pytest` (10 passed).

## Ringkasan

Ada 10 test case untuk fungsi perhitungan biaya: 5 kasus normal dan 5 kasus batas. Kasus batas dipilih dari titik perubahan aturan (batas minimum 1 kg), dari input yang tidak valid secara logika maupun tipe data, dan dari variasi penulisan yang sering muncul di input pengguna. Semua test case dipetakan satu-satu ke fungsi test di D7, dan seluruhnya lulus.
