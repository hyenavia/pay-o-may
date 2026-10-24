# ============================================================
#  PAY O' MAY  (v0.3.7)
#  Gim novel visual edukasi kesadaran finansial mahasiswa perantauan
#  Ren'Py 8.5.3
# ============================================================

# ------------------------------------------------------------
# 1. FUNGSI BANTU & LOGIKA SISTEM (HELPER FUNCTIONS)
# ------------------------------------------------------------
init python:
    import store

    def rp(n):
        """
        Format angka bulat ke format mata uang Rupiah standar Indonesia.
        Contoh: 1700000 -> 'Rp 1.700.000', -250000 -> '-Rp 250.000'
        """
        s = "{:,}".format(abs(int(n))).replace(",", ".")
        if n < 0:
            return "-Rp " + s
        return "Rp " + s

    # ---------- PENGELOLAAN AUDIO (BGM & SFX) ----------
    def _cari_audio(nama):
        """
        Mencari file audio di folder 'audio/' dengan berbagai format (.ogg, .mp3, .wav, .opus).
        Mengembalikan path jika ditemukan, atau None jika belum tersedia.
        """
        if not nama:
            return None
        for ext in ("ogg", "mp3", "wav", "opus"):
            p = "audio/" + nama + "." + ext
            if renpy.loadable(p):
                return p
        return None

    def musik(nama, fadein=1.0, fadeout=1.0, loop=True):
        """
        Memutar musik latar (BGM) pada channel music dengan efek transisi fadein.
        Jika nama None/kosong atau tidak ditemukan, musik akan berhenti bertahap (fadeout).
        """
        if not nama:
            renpy.music.stop(fadeout=fadeout)
            return
        p = _cari_audio(nama)
        if p is None:
            renpy.music.stop(fadeout=fadeout)
        elif renpy.music.get_playing() != p:
            renpy.music.play(p, fadein=fadein, loop=loop)

    def sfx(nama):
        """
        Memutar efek suara (SFX) satu kali pada channel sound jika filenya ada.
        """
        p = _cari_audio(nama)
        if p is not None:
            renpy.sound.play(p)

    def tip_callback(event, interact=True, **kwargs):
        """
        Callback otomatis untuk Character 'Tips Finansial'.
        Memutar sound effect 'sfx_tip' tepat saat dialog tips mulai ditampilkan.
        """
        if event == "begin" and interact:
            sfx("sfx_tip")

    # Musik latar bawaan di menu utama (jika ada file audio/bgm_menu.ogg)
    _menu_bgm = _cari_audio("bgm_menu")
    if _menu_bgm is not None:
        config.main_menu_music = _menu_bgm

    # ---------- SISTEM TRANSAKSI KEUANGAN & NOTIFIKASI ----------
    def _tr(s):
        """
        Menerjemahkan teks runtime Python ke bahasa yang sedang aktif di preferensi game.
        """
        if not s:
            return ""
        return renpy.translation.translate_string(s)

    def _lapor(teks, warna):
        """
        Menampilkan pesan banner notifikasi popup di layar dengan warna teks tertentu.
        """
        renpy.notify("{color=" + warna + "}" + teks + "{/color}")

    def ubah_uang(jumlah, ket=""):
        """
        Menambah atau mengurangi saldo uang jajan harian/bulanan.
        - Jika saldo tidak mencukupi saat terjadi pengeluaran, saldo diset menjadi Rp 0
          dan sisa defisit dialihkan otomatis menjadi tagihan PayLater.
        - Memperbarui variabel 'uang' (dan 'hutang' jika terjadi defisit) di store.
        - Memunculkan banner notifikasi perubahan saldo / pemindahan ke PayLater.
        - Memutar efek suara transaksi 'sfx_koin' / 'sfx_peringatan'.
        """
        if jumlah >= 0:
            store.uang += jumlah
            teks = _tr(_("Uang jajan +")) + rp(jumlah)
            if ket:
                teks += " (" + _tr(_(ket)) + ")"
            _lapor(teks, "#a5d6a7")
            sfx("sfx_koin")
        else:
            biaya = abs(jumlah)
            if store.uang >= biaya:
                store.uang -= biaya
                teks = _tr(_("Uang jajan -")) + rp(biaya)
                if ket:
                    teks += " (" + _tr(_(ket)) + ")"
                _lapor(teks, "#ff8a80")
                sfx("sfx_koin")
            else:
                sisa_uang = max(0, store.uang)
                defisit = biaya - sisa_uang
                store.uang = 0
                store.hutang += defisit
                if sisa_uang > 0:
                    teks = _tr(_("Saldo uang jajan habis! Defisit ")) + rp(defisit) + _tr(_(" dialihkan ke PayLater"))
                else:
                    teks = _tr(_("Saldo Rp 0! Tagihan PayLater +")) + rp(defisit)
                if ket:
                    teks += " (" + _tr(_(ket)) + ")"
                _lapor(teks, "#ffb74d")
                sfx("sfx_peringatan")

    def ubah_dana(jumlah, ket=""):
        """
        Menambah atau mengurangi simpanan Dana Darurat secara langsung.
        - Memperbarui variabel 'dana_darurat' di store.
        - Memunculkan notifikasi berwarna biru muda.
        - Memutar efek suara transaksi 'sfx_koin'.
        """
        store.dana_darurat += jumlah
        tanda = "+" if jumlah > 0 else "-"
        teks = _tr(_("Dana darurat ")) + tanda + rp(abs(jumlah))
        if ket:
            teks += " (" + _tr(_(ket)) + ")"
        _lapor(teks, "#81d4fa")
        sfx("sfx_koin")

    def pindah_ke_dana(jumlah):
        """
        Memindahkan sejumlah uang dari saldo 'uang jajan' ke pos 'dana darurat'.
        Mencerminkan konsep 'Pay Yourself First' di awal/pertengahan bulan.
        """
        store.uang -= jumlah
        store.dana_darurat += jumlah
        _lapor(_tr(_("Dipindah ke dana darurat: ")) + rp(jumlah), "#81d4fa")
        sfx("sfx_koin")

    def tambah_hutang(jumlah, ket=""):
        """
        Mencatat penambahan utang konsumtif PayLater.
        - Menambah variabel 'hutang' di store.
        - Memunculkan notifikasi berwarna oranye peringatan.
        - Memutar efek suara 'sfx_notif'.
        """
        store.hutang += jumlah
        teks = _tr(_("Tagihan PayLater +")) + rp(jumlah)
        if ket:
            teks += " (" + _tr(_(ket)) + ")"
        _lapor(teks, "#ffcc80")
        sfx("sfx_notif")

    # ---------- PLACEHOLDER GAMBAR OTOMATIS (FALLBACK) ----------
    def placeholder_bg(label, color):
        """Membuat displayable latar belakang darurat jika file background asli hilang."""
        return Fixed(
            Solid(color),
            Text("BG: " + label, size=28, color="#ffffff", xalign=0.5, yalign=0.15)
        )

    def placeholder_sprite(label, color):
        """Membuat kotak warna karakter darurat jika sprite asli hilang."""
        return Fixed(
            Solid(color, xsize=240, ysize=520),
            Text(label, size=28, color="#000000", xalign=0.5, yalign=0.5, text_align=0.5),
            xysize=(240, 520)
        )

    def pasang_placeholder():
        """
        Mengecek keberadaan file gambar penting (latar & ekspresi tokoh).
        Jika ada aset yang belum ada, digantikan dengan placeholder agar game tidak crash.
        """
        latar = [
            ("bg kos",    "Kamar Kos (Siang)",   "#5c6bc0"),
            ("bg kampus", "Kampus",              "#26a69a"),
            ("bg malam",  "Kamar Kos (Malam)",   "#263238"),
            ("bg akhir",  "Kamar Kos (Senja)",   "#8d6e63"),
        ]
        for nama, label, warna in latar:
            if not renpy.loadable("images/" + nama + ".png"):
                renpy.image(tuple(nama.split()), placeholder_bg(label, warna))

        tokoh = [("dimas", "#ffb74d"), ("sinta", "#f48fb1"), ("billa", "#4db6ac"), ("mama", "#ff8a65")]
        ekspresi = ["netral", "senang", "khawatir", "kecewa"]
        for t, warna in tokoh:
            for e in ekspresi:
                if not renpy.loadable("images/" + t + " " + e + ".png"):
                    label = t.upper() + "\n" + e
                    renpy.image((t, e), placeholder_sprite(label, warna))

    pasang_placeholder()

