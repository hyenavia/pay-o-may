# ============================================================
#  PAY O' MAY - UI KUSTOM (Kit "Everyday Life Dialogue UI")
#
#  Deskripsi File:
#  File ini bertanggung jawab mengintegrasikan aset visual kit UI
#  (Everyday Life Dialogue UI) dengan sistem internal Ren'Py.
#  Semua screen bawaan (dialog, pilihan, simpan/muat, preferensi,
#  dan menu utama) dibungkus agar memiliki tema pixel art konsisten.
# ============================================================

# ------------------------------------------------------------
# 1. PENGATURAN DASAR & RENDER GRAFIS
# ------------------------------------------------------------
# Menentukan layar jeda kustom saat pemain menekan Esc atau tombol menu
define _game_menu_screen = "pausa_menu"

init python:
    # Memastikan tekstur pixel art dirender secara tajam tanpa blurring
    if hasattr(config, "nearest_neighbor"):
        config.nearest_neighbor = True
    if hasattr(config, "mipmap"):
        config.mipmap = False

# Pengaturan Font Utama Permainan (Fredoka sebagai default, PixelifySans sebagai opsi retro)
init -1 python:
    UI_FONT = "fonts/Fredoka.ttf"
    if not renpy.loadable(UI_FONT):
        UI_FONT = "DejaVuSans.ttf"

style el_ui_text:
    font UI_FONT

# Penyesuaian tata letak pop-up notifikasi transaksi keuangan (+/- Saldo)
# Diposisikan presisi di bagian tengah atas layar di bawah tombol bilah menu
style notify_frame:
    xalign 0.5
    xoffset 0
    ypos el_u(39)
    padding (el_u(8), el_u(3), el_u(8), el_u(4))

style notify_text:
    font UI_FONT
    size el_u(7.5)
    xalign 0.5
    text_align 0.5


# ------------------------------------------------------------
# 2. PERBAIKAN GAYA DIALOG & TEKS SISTEM
# ------------------------------------------------------------
# Me-reset offset dan margin bawaan Ren'Py agar posisi teks dialog
# dan label nama karakter sejajar rapi di dalam kotak dialog UI kustom.
style say_dialogue:
    xpos 0
    ypos 0
    xanchor 0.0
    xminimum 0
    xmaximum el_u(556)
    font UI_FONT
    outlines []

style say_thought is say_dialogue

style say_label:
    xalign 0.0
    yalign 0.0
    font UI_FONT
    outlines []

# Lokalisasi teks konfirmasi bawaan Ren'Py ke Bahasa Indonesia
init 1 python:
    layout.QUIT = _("Yakin ingin keluar?")
    layout.MAIN_MENU = _("Yakin ingin kembali ke menu utama?\nProgres yang belum disimpan akan hilang.")
    layout.OVERWRITE_SAVE = _("Yakin ingin menimpa data simpananmu?")
    layout.LOADING = _("Memuat akan menghapus progres yang belum disimpan.\nYakin ingin melanjutkan?")
    layout.DELETE_SAVE = _("Yakin ingin menghapus data simpanan ini?")

# Tampilan teks transisi tengah layar (centered) berlatar belakang gelap pekat
define centered = Character(None, what_style="centered_text", window_style="centered_window", screen="centered_say")

screen centered_say(who, what):
    window:
        id "window"
        background Solid("#10182e")
        xfill True
        yfill True
        text what:
            id "what"
            color "#fdf5cc"
            size el_ui_font_size(14)
            xalign 0.5
            yalign 0.5
            text_align 0.5
            xmaximum el_u(500)


# ------------------------------------------------------------
# 3. PEMBUNGKUS SCREEN STANDAR REN'PY -> KOMPONEN KIT
# ------------------------------------------------------------
# Membelokkan panggilan screen standar Ren'Py ke implementasi screen Everyday Life
screen say(who, what):
    use el_ui_say(who, what)

screen choice(items):
    use el_ui_choices(items)

