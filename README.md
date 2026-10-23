# Pay o' May 💰🎮

[![Engine](https://img.shields.io/badge/Engine-Ren'Py%208.5-blue.svg)](https://www.renpy.org/)
[![Python](https://img.shields.io/badge/Python-3.12-brightgreen.svg)](https://www.python.org/)
[![Metodologi](https://img.shields.io/badge/Methodology-GDLC-orange.svg)](https://en.wikipedia.org/wiki/Video_game_development)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Android%20|%20Linux%20|%20macOS-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-0.3.3-teal.svg)](CHANGELOG.md)

**Pay o' May** adalah gim novel visual (*visual novel*) simulasi edukasi kesadaran finansial yang dirancang khusus untuk mahasiswa perantauan. Pemain berperan sebagai mahasiswa tahun pertama yang harus mengelola uang saku bulanan terbatas sebesar **Rp 2.000.000** selama 31 hari (4 minggu) di tengah berbagai tekanan sosial, godaan belanja konsumtif, dan keadaan darurat nyata.

Proyek ini dikembangkan sebagai karya **Tugas Akhir** program studi **S1 Terapan Teknologi Rekayasa Multimedia (TRM)**, Fakultas Ilmu Terapan, **Universitas Telkom**.

---

## 📌 Latar Belakang & Tujuan

Banyak mahasiswa perantau yang menghadapi kesulitan mengelola keuangan pribadi karena belum terbiasa hidup mandiri, terjebak ilusi belanja kemudahan *PayLater*, atau terpengaruh tekanan sosial kawan sebaya (*FOMO*). 

**Tujuan Edukasi Gim:**
1. Memberikan pemahaman konsep *Pay Yourself First* dan pentingnya pos **Dana Darurat**.
2. Mengasah kemampuan membedakan kebutuhan pokok (*Needs*) dan keinginan gaya hidup (*Wants*).
3. Mengedukasi bahaya laten bunga serta biaya layanan utang konsumtif (*PayLater*).
4. Melatih keberanian menetapkan batasan finansial yang sehat (*financial boundary*) saat meminjamkan uang kepada kawan sebaya.
5. Mengukur efektivitas media pembelajaran interaktif menggunakan instrumen kuesioner **Pre-Test** dan **Post-Test**.

---

## 🎮 Fitur Utama

- **Papan Status HUD Real-Time (M-Banking Style):** Menampilkan sisa Saldo Uang Jajan dengan *progress bar* dinamis, akumulasi simpanan Dana Darurat, beban tagihan PayLater, dan status Piutang Teman.
- **Sistem Notifikasi Smartphone Adaptif (`layar_hp`):** Simulasi pesan push notifikasi ponsel pop-up (M-Banking, toko online, chat WhatsApp teman, dan promo supermarket).
- **11 Titik Keputusan Finansial:** Setiap pilihan memiliki konsekuensi langsung pada arus kas, rasio kebutuhan/keinginan, tingkat stres keuangan, dan alur naratif.
- **4 Cabang Ending Cerita:**
  - 🏆 **Ending A (Bendahara Handal):** Pengelolaan seimbang, memiliki dana darurat, bebas utang, dan mandiri tanpa bantuan tambahan.
  - 🛡️ **Ending B (Selamat Sampai Akhir Bulan):** Berhasil bertahan melewati bulan tanpa krisis utang.
  - ⚠️ **Ending C (Terjerat PayLater):** Menunda pembayaran belanja konsumtif hingga terjebak beban tagihan di bulan berikutnya.
  - 🍜 **Ending D (Mie Instan Akhir Bulan):** Uang saku habis sebelum akhir bulan akibat belanja impulsif dan ketiadaan dana darurat.
- **Rapor Keuangan Bulanan (E-Statement):** Evaluasi performa literasi keuangan komprehensif di akhir gim, menyajikan rekap arus kas, persentase skor, analisis *Needs vs Wants*, serta predikat Gelar Finansial (seperti *Akuntan Kos Teladan*, *Master Dana Darurat*, *Survivor Tanggal Tua*, atau *Korban Sungkan Teman*).
- **Estetika Retro Pixel Art:** Mengintegrasikan kit antarmuka pixel art *Everyday Life*, animasi partikel cuaca dinamis (*petals/rain*), dan efek transisi adegan kustom.

---

## 👥 Tokoh & Peran Naratif

| Karakter | Peran & Representasi |
| :--- | :--- |
| **(Pemain)** | Mahasiswa perantauan yang memegang kendali penuh atas uang sakunya. |
| **Dimas** | Sahabat karib yang impulsif, suka nongkrong, dan sering menjadi sumber tekanan sosial (*FOMO*). |
| **Sinta** | Mahasiswi bijak yang disiplin mencatat pengeluaran dan merepresentasikan literasi keuangan yang baik. |
| **Mama** | Orang tua yang mengirimkan uang saku dan memberikan dukungan moral serta nasihat keuangan. |
| **Tips Finansial** | Narator edukasi yang mengulas prinsip keuangan di setiap akhir keputusan dengan efek suara lonceng. |

---

## 🔬 Metodologi Pengembangan

Pengembangan gim mengadopsi kerangka kerja **Game Development Life Cycle (GDLC)**:
1. **Initiation:** Identifikasi masalah literasi keuangan mahasiswa dan penetapan tujuan edukasi.
2. **Pre-Production:** Penyusunan skenario percabangan cerita, perancangan mekanika anggaran, dan pembuatan instrumen Pre-Test/Post-Test.
3. **Production:** Pemrograman logika simulasi Ren'Py (Python), penataan UI pixel art, integrasi audio/SFX, dan pembuatan sprite ekspresi tokoh.
4. **Testing:** Verifikasi gameplay, pengujian validitas skenario, dan uji coba pengguna (responden mahasiswa).
5. **Release:** Kompilasi multiplatform (*Windows executable* dan *Android APK/AAB*) beserta evaluasi data kuesioner.

---

## 📥 Unduh & Mainkan (Download)

Gim **Pay o' May** dapat diunduh langsung untuk platform Windows PC dan perangkat Android melalui tautan di bawah ini:

| Platform | Format Berkas | Status | Tautan Unduhan (Download Link) |
| :--- | :--- | :--- | :--- |
| 🪟 **Windows PC** | `PayoMay-0.3.3-pc.zip` (Standalone Executable) | Siap Main | [🔗 Unduh untuk Windows](https://drive.google.com/drive/folders/1y-or1POxvo8BAoI7AzyYqSQIEUpLPOaK?usp=sharing) |
| 📱 **Android** | `cam.axcom.payomay-0.3.3-1792734216-release.apk` (Direct Install) | Siap Main | [🔗 Unduh APK Android](https://drive.google.com/drive/folders/1Vc10KSKxE-nm8-ji-it3tGMRei7bwDAj?usp=sharing) |

> 💡 **Petunjuk Pengguna Android:**  
> Jika menginstal file `.apk` secara manual di ponsel Android, pastikan mengaktifkan izin *"Install from Unknown Sources"* pada pengaturan keamanan perangkat.

---

## 💻 Cara Menjalankan & Mengembangkan

### Prasyarat
- [Ren'Py SDK](https://www.renpy.org/latest.html) versi 8.2 atau yang lebih baru (disarankan Ren'Py 8.4+ / 8.5+).
- Komputer dengan sistem operasi Windows, macOS, atau Linux.

### Menjalankan dari Kode Sumber (Source Code)
1. Klon repositori ini ke komputer lokal:
   ```bash
   git clone https://github.com/luthfirais/pay-o-may.git
   ```
2. Buka aplikasi **Ren'Py Launcher**.
3. Tambahkan direktori proyek `Pay o May` ke dalam daftar proyek di Ren'Py Launcher.
4. Pilih proyek **Pay o' May** dan klik tombol **Launch Project**.

### Kontrol Permainan
- **Klik Kiri / Spasi / Enter:** Melanjutkan dialog atau memilih opsi.
- **Roda Mouse (Scroll Up):** Membuka riwayat dialog sebelumnya (*backlog / history*).
- **Esc:** Membuka menu jeda (*pause menu*: Simpan, Muat, Opsi, Bantuan, Tentang).
- **Bilah Menu Atas:** Akses cepat ke Simpan Cepat, Muat, dan Pengaturan audio/tampilan.

---

## 📁 Struktur Direktori Proyek

```text
Pay o May/
├── game/
│   ├── audio/                # Musik latar (BGM Kevin MacLeod) & SFX UI
│   ├── everyday_transitions/ # Shader & ImageDissolve transisi kustom
│   ├── everyday_ui/          # Aset frame, tombol, dan ikon Everyday Life UI
│   ├── everyday_weather/     # Animasi efek cuaca partikel (petals/rain)
│   ├── fonts/                # Berkas tipografi PixelifySans.ttf
│   ├── images/               # Latar tempat (background) & sprite tokoh (Dimas, Sinta)
│   ├── gui.rpy               # Konfigurasi dimensi antarmuka Ren'Py
│   ├── options.rpy           # Informasi metadata versi & build gim
│   ├── screens.rpy           # Screen internal bawaan Ren'Py
│   ├── script.rpy            # Alur cerita utama, logika transaksi, HUD, & ending
│   └── ui_custom.rpy         # Screen kustom (Menu Utama, Rapor Finansial, About)
├── CHANGELOG.md              # Catatan riwayat pembaruan versi proyek
├── .gitignore                # Aturan pengecualian berkas git & proteksi keystore
└── README.md                 # Dokumentasi utama proyek repositori
```

---

## 🎨 Kredit & Lisensi Aset

- **Aset Visual & UI Kit:** *Everyday Life Dialogue UI* oleh **DaddyDarko** ([itch.io](https://daddydarko.itch.io/)).
- **Musik Latar (BGM):** Diciptakan oleh **Kevin MacLeod** ([incompetech.com](https://incompetech.com/)), dilisensikan di bawah *Creative Commons: By Attribution 4.0 International (CC BY 4.0)*.
- **Efek Suara (SFX):** *Everyday Life UI Sound Pack*.
- **Game Engine:** [Ren'Py Engine](https://www.renpy.org/) (Lisensi MIT).

---

## ⚠️ Penafian (Disclaimer)

Kisah, tokoh, dan skenario dalam permainan ini adalah fiksi yang dirancang untuk tujuan edukasi kesadaran finansial dalam rangka Tugas Akhir akademik. Nilai nominal, perhitungan bunga, dan situasi yang disajikan merupakan simplifikasi simulasi dan tidak dimaksudkan sebagai nasihat keuangan profesional (*financial advice*).

---

**Pengembang:**  
**Luthfi Rais Asral**  
Program Studi S1 Terapan Teknologi Rekayasa Multimedia  
Fakultas Ilmu Terapan, Universitas Telkom