# ------------------------------------------------------------
# 2. DEFINISI KARAKTER & PERAN NARATIF
# ------------------------------------------------------------
# Karakter Utama & Pendukung:
# - p: Tokoh utama (default 'Billa'), mahasiswa rantau
# - dimas: Axel, sahabat impulsif yang sering mengajak nongkrong/belanja (representasi tekanan sosial / FOMO)
# - sinta: Michelle, sahabat bijak yang terbiasa mencatat keuangan dan berhemat (representasi literasi finansial)
# - mama: Orang tua yang mengirimkan uang saku bulanan dan memberikan nasihat keuangan
# - tip: Karakter narator khusus penyampai edukasi keuangan dengan SFX lonceng
define p     = Character("[nama]")
define dimas = Character("Axel")
define sinta = Character("Michelle")
define mama  = Character(_("Mama"))
define tip   = Character(_("Tips Finansial"), what_italic=True, callback=tip_callback)

# ------------------------------------------------------------
# 3. VARIABEL STATUS & TRACKING KEUANGAN (GAME STATE)
# ------------------------------------------------------------
default nama = "Billa"             # Nama pemain (dapat diubah saat awal game)
default pakai_sprite_billa = True  # True jika memakai nama default Billa, False jika nama kustom
default telepon_mama = None        # Status panggilan telepon Mama ('senang', 'netral', 'khawatir', 'kecewa', atau None)
default uang = 0                  # Saldo uang jajan aktif untuk belanja sehari-hari
default dana_darurat = 0          # Saldo simpanan terpisah khusus keadaan darurat
default hutang = 0                # Total pokok tagihan utang PayLater
default skor = 0                  # Akumulasi poin keputusan finansial yang bijak
define skor_max = 22             # Skor maksimal (11 titik keputusan x 2 poin maksimal)
default minggu = 1                # Indikator progres minggu (Minggu 1 s.d. 4)
default catat = False             # Status pencatatan keuangan (diaktifkan di Minggu 2 jika setuju)
default wants = 0                 # Penghitung berapa kali pemain memilih pengeluaran Keinginan
default needs = 0                 # Penghitung berapa kali pemain memilih pengeluaran Kebutuhan/Tabungan
default mama_bantu = False        # Penanda apakah pemain meminta bantuan dana ke orang tua saat darurat
default biaya_darurat = 275000    # Biaya perbaikan/penggantian charger laptop saat darurat
default persen = 0

# Jejak keputusan (dipakai untuk percabangan cerita)
default nongkrong = ""            # "boros" / "hemat" / "tolak"  (Minggu 1)
default headset = ""              # "paylater" / "tunai" / "tunda"  (Minggu 1)
default makan = ""                # "online" / "campur" / "masak"  (Minggu 2)
default langganan = ""            # "tahunan" / "bulanan" / "nobar"  (Minggu 2)
default pinjam_dimas = ""         # "penuh" / "sebagian" / "tolak"  (Minggu 3)
default pinjaman_dimas = 0        # Nominal uang yang dipinjamkan ke Axel
default uang_awal_minggu = 0      # Untuk rekap pengeluaran mingguan
default dana_awal_minggu = 0                # Persentase skor akhir kesadaran finansial
default ending_nama = _("Selamat Sampai Akhir Bulan")  # Nama ending yang diraih pemain

# Status Instrumen Penelitian GDLC (Pre-Test & Post-Test)
default pretest_dibuka = False                   # Penanda tautan Pre-Test telah dibuka di browser
default pretest_selesai = False                  # Penanda pemain telah mengonfirmasi pengisian Pre-Test
default posttest_dibuka = False                  # Penanda tautan Post-Test telah dibuka di browser
default posttest_selesai = False                 # Penanda pemain telah mengonfirmasi pengisian Post-Test

# Definisi Aset Audio Ren'Py (BGM & SFX)
define audio.bgm_menu = "audio/bgm_menu.ogg"
define audio.bgm_kos = "audio/bgm_kos.ogg"
define audio.bgm_kampus = "audio/bgm_kampus.ogg"
define audio.bgm_darurat = "audio/bgm_darurat.ogg"
define audio.bgm_ending_baik = "audio/bgm_ending_baik.ogg"
define audio.bgm_ending_reflektif = "audio/bgm_ending_reflektif.ogg"

define audio.sfx_click = "audio/sfx_click.ogg"
define audio.sfx_koin = "audio/sfx_koin.ogg"
define audio.sfx_notif = "audio/sfx_notif.ogg"
define audio.sfx_peringatan = "audio/sfx_peringatan.ogg"
define audio.sfx_tip = "audio/sfx_tip.ogg"

# Tautan Kuesioner Penelitian Tugas Akhir S1 TRM
define url_pretest = "https://forms.gle/naX1XzHjQ1eWTvyXA"
define url_posttest = "https://forms.gle/rdtdaCXnA6eVhbHU8"
define kredit_visual = "Aset visual dan UI: Everyday Life oleh DadddyDarko (itch.io)"
define kredit_audio = "Musik & BGM: Kevin MacLeod (incompetech.com) - Lisensi Creative Commons By Attribution 4.0\nSFX: Everyday Life UI Sound Pack"

