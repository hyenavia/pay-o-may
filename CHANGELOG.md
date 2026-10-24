# Changelog / Catatan Riwayat Perubahan 📜

Semua perubahan penting pada proyek gim **Pay o' May** (Gim Novel Visual Edukasi Kesadaran Finansial Mahasiswa Perantauan) akan didokumentasikan di berkas ini.  
*All notable changes to the **Pay o' May** educational financial awareness visual novel project will be documented in this file.*

Format berkas ini mengacu pada [Keep a Changelog](https://keepachangelog.com/id/1.0.0/) dan mengikuti kaidah [Semantic Versioning](https://semver.org/lang/id/).  
*This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and adheres to [Semantic Versioning](https://semver.org/).*

---

## [0.3.7] - 2026-10-24

### 🇬🇧 English
#### Fixed
- **Comprehensive Story Dialogue & In-Game Text Localization:**
  - Translated all remaining 119 story dialogue blocks in `game/tl/english/script.rpy` covering Week 2 through Week 4 storylines, subroutines, and all 4 narrative endings.
  - Fixed HUD calendar week label `text _("Minggu [minggu]")` -> `Week [minggu]` and discretionary spending tracker `text _("Belanja Keinginan: [wants]x")` -> `Wants Spending: [wants]x`.
  - Translated top quick menu button `Opsi` -> `Options` with adjusted button width in `game/everyday_ui/everyday_ui_components.rpy`.
  - Localized all smartphone push notifications (`screen layar_hp`) including app labels (`Toko Online` -> `Online Store`), titles (`FLASH SALE!`, `Promo Paket Tahunan`, `DISKON AKHIR BULAN`, `Tagihan jatuh tempo`), and promotional message bodies.
  - Translated all transaction description tags (`ket`) across wallet, emergency fund, and PayLater records (e.g. `Kebutuhan pokok` -> `Basic needs`, `Nongkrong di kafe` -> `Cafe hangout`, `Sneakers baru` -> `New sneakers`, etc.) and debt status `Rp 0 (Bebas Utang)` -> `Rp 0 (Debt Free)`.
- **Ren'Py String Interpolation Runtime Error:**
  - Resolved `TypeError: %i format: a real number is required, not TagQuotingDict` in `game/tl/english/script.rpy` caused by unescaped percent signs (`0% interest` -> `0 percent interest`).
- **Comprehensive In-Game English Translations:**
  - Added full English translations for all previously untranslated game screens: About screen (`screen about`), How to Play guide (`screen help`), Monthly Financial Report / E-Statement (`screen rekap_finansial`), Pre-Test modal questionnaire (`screen kuesioner_pretest`), Ren'Py quit/return confirmation modals (`layout`), dynamic financial honorific evaluation titles (`hitung_gelar_finansial`), smartphone push banners (`screen layar_hp`), and live transaction notifications (`_lapor`).
- **Complete Landing Page Localization (`docs/`):**
  - Added missing `data-i18n` attributes and comprehensive translations for the 4 Pillars cards and subtitle, 50/30/20 budget slider marks and category cards, Ending cards (badges, conditions, and star ratings), character bios, and hero showcase tabs.
#### Added
- **Bilingual Project Documentation:**
  - Converted both [README.md](README.md) and [CHANGELOG.md](CHANGELOG.md) into comprehensive dual-language editions (English & Bahasa Indonesia).
#### Changed
- **Version Bump to 0.3.7:**
  - Bumped version number across `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, and `docs/index.html`.

---

### 🇮🇩 Bahasa Indonesia
#### Diperbaiki (Fixed)
- **Pelokalan Dialog Cerita & Antarmuka Gim Lengkap:**
  - Menerjemahkan 119 blok dialog cerita yang sebelumnya masih berbahasa Indonesia pada `game/tl/english/script.rpy` meliputi seluruh alur narasi Minggu 2 hingga Minggu 4, subrutin akhir minggu, serta ke-4 ending cerita.
  - Memperbaiki label kalender HUD `text _("Minggu [minggu]")` -> `Week [minggu]` dan penghitung belanja keinginan `text _("Belanja Keinginan: [wants]x")` -> `Wants Spending: [wants]x`.
  - Menerjemahkan tombol menu cepat bilah atas `Opsi` -> `Options` beserta penyesuaian lebar tombol pada `game/everyday_ui/everyday_ui_components.rpy`.
  - Melokalisasi seluruh push notification smartphone (`screen layar_hp`) mencakup label aplikasi (`Toko Online` -> `Online Store`), judul penawaran (`FLASH SALE!`, `Promo Paket Tahunan`, `DISKON AKHIR BULAN`, `Tagihan jatuh tempo`), serta isi pesannya.
  - Menerjemahkan seluruh keterangan transaksi (`ket`) pada mutasi saldo uang jajan, dana darurat, dan PayLater (seperti `Kebutuhan pokok` -> `Basic needs`, `Nongkrong di kafe` -> `Cafe hangout`, `Sneakers baru` -> `New sneakers`, dst.) serta status pelunasan `Rp 0 (Bebas Utang)` -> `Rp 0 (Debt Free)`.
- **Galat Format String Ren'Py (Crash Runtime):**
  - Mengatasi `TypeError: %i format: a real number is required, not TagQuotingDict` pada baris 163 `game/tl/english/script.rpy` akibat interpolasi karakter persen (`0% interest` -> `0 percent interest`).
- **Penerjemahan Antarmuka Gim Lengkap:**
  - Menerjemahkan seluruh layar dan komponen yang sebelumnya belum terlokalisasi: layar Tentang (`screen about`), Cara Bermain (`screen help`), Rapor Keuangan Bulanan / E-Statement (`screen rekap_finansial`), modal Pre-Test (`screen kuesioner_pretest`), dialog konfirmasi keluar/kembali Ren'Py (`layout`), gelar evaluasi finansial (`hitung_gelar_finansial`), banner push notification HP (`screen layar_hp`), dan teks notifikasi transaksi langsung (`_lapor`).
- **Pelokalan Menyeluruh Landing Page (`docs/`):**
  - Melengkapi atribut `data-i18n` dan kamus translasi untuk section 4 Pilar Pembelajaran Finansial, penanda slider & kartu kategori kalkulator 50/30/20, kartu cabang ending (lencana, syarat, dan gelar bintang), biografi tokoh, serta tab cuplikan hero.
#### Ditambahkan (Added)
- **Dokumentasi Dwibahasa Proyek:**
  - Menyusun berkas [README.md](README.md) dan [CHANGELOG.md](CHANGELOG.md) dalam format dwibahasa (Bahasa Indonesia & English).
#### Diubah (Changed)
- **Pembaruan Versi Gim ke 0.3.7:**
  - Memperbarui nomor versi pada `game/options.rpy`, komentar `game/script.rpy`, berkas `README.md`, `CHANGELOG.md`, dan landing page `docs/index.html`.

---

## [0.3.6] - 2026-10-24

### Ditambahkan (Added)
- **Dukungan Multi-Bahasa Gim (Bahasa Indonesia & English):**
  - Mengimplementasikan sistem pelokalan bahasa ganda (ID / EN) penuh menggunakan framework translasi bawaan Ren'Py (`Language(None)` untuk Bahasa Indonesia dan `Language("english")` untuk English).
  - Menambahkan baris konfigurasi bahasa (`Bahasa: [ ID ] [ EN ]`) pada layar Pengaturan/Preferensi gim (`game/everyday_ui/everyday_ui_components.rpy`).
  - Menyediakan berkas translasi bahasa Inggris lengkap untuk seluruh dialog cerita, narator, pilihan opsi, dan tips finansial (`game/tl/english/script.rpy`).
- **Dukungan Multi-Bahasa pada Landing Page Resmi (`docs/`):**
  - Menambahkan tombol pengalih bahasa interaktif (`ID / EN`) pada bilah navigasi atas (navbar) landing page.
  - Mengintegrasikan kamus translasi menyeluruh di `docs/script.js` untuk seluruh teks di landing page.
  - Menyesuaikan kalkulator anggaran 50/30/20 dan pesan kutipan cuplikan adegan agar memberikan nasihat finansial yang reaktif sesuai bahasa yang aktif.
  - Menerapkan penyimpanan preferensi bahasa pengguna di `localStorage` peramban.
- **Widget Antarmuka Panggilan Telepon Mama (`screen hud`):**
  - Mengintegrasikan kotak kartu panggilan khusus (*incoming call card*) di pojok kanan atas layar permainan tepat di bawah papan status M-Banking.
  - Menampilkan lencana hijau `📞 PANGGILAN`, status *"Tersambung"*, dan indikator *"● Suara aktif..."*.
  - Menampilkan avatar pixel art wajah Mama (`mama_avatar_[ekspresi].png`) yang reaktif sesuai emosi percakapan (senang, netral, khawatir, kecewa).

### Diubah (Changed)
- **Penyelarasan Tata Letak Kotak Informasi Riset Pre-Test pada Menu Utama (`screen main_menu`):**
  - Memindahkan kotak tooltip informasi riset dari pojok kanan bawah ke posisi tepat di bawah kolom tombol navigasi menu utama di sisi kiri layar.

---

## [0.3.5] - 2026-10-24

### Ditambahkan (Added)
- **Integrasi Aset Sprite Karakter Billa & Mama:**
  - Mengintegrasikan set ekspresi visual lengkap (senang, netral, khawatir, kecewa) untuk karakter utama **Billa** (`game/images/billa [ekspresi].png`) yang diadaptasi dari outfit karakter guru (*teacher*).
  - Mengintegrasikan set ekspresi visual lengkap (senang, netral, khawatir, kecewa) untuk karakter orang tua **Mama** (`game/images/mama [ekspresi].png`) yang diadaptasi dari outfit pemilik toko (*shopkeeper*).
- **Mekanisme Logika Sprite Dinamis untuk Karakter Utama (`pakai_sprite_billa`):**
  - Mengimplementasikan sistem pengenalan nama di `label nama_pemain`:
    1. Jika pemain menggunakan nama bawaan (*default* `Billa`), sprite visual Billa aktif (`pakai_sprite_billa = True`).
    2. Jika pemain menginput nama kustom, gim beralih ke mode visual sudut pandang orang pertama (*first-person point of view*).
- **Visualisasi Sprite Mama dalam Adegan Cerita:**
  - Menampilkan sprite Mama saat panggilan telepon uang saku di Prolog, telepon permohonan dana darurat charger di Minggu ke-3, sesi evaluasi mingguan di Minggu ke-4, serta di adegan penutup Ending A dan Ending D.
- **Tata Letak Dialog Multi-Karakter (`left` & `right`):**
  - Menyesuaikan posisi tampilan sprite saat dialog bersama Axel, Michelle, atau Mama: Billa berada di sisi kiri (`at left`) dan karakter kawan/orang tua di sisi kanan (`at right`).

### Diubah (Changed)
- **Penyelarasan Framing Avatar Karakter pada Landing Page (`docs/`):**
  - Mengoptimalkan framing avatar bundar pada section *Dramatis Personae* (`docs/style.css` - `.char-avatar-img`) dengan penyesuaian `object-position: center 8%` dan `transform-origin: center 14%`.
  - Memperbarui kartu karakter Billa dan Mama pada landing page (`docs/index.html`) dengan foto avatar resmi dari file sprite `billa.png` dan `mama.png`.

---

## [0.3.4] - 2026-10-23

### Ditambahkan (Added)
- **Modal Screen Kuesioner Pre-Test (`screen kuesioner_pretest`):**
  - Mengubah alur pengisian kuesioner Pre-Test di awal permainan dengan modal antarmuka tersendiri berbasis desain *Everyday Life UI*.
  - Menerapkan penguncian tombol konfirmasi (*gating*): tombol *"Saya sudah mengisi Pre-Test"* dinonaktifkan (`sensitive=False`) sampai pemain mengklik *"Buka tautan Pre-Test"*.
- **Aset Visual Latar Nobar (`bg nobar.png`):**
  - Menambahkan gambar latar pixel art baru (1920x1080) bernuansa malam yang menggambarkan kamar kos Dimas saat nobar serial streaming.
- **Aset Logo Judul Kustom & Tipografi Home Screen:**
  - Menambahkan logo plang pixel art Pay O' May berhias ornamen dedaunan dan bunga melati (`images/title_logo.png`) di pojok kanan atas layar menu utama beserta nomor versi di bawahnya.
  - Mengintegrasikan jenis huruf *Cinzel* (`fonts/Cinzel.ttf`) pada seluruh tombol navigasi menu utama, teks nomor versi, dan kotak informasi instrumen riset GDLC.

---

## [0.3.3] - 2026-10-23

### Ditambahkan (Added)
- **Integrasi Penuh Tautan Kuesioner Evaluasi Penelitian GDLC:**
  - Tautan formulir instrumen **Pre-Test** (`https://forms.gle/naX1XzHjQ1eWTvyXA`) pada introduksi cerita permainan.
  - Tautan formulir instrumen **Post-Test** (`https://forms.gle/rdtdaCXnA6eVhbHU8`) pada modal Rapor Finansial akhir bulan.
- Papan status peringatan dan instruksi pengisian kuesioner pada layar Rapor Finansial.

---

## [0.3.2] - 2026-10-23

### Diubah (Changed)
- Peningkatan keterbacaan tipografi teks judul antarmuka *Everyday Life UI*.
- Restrukturisasi panel navigasi *Quick Menu* in-game.

---

## [0.3.1] - 2026-10-23

### Ditambahkan (Added)
- Variasi opsi naratif tambahan pada skenario percabangan Minggu 1 s.d. 4.
- Penyesuaian bobot skor kesadaran finansial edukatif.

---

## [0.3.0] - 2026-10-23

### Ditambahkan (Added)
- Peningkatan alur cerita visual novel dari 8 keputusan menjadi 11 keputusan finansial.
- Skenario baru: ajakan ngopi estetik (Minggu 1), langganan streaming vs nobar kosan (Minggu 2), peminjaman uang darurat kawan sebaya (Minggu 3), dan promo diskon supermarket bulanan (Minggu 4).
- Peningkatan batas skor maksimal (`skor_max = 22`).

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
- Format angka mata uang Rupiah (`rp()`), sistem BGM/SFX, dan karakter cerita (Billa/Pemain, Axel, Michelle, Mama, Tips Finansial).
