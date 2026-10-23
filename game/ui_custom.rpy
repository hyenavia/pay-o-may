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

# Pengaturan Font Utama Permainan (PixelifySans untuk nuansa retro)
init -1 python:
    UI_FONT = "fonts/PixelifySans.ttf"
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
    layout.QUIT = "Yakin ingin keluar?"
    layout.MAIN_MENU = "Yakin ingin kembali ke menu utama?\nProgres yang belum disimpan akan hilang."
    layout.OVERWRITE_SAVE = "Yakin ingin menimpa data simpananmu?"
    layout.LOADING = "Memuat akan menghapus progres yang belum disimpan.\nYakin ingin melanjutkan?"
    layout.DELETE_SAVE = "Yakin ingin menghapus data simpanan ini?"

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

    frame:
        background el_ui_frame("menu_panel")
        xpos el_u(24)
        ypos el_u(22)
        xsize el_u(250)
        ysize el_u(330)
        padding (el_u(24), el_u(18), el_u(24), el_u(18))

        vbox:
            spacing el_u(6)
            text "PAY O' MAY" style "el_ui_text" color el_ui_color() size el_u(22)
            null height el_u(4)
            use el_ui_button("Mulai Main", Start(), width=190)
            use el_ui_button("Muat Game", ShowMenu("el_ui_load"), width=190)
            use el_ui_button("Pengaturan", ShowMenu("el_ui_preferences"), width=190)
            use el_ui_button("Tentang", ShowMenu("about"), width=190)
            use el_ui_button("Cara Bermain", ShowMenu("help"), width=190)
            use el_ui_button("Keluar", Quit(confirm=True), width=190)
            null height el_u(4)
            text "v[config.version]" style "el_ui_text" color el_ui_color(1) size el_u(10) xalign 0.5

    frame:
        background el_ui_frame("tooltip")
        xalign 0.97
        yalign 0.95
        xmaximum el_u(230)
        padding (el_u(14), el_u(10), el_u(14), el_u(10))
        text "Pre-Test akan muncul sebelum cerita dimulai, dan Post-Test setelah ending." style "el_ui_text" color el_ui_color() size el_ui_font_size(11)