# ------------------------------------------------------------
# ------------------------------------------------------------
# 4. HUD (PAPAN STATUS M-BANKING & WIDGET PANGGILAN DI POJOK KANAN ATAS)
# ------------------------------------------------------------
screen hud():
    # Tampilan status keuangan real-time bergaya aplikasi Mobile Banking:
    # - Badge M-Banking dan indikator Minggu aktif (1-4).
    # - Saldo Uang Jajan dengan warna adaptif (Hijau: aman, Oranye: waspada, Merah: kritis).
    # - Progress bar visual kapasitas sisa uang dari plafon Rp 2.000.000.
    # - Nominal simpanan Dana Darurat terproteksi.
    # - Kotak peringatan Tagihan PayLater (hanya muncul saat memiliki utang).
    # - Penghitung belanja Keinginan (jika fitur pencatatan diaktifkan).
    # - Kotak Panggilan Masuk Mama (jika Mama sedang menelepon pemain).
    zorder 100
    vbox:
        xalign 1.0
        yalign 0.0
        xoffset el_u(-10)
        yoffset el_u(8)
        spacing el_u(4)

        # 1. Papan Status M-Banking
        frame:
            background el_ui_frame("menu_panel")
            xsize el_u(120)
            padding (el_u(8), el_u(7), el_u(8), el_u(7))

            vbox:
                spacing el_u(3)

                # Header M-Banking: Badge & Minggu
                hbox:
                    xfill True
                    yalign 0.5

                    frame:
                        background Solid("#3d7b7a" if el_ui_theme == "cream" else "#fac371")
                        padding (el_u(4), el_u(1), el_u(4), el_u(1))
                        yalign 0.5
                        text "M-BANKING":
                            style "el_ui_text"
                            color ("#fdf5cc" if el_ui_theme == "cream" else "#10182e")
                            size el_u(6.5)
                            bold True

                    hbox:
                        xalign 1.0
                        yalign 0.5
                        spacing el_u(2)
                        add el_pj_path("icon_calendar_idle") xsize el_u(8) ysize el_u(8) yalign 0.5
                        text _("Minggu [minggu]"):
                            style "el_ui_text"
                            color el_ui_color(1)
                            size el_u(6.5)
                            yalign 0.5

                # Saldo Uang Jajan
                vbox:
                    spacing 0
                    text _("Saldo Uang Jajan"):
                        style "el_ui_text"
                        color el_ui_color(1)
                        size el_u(6.5)

                    $ warna_uang = ("#2e7d32" if el_ui_theme == "cream" else "#a5d6a7") if uang >= 500000 else (("#e65100" if el_ui_theme == "cream" else "#ffb74d") if uang >= 200000 else ("#c62828" if el_ui_theme == "cream" else "#ff8a80"))
                    text rp(uang):
                        style "el_ui_text"
                        color warna_uang
                        size el_u(11)
                        bold True

                # Progress bar sisa uang jajan (pixel-style)
                bar:
                    value StaticValue(max(uang, 0), 2000000)
                    xsize el_u(104)
                    ysize el_u(4)
                    left_bar Solid(warna_uang)
                    right_bar Solid(el_ui_color(1) + "33")
                    thumb Null()
                    thumb_shadow None

                # Kantong Tabungan (Dana Darurat)
                hbox:
                    xfill True
                    yalign 0.5
                    hbox:
                        spacing el_u(2)
                        yalign 0.5
                        add el_pj_path("icon_lock_idle") xsize el_u(7.5) ysize el_u(7.5) yalign 0.5
                        text _("Dana Darurat:"):
                            style "el_ui_text"
                            color el_ui_color()
                            size el_u(6.5)
                            yalign 0.5
                    text rp(dana_darurat):
                        style "el_ui_text"
                        color ("#1976d2" if el_ui_theme == "cream" else "#81d4fa")
                        size el_u(7.5)
                        bold True
                        xalign 1.0
                        yalign 0.5

                # Tagihan PayLater (jika berutang)
                if hutang > 0:
                    frame:
                        background Solid("#ff525222")
                        padding (el_u(4), el_u(2), el_u(4), el_u(2))
                        xfill True
                        hbox:
                            xfill True
                            yalign 0.5
                            text _("PayLater:"):
                                style "el_ui_text"
                                color ("#c62828" if el_ui_theme == "cream" else "#ff8a80")
                                size el_u(6.5)
                                bold True
                                yalign 0.5
                            text rp(hutang):
                                style "el_ui_text"
                                color ("#c62828" if el_ui_theme == "cream" else "#ff8a80")
                                size el_u(7)
                                bold True
                                xalign 1.0
                                yalign 0.5

                # Indikator Piutang Teman (jika ada uang yang dipinjamkan ke Axel dan belum kembali)
                if pinjaman_dimas > 0 and pinjam_dimas == "penuh" and minggu >= 4:
                    frame:
                        background Solid("#ffb74d22")
                        padding (el_u(4), el_u(2), el_u(4), el_u(2))
                        xfill True
                        hbox:
                            xfill True
                            yalign 0.5
                            text _("Piutang:"):
                                style "el_ui_text"
                                color ("#e65100" if el_ui_theme == "cream" else "#ffb74d")
                                size el_u(6.5)
                                bold True
                                yalign 0.5
                            text rp(pinjaman_dimas):
                                style "el_ui_text"
                                color ("#e65100" if el_ui_theme == "cream" else "#ffb74d")
                                size el_u(7)
                                bold True
                                xalign 1.0
                                yalign 0.5

                # Catatan Keinginan
                if catat:
                    text _("Belanja Keinginan: [wants]x"):
                        style "el_ui_text"
                        color el_ui_color(1)
                        size el_u(6.5)

        # 2. Kotak Panggilan Telepon Mama (Muncul di bawah M-Banking saat Mama menelpon)
        if telepon_mama:
            frame:
                background el_ui_frame("menu_panel")
                xsize el_u(120)
                padding (el_u(7), el_u(6), el_u(7), el_u(6))

                vbox:
                    spacing el_u(2.5)

                    # Header Status Panggilan
                    hbox:
                        xfill True
                        yalign 0.5

                        frame:
                            background Solid("#2e7d32" if el_ui_theme == "cream" else "#43a047")
                            padding (el_u(3.5), el_u(1), el_u(3.5), el_u(1))
                            yalign 0.5
                            text _("📞 PANGGILAN"):
                                style "el_ui_text"
                                color "#ffffff"
                                size el_u(5.5)
                                bold True
                                yalign 0.5

                        text _("Tersambung"):
                            style "el_ui_text"
                            color el_ui_color(1)
                            size el_u(5.5)
                            xalign 1.0
                            yalign 0.5

                    # Info Kontak & Avatar Mama
                    hbox:
                        spacing el_u(3.5)
                        yalign 0.5

                        # Avatar Mama Berbingkai Pixel
                        frame:
                            background Solid("#3d7b7a" if el_ui_theme == "cream" else "#fac371")
                            padding (el_u(1), el_u(1), el_u(1), el_u(1))
                            xsize el_u(24)
                            ysize el_u(24)
                            yalign 0.5

                            $ _img_mama_ava = "images/mama_avatar_" + str(telepon_mama) + ".png"
                            if not renpy.loadable(_img_mama_ava):
                                $ _img_mama_ava = "images/mama_avatar_senang.png"
                            add _img_mama_ava xsize el_u(22) ysize el_u(22)

                        vbox:
                            spacing el_u(0.8)
                            yalign 0.5

                            text _("Mama"):
                                style "el_ui_text"
                                color el_ui_color()
                                size el_u(7.5)
                                bold True

                            text _("Orang Tua di Rumah"):
                                style "el_ui_text"
                                color el_ui_color(1)
                                size el_u(5)

                            text _("● Suara aktif..."):
                                style "el_ui_text"
                                color ("#2e7d32" if el_ui_theme == "cream" else "#81c784")
                                size el_u(5)
                                italic True


# ------------------------------------------------------------
# 5. ANIMASI & NOTIFIKASI PUSH SMARTPHONE (LAYAR HP)
# ------------------------------------------------------------
# Transform animasi pop-down halus saat notifikasi push HP muncul & menghilang
transform hp_notif_appear:
    on show:
        alpha 0.0 yoffset -20
        easein_cubic 0.25 alpha 1.0 yoffset 0
    on hide:
        easeout_cubic 0.2 alpha 0.0 yoffset -20

screen layar_hp(app, judul, isi, warna="#4fc3f7"):
    # Tampilan banner push notification ponsel di pojok kiri atas layar:
    # - Menyimulasikan notifikasi aplikasi bank, toko online, atau tagihan PayLater.
    # - Parameter:
    #     * app: Nama aplikasi pengirim (misal: 'M-Banking', 'PayLater', 'Toko Online')
    #     * judul: Judul ringkas notifikasi
    #     * isi: Konten pesan notifikasi
    #     * warna: Warna badge aplikasi (hijau/oranye/merah/biru)
    # - Posisi di kiri atas diatur agar tidak bertabrakan dengan menu pilihan (choices).
    zorder 90
    frame at hp_notif_appear:
        background el_ui_frame("menu_panel")
        xpos el_u(10)
        ypos el_u(8)
        xsize el_u(108)
        padding (el_u(8), el_u(7), el_u(8), el_u(7))

        vbox:
            spacing el_u(3)

            # Header bar notifikasi
            hbox:
                xfill True
                yalign 0.5

                hbox:
                    spacing el_u(3)
                    yalign 0.5
                    $ _app_icon = "icon_message_idle" if app == "Chat" else ("icon_bookmark_idle" if app in ("Streaming", "Supermarket", "Toko Online") else "icon_bell_idle")
                    add el_pj_path(_app_icon) xsize el_u(8) ysize el_u(8) yalign 0.5

                    frame:
                        background Solid(warna)
                        padding (el_u(4), el_u(1), el_u(4), el_u(1))
                        yalign 0.5
                        text _(app):
                            style "el_ui_text"
                            color "#10182e"
                            size el_u(6.5)
                            bold True

                text _("baru saja"):
                    style "el_ui_text"
                    color el_ui_color(1)
                    size el_u(6)
                    xalign 1.0
                    yalign 0.5

            # Judul Notifikasi
            text _(judul):
                style "el_ui_text"
                color el_ui_color()
                size el_u(9)
                bold True
                xmaximum el_u(92)

            # Pesan Notifikasi
            text _(isi):
                style "el_ui_text"
                color el_ui_color()
                size el_u(7)
                xmaximum el_u(92)


# ------------------------------------------------------------
# 6. BANNER NOTIFIKASI TRANSAKSI CEPAT (CUSTOM NOTIFY)
# ------------------------------------------------------------
screen notify(message):
    # Kustomisasi screen notify bawaan Ren'Py.
    # Memungkinkan tag teks seperti {color=...} dirender langsung dengan warna
    # hijau (+ uang), merah (- uang), atau biru (+ dana darurat) tanpa di-escape.
    zorder 200
    style_prefix "notify"
    frame at notify_appear:
        text message
    timer 3.25 action Hide('notify')


# ============================================================
# 7. ALUR UTAMA PERMAINAN (MAIN STORYLINE)
# ============================================================

# ---------- TITIK AWAL: INTRODUKSI ----------
label start:
    $ pretest_dibuka = False
    $ pretest_selesai = False
    $ posttest_dibuka = False
    $ posttest_selesai = False
    $ skor = 0
    $ skor_max = 22
    scene black
    $ musik("bgm_menu")
    centered "{size=48}{b}PAY O' MAY{/b}{/size}\n{size=26}Gim edukasi kesadaran finansial untuk mahasiswa perantauan{/size}"
    centered "Cerita ini fiktif, tetapi dilema keuangannya nyata.\nSebelum mulai, kamu akan diminta mengisi {b}Pre-Test{/b}."

    jump pretest

