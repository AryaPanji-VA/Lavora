# Test — Lavora

Folder ini berisi deliverable **D6 (Test Case Design)** dan **D7 (Unit-Tested Code)**.

## Isi folder

| File | Isi |
|---|---|
| [`test_pricing.py`](test_pricing.py) | 10 unit test untuk fungsi `calculate_laundry_cost` |
| [`Test_Case_Design.md`](Test_Case_Design.md) | Tabel desain test case D6 (TC-01 s/d TC-10) |
| [`screenshot-2026-10-27_19-55-03.png`](screenshot-2026-10-27_19-55-03.png) | Bukti `pytest -v` lulus semua |
| `__init__.py` | Menandai folder ini sebagai package Python |

## Cara menjalankan

Dari root repo:

```bash
python3 -m pytest
```

Konfigurasi ada di [`../pytest.ini`](../pytest.ini) — `testpaths = test` membuat pytest hanya memindai folder ini, dan `pythonpath = .` membuat `from src.pricing import ...` bisa di-resolve dari direktori mana pun perintah dijalankan.

Untuk melihat nama tiap test:

```bash
python3 -m pytest -v
```

Hasil terakhir: **10 passed**.

## Fungsi yang diuji

`src/pricing.py` → `calculate_laundry_cost(weight_kg, service_type)`

Aturan bisnis yang diuji:

- Tarif `regular` Rp6.000/kg, `express` Rp10.000/kg.
- Berat di bawah 1 kg tetap dihitung 1 kg (minimum charge).
- Berat ≤ 0 ditolak dengan `ValueError`.
- Jenis layanan di luar daftar ditolak dengan `ValueError`.
- Input bukan angka ditolak dengan `TypeError` (termasuk `bool`, karena `True` di Python adalah `int`).
- Jenis layanan tidak peka huruf besar/kecil dan spasi di awal/akhir.

## Pemetaan test case D6 → unit test D7

| ID | Test case (D6) | Fungsi test (D7) | Hasil |
|---|---|---|---|
| TC-01 | Regular, berat bulat 3 kg | `test_regular_integer_weight` | Rp18.000 |
| TC-02 | Regular, berat desimal 2,5 kg | `test_regular_decimal_weight` | Rp15.000 |
| TC-03 | Express, berat bulat 2 kg | `test_express_integer_weight` | Rp20.000 |
| TC-04 | Express, berat desimal 1,5 kg | `test_express_decimal_weight` | Rp15.000 |
| TC-05 | Jenis layanan `" Express "` (kapital + spasi) | `test_case_insensitive_and_whitespace` | Rp20.000 |
| TC-06 | Berat 0,5 kg (di bawah minimum) | `test_minimum_weight_threshold` | Rp6.000 |
| TC-07 | Berat tepat 1 kg (batas minimum) | `test_exact_minimum_weight` | Rp6.000 |
| TC-08 | Berat 0 dan -1,5 kg | `test_zero_or_negative_weight` | `ValueError` |
| TC-09 | Jenis layanan `"super_fast"` | `test_invalid_service_type` | `ValueError` |
| TC-10 | Berat `"tiga kg"` dan `True` | `test_invalid_data_type` | `TypeError` |

## Cakupan pengujian

**Yang diuji:** perhitungan tarif untuk dua jenis layanan, aturan minimum charge, validasi berat, validasi jenis layanan, validasi tipe data, dan normalisasi input.

**Yang tidak diuji:** tampilan/UI, penyimpanan database, dan proses I/O lain. Sesuai ketentuan D7, fungsi yang diuji adalah satu aturan bisnis murni tanpa efek samping.