screen confirm(message, yes_action, no_action):
    use el_ui_confirm(message, yes_action, no_action)

screen save():
    tag menu
    use el_ui_save

screen load():
    tag menu
    use el_ui_load

screen preferences():
    tag menu
    use el_ui_preferences

screen history():
    tag menu
    use el_ui_history

# Quick menu bawaan dinonaktifkan karena navigasi cepat memakai bilah atas el_ui_quick_menu
screen quick_menu():
    null


# ============================================================
# COVER (MENU UTAMA)
# ============================================================
# ------------------------------------------------------------
# 4. COVER / MENU UTAMA (HOME SCREEN)
# ------------------------------------------------------------
screen main_menu():
    """
    Tampilan Menu Utama (Home Screen) permainan.
    Fitur:
    - Background dinamis yang warnanya menyesuaikan tema aktif pilihan pemain.
    - Efek partikel visual cuaca kelopak bunga melayang (el_weather petals).
    - Panel menu interaktif: Mulai Main, Muat Game, Pengaturan, Tentang, Cara Bermain, Keluar.
    - Nomor versi permainan otomatis dari config.version.
    - Kotak informasi pengisian kuesioner Pre-Test & Post-Test penelitian.
    """
    tag menu

    # Memuat gambar latar cover sesuai tema warna UI yang dipilih (cream, blue, dark, dll)
    $ _cover_file = "images/cover_" + getattr(store, "el_ui_theme", "cream") + ".png"
    if renpy.loadable(_cover_file):
        add _cover_file
    elif renpy.loadable("images/cover.png"):
        add "cover"
    else:
        add "bg akhir"

    ## Animasi cuaca kelopak bunga di home screen
    add el_weather("petals")

    # --- LOGO JUDUL & VERSI GAME (KANAN ATAS) ---
    vbox:
        xalign 0.95
        ypos el_u(16)
        spacing el_u(2)

        add "images/title_logo.png" xsize el_u(165) ysize el_u(115) xalign 0.5
        $ _ver_shadow = "#ffffffbb" if getattr(store, "el_ui_theme", "cream") == "cream" else "#10182ebb"
        text "v[config.version]" style "el_ui_text" font "fonts/Cinzel.ttf" color el_ui_color(1) size el_u(9.5) bold True xalign 0.5 outlines [(1, _ver_shadow, 0, 0)]

    # --- KOLOM MENU UTAMA (TOMBOL & INFORMASI RISET) ---
    vbox:
        xpos el_u(24)
        ypos el_u(18)
        spacing el_u(5)

        # Panel Menu Tombol
        frame:
            background el_ui_frame("menu_panel")
            xsize el_u(240)
            ysize el_u(255)
            padding (el_u(20), el_u(16), el_u(20), el_u(16))

            vbox:
                spacing el_u(5)
                xalign 0.5
                yalign 0.5
                use el_ui_button(_("Mulai Main"), Start(), width=190)
                use el_ui_button(_("Muat Game"), ShowMenu("el_ui_load"), width=190)
                use el_ui_button(_("Pengaturan"), ShowMenu("el_ui_preferences"), width=190)
                use el_ui_button(_("Tentang"), ShowMenu("about"), width=190)
                use el_ui_button(_("Cara Bermain"), ShowMenu("help"), width=190)
                use el_ui_button(_("Keluar"), Quit(confirm=True), width=190)

        # Kotak Informasi Riset GDLC (Tepat di bawah kolom tombol)
        frame:
            background el_ui_frame("tooltip")
            xsize el_u(240)
            padding (el_u(12), el_u(8), el_u(12), el_u(8))
            text _("Pre-Test akan muncul sebelum cerita dimulai, dan Post-Test setelah ending.") style "el_ui_text" color el_ui_color() size el_ui_font_size(9.5) text_align 0.5 xalign 0.5


