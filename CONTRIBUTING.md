# Contributing — alur kerja tim Lavora

Panduan ini dipakai semua anggota supaya riwayat commit dan pull request di repo ini bisa dicocokkan dengan [`ACTIVITY_LOG.md`](ACTIVITY_LOG.md).

## 1. Setup awal (sekali per orang)

```bash
git clone https://github.com/AryaPanji-VA/Lavora.git
cd Lavora

git config user.name "Nama Lengkap"
git config user.email "email@kampus.ac.id"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`git config` wajib diisi nama masing-masing. Commit atas nama orang lain tidak dihitung sebagai kontribusi.

## 2. Jangan commit langsung ke `main`

```bash
git checkout -b docs/d3-use-case
# kerjakan sesuatu
git add docs/D3-use-case.md
git commit -m "docs(d3): add use case explanation"
git push -u origin docs/d3-use-case
```

Lalu buka Pull Request ke `main`, dan minta minimal satu anggota lain memberi komentar.

## 3. Konvensi commit

```
<tipe>(<deliverable>): <ringkasan>
```

| Tipe | Dipakai untuk | Contoh |
|---|---|---|
| `docs` | dokumen deliverable | `docs(d4): explain why each scenario matters` |
| `feat` | kode fitur | `feat(d7): implement calculate_laundry_cost` |
| `test` | unit test | `test(d7): add 10 cases mirroring D6` |
| `fix` | perbaikan bug | `fix(d7): reject zero weight` |
| `chore` | konfigurasi repo | `chore: add pytest config` |

Hindari pesan seperti `update`, `Add files via upload`, atau `fix` tanpa keterangan — pesan seperti itu tidak bisa dipakai sebagai bukti kontribusi di activity log.

## 4. Review dan merge

- Minimal **2 Pull Request** per proyek, masing-masing dikomentari anggota lain.
- Komentar review harus substantif: sebut bagian mana yang dibaca dan apa yang perlu diperbaiki. `LGTM` atau `mantap` saja tidak dihitung.
- Author yang menanggapi komentar, lalu merge sendiri.

## 5. Sebelum membuka PR

```bash
python3 -m pytest
```

Harus semua lulus. Konfigurasi pytest ada di [`pytest.ini`](pytest.ini) (`testpaths = test`, `pythonpath = .`), jadi perintah di atas bisa dijalankan dari root repo.

## 6. Render ulang diagram

Source PlantUML ada di `docs/diagrams/`. Setelah mengubah `.puml`, render ulang PNG-nya — jangan pernah menghapus PNG tanpa menggantinya, karena gambar adalah bagian dari deliverable.

```bash
cd "docs/diagrams/Use Case Diagram"
curl -sS -X POST -H 'Content-Type: text/plain' \
  --data-binary @"use case lavora.puml" \
  https://kroki.io/plantuml/png -o "use case lavora.png"
file "use case lavora.png"    # harus "PNG image data", bukan "ASCII text"
```

Kalau hasil `file` berupa teks, berarti PlantUML menemukan kesalahan sintaks — baca isi file itu untuk melihat pesan errornya. Commit **source dan hasil render sekaligus**.

## 7. Mencatat aktivitas

Setiap selesai satu pekerjaan nyata, tambahkan satu baris di [`ACTIVITY_LOG.md`](ACTIVITY_LOG.md) dengan hash commit atau nomor PR-nya. Catat saat itu juga, bukan di akhir proyek.