# ---------- KUESIONER PRE-TEST (INSTRUMEN PENELITIAN GDLC) ----------
label pretest:
    # Menyajikan modal kuesioner Pre-Test untuk mengukur tingkat
    # pengetahuan awal finansial responden sebelum memainkan visual novel.
    scene black
    call screen kuesioner_pretest

    jump nama_pemain

# ---------- INPUT NAMA PEMAIN & MEMULAI PROLOG ----------
label nama_pemain:
    # Meminta nama pemain (default: 'Billa') untuk personalisasi dialog dan e-statement.
    # Jika pemain memakai nama default (Billa), aset visual sprite Billa akan digunakan.
    # Jika pemain memasukkan nama kustom, visual sprite Billa dinonaktifkan (mode first-person).
    $ nama = renpy.input(_("Siapa namamu?"), length=14)
    $ nama = nama.strip()
    if nama == "" or nama.lower() == "billa":
        $ nama = "Billa"
        $ pakai_sprite_billa = True
    else:
        $ pakai_sprite_billa = False

    # ========================================================
    # PROLOG - Awal Bulan
    # ========================================================
    $ uang = 2000000
    $ musik("bgm_kos")
    scene bg kos with el_train_doors
    show screen hud
    show screen el_ui_quick_menu

    if pakai_sprite_billa:
        show billa netral with dissolve

    "Awal bulan. Kamu baru enam bulan merantau ke kota ini untuk kuliah."

    $ sfx("sfx_notif")
    show screen layar_hp("M-Banking", "Transfer masuk", "Uang saku bulanan sebesar Rp 2.000.000 dari Mama sudah masuk ke rekeningmu.", "#66bb6a")
    "HP-mu bergetar. Notifikasi m-banking: uang saku bulanan {b}Rp 2.000.000{/b} masuk."
    hide screen layar_hp

    $ telepon_mama = "senang"
    if pakai_sprite_billa:
        show billa senang at center with dissolve

    mama "Halo Nak, uang saku bulan ini sudah Mama kirim ya. Uang kos sudah Mama bayar langsung ke Ibu Kos."
    mama "Uang itu untuk makan, transport, kuota, semuanya, sampai akhir bulan. Diatur baik-baik ya."
    p "Siap, Ma. Aku bisa atur kok."
    mama "Mama percaya. Jangan sampai kehabisan di tanggal tua ya."

    $ telepon_mama = None
    if pakai_sprite_billa:
        show billa netral with dissolve

    "Dua juta rupiah untuk sebulan. Rasanya banyak sekali. Tapi benarkah begitu?"

    menu:
        "Bagaimana kamu mengatur uang ini?"

        "Bagi ke pos-pos: kebutuhan, dana darurat Rp 300.000, dan sisanya untuk keinginan.":
            $ pindah_ke_dana(300000)
            $ skor += 2
            $ needs += 1
            if pakai_sprite_billa:
                show billa senang
            "Kamu memindahkan Rp 300.000 ke tabungan terpisah dan memberinya nama 'Dana Darurat - Jangan Disentuh'."
            tip "Pay yourself first: sisihkan dana darurat di awal bulan, bukan dari sisa di akhir bulan. Sisa uang biasanya tidak pernah ada."

        "Biarkan semua di satu rekening dulu. Lihat nanti saja.":
            $ skor += 1
            if pakai_sprite_billa:
                show billa netral
            "Semua uang menumpuk di satu rekening. Aman? Mungkin. Terarah? Belum."
            tip "Tanpa pos-pos yang jelas, sulit melihat ke mana uang pergi. Uang yang tidak punya tugas cenderung habis tanpa terasa."

        "Tanggal muda! Beli sneakers incaran seharga Rp 350.000 dulu, sisanya dipikir belakangan.":
            $ ubah_uang(-350000, "Sneakers baru")
            $ wants += 1
            if pakai_sprite_billa:
                show billa khawatir
            "Sepatu baru kinclong. Saldo menyusut seketika."
            tip "Membeli keinginan sebelum memenuhi kebutuhan adalah pola yang paling sering membuat mahasiswa kehabisan uang di pertengahan bulan."

    if pakai_sprite_billa:
        hide billa with dissolve

    $ uang_awal_minggu = uang
    $ dana_awal_minggu = dana_darurat

    # ========================================================
    # MINGGU 1
    # ========================================================
    $ minggu = 1
    $ musik("bgm_kampus")
    scene bg kampus with el_mosaic_tiles

    if pakai_sprite_billa:
        show billa netral at left with dissolve
        show dimas senang at right with dissolve
    else:
        show dimas senang with dissolve

    dimas "[nama]! Uang saku udah masuk, kan? Ayo nongkrong di kafe baru itu, lagi viral banget!"
    dimas "Anak-anak kelas udah pada ke sana. Masa cuma kamu yang nggak ikut?"
    "Perutmu mulas sedikit. Itu rasanya FOMO: takut ketinggalan, takut dianggap kurang gaul."

    menu:
        "Apa jawabanmu?"

        "Ikut, pesan apa saja yang diinginkan. Sekali-sekali kan nggak apa-apa.":
            $ ubah_uang(-250000, "Nongkrong di kafe")
            $ nongkrong = "boros"
            $ wants += 1
            if pakai_sprite_billa:
                show billa senang at left
            show dimas senang at right
            "Makanan, minuman, dessert, patungan live music. Struknya: {b}Rp 250.000{/b} untuk satu malam."
            tip "Pengeluaran 'sekali-sekali' yang besar bisa menghabiskan seperempat uang saku bulananmu dalam satu malam."

        "Ikut, tapi pesan satu minuman saja dan bawa tumbler dari kos.":
            $ ubah_uang(-40000, "Minuman di kafe")
            $ nongkrong = "hemat"
            $ wants += 1
            $ skor += 2
            if pakai_sprite_billa:
                show billa netral at left
            show dimas netral at right
            "Kamu tetap ikut seru-seruan, dompet tetap aman. Total: Rp 40.000."
            tip "Hemat bukan berarti anti sosial. Kamu bisa tetap hadir dengan batas pengeluaran yang sudah kamu tentukan sendiri."

        "Tolak dengan halus dan ajak Axel nongkrong di taman kampus minggu depan.":
            $ skor += 1
            if pakai_sprite_billa:
                show billa khawatir at left
            show dimas kecewa at right
            dimas "Yah... oke deh, tapi minggu depan beneran ya!"
            $ nongkrong = "tolak"
            "Dompet aman, tapi kamu agak terlewat dari obrolan seru malam itu."
            tip "Menolak itu sah. Tapi cari cara tetap terhubung dengan teman, karena menarik diri sepenuhnya sulit dipertahankan."

    hide dimas with dissolve
    if pakai_sprite_billa:
        hide billa with dissolve

    $ musik("bgm_kos")
    scene bg malam with el_sunset_horizon
    if pakai_sprite_billa:
        show billa netral with dissolve
    "Malamnya, di kamar kos, HP-mu bergetar lagi."
    $ sfx("sfx_notif")
    show screen layar_hp("Toko Online", "FLASH SALE!", "Headset Bluetooth Rp 399.000. Bayar Nanti dengan PayLater, bunga 0 persen bulan pertama! Berakhir 2 jam lagi.", "#ffa726")
    "{b}FLASH SALE!{/b} Headset Bluetooth Rp 399.000. Bayar Nanti dengan PayLater, bunga 0 persen bulan pertama!"
    "Headset lamamu sebenarnya masih berfungsi. Hanya saja baterainya agak cepat habis."

    menu:
        "Apa yang kamu lakukan?"

        "Checkout pakai PayLater. Bayarnya kan bulan depan.":
            $ tambah_hutang(399000, "Headset")
            $ headset = "paylater"
            $ wants += 1
            if pakai_sprite_billa:
                show billa senang
            "Klik. Selesai. Kamu merasa belum mengeluarkan uang sepeser pun. Padahal tagihannya sudah menunggu di ujung bulan."
            tip "PayLater itu utang, bukan uang tambahan. Rasa 'belum bayar' membuat kita lebih mudah belanja berlebihan."

        "Beli tunai dari uang jajan.":
            $ ubah_uang(-399000, "Headset baru")
            $ headset = "tunai"
            $ wants += 1
            $ skor += 1
            if pakai_sprite_billa:
                show billa khawatir
            "Headset baru datang dua hari kemudian. Uang jajanmu menipis hampir seperlima."
            tip "Membayar tunai memang lebih sehat daripada berutang. Tapi pertanyaan utamanya tetap: apakah ini kebutuhan atau keinginan?"

        "Simpan di keranjang dulu. Tunggu tiga hari, kalau masih butuh baru beli.":
            $ skor += 2
            $ headset = "tunda"
            $ needs += 1
            if pakai_sprite_billa:
                show billa netral
            "Tiga hari kemudian, kamu sadar headset lamamu masih oke. Keranjang dikosongkan tanpa penyesalan."
            tip "Aturan tunggu 24 jam sampai 3 hari efektif mengurangi belanja impulsif. Keinginan yang sungguhan akan tetap ada setelah ditunggu."

    hide screen layar_hp
    if pakai_sprite_billa:
        hide billa with dissolve
    call akhir_minggu from _call_akhir_minggu

    # ========================================================
    # MINGGU 2
    # ========================================================
    $ musik("bgm_kos")
    scene bg kos with el_diamond_iris
    "Minggu kedua dimulai."

    # --- Konsekuensi dari keputusan Minggu 1 ---
    if nongkrong == "boros":
        "Grup kelas masih ramai dengan foto kafe viral itu. Kamu membuka struk Rp 250.000 dan menggeleng pelan."
    elif nongkrong == "hemat":
        "Tumbler dari kos jadi bahan candaan di grup kelas. Tapi dompetmu tertawa paling terakhir."
    else:
        "Kamu melewatkan malam kafe itu. Di grup kelas, foto-foto bermunculan dan kamu menatapnya agak lama."

    if headset == "paylater":
        $ sfx("sfx_notif")
        "Setiap kali membuka aplikasi bank, kamu teringat tagihan PayLater Rp 399.000 yang menunggu di ujung bulan."
    elif headset == "tunai":
        "Headset baru nyaman di telinga, tapi setiap melihat saldo kamu menghitung ulang uang makan minggu ini."
    else:
        "Keranjang belanja yang kosong itu membuatmu merasa ringan. Saldo masih utuh."

    "Kamu mulai sadar bahwa urusan makan adalah pos pengeluaran terbesar yang paling sering terlupa."

    menu:
        "Bagaimana kamu mengatur makan minggu ini?"

        "Pesan makanan online hampir tiap hari. Praktis dan banyak promo.":
            $ ubah_uang(-200000, "Pesan makanan online")
            $ makan = "online"
            $ wants += 1
            "Ongkir, biaya layanan, dan harga yang naik di aplikasi. Terkumpul tambahan {b}Rp 200.000{/b} minggu ini."
            tip "Biaya kecil seperti ongkir dan biaya layanan terasa remeh satu per satu, tetapi menumpuk menjadi pengeluaran besar."

        "Campur: masak saat sempat, pesan online sesekali.":
            $ ubah_uang(-80000, "Makan campur")
            $ makan = "campur"
            $ skor += 1
            "Kamu masak dua kali, sisanya pesan. Tambahan pengeluaran: Rp 80.000."
            tip "Kompromi yang masuk akal, dan lebih baik daripada tanpa rencana sama sekali."

        "Meal prep hari Minggu: masak sendiri dan bawa bekal ke kampus.":
            $ skor += 2
            $ makan = "masak"
            $ needs += 1
            "Kamu masak nasi, telur, dan sayur untuk beberapa hari. Tidak ada pengeluaran tambahan, dan perut tetap kenyang."
            tip "Makan adalah kebutuhan, tetapi cara memenuhinya bisa dipilih. Memasak sendiri biasanya jauh lebih murah dari memesan."

    $ musik("bgm_kampus")
    scene bg kampus with el_mosaic_tiles

    if pakai_sprite_billa:
        show billa netral at left with dissolve
        show sinta netral at right with dissolve
    else:
        show sinta netral with dissolve

    sinta "Hei [nama], kok mukamu bingung lihat saldo? Aku juga dulu begitu."
    sinta "Sejak aku mencatat semua pengeluaran, aku jadi tahu uangku bocor ke mana."
    sinta "Coba aturan 50, 30, 20 versi mahasiswa: 50 persen kebutuhan, 30 persen keinginan, 20 persen tabungan. Gampang kok."

    menu:
        "Apa tanggapanmu?"

        "Oke, mulai hari ini aku catat semua pengeluaran di aplikasi catatan.":
            $ catat = True
            $ skor += 2
            if pakai_sprite_billa:
                show billa senang at left
            show sinta senang at right
            sinta "Nah gitu! Nanti kamu bakal kaget lihat kebocoran kecilnya."
            "Mulai sekarang, kamu bisa melihat jumlah keinginan yang sudah kamu penuhi di papan status."
            tip "Mencatat pengeluaran membuat kebocoran kecil terlihat. Kopi Rp 25.000 dikali 20 hari sama dengan Rp 500.000 per bulan."

        "Nanti aja deh, kelihatannya ribet.":
            if pakai_sprite_billa:
                show billa khawatir at left
            show sinta khawatir at right
            sinta "Ya udah, tapi kalau butuh bantuan bilang ya."
            "Kamu kembali menjalani minggu tanpa catatan. Saldo cuma kamu cek kalau ingat."
            tip "Tanpa pencatatan, kita hanya menebak. Kebanyakan orang menebak pengeluarannya jauh lebih kecil dari kenyataan."

    hide sinta with dissolve
    if pakai_sprite_billa:
        hide billa with dissolve

    # --- Keputusan baru: langganan streaming ---
    $ musik("bgm_kos")
    scene bg malam with el_lantern_glow
    "Malam hari. Serial yang ramai dibicarakan satu angkatan hanya tayang di layanan streaming berbayar."
    $ sfx("sfx_notif")
    show screen layar_hp("Streaming", "Promo Paket Tahunan", "Hemat 40 persen jika berlangganan setahun: Rp 300.000. Paket bulanan Rp 54.000.", "#7e57c2")
    "Teman-temanmu mulai saling spoiler di grup. Kamu mulai tergoda."

    menu:
        "Bagaimana kamu menontonnya?"

        "Ambil paket tahunan. Katanya lebih hemat 40 persen.":
            hide screen layar_hp
            $ ubah_uang(-300000, "Paket tahunan streaming")
            $ wants += 1
            $ langganan = "tahunan"
            $ sfx("sfx_peringatan")
            "Terasa hemat, padahal kamu baru saja mengeluarkan Rp 300.000 sekaligus di awal bulan dengan uang saku terbatas."
            tip "Diskon tahunan baru hemat jika kamu benar-benar memakainya. Ia juga mengunci uang yang mungkin kamu butuhkan bulan ini."

        "Langganan satu bulan saja, lalu berhenti setelah serialnya tamat.":
            hide screen layar_hp
            $ ubah_uang(-54000, "Streaming bulanan")
            $ wants += 1
            $ skor += 1
            $ langganan = "bulanan"
            $ sfx("sfx_click")
            "Kamu memasang pengingat di kalender HP untuk membatalkan langganan sebelum bulan berikutnya."
            tip "Langganan bulanan fleksibel, tapi mudah terlupa dibatalkan. Pasang pengingat agar tidak menjadi pengeluaran diam-diam."

        "Nonton bareng di kos teman yang sudah berlangganan, bawa camilan saja.":
            hide screen layar_hp
            $ ubah_uang(-15000, "Camilan nobar")
            $ wants += 1
            $ skor += 2
            $ langganan = "nobar"
            scene bg nobar with el_lantern_glow
            if pakai_sprite_billa:
                show billa senang at left with dissolve
                show dimas senang at right with dissolve
            else:
                show dimas senang with dissolve
            dimas "Nah, camilan datang! Nobar di kos emang paling mantap, serunya dapet, dompet tetep aman!"
            hide dimas with dissolve
            if pakai_sprite_billa:
                hide billa with dissolve
            "Nobar ternyata jauh lebih seru daripada nonton sendirian di kamar, dan kamu hanya mengeluarkan Rp 15.000 untuk camilan."
            tip "Keinginan bisa dipenuhi dengan cara yang lebih murah. Sering kali cara itu sekaligus lebih menyenangkan."

    hide screen layar_hp
    call akhir_minggu from _call_akhir_minggu_1

    # ========================================================
    # MINGGU 3
    # ========================================================
    $ musik("bgm_darurat")
    scene bg malam with el_lantern_glow
    "Minggu ketiga. Kamis malam, jam sepuluh. Tugas besar harus dikumpulkan besok pagi."
    "Tiba-tiba laptopmu mati. Charger-nya putus tepat di sambungan kabel. Baterai tinggal sedikit."
    "Charger original di toko resmi harganya {b}Rp 275.000{/b}. Toko buka besok pagi dan kamu harus memutuskan sumber dananya sekarang."

    menu:
        "Dari mana uangnya?"

        "Pakai dana darurat. Memang untuk hal seperti ini." if dana_darurat >= biaya_darurat:
            $ ubah_dana(-biaya_darurat, "Charger baru")
            $ skor += 2
            $ needs += 1
            "Tugas selesai tepat waktu, dan uang makanmu tidak terganggu. Dana darurat menjalankan tugasnya."
            tip "Dana darurat ada agar kejadian tak terduga tidak berubah menjadi krisis. Idealnya mencakup beberapa minggu sampai beberapa bulan kebutuhan pokok."

        "Ambil dari uang jajan. Minggu depan makan seadanya.":
            $ ubah_uang(-biaya_darurat, "Charger baru")
            $ skor += 1
            $ needs += 1
            "Charger terbeli, tugas aman. Tapi uang makan minggu depan terpaksa diirit."
            tip "Tanpa dana darurat, kejadian tak terduga memotong uang kebutuhan sehari-hari."

        "Pakai PayLater saja. Gampang dan cepat.":
            $ tambah_hutang(biaya_darurat, "Charger")
            "Charger terbeli. Tagihannya masuk ke daftar yang akan jatuh tempo di akhir bulan."
            tip "Menutup kebutuhan mendadak dengan utang konsumtif adalah awal dari lingkaran gali lubang tutup lubang."

        "Telepon Mama dan minta tambahan uang.":
            $ mama_bantu = True
            $ skor += 1
            $ telepon_mama = "khawatir"
            if pakai_sprite_billa:
                show billa khawatir with dissolve
            mama "Ya ampun, charger rusak? Mama transfer sekarang. Tapi lain kali sisihkan dana darurat sendiri ya, Nak."
            $ telepon_mama = None
            if pakai_sprite_billa:
                hide billa with dissolve
            "Masalah selesai, tapi ada rasa tidak enak karena harus merepotkan Mama."
            tip "Meminta bantuan keluarga sah-sah saja untuk keadaan darurat sungguhan, tapi tujuan utamanya adalah mandiri secara finansial."

    $ musik("bgm_kampus")
    scene bg kampus with el_postcard_diagonal
    if pakai_sprite_billa:
        show billa netral at left with dissolve
        show sinta khawatir at right with dissolve
    else:
        show sinta khawatir with dissolve
    sinta "Sekarang udah tanggal 20-an. Biasanya di titik ini mulai kerasa tipisnya."
    sinta "Kalau masih ada sisa, sisihkan dulu ke dana darurat sebelum kamu habiskan."

    if makan == "masak":
        sinta "Oh ya, aku lihat bekalmu minggu lalu. Keren! Itu salah satu cara terbaik menghemat."
    elif makan == "online":
        sinta "Aku sempat lihat riwayat pesan antarmu. Ongkir dan biaya layanannya lumayan bikin deg-degan, ya?"

    if langganan == "tahunan":
        sinta "Eh, kamu beneran ambil paket tahunan streaming itu? Lumayan nguras saldo awal bulan ya."
    elif langganan == "nobar":
        sinta "Seru ya nobar di kos kemarin. Kadang kumpul bareng jauh lebih asyik daripada bayar langganan mahal sendirian."

    if catat:
        $ t = rp(uang)
        "Kamu membuka catatan pengeluaranmu. Sisa uang jajan saat ini: [t]."
    if uang < 50000:
        "Sisa uangmu begitu tipis sampai menabung terasa mustahil."

    menu:
        "Berapa yang kamu sisihkan?"

        "Sisihkan Rp 100.000 ke dana darurat." if uang >= 100000:
            $ pindah_ke_dana(100000)
            $ skor += 2
            $ needs += 1
            if pakai_sprite_billa:
                show billa senang at left
            show sinta senang at right
            "Kamu memindahkan Rp 100.000. Sedikit demi sedikit, bantalan pengamanmu menebal."
            tip "Menabung rutin dalam jumlah kecil lebih berhasil daripada menunggu punya uang lebih."

        "Sisihkan Rp 50.000 saja." if uang >= 50000:
            $ pindah_ke_dana(50000)
            $ skor += 1
            if pakai_sprite_billa:
                show billa netral at left
            "Tidak banyak, tapi kamu memulai kebiasaannya."
            tip "Kebiasaan menabung lebih penting daripada jumlahnya. Naikkan nominalnya pelan-pelan."

        "Nanti saja. Sisanya buat jaga-jaga di dompet.":
            if pakai_sprite_billa:
                show billa khawatir at left
            "Kamu menyimpan sisanya di rekening yang sama. Tentu saja uang itu mudah tergoda untuk dipakai."
            tip "Uang yang bercampur dengan uang jajan jarang bertahan menjadi tabungan. Pisahkan rekening atau dompetnya."

    hide sinta with dissolve
    if pakai_sprite_billa:
        hide billa with dissolve

    # --- Keputusan baru: teman meminjam uang ---
    $ musik("bgm_kos")
    scene bg malam with el_lantern_glow
    "Malam itu HP-mu bergetar. Pesan dari Axel."
    $ sfx("sfx_notif")
    show screen layar_hp("Chat", "Axel", "Bro, boleh pinjam Rp 200.000? Uang saku udah mepet banget. Aku ganti pas dikirim bulan depan!", "#ffb74d")

    if nongkrong == "boros":
        "Kamu teringat malam di kafe viral itu. Struk Rp 250.000-mu ternyata punya kembaran di dompet Axel."
    elif nongkrong == "hemat":
        "Kamu teringat Axel memesan jauh lebih banyak dari yang kamu pesan di kafe waktu itu."
    else:
        "Kamu teringat Axel yang kecewa saat kamu menolak ke kafe. Rupanya dia terus mengikuti ajakan lain tanpa batas."

    menu:
        "Bagaimana kamu membalasnya?"

        "Pinjamkan Rp 200.000 penuh. Namanya juga teman." if uang >= 200000:
            hide screen layar_hp
            $ ubah_uang(-200000, "Pinjaman Axel")
            $ pinjaman_dimas = 200000
            $ pinjam_dimas = "penuh"
            "Kamu transfer tanpa banyak berpikir. 'Makasih banget, bro!' balasnya. Sisa uangmu ikut menipis drastis."
            tip "Meminjamkan uang yang kamu butuhkan sendiri berisiko dua kali: uangmu tertahan, dan pertemanan bisa canggung jika terlambat dikembalikan."

        "Pinjamkan Rp 50.000 saja, sebatas yang rela kamu ikhlaskan." if uang >= 50000:
            hide screen layar_hp
            $ ubah_uang(-50000, "Pinjaman Axel")
            $ pinjaman_dimas = 50000
            $ pinjam_dimas = "sebagian"
            $ skor += 1
            "Kamu mengetik balasan dan mentransfer seikhlasnya. 'Cuma segini yang bisa aku bantu,' tulismu. 'Cukup kok, makasih!' balas Axel."
            tip "Aturan sederhana: pinjamkan hanya jumlah yang siap kamu relakan jika tidak kembali."

        "Tolak dengan sopan, lalu ajak Axel menyusun anggaran sisa bulan bersama.":
            hide screen layar_hp
            $ sfx("sfx_click")
            $ pinjam_dimas = "tolak"
            $ skor += 2
            "Kamu menjelaskan dengan jujur bahwa uangmu juga terbatas, lalu menawarkan bantuan lain: menyusun anggaran sisa bulan bersama. Balasan Axel agak lama, tapi akhirnya dia setuju."
            tip "Menolak pinjaman bukan berarti tidak peduli. Membantu mencari solusi sering lebih berguna daripada memberi uang."

    hide screen layar_hp
    call akhir_minggu from _call_akhir_minggu_2

    # ========================================================
    # MINGGU 4
    # ========================================================

    # --- Telepon Mama: tanggapannya bergantung pada kondisi keuanganmu ---
    $ musik("bgm_kos")
    scene bg kos with el_diamond_iris
    "Minggu terakhir. Sore itu, Mama menelepon."

    $ sfx("sfx_notif")
    $ telepon_mama = "netral"
    if pakai_sprite_billa:
        show billa netral with dissolve

    mama "Halo Nak, sudah minggu terakhir ya. Bagaimana uang sakumu?"

    if uang < 0:
        $ telepon_mama = "khawatir"
        if pakai_sprite_billa:
            show billa kecewa
        p "Hmm... sebenarnya saldoku sudah minus, Ma."
        mama "Ya ampun. Tidak apa-apa, Nak. Yang penting kamu cerita. Nanti kita atur bareng ya."
    elif hutang > 0:
        $ telepon_mama = "khawatir"
        if pakai_sprite_billa:
            show billa khawatir
        p "Aman kok, Ma..."
        mama "Suaramu tidak seyakin biasanya. Ada yang ingin kamu ceritakan?"
        "Kamu menelan ludah. Ada tagihan PayLater yang belum kamu ceritakan."
    elif mama_bantu:
        $ telepon_mama = "senang"
        if pakai_sprite_billa:
            show billa netral
        mama "Mama senang kamu mau cerita soal charger kemarin. Bulan depan, coba sisihkan dana darurat sendiri ya."
    elif dana_darurat >= 100000:
        $ telepon_mama = "senang"
        if pakai_sprite_billa:
            show billa senang
        mama "Wah, Mama dengar kamu punya dana darurat sendiri? Mama bangga sekali, Nak."
    else:
        $ telepon_mama = "netral"
        if pakai_sprite_billa:
            show billa netral
        mama "Jangan lupa sisihkan sedikit untuk jaga-jaga ya, Nak."

    $ telepon_mama = None
    if pakai_sprite_billa:
        hide billa with dissolve

    $ musik("bgm_kampus")
    scene bg kampus with el_crosswalk

    if pakai_sprite_billa:
        show billa netral at left with dissolve
        show dimas senang at right with dissolve
    else:
        show dimas senang with dissolve

    # --- Konsekuensi dari keputusan meminjamkan uang ---
    if pinjam_dimas == "sebagian":
        dimas "Eh [nama], ini uang kemarin Rp 50.000 udah aku transfer balik. Makasih banget ya!"
        $ ubah_uang(50000, "Axel mengganti")
        $ pinjaman_dimas = 0
    elif pinjam_dimas == "penuh":
        show dimas khawatir at right
        dimas "Soal pinjaman kemarin, maaf ya, belum bisa aku ganti dulu. Uang saku bulananku ternyata udah mepet banget... Bulan depan pasti!"
        $ sfx("sfx_peringatan")
        "Kamu tersenyum kaku. Uang Rp 200.000 itu sekarang menggantung di antara kalian."
        show dimas senang at right
    elif pinjam_dimas == "tolak":
        show dimas netral at right
        dimas "Kemarin aku sempat agak kesal waktu kamu tolak, sih. Tapi setelah kita susun pos anggaran bareng kemarin, kamu bener juga. Aku mulai coba catat pengeluaran sekarang."
        show dimas senang at right
    dimas "[nama], weekend ini kita ke Lembang! Sewa vila patungan, BBQ, foto-foto. Total {b}Rp 300.000{/b} all-in."
    dimas "Ini momen terakhir sebelum UAS. Kalau nggak ikut, nyesel loh!"

    if catat:
        $ t = rp(uang)
        "Kamu membuka catatan pengeluaranmu. Sisa uang jajan: [t]. Sisa waktu hingga akhir bulan: beberapa hari."
    else:
        "Kamu mencoba mengingat-ingat. Sisa uangmu berapa ya? Sepertinya masih cukup."

    menu:
        "Bagaimana jawabanmu?"

        "Ikut paket lengkap Rp 300.000.":
            $ ubah_uang(-300000, "Trip ke Lembang")
            $ wants += 1
            if pakai_sprite_billa:
                show billa senang at left
            "Seru banget. Foto-fotonya bagus. Tapi saat pulang, saldo di aplikasi bank membuatmu menelan ludah."
            tip "FOMO sering hanya bertahan satu malam, sedangkan dampak ke dompet bertahan sampai akhir bulan."

        "Ikut versi hemat: patungan bensin dan bawa bekal sendiri (Rp 120.000).":
            $ ubah_uang(-120000, "Trip hemat")
            $ wants += 1
            $ skor += 1
            if pakai_sprite_billa:
                show billa netral at left
            "Kamu tetap ikut seru-seruan dengan biaya lebih ringan."
            tip "Menawar versi yang lebih murah adalah kompromi cerdas antara keinginan dan kemampuan."

        "Tidak ikut kali ini, tapi ajak mereka main ke tempat gratis atau murah.":
            $ skor += 2
            if pakai_sprite_billa:
                show billa netral at left
            show dimas kecewa at right
            dimas "Hmm, ya sudah. Tapi janji ya lain kali!"
            "Kamu menolak dengan sopan dan merasa tenang karena sudah tahu batasanmu."
            tip "Mengatakan 'tidak' untuk keinginan hari ini adalah mengatakan 'ya' untuk ketenangan di akhir bulan."

    hide dimas with dissolve
    if pakai_sprite_billa:
        hide billa with dissolve

    # --- Keputusan baru: promo belanja kebutuhan ---
    $ musik("bgm_kos")
    scene bg kos with el_diamond_iris
    $ sfx("sfx_notif")
    show screen layar_hp("Supermarket", "DISKON AKHIR BULAN", "Beli 3 gratis 1: sabun, mie instan, dan tisu. Paket hemat Rp 180.000. Hanya sampai malam ini!", "#ef5350")
    "Notifikasi promo muncul tepat saat uangmu mulai tipis. Di kamar, sabunmu tinggal sedikit dan tisumu hampir habis."

    menu:
        "Apa yang kamu lakukan?"

        "Borong paket promo. Beli 3 gratis 1, kan hemat.":
            hide screen layar_hp
            $ ubah_uang(-180000, "Paket borong promo")
            $ wants += 1
            if uang < 100000:
                $ sfx("sfx_peringatan")
            "Barang datang bertumpuk di pojok kamar kos. Sebagian besar baru akan terpakai beberapa bulan lagi, sementara uang saku akhir bulanmu terkuras seketika."
            tip "Diskon hanya menghemat jika barangnya memang kamu butuhkan sekarang. Barang yang menumpuk adalah uang yang tertidur."

        "Beli seperlunya saja: sabun dan tisu yang memang hampir habis.":
            hide screen layar_hp
            $ ubah_uang(-45000, "Sabun dan tisu")
            $ needs += 1
            $ skor += 2
            "Kamu membeli sabun dan tisu yang memang mendesak, lalu menyingkirkan barang promo lainnya dari keranjang belanja."
            tip "Belanja dengan daftar kebutuhan membuat kamu mengendalikan promo, bukan sebaliknya."

        "Lewati dulu dan pakai stok yang ada sampai uang saku berikutnya.":
            hide screen layar_hp
            $ sfx("sfx_click")
            $ skor += 1
            "Kamu menutup aplikasi belanja dan menghela napas lega. Kamu menghemat uang, meski sabun dan tisumu harus diirit sampai bulan depan."
            tip "Menunda pembelian itu baik, tetapi pastikan kebutuhan dasar tetap terpenuhi agar tidak jadi masalah di kemudian hari."

    hide screen layar_hp
    call akhir_minggu from _call_akhir_minggu_3

    # ========================================================
    # FASE PENYELESAIAN: TAGIHAN PAYLATER
    # ========================================================
    # Segmen ini hanya dieksekusi jika pemain pernah menggunakan PayLater.
    # Mengedukasi konsep bunga utang konsumtif (10%) dan ilusi pembayaran minimum (minimum payment trap).
    if hutang > 0:
        $ musik("bgm_darurat")
        scene bg malam with el_lantern_glow
        $ tagihan = hutang
        $ t = rp(tagihan)
        $ minimum = int(tagihan * 0.2)
        $ t_min = rp(minimum)
        $ isi_tagihan = _tr(_("Total tagihan ")) + t + _tr(_(" (pokok beserta akumulasi bunga). Jatuh tempo besok."))
        $ sfx("sfx_peringatan")
        show screen layar_hp("PayLater", "Tagihan jatuh tempo", isi_tagihan, "#ef5350")
        "Notifikasi: {b}Tagihan PayLater jatuh tempo besok.{/b}"
        "Total tagihan saat ini: [t] (pokok beserta akumulasi bunga mingguan)."

        menu:
            "Bagaimana kamu membayarnya?"

            "Bayar lunas dari uang jajan." if uang >= tagihan:
                $ ubah_uang(-tagihan, "Lunas PayLater")
                $ hutang = 0
                "Lunas. Tapi uang jajanmu terkuras."

            "Bayar lunas dari dana darurat." if dana_darurat >= tagihan:
                $ ubah_dana(-tagihan, "Lunas PayLater")
                $ hutang = 0
                "Lunas, tapi dana daruratmu terpakai untuk menutup keinginan bulan lalu."

            "Bayar minimum saja ([t_min]), sisanya bulan depan." if uang >= minimum:
                $ ubah_uang(-minimum, "Cicilan minimum")
                $ hutang = tagihan - minimum
                "Sisa tagihan terbawa ke bulan depan, dan bunga mingguan akan terus bertambah."

            "Tidak mampu membayar sekarang (Tagihan menunggak).":
                $ sfx("sfx_peringatan")
                "Kamu tidak mampu membayar tagihan sama sekali. Tagihan PayLater menunggak dan bunga denda akan membengkak ke bulan depan."

        hide screen layar_hp
        tip "Utang konsumtif menggerus uang saku bulan berikutnya. Bayar lunas tepat waktu, atau lebih baik jangan berutang untuk keinginan."

    # ========================================================
    # EPILOG: EVALUASI KONDISI KEUANGAN AKHIR BULAN
    # ========================================================
    # Memeriksa parameter akhir untuk menentukan 1 dari 4 cabang ending:
    # 1. Defisit / Uang minus -> Ending D
    # 2. Masih memiliki tanggungan PayLater -> Ending C
    # 3. Mandiri, sisa uang >= Rp 300rb, dana darurat >= Rp 100rb, skor >= 75% -> Ending A
    # 4. Selamat bertahan tanpa utang -> Ending B
    scene bg akhir with el_shoreline_sweep
    show weather kelopak with dissolve
    $ musik(None, fadeout=1.5)
    "Hari terakhir bulan ini. Malam yang tenang. Kamu membuka aplikasi bank dan menatap angkanya."
    $ skor_max = 22
    $ persen = (skor * 100) // 22

    if uang <= 0:
        jump ending_habis
    elif hutang > 0:
        jump ending_paylater
    elif uang >= 300000 and dana_darurat >= 100000 and persen >= 75 and not mama_bantu:
        jump ending_bendahara
    else:
        jump ending_selamat