# ------------------------------------------------------------
# 5. MENU JEDA (PAUSE MENU / TOMBOL ESC SAAT BERMAIN)
# ------------------------------------------------------------
screen pausa_menu():
    """
    Menu jeda saat pemain menekan Esc atau tombol jeda di dalam cerita.
    Menyediakan akses cepat ke Simpan, Muat, Pengaturan, Bantuan, Tentang, dan Menu Utama.
    """
    tag menu

    use el_ui_shell(_("Jeda")):
        hbox:
            xpos el_u(40)
            ypos el_u(72)
            spacing el_u(16)
            vbox:
                spacing el_u(8)
                use el_ui_button(_("Simpan"), ShowMenu("el_ui_save"), width=200)
                use el_ui_button("Muat Game", ShowMenu("el_ui_load"), width=200)
                use el_ui_button("Pengaturan", ShowMenu("el_ui_preferences"), width=200)
            vbox:
                spacing el_u(8)
                use el_ui_button("Cara Bermain", ShowMenu("help"), width=200)
                use el_ui_button("Tentang", ShowMenu("about"), width=200)
                use el_ui_button(_("Menu Utama"), MainMenu(), width=200)


# ------------------------------------------------------------
# 6. PARAGRAF BANTU (HELPER LAYOUT TEKS)
# ------------------------------------------------------------
screen pom_p(teks, judul=False):
    """
    Komponen pembantu format paragraf untuk halaman Tentang dan Cara Bermain.
    """
    text teks:
        style "el_ui_text"
        color (el_ui_color(2) if judul else el_ui_color())
        size el_ui_font_size(12)
        xmaximum el_u(540)


# ------------------------------------------------------------
# 7. LAYAR TENTANG (INFORMASI AKADEMIK & PENGEMBANG)
# ------------------------------------------------------------
screen about():
    """
    Menampilkan informasi proyek gim Pay o' May oleh Hyenavia,
    metodologi perancangan (GDLC), kredit aset visual/audio,
    dan informasi lisensi Ren'Py.
    """
    tag menu

    use el_ui_shell(_("Tentang")): 
        viewport:
            xpos el_u(40)
            ypos el_u(66)
            xsize el_u(560)
            ysize el_u(220)
            mousewheel True
            draggable True

            vbox:
                spacing el_u(8)

                use pom_p("Pay o' May", True)
                use pom_p(_("Versi [config.version!t]"))
                use pom_p(_("Gim novel visual edukasi untuk meningkatkan kesadaran finansial mahasiswa perantauan. Kamu menjalani satu bulan dengan uang saku terbatas dan memutuskan sendiri ke mana uang itu pergi."))

                use pom_p(_("Pengembang"), True)
                use pom_p("Hyenavia")

                use pom_p(_("Tentang Proyek"), True)
                use pom_p(_("Dikembangkan sebagai Tugas Akhir dengan metode Game Development Life Cycle (GDLC). Cerita dan angka dalam game adalah fiksi untuk keperluan edukasi, bukan nasihat keuangan profesional."))

                use pom_p(_("Kredit"), True)
                use pom_p("[kredit_visual]\n[kredit_audio]")

                use pom_p(_("Catatan Pembaruan"), True)
                use pom_p(_("Riwayat pembaruan dan perubahan versi lengkap tercatat pada berkas CHANGELOG.md di direktori gim."))

                use pom_p(_("Dibuat dengan Ren'Py"), True)
                use pom_p("Ren'Py [renpy.version_only].")


