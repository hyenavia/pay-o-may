# Changelog

Semua perubahan penting pada proyek gim **Pay o' May** (Gim Novel Visual Edukasi Kesadaran Finansial Mahasiswa Perantauan) akan didokumentasikan di berkas ini.

Format berkas ini mengacu pada [Keep a Changelog](https://keepachangelog.com/id/1.0.0/) dan mengikuti kaidah [Semantic Versioning](https://semver.org/lang/id/).

---

## [0.3.3] - 2026-10-23

### Diubah (Changed)
- Menggabungkan konfigurasi `.gitignore` dan `gitignore-2` ke dalam satu berkas `.gitignore` yang komprehensif (mencakup pengecualian direktori cache/saves Ren'Py, artefak build `*-dists/`, kunci penandatanganan Android `*.keystore`/`*.jks`, serta pengaturan editor lokal dan OS).
- Menghapus berkas redundan `gitignore-2`.

---

## [0.3.2] - 2026-10-23

### Ditambahkan (Added)
- Berkas `CHANGELOG.md` untuk mencatat riwayat perubahan dan pembaruan versi proyek secara terstruktur.
- Aturan dokumentasi perubahan versi otomatis pada panduan pengembang `AGENTS.md`.
- Rangkuman catatan pembaruan versi pada layar info `Tentang` di dalam gim (`screen about`).

---

## [0.3.1] - 2026-10-23

### Ditambahkan (Added)
- **UI Papan Status (HUD):** Indikator *Piutang Teman* adaptif di pojok kanan atas yang muncul pada Minggu ke-4 jika pemain meminjamkan uang ke Dimas dan belum terlunasi.
- **UI Notifikasi Ponsel (`layar_hp`):** Ikon dinamis adaptif pada header banner push notification (`icon_message_idle` untuk pesan chat Dimas, `icon_bookmark_idle` untuk langganan streaming dan supermarket, serta `icon_bell_idle` untuk perbankan/PayLater).
- **Rapor Finansial (E-Statement):** Baris status *Piutang Teman* pada kolom Arus Kas & Saldo serta baris evaluasi *Langganan Hiburan* pada kolom Analisis Keputusan.
- **Sistem Gelar Finansial:** Gelar evaluasi baru *"Korban Sungkan Teman"* untuk mengedukasi batas kerelaan meminjamkan uang kepada teman sebaya.
- **Efek Audio (SFX):**
  - Efek suara `sfx_peringatan` saat mengambil paket tahunan streaming mahal, saat Dimas mengabarkan penundaan ganti utang, dan saat belanja borongan saat saldo kritis.
  - Efek suara `sfx_click` saat memasang pengingat kalender HP, menolak tawaran pinjaman secara sopan dengan solusi anggaran, dan menutup aplikasi diskon.
- **Sprite Karakter Dinamis:**
  - Kemunculan sprite Dimas berekspresi senang saat pemain memilih opsi nobar camilan di kos pada Minggu ke-2.
  - Transisi ekspresi Dimas di Minggu ke-4: ekspresi khawatir saat belum bisa membayar utang, dan ekspresi netral reflektif saat merefleksikan penyusunan anggaran bersama.
  - Dialog kontekstual Sinta di Minggu ke-3 yang menanggapi keputusan langganan streaming pemain.

### Diperbaiki (Fixed)
- Nilai fallback skor maksimal pada fungsi evaluasi gelar `hitung_gelar_finansial()` dan `screen rekap_finansial()` disinkronkan menjadi `22` (11 titik keputusan x 2 poin).
- Ambang batas frekuensi keputusan keinginan (*wants*) disesuaikan menjadi $\le 3$ untuk gelar *"Pejuang Hemat & Terencana"*.
- Variabel state `pinjaman_dimas` di-reset menjadi `0` secara otomatis saat Dimas mengembalikan uang pinjaman parsial di Minggu ke-4.
- Banner push notification HP ditutup seketika setelah pilihan menu diklik agar tidak menutupi tampilan dialog dan sprite karakter.

---

## [0.3.0] - 2026-10-23

### Ditambahkan (Added)
- **Percabangan Baru 1 (Minggu 2):** Dilema langganan serial film streaming (Paket Tahunan Rp 300.000 vs Bulanan Rp 54.000 vs Nonton Bareng di Kos Teman Rp 15.000).
- **Percabangan Baru 2 (Minggu 3):** Dilema pinjaman uang antar-teman sebaya (Pinjamkan Penuh Rp 200.000 vs Pinjamkan Seikhlasnya Rp 50.000 vs Tolak Sopan & Susun Anggaran Bersama).
- **Percabangan Baru 3 (Minggu 4):** Godaan diskon promo akhir bulan supermarket (Borong Promo Rp 180.000 vs Beli Kebutuhan Mendesak Rp 45.000 vs Pakai Stok yang Ada).
- Peningkatan total skor maksimal kesadaran finansial (`skor_max`) dari 16 poin (8 keputusan) menjadi 22 poin (11 keputusan).
- Variabel tracking baru: `langganan`, `pinjam_dimas`, dan `pinjaman_dimas`.

---

## [0.2.1] - 2026-10-23

### Ditambahkan (Added)
- Efek animasi partikel cuaca kelopak bunga melayang (`el_weather petals`) pada Menu Utama (Home Screen).
- Efek transisi kustom pixel art Everyday Life (`el_shoreline_sweep`, `el_diamond_iris`, `el_mosaic_tiles`, `el_lantern_glow`).
- Sistem banner notifikasi pop-up transaksi real-time adaptif (+/- saldo uang jajan, dana darurat, dan utang PayLater).
- Pengaturan rendering grafis pixel art tajam (`nearest_neighbor = True`, `mipmap = False`) dengan font retro *Pixelify Sans*.

---

## [0.2.0] - 2026-10-22

### Ditambahkan (Added)
- Integrasi kit antarmuka kustom *Everyday Life Dialogue UI* (DaddyDarko) ke dalam seluruh sistem screen Ren'Py.
- Layar jeda kustom (`pausa_menu`), layar konfirmasi kustom, dan layar slot simpan/muat (`save`/`load`).
- Layar Menu Utama dinamis dengan dukungan pergantian tema warna (`cream`, `midnight`, `sunset`).
- Layar panduan bermain (`screen help`) dan informasi proyek Tugas Akhir GDLC (`screen about`).
- Modal Rapor Keuangan Mahasiswa (`screen rekap_finansial`) sebagai e-statement penutup evaluasi permainan.

---

## [0.1.0] - 2026-10-21

### Ditambahkan (Added)
- Inisialisasi awal proyek gim novel visual edukasi literasi keuangan mahasiswa perantauan *Pay o' May*.
- Mekanisme simulasi anggaran bulanan Rp 2.000.000 selama 4 minggu (alokasi kebutuhan pokok mingguan Rp 250.000/minggu).
- Logika instrumen penelitian GDLC: kuesioner Pre-Test sebelum prolog dan kuesioner Post-Test setelah epilog permainan.
- Sistem 4 cabang ending naratif (Ending A: Bendahara Handal, Ending B: Selamat, Ending C: Terjerat PayLater, Ending D: Defisit/Mie Instan).
- Format angka mata uang Rupiah (`rp()`), sistem BGM/SFX, dan karakter cerita (Raka/Pemain, Dimas, Sinta, Mama, Tips Finansial).