# ============================================================
# 8. CABANG ENDING (CERITA PENUTUP)
# ============================================================

# ---------- ENDING A: LITERASI TINGGI & MANDIRI ----------
label ending_bendahara:
    # Ending terbaik: Pemain berhasil mengelola anggaran secara seimbang, memiliki dana darurat,
    # tidak berutang, dan mandiri tanpa merepotkan orang tua.
    $ musik("bgm_ending_baik")
    $ ending_nama = _("Ending A: Bendahara Handal")
    "{b}ENDING A: Bendahara Handal{/b}"
    "Uang jajanmu masih ada, dana darurat terjaga, dan tidak ada utang. Kamu bahkan masih bisa traktir Axel dan Michelle."
    if pakai_sprite_billa:
        show billa senang at left with dissolve
        show sinta senang at right with dissolve
    else:
        show sinta senang with dissolve
    sinta "Hebat, [nama]! Kamu sudah jadi bendahara untuk dirimu sendiri."
    hide sinta with dissolve

    $ telepon_mama = "senang"
    mama "Mama bangga. Bulan depan Mama tetap kirim ya, tapi kamu sekarang sudah paham caranya."
    $ telepon_mama = None

    if pakai_sprite_billa:
        hide billa with dissolve
    jump rekap

# ---------- ENDING B: BERTAHAN AMAN TANPA UTANG ----------
label ending_selamat:
    # Ending moderat: Pemain berhasil melewati bulan tanpa utang, meski alokasi dana darurat
    # atau belanja keinginan masih bisa ditingkatkan.
    $ musik("bgm_ending_baik")
    $ ending_nama = _("Ending B: Selamat Sampai Akhir Bulan")
    "{b}ENDING B: Selamat Sampai Akhir Bulan{/b}"
    if pakai_sprite_billa:
        show billa netral with dissolve
    "Kamu berhasil melewati bulan ini tanpa utang. Tidak sempurna, tapi tidak ada krisis."
    "Masih ada beberapa keputusan yang bisa lebih baik: dana darurat yang lebih tebal, atau keinginan yang lebih terkendali."
    if pakai_sprite_billa:
        hide billa with dissolve
    jump rekap

