# Lavora

Aplikasi pengelolaan laundry untuk mencatat pesanan, menghitung biaya otomatis, melacak status cucian, dan mencatat pembayaran.

Lavora dibuat untuk usaha laundry skala kecil yang masih memakai nota tulis tangan, hitungan manual, dan WhatsApp. Pencatatan terpusat membuat pesanan, biaya, status pengerjaan, pembayaran, dan metode penyerahan tidak lagi tercecer — dan pelanggan bisa memantau perkembangan cuciannya sendiri tanpa harus menghubungi staf.

## Tim

| Nama | NIM | GitHub |
|---|---|---|
| Arya Panji Vici Ayanda | `26110300014 ` | [@AryaPanji-VA](https://github.com/AryaPanji-VA) |
| Aryasatya Mu'adz Ramadhan | `26110300003` | [@aryasatyamr](https://github.com/aryasatyamr) |
| Bernardus Rionard L.S | `26110300017` | [@Rionard956](https://github.com/Rionard956) |

## Deliverables

| Kode | Deliverable | Dokumen | Bukti pendukung |
|---|---|---|---|
| D1 | Topic & Problem Statement | [`docs/D1-problem-statement.md`](docs/D1-problem-statement.md) | — |
| D2 | Module Breakdown | [`docs/D2-modules.md`](docs/D2-modules.md) | [`docs/modules/`](docs/modules/) (7 file modul) |
| D3 | Use Case Diagram | [`docs/D3-Use-Case.md`](docs/D3-Use-Case.md) | [PNG](docs/diagrams/Use%20Case%20Diagram/use%20case%20lavora.png) · [PlantUML](docs/diagrams/Use%20Case%20Diagram/use%20case%20lavora.puml) |
| D4 | Sequence Diagrams | [`docs/D4-Sequence-Diagrams.md`](docs/D4-Sequence-Diagrams.md) | [SD1](docs/diagrams/Sequence%20Diagram/sd1-login-pemesanan.puml) · [SD2](docs/diagrams/Sequence%20Diagram/SD2-Pemrosesan%20Laundry%20dan%20Pembaruan%20Status.puml) · [SD3](docs/diagrams/Sequence%20Diagram/SD3%20-%20Pembayaran%20dan%20Serah%20Terima%20Pesanan.puml) |
| D5 | Collaboration | [`ACTIVITY_LOG.md`](ACTIVITY_LOG.md) | [`README.md`](README.md) (file ini) |
| D6 | Test Case Design | [`docs/D6-test-cases.md`](docs/D6-test-cases.md) | [`test/Test_Case_Design.md`](test/Test_Case_Design.md) |
| D7 | Unit-Tested Code | [`src/pricing.py`](src/pricing.py) | [`test/test_pricing.py`](test/test_pricing.py) · [screenshot](test/screenshot-2026-10-27_19-55-03.png) |

Penjelasan folder test ada di [`test/README.md`](test/README.md).

## Cara menjalankan unit test

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

Untuk melihat nama tiap test, tambahkan `-v`:

```bash
python3 -m pytest -v
```

Konfigurasi pytest ada di [`pytest.ini`](pytest.ini): `testpaths = test` dan `pythonpath = .`, sehingga perintah di atas bisa dijalankan dari root repo.

## Struktur repo

```
.
├── README.md                  # file ini — peta deliverable
├── ACTIVITY_LOG.md            # log kontribusi per anggota
├── pytest.ini                 # konfigurasi pytest
├── requirements.txt           # dependensi
├── docs/
│   ├── D1-problem-statement.md
│   ├── D2-modules.md
│   ├── D3-Use-Case.md
│   ├── D4-Sequence-Diagrams.md
│   ├── D6-test-cases.md
│   ├── modules/               # rincian 7 modul
│   └── diagrams/              # source PlantUML + hasil render PNG
├── src/
│   └── pricing.py             # fungsi yang diuji (D7)
└── test/
    ├── test_pricing.py        # 10 unit test
    ├── Test_Case_Design.md    # tabel test case (D6)
    └── README.md
```

## Teknologi

- **Python 3** — bahasa implementasi
- **pytest** — framework unit test
- **PlantUML** (render via Kroki) — source diagram
- **Git & GitHub** — kolaborasi, pull request, dan activity log

## AI tools yang dipakai

| Alat | Kegunaan | Ditinjau oleh |
|---|---|---|
| Hermes Agent (Model: Gemini)| Membantu susun Diagram dan memeriksa konsistensi link antar dokumen serta hasil test, dan Menyusun pytest | Arya Panji |
| Chatgpt dan Claude | Membantu menyusun kalimat di Dokumentasi, Membuat Diagram, dan check inkonsistensi doc yang di buat sebelum commit | Bernardus Rionard |
| Claude | Membantu menyusun kalimat di Dokumentasi, Membuat Diagram, serta Menyusun ide, dan revisi inkonsistensi doc yang dibuat | Aryasatya Mu'adz Ramadhan |

Seluruh isi dokumen dan kode di repo ini diperiksa manual: setiap klaim di dokumen dicocokkan dengan file yang dirujuk, dan unit test dijalankan ulang sebelum diserahkan.

## Kontribusi

Aturan kerja tim dan konvensi commit dijelaskan di [`ACTIVITY_LOG.md`](ACTIVITY_LOG.md) bagian Notes. Setiap entri di log menunjuk ke commit atau pull request yang bisa diperiksa di GitHub.