# ------------------------------------------------------------
# 8. LAYAR CARA BERMAIN (PANDUAN PEMAIN)
# ------------------------------------------------------------
screen help():
    """
    Panduan bermain yang menjelaskan mekanisme anggaran bulanan, papan status HUD,
    konsekuensi pengambilan keputusan, 4 cabang ending, dan kontrol input permainan.
    """
    tag menu

    use el_ui_shell(_("Cara Bermain")): 
        viewport:
            xpos el_u(40)
            ypos el_u(66)
            xsize el_u(560)
            ysize el_u(220)
            mousewheel True
            draggable True

            vbox:
                spacing el_u(8)

                use pom_p(_("Tujuan"), True)
                use pom_p(_("Kamu mahasiswa perantauan yang menerima uang saku Rp 2.000.000 untuk satu bulan. Bertahanlah sampai 1 Bulan dengan keputusan keuangan yang cerdas."))

                use pom_p(_("Papan Status (pojok kanan atas)"), True)
                use pom_p(_("Uang jajan: sisa uang untuk kebutuhan sehari-hari. Baranya berubah warna saat uangmu menipis.\nDana darurat: tabungan terpisah untuk kejadian tak terduga.\nTagihan PayLater: utang yang harus dibayar di akhir bulan (muncul jika kamu berutang)."))

                use pom_p(_("Mengambil Keputusan"), True)
                use pom_p(_("Di beberapa momen kamu harus memilih. Tidak ada jawaban benar mutlak, tetapi setiap pilihan punya konsekuensi pada uang, utang, dan ending. Baca Tips Finansial yang muncul setelah tiap keputusan."))

                use pom_p(_("Ending"), True)
                use pom_p(_("Ada 4 ending yang ditentukan oleh sisa uang, dana darurat, utang, dan kualitas keputusanmu."))

                use pom_p(_("Setelah Selesai"), True)
                use pom_p(_("Jangan lupa mengisi Post-Test yang diberikan."))

                use pom_p(_("Kontrol"), True)
                use pom_p(_("Klik, Enter, atau Spasi: lanjut dialog.\nRoda mouse: gulir menu atau kembali ke dialog sebelumnya.\nCtrl (tahan) atau Tab: lewati dialog yang sudah dibaca.\nEsc: buka menu Jeda.\nBilah atas: Riwayat, Simpan, Muat, dan Opsi."))


# ------------------------------------------------------------
# 9. RAPOR KEUANGAN BULANAN (E-STATEMENT REKAP AKHIR BULAN)
# ------------------------------------------------------------
init python:
    def hitung_gelar_finansial():
        """
        Mengevaluasi keputusan finansial pemain di akhir permainan.
        Menghasilkan tuple: (Nama Gelar, Kode Warna Hex, Pesan Ulasan/Evaluasi).
        Kriteria didasarkan pada:
        - Saldo sisa uang jajan (uang)
        - Dana darurat yang terkumpul (dana_darurat)
        - Beban tagihan utang PayLater (hutang)
        - Persentase pilihan tepat (persen)
        - Status bantuan finansial orang tua (mama_bantu)
        - Frekuensi keputusan keinginan konsumtif (wants)
        """
        u = getattr(store, "uang", 0)
        d = getattr(store, "dana_darurat", 0)
        h = getattr(store, "hutang", 0)
        s = getattr(store, "skor", 0)
        s_max = 22
        p = (s * 100) // s_max if s_max else 0
        mb = getattr(store, "mama_bantu", False)
        w = getattr(store, "wants", 0)

        def _t(s):
            return renpy.translation.translate_string(s) if s else ""

        if u <= 0:
            return (_t(_("Sobat Mie Instan Akhir Bulan")), "#ef5350", _t(_("Uang saku habis sebelum akhir bulan. Perlu evaluasi pos pengeluaran besar dan mulai sisihkan dana darurat sejak awal bulan.")))
        elif h > 0:
            return (_t(_("Korban Kemudahan PayLater")), "#ffa726", _t(_("Terjebak ilusi belanja sekarang bayar nanti. Berhati-hatilah dengan bunga dan biaya layanan utang konsumtif.")))
        elif getattr(store, "pinjam_dimas", "") == "penuh" and u < 100000:
            return (_t(_("Korban Sungkan Teman")), "#ff7043", _t(_("Uangmu tertahan karena meminjamkan melebihi batas kerelaan diri. Belajarlah berani berkata tidak saat kondisi keuangan pribadi belum stabil.")))
        elif u >= 300000 and d >= 100000 and p >= 75 and not mb:
            if d >= 200000:
                return (_t(_("Master Dana Darurat")), "#4caf50", _t(_("Luar biasa! Mampu membangun benteng keamanan finansial yang kokoh dan tetap mandiri sepanjang bulan.")))
            else:
                return (_t(_("Akuntan Kos Teladan")), "#42a5f5", _t(_("Sangat disiplin membedakan kebutuhan dan keinginan. Anggaran bulanan terkelola secara seimbang dan terarah.")))
        elif w <= 3:
            return (_t(_("Pejuang Hemat & Terencana")), "#26a69a", _t(_("Mampu menahan godaan konsumtif dan memprioritaskan kebutuhan pokok dengan sangat baik.")))
        else:
            return (_t(_("Survivor Tanggal Tua")), "#78909c", _t(_("Berhasil bertahan melewati bulan tanpa utang, meski pengeluaran keinginan masih bisa ditekan lebih efisien.")))

