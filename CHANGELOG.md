# Changelog / Catatan Riwayat Perubahan 📜

Semua perubahan penting pada proyek gim **Pay o' May** (Gim Novel Visual Edukasi Kesadaran Finansial Mahasiswa Perantauan) akan didokumentasikan di berkas ini.  
*All notable changes to the **Pay o' May** educational financial awareness visual novel project will be documented in this file.*

Format berkas ini mengacu pada [Keep a Changelog](https://keepachangelog.com/id/1.0.0/) dan mengikuti kaidah [Semantic Versioning](https://semver.org/lang/id/).  
*This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and adheres to [Semantic Versioning](https://semver.org/).*

---

## [0.3.8] - 2026-10-24

### 🇬🇧 English
#### Added
- **Story Thread: Group Project Across the Month:**
  - Week 1 assigns a big group project (Billa, Axel, Michelle), Week 2 hosts the group at the player's place (raising the meal decision's stakes), Week 3 ties the charger emergency to the group deadline, and Week 4 opens with the presentation before Axel's trip invitation.
- **Vulnerable Sides of Axel and Michelle:**
  - Michelle admits strict budgeting is exhausting and explains why the 50/30/20 rule reserves 30 percent for wants (Week 3). Axel confesses he follows along out of fear of being excluded (Week 4), with a follow-up line if the player declines the trip.
- **Honesty Dilemma in Mom's Call (Week 4):**
  - When the player has PayLater debt, they choose between telling Mom everything (+2), telling part of it (+1), or claiming everything is fine (0). The choice changes Ending C's closing lines. `skor_max` increases by 2 only when this decision appears.
- Full English translations for all new dialogue, menu choices, and tips in `game/tl/english/script.rpy`.
#### Fixed
- `skor_max` changed from `define` to `default` so the dynamic maximum score is saved and restored correctly.
#### Changed
- **Version Bump to 0.3.8:**
  - Bumped version number in `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, and the hero badge in `docs/index.html`.

---

### 🇮🇩 Bahasa Indonesia
#### Ditambahkan (Added)
- **Benang Merah Cerita: Tugas Kelompok Sepanjang Bulan:**
  - Minggu 1 membagikan tugas besar kelompok (Billa, Axel, Michelle), Minggu 2 kelompok bekerja di kos pemain (menaikkan bobot keputusan makan), Minggu 3 menghubungkan keadaan darurat charger dengan tenggat kelompok, dan Minggu 4 dibuka dengan presentasi sebelum ajakan trip dari Axel.
- **Sisi Rapuh Axel dan Michelle:**
  - Michelle mengaku terlalu ketat menjaga anggaran itu melelahkan dan menjelaskan mengapa aturan 50/30/20 menyisakan 30 persen untuk keinginan (Minggu 3). Axel mengaku sering ikut-ikutan karena takut dijauhi (Minggu 4), dengan dialog lanjutan jika pemain menolak trip.
- **Dilema Kejujuran pada Telepon Mama (Minggu 4):**
  - Jika pemain punya utang PayLater, pemain memilih menceritakan semuanya (+2), sebagian (+1), atau mengaku semuanya aman (0). Pilihan ini memengaruhi kalimat penutup Ending C. `skor_max` bertambah 2 hanya saat keputusan ini muncul.
- Terjemahan Inggris lengkap untuk seluruh dialog, pilihan menu, dan tips baru pada `game/tl/english/script.rpy`.
#### Diperbaiki (Fixed)
- `skor_max` diubah dari `define` menjadi `default` agar skor maksimal dinamis tersimpan dan dipulihkan dengan benar.
#### Diubah (Changed)
- **Pembaruan Versi Gim ke 0.3.8:**
  - Memperbarui nomor versi pada `game/options.rpy`, komentar `game/script.rpy`, `README.md`, `CHANGELOG.md`, dan hero badge `docs/index.html`.

---

## [0.3.72] - 2026-10-24

### 🇬🇧 English
#### Added
- **Emergency Fund Withdrawal to Main Wallet Mechanic:**
  - Implemented the ability to withdraw savings from the digital bank emergency fund (`dana_darurat`) back into the main daily allowance (`uang`) whenever money runs low.
  - Added an interactive **⇄ Withdraw to Allowance** (`screen modal_tarik_dana`) button directly in the M-Banking HUD, enabling players to liquidate custom preset increments (Rp 50,000, Rp 100,000, Rp 200,000, or the full balance) at will.
  - Added in-story narrative financial check-in menus (`menu_tarik_darurat`) at the end of each week and before month-end evaluation, offering timely lifelines to prevent unexpected deficits or unfair starvation endings.
#### Changed
- **Version Bump to Minor Patch 0.3.72:**
  - Synchronized version `0.3.72` across `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, `docs/index.html`, and `docs/script.js`.
  - Added complete bilingual English translations in `game/tl/english/script.rpy` with zero lint errors and zero orphan translations.

---

### 🇮🇩 Bahasa Indonesia
#### Ditambahkan (Added)
- **Mekanik Penarikan Dana Darurat ke Tabungan Utama:**
  - Mengimplementasikan fitur pencairan simpanan dari pos dana darurat bank digital (`dana_darurat`) kembali ke rekening uang saku utama (`uang`) ketika saldo harian menipis.
  - Menambahkan tombol interaktif **⇄ Tarik ke Uang Saku** pada HUD M-Banking yang membuka modal pencairan (`screen modal_tarik_dana`), memungkinkan pemain mencairkan nominal sesuai kebutuhan (Rp 50.000, Rp 100.000, Rp 200.000, atau seluruh saldo).
  - Menghadirkan menu naratif otomatis (`menu_tarik_darurat`) pada akhir minggu dan sebelum evaluasi penutup akhir bulan, memberikan kesempatan bagi pemain menyelamatkan keuangan tanpa harus terjebak defisit jika masih memiliki simpanan darurat.
#### Diubah (Changed)
- **Pembaruan Versi ke Minor Patch 0.3.72:**
  - Menyelaraskan nomor versi `0.3.72` pada `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, `docs/index.html`, dan `docs/script.js`.
  - Melengkapi pelokalan dwibahasa Inggris di `game/tl/english/script.rpy` dengan 0 galat lint dan 0 orphan translations.

---

## [0.3.71] - 2026-10-24

### 🇬🇧 English
#### Added
- **Digital Bank Emergency Fund Interest Yield:**
  - Implemented weekly passive interest payout for emergency savings placed in digital bank pocket (`dana_darurat > 0`). Players receive 0.25% weekly yield (minimum Rp 500) accompanied by audio feedback (`sfx_koin`).
- **Student Financial Crisis Dilemma (Week 3):**
  - Enhanced the Week 3 broken charger crisis by introducing an explicit branching choice between liquidating digital bank emergency fund savings (protecting daily allowance) vs preserving savings yield by sacrificing living allowance (forcing extreme frugality on meals next week). Added partial combination support when emergency funds are partially funded.
- **Narrative Continuity & Watch Party Variation for Billa:**
  - In Week 2, when playing as default character Billa (`pakai_sprite_billa`), the movie watch party scene is set in Michelle's dorm room (`sinta`) with Michelle welcoming Billa, reflecting a natural friendship dynamic between female peers.
  - Michelle's dialogue in Week 3 was updated to warmly reminisce about the cozy girls' movie night in her room.
- **Minor vs Major Patch Versioning Rules:**
  - Updated [AGENTS.md](AGENTS.md) to define standard criteria differentiating Major Patches (`vX.X.(+1)`) from Minor Patches (`vX.X.X(+1)`).
#### Changed
- **Version Bump to Minor Patch 0.3.71:**
  - Synchronized version `0.3.71` across `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, `docs/index.html`, and `docs/script.js`.
  - Updated bilingual English translations in `game/tl/english/script.rpy` with zero lint errors and zero orphan translations.

---

### 🇮🇩 Bahasa Indonesia
#### Ditambahkan (Added)
- **Mekanik Bunga Tabungan Dana Darurat Bank Digital:**
  - Mengimplementasikan keuntungan bunga simpanan pasif mingguan jika pemain mengalokasikan dana darurat di kantong bank digital (`dana_darurat > 0`). Pemain memperoleh imbal hasil 0,25% per minggu (minimal Rp 500) dengan efek suara koin (`sfx_koin`).
- **Dilema Krisis Finansial Mahasiswa Perantauan (Minggu 3):**
  - Memperdalam momen darurat charger rusak di Minggu 3 dengan menghadirkan dilema nyata: memilih mencairkan dana darurat bank digital (uang makan harian aman) atau mempertahankan saldo tabungan demi bunga simpanan namun memangkas uang jajan (minggu depan makan seadanya). Dilengkapi opsi kombinasi jika dana darurat terisi sebagian.
- **Variasi Nobar Kamar Kos Michelle untuk Karakter Billa:**
  - Pada Minggu 2, jika menggunakan karakter default Billa (`pakai_sprite_billa`), kegiatan nonton bareng berpindah ke kamar kos Michelle (`sinta`) yang menyambut Billa dengan hangat, menciptakan dinamika pertemanan sesama mahasiswi yang lebih klop dan natural.
  - Dialog Michelle di Minggu 3 disesuaikan untuk mengingat momen seru nobar di kamarnya bersama Billa.
- **Aturan Pembaruan Patch Minor & Major:**
  - Memperbarui [AGENTS.md](AGENTS.md) dengan panduan resmi pembeda rilis Major Patch (`vX.X.(+1)`) dan Minor Patch (`vX.X.X(+1)`).
#### Diubah (Changed)
- **Pembaruan Versi ke Minor Patch 0.3.71:**
  - Menyelaraskan nomor versi `0.3.71` pada `game/options.rpy`, `game/script.rpy`, `README.md`, `CHANGELOG.md`, `docs/index.html`, dan `docs/script.js`.
  - Memperbarui pelokalan dwibahasa Inggris di `game/tl/english/script.rpy` dengan 0 galat lint dan 0 orphan translations.

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