# ---------- ENDING C: TERJEBAK UTANG KONSUMTIF PAYLATER ----------
label ending_paylater:
    # Ending buruk (utang): Pemain menunda pembayaran belanja keinginan dan terjerat tagihan
    # yang memotong anggaran bulan berikutnya.
    $ musik("bgm_ending_reflektif")
    $ ending_nama = _("Ending C: Terjerat PayLater")
    "{b}ENDING C: Terjerat PayLater{/b}"
    if pakai_sprite_billa:
        show billa khawatir with dissolve
    "Uang jajanmu masih ada, tapi utang PayLater ikut terbawa ke bulan depan beserta biayanya."
    "Bulan depan akan terasa lebih berat dari yang kamu kira. Sebagian uang saku langsung terpotong untuk membayar tagihan lama."
    if pakai_sprite_billa:
        hide billa with dissolve
    jump rekap

# ---------- ENDING D: KEHABISAN UANG SAKU (DEFISIT TOTAL) ----------
label ending_habis:
    # Ending terburuk (defisit): Uang saku habis sebelum akhir bulan karena belanja impulsif
    # atau ketiadaan dana darurat saat terjadi krisis.
    $ musik("bgm_ending_reflektif")
    $ ending_nama = _("Ending D: Mie Instan Akhir Bulan")
    "{b}ENDING D: Mie Instan Akhir Bulan{/b}"
    if pakai_sprite_billa:
        show billa kecewa with dissolve
    "Saldomu habis dan masih ada beberapa hari tersisa. Kamu terpaksa makan mie instan dan meminjam uang ke teman."
    $ telepon_mama = "kecewa"
    mama "Nak, kok sudah kehabisan lagi? Ayo kita bicara dan susun rencana bersama."
    $ telepon_mama = None
    if pakai_sprite_billa:
        hide billa with dissolve
    "Ini bukan akhir dunia. Kesalahan pengelolaan uang adalah pelajaran, dan kamu bisa mencoba lagi bulan depan dengan strategi yang lebih baik."
    jump rekap