screen rekap_finansial():
    """
    Screen Rapor Finansial (E-Statement Bulanan Mahasiswa).
    Menampilkan rangkuman performa literasi keuangan pemain di akhir cerita:
    - Ringkasan Saldo Akhir, Tabungan Dana Darurat, Tagihan PayLater, Status Bantuan, dan Piutang Teman.
    - Skor Kesadaran Finansial (skor/skor_max).
    - Analisis alokasi Kebutuhan (Needs), Keinginan (Wants), dan Langganan Layanan.
    - Gelar finansial dan ulasan evaluasi dari hitung_gelar_finansial().
    - Tombol tautan langsung ke kuesioner Post-Test penelitian dan tombol kembali ke menu utama.
    """
    modal True
    zorder 150

    add Solid("#10182ecc")

    frame:
        background el_ui_frame("menu_panel")
        xalign 0.5
        yalign 0.5
        xsize el_u(590)
        padding (el_u(20), el_u(10), el_u(20), el_u(10))

        vbox:
            spacing el_u(3)

            # --- HEADER ---
            hbox:
                xfill True
                vbox:
                    spacing el_u(1)
                    text _("RAPOR KEUANGAN BULANAN") style "el_ui_text" color el_ui_color(2) size el_ui_font_size(15) bold True
                    $ _nama_display = getattr(store, "nama", "Billa")
                    $ _ending_display = getattr(store, "ending_nama", "Selesai")
                    text _("E-Statement Mahasiswa: [_nama_display] | [_ending_display!t]") style "el_ui_text" color el_ui_color(1) size el_ui_font_size(9.5)

                $ _gelar_info = hitung_gelar_finansial()
                frame:
                    background el_ui_frame("tooltip")
                    xalign 1.0
                    yalign 0.5
                    padding (el_u(10), el_u(3), el_u(10), el_u(3))
                    text "[_gelar_info[0]!t]" style "el_ui_text" color _gelar_info[1] size el_ui_font_size(10.5) bold True

            null height el_u(1)

            # --- DUA KOLOM LAPORAN ---
            hbox:
                spacing el_u(12)

                # KOLOM KIRI: ARUS KAS & SALDO
                frame:
                    background el_ui_frame("tooltip")
                    xsize el_u(266)
                    padding (el_u(12), el_u(6), el_u(12), el_u(6))

                    vbox:
                        spacing el_u(3)
                        text _("RINGKASAN SALDO & ARUS KAS") style "el_ui_text" color el_ui_color(2) size el_ui_font_size(9.5) bold True
                        null height el_u(1)

                        hbox:
                            xfill True
                            text _("Saldo Sisa Uang Jajan:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _u = getattr(store, "uang", 0)
                            $ _t_uang = rp(_u)
                            text "[_t_uang]" style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#2e7d32" if _u >= 300000 else ("#e65100" if _u > 0 else "#c62828"))

                        hbox:
                            xfill True
                            text _("Simpanan Dana Darurat:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _d = getattr(store, "dana_darurat", 0)
                            $ _t_dana = rp(_d)
                            text "[_t_dana]" style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#1976d2" if _d > 0 else el_ui_color(1))

                        hbox:
                            xfill True
                            text _("Sisa Tagihan PayLater:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _h = getattr(store, "hutang", 0)
                            if _h <= 0:
                                text _("Rp 0 (Bebas Utang)") style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                $ _t_hutang = rp(_h)
                                text "[_t_hutang]" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#c62828"

                        hbox:
                            xfill True
                            text _("Piutang Teman:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _pj_status = getattr(store, "pinjam_dimas", "")
                            if _pj_status == "penuh":
                                text _("Rp 200.000 (Macet)") style "el_ui_text" size el_ui_font_size(9.5) bold True color "#c62828"
                            elif _pj_status == "sebagian":
                                text _("Rp 0 (Sudah Lunas)") style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                text "Rp 0" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                        hbox:
                            xfill True
                            text _("Bantuan Dana Darurat:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            if not getattr(store, "mama_bantu", False):
                                text _("100% Mandiri") style "el_ui_text" size el_ui_font_size(9.5) color "#2e7d32"
                            else:
                                text _("Dibantu Mama") style "el_ui_text" size el_ui_font_size(9.5) color "#e65100"

                        hbox:
                            xfill True
                            text _("Pencatatan Keuangan:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            text (_("Aktif Mencatat") if getattr(store, "catat", False) else _("Tidak Mencatat")) style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                # KOLOM KANAN: SKOR & ANALISIS KEPUTUSAN
                frame:
                    background el_ui_frame("tooltip")
                    xsize el_u(266)
                    padding (el_u(12), el_u(6), el_u(12), el_u(6))

                    vbox:
                        spacing el_u(3)
                        text _("SKOR KESADARAN FINANSIAL") style "el_ui_text" color el_ui_color(2) size el_ui_font_size(9.5) bold True
                        null height el_u(1)

                        $ _s = getattr(store, "skor", 0)
                        $ _sm = 22
                        $ _p = (_s * 100) // _sm if _sm else 0

                        hbox:
                            xfill True
                            text _("Skor:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            text "[_s] / [_sm] ([_p]%)" style "el_ui_text" size el_ui_font_size(9.5) bold True color el_ui_color(2)

                        hbox:
                            xfill True
                            text _("Kebutuhan/Tabungan (Needs):") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _needs = getattr(store, "needs", 0)
                            text (_("[_needs] kali")) style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"

                        hbox:
                            xfill True
                            text _("Keinginan/Gaya Hidup (Wants):") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _wants = getattr(store, "wants", 0)
                            text (_("[_wants] kali")) style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#e65100" if _wants >= 5 else el_ui_color(1))

                        hbox:
                            xfill True
                            text _("Langganan Hiburan:") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _lang = getattr(store, "langganan", "")
                            if _lang == "tahunan":
                                text _("Tahunan (Impulsif)") style "el_ui_text" size el_ui_font_size(9.5) bold True color "#e65100"
                            elif _lang == "bulanan":
                                text _("Bulanan (Fleksibel)") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)
                            elif _lang == "nobar":
                                text _("Nobar (Hemat Cerdas)") style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                text "-" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                        null height el_u(1)
                        $ _gelar_msg = _gelar_info[2]
                        text "[_gelar_msg!t]" style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(1) italic True

            # --- PELAJARAN KUNCI ---
            frame:
                background None
                padding (el_u(4), 0, el_u(4), 0)
                text _("💡 {b}Kunci Sukses Finansial:{/b} Sisihkan dana darurat di awal bulan, batasi belanja keinginan, dan hindari utang konsumtif PayLater.") style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(1)

            null height el_u(1)

            # --- TOMBOL AKSI BAWAH ---
            $ _buka_post = getattr(store, "posttest_dibuka", False)

            vbox:
                xalign 0.5
                spacing el_u(2)

                if not _buka_post:
                    text _("⚠️ Harap buka kuesioner Post-Test terlebih dahulu sebelum menekan tombol Selesai.") style "el_ui_text" size el_ui_font_size(8.5) color "#e65100" xalign 0.5 italic True
                else:
                    text _("💡 Setelah selesai mengisi Post-Test di browser, klik tombol 'Saya Sudah Mengisi & Selesai'.") style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(2) xalign 0.5 italic True

                null height el_u(1)

                hbox:
                    xalign 0.5
                    spacing el_u(16)

                    use el_ui_button(_("Buka Post-Test (Kuesioner)"), [OpenURL(url_posttest), SetVariable("posttest_dibuka", True)], width=225)

                    if not _buka_post:
                        use el_ui_button(_("Selesai & Menu Utama"), Return(), sensitive=False, width=225)
                    else:
                        use el_ui_button(_("Saya Sudah Mengisi & Selesai"), [SetVariable("posttest_selesai", True), Return()], sensitive=True, width=225)


# ------------------------------------------------------------
# 10. SCREEN KUESIONER PRE-TEST (INSTRUMEN PENELITIAN GDLC)
# ------------------------------------------------------------
screen kuesioner_pretest():
    """
    Screen Kuesioner Pre-Test (Instrumen Penelitian GDLC).
    Pemain diwajibkan membuka kuesioner Pre-Test terlebih dahulu sebelum tombol
    lanjut / mulai permainan terbuka, konsisten dengan alur Post-Test pada Rapor Finansial.
    """
    modal True
    zorder 150

    add Solid("#10182ecc")

    $ _buka_pre = getattr(store, "pretest_dibuka", False)

    frame:
        background el_ui_frame("menu_panel")
        xalign 0.5
        yalign 0.5
        xsize el_u(520)
        padding (el_u(24), el_u(18), el_u(24), el_u(18))

        vbox:
            spacing el_u(5)
            xalign 0.5

            # --- HEADER ---
            vbox:
                xalign 0.5
                spacing el_u(1)
                text _("KUESIONER PRE-TEST") style "el_ui_text" color el_ui_color(2) size el_ui_font_size(15) bold True xalign 0.5
                text _("Instrumen Penelitian Evaluasi Literasi Keuangan Mahasiswa") style "el_ui_text" color el_ui_color(1) size el_ui_font_size(9) xalign 0.5

            null height el_u(1)

            # --- KOTAK PENJELASAN ---
            frame:
                background el_ui_frame("tooltip")
                xalign 0.5
                xfill True
                padding (el_u(14), el_u(9), el_u(14), el_u(9))
                text _("Sebelum mulai bermain, silakan isi kuesioner singkat untuk mengukur pemahaman awal pengelolaan keuanganmu.\n\nData kuesioner ini digunakan untuk pengujian efektivitas media pembelajaran gim edukatif Pay o' May.") style "el_ui_text" color el_ui_color() size el_ui_font_size(9) text_align 0.5 xalign 0.5

            null height el_u(1)

            # --- PETUNJUK STATUS PENGISIAN (KONSISTEN DENGAN ENDING) ---
            vbox:
                xalign 0.5
                spacing el_u(2)

                if not _buka_pre:
                    text _("⚠️ Harap buka kuesioner Pre-Test terlebih dahulu sebelum melanjutkan.") style "el_ui_text" size el_ui_font_size(8.5) color "#e65100" xalign 0.5 italic True
                else:
                    text _("💡 Setelah selesai mengisi Pre-Test di browser, klik tombol 'Saya sudah mengisi Pre-Test'.") style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(2) xalign 0.5 italic True

            null height el_u(2)

            # --- TOMBOL AKSI (KONSISTEN DENGAN ENDING POST-TEST) ---
            hbox:
                xalign 0.5
                spacing el_u(14)

                use el_ui_button(_("Buka tautan Pre-Test"), [OpenURL(url_pretest), SetVariable("pretest_dibuka", True)], width=225)

                if not _buka_pre:
                    use el_ui_button(_("Saya sudah mengisi Pre-Test"), Return(), sensitive=False, width=225)
                else:
                    use el_ui_button(_("Saya sudah mengisi Pre-Test"), [SetVariable("pretest_selesai", True), Return()], sensitive=True, width=225)



