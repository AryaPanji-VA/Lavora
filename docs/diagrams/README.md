# Diagram Lavora

Semua diagram dimodelkan dengan PlantUML. Setiap diagram disimpan dalam dua bentuk: source `.puml` dan hasil render `.png`. Keduanya wajib ada di repo.

| Folder | Isi | Penjelasan |
|---|---|---|
| [`Use Case Diagram/`](Use%20Case%20Diagram/) | `use case lavora.puml` + `.png` | Use case diagram sistem, 3 aktor, 17 use case — lihat [`docs/D3-use-case.md`](../D3-use-case.md) |
| [`Sequence Diagram/`](Sequence%20Diagram/) | `sd1-*.puml`, `SD2-*.puml`, `SD3-*.puml` + `.png` | Tiga sequence diagram — lihat [`docs/D4-sequence-diagrams.md`](../D4-sequence-diagrams.md) |

## Render ulang

```bash
cd "docs/diagrams/Use Case Diagram"
curl -sS -X POST -H 'Content-Type: text/plain' \
  --data-binary @"use case lavora.puml" \
  https://kroki.io/plantuml/png -o "use case lavora.png"
```

Untuk sequence diagram, ganti nama file pada perintah di atas. Periksa hasilnya dengan `file <nama>.png` — harus `PNG image data`, bukan `ASCII text`.