# ============================================================
# 9. REKAP RAPOR KEUANGAN & TAUTAN POST-TEST
# ============================================================
label rekap:
    # Menutup HUD permainan dan menampilkan modal E-Statement Rapor Keuangan Mahasiswa
    # serta tautan kuesioner Post-Test penelitian.
    $ skor_max = 22
    $ persen = (skor * 100) // 22
    hide screen hud
    hide screen el_ui_quick_menu
    hide weather with dissolve
    scene bg akhir with el_soft_fade

    call screen rekap_finansial

    return


# ============================================================
# 10. SUBRUTIN: AKHIR MINGGU (PENGELUARAN KEBUTUHAN POKOK)
# ============================================================
label akhir_minggu:
    # Subrutin otomatis yang dipanggil di akhir setiap minggu (Minggu 1 s.d. 4).
    # Memotong Rp 250.000 untuk biaya hidup pokok mingguan (makan dasar, transport,
    # kuota internet, dan laundry kos).
    # Total sebulan: 4 minggu x Rp 250.000 = Rp 1.000.000 (50% dari uang saku Rp 2.000.000).
    $ ubah_uang(-250000, "Kebutuhan pokok")
    "Akhir minggu ke-[minggu]. Kebutuhan pokok (makan dasar, transport, kuota, laundry) memakai {b}Rp 250.000{/b}."

    # Rekap mingguan: pengeluaran = uang jajan yang keluar, di luar uang yang dipindah ke dana darurat.
    $ keluar_minggu = (uang_awal_minggu - uang) - (dana_darurat - dana_awal_minggu)
    $ t_keluar = rp(keluar_minggu)
    $ t_uang = rp(uang)
    $ t_dana = rp(dana_darurat)
    "{b}Rekap minggu ke-[minggu]{/b}\nPengeluaran: [t_keluar]. Sisa uang jajan: [t_uang]. Dana darurat: [t_dana]."
    if hutang > 0:
        $ bunga_minggu = int(hutang * 0.05)
        $ hutang += bunga_minggu
        $ t_bunga = rp(bunga_minggu)
        $ t_hutang = rp(hutang)
        $ sfx("sfx_peringatan")
        "Tagihan PayLater dikenakan bunga mingguan 5 persen (+[t_bunga]). Total tagihan berjalan: {b}[t_hutang]{/b}."
        tip "Bunga PayLater terus bertambah setiap minggu selama belum lunas. Semakin lama menunda, semakin berat beban finansialmu."
    $ uang_awal_minggu = uang
    $ dana_awal_minggu = dana_darurat

    if minggu < 4:
        $ minggu += 1
    return
