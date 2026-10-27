# D6 & D7 — Test Case Design dan Unit-Tested Code

Dokumen ini menggabungkan dua deliverable yang saling terkait: **D6** (desain test case) dan **D7** (implementasi fungsi beserta unit test-nya). Keduanya dibahas bersama karena setiap test case di D6 punya satu fungsi test pasangannya di D7.

- **Fungsi yang diuji:** [`../src/pricing.py`](../src/pricing.py) → `calculate_laundry_cost`
- **Unit test:** [`../test/test_pricing.py`](../test/test_pricing.py)
- **Bukti test lulus:** [`../test/screenshot-2026-10-27_19-55-03.png`](../test/screenshot-2026-10-27_19-55-03.png)
- **Skenario yang diuji:** SD1 — Login dan Pembuatan Pesanan (bagian perhitungan biaya)

---

# Bagian 1 — D6: Test Case Design

## 1.1 Aturan bisnis yang diuji

| Aturan | Nilai |
|---|---|
| Tarif layanan `regular` | Rp6.000 per kg |
| Tarif layanan `express` | Rp10.000 per kg |
| Minimum charge | Berat di bawah 1 kg tetap dihitung 1 kg |
| Berat tidak valid | ≤ 0 ditolak dengan `ValueError` |
| Jenis layanan tidak dikenal | Ditolak dengan `ValueError` |
| Tipe data berat salah | Ditolak dengan `TypeError` |
| Penulisan jenis layanan | Tidak peka huruf besar/kecil dan spasi di ujung |

## 1.2 Tabel test case

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

## 1.3 Cara memilih edge case

Edge case dipilih dengan mencari titik di mana aturan bisnis berubah perilaku, bukan sekadar menambah variasi input. Batas minimum charge diuji dari dua sisi — 0,5 kg di bawah batas dan tepat 1 kg di batas — karena kesalahan yang paling sering terjadi adalah salah memakai operator pembanding, sehingga 0,9 kg bisa ikut tertagih penuh atau 1 kg justru dianggap di bawah minimum. Input tidak valid diambil dari tiga kategori yang dampaknya berbeda: berat nol atau negatif yang lolos validasi logika, jenis layanan tidak terdaftar yang berpotensi menimbulkan `KeyError` saat tarif dicari, dan tipe data salah seperti teks yang bisa membuat perhitungan menghasilkan nilai palsu. Nilai boolean `True` sengaja diuji karena di Python `True` dianggap `int` sehingga bisa lolos pengecekan tipe biasa dan menghasilkan biaya yang tidak masuk akal. Terakhir, variasi penulisan `" Express "` diuji karena input pengguna sering membawa spasi dan huruf kapital, dan normalisasi yang terlewat akan menolak input yang sebenarnya sah.

---

# Bagian 2 — D7: Unit-Tested Code

## 2.1 Fungsi yang diimplementasikan

```python
RATES = {
    "regular": 6000,
    "express": 10000,
}

def calculate_laundry_cost(weight_kg, service_type):
    if not isinstance(weight_kg, (int, float)) or isinstance(weight_kg, bool):
        raise TypeError("Berat harus berupa angka numerik!")
    if weight_kg <= 0:
        raise ValueError("Berat cucian harus lebih berat dari 0!")

    clean_service = service_type.strip().lower()
    if clean_service not in RATES:
        raise ValueError("Jenis layanan tidak valid!")

    # Aturan batas minimum 1.0kg
    billable_weight = max (1.0, float(weight_kg))

    total = billable_weight * RATES[clean_service]
    return int(total)
```

Fungsi ini dipilih karena merupakan satu aturan bisnis murni: tanpa database, tanpa jaringan, tanpa tampilan. Cukup satu perintah untuk membuktikan benar atau salahnya.

Keputusan implementasi:

