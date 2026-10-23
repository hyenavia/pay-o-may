# Aturan Proyek Pay o' May

## Manajemen Versi Game
- Setiap kali melakukan perubahan kode, perbaikan bug, penyesuaian UI, atau penambahan fitur baru pada proyek game ini, **selalu perbarui (naikkan / bump) versi game dan dokumentasikan perubahannya**:
  1. Perbarui `define config.version = "..."` pada file `game/options.rpy`.
  2. Perbarui catatan versi di baris atas komentar file `game/script.rpy` (misal: `#  PAY O' MAY  (vX.Y.Z)`).
  3. Catat poin-poin perubahan pada berkas `CHANGELOG.md` di bawah judul versi baru tersebut (mengikuti format *Keep a Changelog*).
- Penomoran versi mengikuti pola semantik `0.1.x` (contoh: dari `0.1.5` -> `0.1.6` -> `0.1.7`, dst.) kecuali jika ada pembaruan besar.