# ------------------------------------------------------------
# 5. MENU JEDA (PAUSE MENU / TOMBOL ESC SAAT BERMAIN)
# ------------------------------------------------------------
screen pausa_menu():
    """
    Menu jeda saat pemain menekan Esc atau tombol jeda di dalam cerita.
    Menyediakan akses cepat ke Simpan, Muat, Pengaturan, Bantuan, Tentang, dan Menu Utama.
    """
    tag menu

    use el_ui_shell("Jeda"):
        hbox:
            xpos el_u(40)
            ypos el_u(72)
            spacing el_u(16)
            vbox:
                spacing el_u(8)
                use el_ui_button("Simpan", ShowMenu("el_ui_save"), width=200)
                use el_ui_button("Muat Game", ShowMenu("el_ui_load"), width=200)
                use el_ui_button("Pengaturan", ShowMenu("el_ui_preferences"), width=200)
            vbox:
                spacing el_u(8)
                use el_ui_button("Cara Bermain", ShowMenu("help"), width=200)
                use el_ui_button("Tentang", ShowMenu("about"), width=200)
                use el_ui_button("Menu Utama", MainMenu(), width=200)


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
    Menampilkan informasi proyek Tugas Akhir S1 TRM Universitas Telkom,
    data pengembang, metodologi perancangan (GDLC), kredit aset visual/audio,
    dan informasi lisensi Ren'Py.
    """
    tag menu

    use el_ui_shell("Tentang"):
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
                use pom_p("Versi [config.version!t]")
                use pom_p("Gim novel visual edukasi untuk meningkatkan kesadaran finansial mahasiswa perantauan. Kamu menjalani satu bulan dengan uang saku terbatas dan memutuskan sendiri ke mana uang itu pergi.")

                use pom_p("Pengembang", True)
                use pom_p("Luthfi Rais Asral\nS1 Terapan Teknologi Rekayasa Multimedia\nFakultas Ilmu Terapan, Universitas Telkom")

                use pom_p("Tentang Proyek", True)
                use pom_p("Dikembangkan sebagai Tugas Akhir dengan metode Game Development Life Cycle (GDLC). Cerita dan angka dalam game adalah fiksi untuk keperluan edukasi, bukan nasihat keuangan profesional.")

                use pom_p("Kredit", True)
                use pom_p("[kredit_visual]\n[kredit_audio]")
                use pom_p("itch.io")

                use pom_p("Catatan Pembaruan", True)
                use pom_p("Riwayat pembaruan dan perubahan versi lengkap tercatat pada berkas CHANGELOG.md di direktori gim.")

                use pom_p("Dibuat dengan Ren'Py", True)
                use pom_p("Ren'Py [renpy.version_only]. Informasi lisensi lengkap tersedia di folder permainan.")


# ------------------------------------------------------------
# 8. LAYAR CARA BERMAIN (PANDUAN PEMAIN)
# ------------------------------------------------------------
screen help():
    """
    Panduan bermain yang menjelaskan mekanisme anggaran bulanan, papan status HUD,
    konsekuensi pengambilan keputusan, 4 cabang ending, dan kontrol input permainan.
    """
    tag menu

    use el_ui_shell("Cara Bermain"):
        viewport:
            xpos el_u(40)
            ypos el_u(66)
            xsize el_u(560)
            ysize el_u(220)
            mousewheel True
            draggable True

            vbox:
                spacing el_u(8)

                use pom_p("Tujuan", True)
                use pom_p("Kamu mahasiswa perantauan yang menerima uang saku Rp 2.000.000 untuk satu bulan. Bertahanlah sampai 1 Bulan dengan keputusan keuangan yang cerdas.")

                use pom_p("Papan Status (pojok kanan atas)", True)
                use pom_p("Uang jajan: sisa uang untuk kebutuhan sehari-hari. Baranya berubah warna saat uangmu menipis.\nDana darurat: tabungan terpisah untuk kejadian tak terduga.\nTagihan PayLater: utang yang harus dibayar di akhir bulan (muncul jika kamu berutang).")

                use pom_p("Mengambil Keputusan", True)
                use pom_p("Di beberapa momen kamu harus memilih. Tidak ada jawaban benar mutlak, tetapi setiap pilihan punya konsekuensi pada uang, utang, dan ending. Baca Tips Finansial yang muncul setelah tiap keputusan.")

                use pom_p("Ending", True)
                use pom_p("Ada 4 ending yang ditentukan oleh sisa uang, dana darurat, utang, dan kualitas keputusanmu.")

                use pom_p("Setelah Selesai", True)
                use pom_p("Jangan lupa mengisi Post-Test yang diberikan peneliti.")

                use pom_p("Kontrol", True)
                use pom_p("Klik, Enter, atau Spasi: lanjut dialog.\nRoda mouse: gulir menu atau kembali ke dialog sebelumnya.\nCtrl (tahan) atau Tab: lewati dialog yang sudah dibaca.\nEsc: buka menu Jeda.\nBilah atas: Riwayat, Simpan, Muat, dan Opsi.")


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
        s_max = getattr(store, "skor_max", 22)
        p = getattr(store, "persen", (s * 100) // s_max if s_max else 0)
        mb = getattr(store, "mama_bantu", False)
        w = getattr(store, "wants", 0)

        if u < 0:
            return ("Sobat Mie Instan Akhir Bulan", "#ef5350", "Uang saku habis sebelum akhir bulan. Perlu evaluasi pos pengeluaran besar dan mulai sisihkan dana darurat sejak awal bulan.")
        elif h > 0:
            return ("Korban Kemudahan PayLater", "#ffa726", "Terjebak ilusi belanja sekarang bayar nanti. Berhati-hatilah dengan bunga dan biaya layanan utang konsumtif.")
        elif getattr(store, "pinjam_dimas", "") == "penuh" and u < 100000:
            return ("Korban Sungkan Teman", "#ff7043", "Uangmu tertahan karena meminjamkan melebihi batas kerelaan diri. Belajarlah berani berkata tidak saat kondisi keuangan pribadi belum stabil.")
        elif u >= 300000 and d >= 100000 and p >= 75 and not mb:
            if d >= 200000:
                return ("Master Dana Darurat", "#4caf50", "Luar biasa! Mampu membangun benteng keamanan finansial yang kokoh dan tetap mandiri sepanjang bulan.")
            else:
                return ("Akuntan Kos Teladan", "#42a5f5", "Sangat disiplin membedakan kebutuhan dan keinginan. Anggaran bulanan terkelola secara seimbang dan terarah.")
        elif w <= 3:
            return ("Pejuang Hemat & Terencana", "#26a69a", "Mampu menahan godaan konsumtif dan memprioritaskan kebutuhan pokok dengan sangat baik.")
        else:
            return ("Survivor Tanggal Tua", "#78909c", "Berhasil bertahan melewati bulan tanpa utang, meski pengeluaran keinginan masih bisa ditekan lebih efisien.")

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
                    text "RAPOR KEUANGAN BULANAN" style "el_ui_text" color el_ui_color(2) size el_ui_font_size(15) bold True
                    $ _nama_display = getattr(store, "nama", "Raka")
                    $ _ending_display = getattr(store, "ending_nama", "Selesai")
                    text "E-Statement Mahasiswa: [_nama_display] | [_ending_display]" style "el_ui_text" color el_ui_color(1) size el_ui_font_size(9.5)

                $ _gelar_info = hitung_gelar_finansial()
                frame:
                    background el_ui_frame("tooltip")
                    xalign 1.0
                    yalign 0.5
                    padding (el_u(10), el_u(3), el_u(10), el_u(3))
                    text "[_gelar_info[0]]" style "el_ui_text" color _gelar_info[1] size el_ui_font_size(10.5) bold True

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
                        text "RINGKASAN SALDO & ARUS KAS" style "el_ui_text" color el_ui_color(2) size el_ui_font_size(9.5) bold True
                        null height el_u(1)

                        hbox:
                            xfill True
                            text "Saldo Sisa Uang Jajan:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _u = getattr(store, "uang", 0)
                            $ _t_uang = rp(_u)
                            text "[_t_uang]" style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#2e7d32" if _u >= 300000 else ("#e65100" if _u > 0 else "#c62828"))

                        hbox:
                            xfill True
                            text "Simpanan Dana Darurat:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _d = getattr(store, "dana_darurat", 0)
                            $ _t_dana = rp(_d)
                            text "[_t_dana]" style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#1976d2" if _d > 0 else el_ui_color(1))

                        hbox:
                            xfill True
                            text "Sisa Tagihan PayLater:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _h = getattr(store, "hutang", 0)
                            if _h <= 0:
                                text "Rp 0 (Bebas Utang)" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                $ _t_hutang = rp(_h)
                                text "[_t_hutang]" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#c62828"

                        hbox:
                            xfill True
                            text "Piutang Teman:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _pj_status = getattr(store, "pinjam_dimas", "")
                            if _pj_status == "penuh":
                                text "Rp 200.000 (Macet)" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#c62828"
                            elif _pj_status == "sebagian":
                                text "Rp 0 (Sudah Lunas)" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                text "Rp 0" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                        hbox:
                            xfill True
                            text "Bantuan Dana Darurat:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            if not getattr(store, "mama_bantu", False):
                                text "100% Mandiri" style "el_ui_text" size el_ui_font_size(9.5) color "#2e7d32"
                            else:
                                text "Dibantu Mama" style "el_ui_text" size el_ui_font_size(9.5) color "#e65100"

                        hbox:
                            xfill True
                            text "Pencatatan Keuangan:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            text ("Aktif Mencatat" if getattr(store, "catat", False) else "Tidak Mencatat") style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                # KOLOM KANAN: SKOR & ANALISIS KEPUTUSAN
                frame:
                    background el_ui_frame("tooltip")
                    xsize el_u(266)
                    padding (el_u(12), el_u(6), el_u(12), el_u(6))

                    vbox:
                        spacing el_u(3)
                        text "SKOR KESADARAN FINANSIAL" style "el_ui_text" color el_ui_color(2) size el_ui_font_size(9.5) bold True
                        null height el_u(1)

                        $ _s = getattr(store, "skor", 0)
                        $ _sm = getattr(store, "skor_max", 22)
                        $ _p = getattr(store, "persen", (_s * 100) // _sm if _sm else 0)

                        hbox:
                            xfill True
                            text "Skor:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            text "[_s] / [_sm] ([_p]%)" style "el_ui_text" size el_ui_font_size(9.5) bold True color el_ui_color(2)

                        hbox:
                            xfill True
                            text "Kebutuhan/Tabungan (Needs):" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _needs = getattr(store, "needs", 0)
                            text "[_needs] kali" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"

                        hbox:
                            xfill True
                            text "Keinginan/Gaya Hidup (Wants):" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _wants = getattr(store, "wants", 0)
                            text "[_wants] kali" style "el_ui_text" size el_ui_font_size(9.5) bold True color ("#e65100" if _wants >= 5 else el_ui_color(1))

                        hbox:
                            xfill True
                            text "Langganan Hiburan:" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color()
                            $ _lang = getattr(store, "langganan", "")
                            if _lang == "tahunan":
                                text "Tahunan (Impulsif)" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#e65100"
                            elif _lang == "bulanan":
                                text "Bulanan (Fleksibel)" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)
                            elif _lang == "nobar":
                                text "Nobar (Hemat Cerdas)" style "el_ui_text" size el_ui_font_size(9.5) bold True color "#2e7d32"
                            else:
                                text "-" style "el_ui_text" size el_ui_font_size(9.5) color el_ui_color(1)

                        null height el_u(1)
                        $ _gelar_msg = _gelar_info[2]
                        text "[_gelar_msg]" style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(1) italic True

            # --- PELAJARAN KUNCI ---
            frame:
                background None
                padding (el_u(4), 0, el_u(4), 0)
                text "💡 {b}Kunci Sukses Finansial:{/b} Sisihkan dana darurat di awal bulan, batasi belanja keinginan, dan hindari utang konsumtif PayLater." style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(1)

            null height el_u(1)

            # --- TOMBOL AKSI BAWAH ---
            $ _buka_post = getattr(store, "posttest_dibuka", False)

            vbox:
                xalign 0.5
                spacing el_u(2)

                if not _buka_post:
                    text "⚠️ Harap buka kuesioner Post-Test terlebih dahulu sebelum menekan tombol Selesai." style "el_ui_text" size el_ui_font_size(8.5) color "#e65100" xalign 0.5 italic True
                else:
                    text "💡 Setelah selesai mengisi Post-Test di browser, klik tombol 'Saya Sudah Mengisi & Selesai'." style "el_ui_text" size el_ui_font_size(8.5) color el_ui_color(2) xalign 0.5 italic True

                null height el_u(1)

                hbox:
                    xalign 0.5
                    spacing el_u(16)

                    use el_ui_button("Buka Post-Test (Kuesioner)", [OpenURL(url_posttest), SetVariable("posttest_dibuka", True)], width=225)

                    if not _buka_post:
                        use el_ui_button("Selesai & Menu Utama", Return(), sensitive=False, width=225)
                    else:
                        use el_ui_button("Saya Sudah Mengisi & Selesai", Return(), sensitive=True, width=225)