- **Validasi menolak, bukan mengoreksi diam-diam.** Berat `0`, negatif, atau bertipe salah langsung melempar exception, sehingga kesalahan input tidak berubah menjadi tagihan palsu.
- **`bool` diperiksa terpisah.** Di Python `True == 1` dan `True` adalah `int`, jadi tanpa pengecekan khusus `calculate_laundry_cost(True, "regular")` akan menghasilkan Rp6.000.
- **Minimum charge memakai `max(1.0, berat)`.** Satu baris, dan nilainya persis di batas 1 kg tanpa pembulatan ke atas yang bisa melewati batas satu langkah.
- **Hasil dikembalikan sebagai `int`.** Rupiah tidak punya pecahan sen, jadi tipe keluaran ikut dipastikan.

## 2.2 Cara menjalankan test

Dari root repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m pytest
```

Hasil yang diharapkan:

```
10 passed
```

Konfigurasi ada di [`../pytest.ini`](../pytest.ini): `testpaths = test` membatasi pemindaian ke folder `test/`, dan `pythonpath = .` membuat `from src.pricing import calculate_laundry_cost` bisa di-resolve dari direktori mana pun perintah dijalankan.

## 2.3 Pemetaan test case D6 → unit test D7

| ID | Test case (D6) | Fungsi test (D7) | Hasil |
|---|---|---|---|
| TC-01 | Regular, berat bulat 3 kg | `test_regular_integer_weight` | Rp18.000 |
| TC-02 | Regular, berat desimal 2,5 kg | `test_regular_decimal_weight` | Rp15.000 |
| TC-03 | Express, berat bulat 2 kg | `test_express_integer_weight` | Rp20.000 |
| TC-04 | Express, berat desimal 1,5 kg | `test_express_decimal_weight` | Rp15.000 |
| TC-05 | Jenis layanan `" Express "` | `test_case_insensitive_and_whitespace` | Rp20.000 |
| TC-06 | Berat 0,5 kg (di bawah minimum) | `test_minimum_weight_threshold` | Rp6.000 |
| TC-07 | Berat tepat 1 kg (batas minimum) | `test_exact_minimum_weight` | Rp6.000 |
| TC-08 | Berat 0 dan -1,5 kg | `test_zero_or_negative_weight` | `ValueError` |
| TC-09 | Jenis layanan `"super_fast"` | `test_invalid_service_type` | `ValueError` |
| TC-10 | Berat `"tiga kg"` dan `True` | `test_invalid_data_type` | `TypeError` |

Sepuluh test case di D6 punya sepuluh fungsi test pasangan di D7 — tidak ada test case tanpa bukti eksekusi, dan tidak ada test yang menguji hal di luar tabel.

## 2.4 Cakupan pengujian

**Diuji:** perhitungan tarif dua jenis layanan, aturan minimum charge, validasi berat (nol dan negatif), validasi jenis layanan, validasi tipe data termasuk `bool`, dan normalisasi penulisan input.

**Tidak diuji:** tampilan/UI, penyimpanan database, dan proses I/O lain. Sesuai ketentuan D7, yang diuji adalah satu aturan bisnis murni tanpa efek samping, sehingga hasilnya bisa dibuktikan hanya dengan `pytest`.

**Bukti eksekusi:** [`screenshot-2026-10-27_19-55-03.png`](../test/screenshot-2026-10-27_19-55-03.png) — 10 test PASSED, `configfile: pytest.ini`.

---

## Ringkasan

D6 menghasilkan 10 test case untuk fungsi perhitungan biaya laundry: 5 kasus normal dan 5 kasus batas yang dipilih dari titik perubahan aturan, dari input tidak valid secara logika maupun tipe data, dan dari variasi penulisan yang sering muncul. D7 mengimplementasikan `calculate_laundry_cost` sebagai fungsi murni dengan validasi yang menolak input salah, lalu menutup kesepuluh test case itu dengan 10 unit test yang semuanya lulus lewat satu perintah `python3 -m pytest`.
