# DIMODIFIKASI untuk Pay o' May: label diterjemahkan ke bahasa Indonesia.
# Everyday Life UI v1.0. Copy this file and the PNG folder into game/everyday_ui/.
# All names are prefixed; importing this file does not replace your game's screens.
default persistent.el_ui_theme = "cream"
default el_ui_theme = persistent.el_ui_theme
default el_ui_large_text = False
default el_ui_animate = False
default persistent.game_font = "fredoka"
default game_font = persistent.game_font

init -20 python:
    if not hasattr(store, "el_ui_asset_root"):
        el_ui_asset_root = "everyday_ui/PNG"

init python:
    EL_UI_COLORS = {
        "cream": ("#10182e", "#426072", "#3d7b7a"),
        "sunset": ("#fdf5cc", "#e9b6b2", "#fac371"),
        "midnight": ("#fdf5cc", "#91aac6", "#fac371"),
    }

    def el_ui_scale():
        # Supported virtual canvases: 640x360, 1280x720 and 1920x1080.
        return {640: 1, 1280: 2, 1920: 3}.get(config.screen_width, 3)

    def el_u(value):
        return int(value * el_ui_scale())

    def el_ui_path(name, theme=None):
        resolution = {1: "native", 2: "720p", 3: "1080p"}[el_ui_scale()]
        return "%s/%s/%s/el_ui_%s.png" % (el_ui_asset_root, resolution, theme or getattr(store, "el_ui_theme", "cream"), name)

    def el_pj_path(name, theme=None):
        resolution = {1: "native", 2: "720p", 3: "1080p"}[el_ui_scale()]
        return "everyday_ui/phone_png/%s/%s/el_pj_%s.png" % (resolution, theme or getattr(store, "el_ui_theme", "cream"), name)

    def el_ui_frame(name, button=False):
        if button:
            borders = (20, 14, 16, 10)
        elif name in ("dialogue_wide", "dialogue_compact", "narration"):
            borders = (12, 8, 28, 16)
        else:
            borders = (12, 8, 16, 8)
        return Frame(el_ui_path(name), *[el_u(n) for n in borders], tile=True)

    def el_ui_color(kind=0):
        return EL_UI_COLORS[getattr(store, "el_ui_theme", "cream")][kind]

    def el_ui_font_size(size=13):
        return el_u(size + (2 if getattr(store, "el_ui_large_text", False) else 0))

    if renpy.loadable("audio/sfx_click.ogg"):
        style.button.activate_sound = "audio/sfx_click.ogg"

    def get_game_font_path(choice=None):
        if choice is None:
            choice = getattr(store, "game_font", None) or getattr(persistent, "game_font", "fredoka")
        if choice == "pixel":
            return "fonts/PixelifySans.ttf"
        return "fonts/Fredoka.ttf"

    def el_ui_font():
        return get_game_font_path()

    def set_game_font(font_choice):
        persistent.game_font = font_choice
        store.game_font = font_choice
        target = get_game_font_path(font_choice)

        style.default.font = target
        style.el_ui_text.font = target
        style.el_ui_button_text.font = target
        if hasattr(style, "say_dialogue"):
            style.say_dialogue.font = target
        if hasattr(style, "say_thought"):
            style.say_thought.font = target
        if hasattr(style, "say_label"):
            style.say_label.font = target
        if hasattr(style, "notify_text"):
            style.notify_text.font = target

        gui.text_font = target
        gui.name_text_font = target
        gui.interface_text_font = target

        renpy.style.rebuild()
        renpy.restart_interaction()

init 50 python:
    def _apply_saved_game_font():
        _cur_f = get_game_font_path()
        style.default.font = _cur_f
        style.el_ui_text.font = _cur_f
        style.el_ui_button_text.font = _cur_f
        if hasattr(style, "say_dialogue"):
            style.say_dialogue.font = _cur_f
        if hasattr(style, "say_thought"):
            style.say_thought.font = _cur_f
        if hasattr(style, "say_label"):
            style.say_label.font = _cur_f
        if hasattr(style, "notify_text"):
            style.notify_text.font = _cur_f
        gui.text_font = _cur_f
        gui.name_text_font = _cur_f
        gui.interface_text_font = _cur_f

    _apply_saved_game_font()
    if hasattr(config, "start_callbacks"):
        config.start_callbacks.append(_apply_saved_game_font)
    if hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks.append(_apply_saved_game_font)

style el_ui_text:
    font "fonts/Fredoka.ttf"
    color el_ui_color()
    size el_ui_font_size()
    outlines []

style el_ui_button:
    background el_ui_frame("button_idle", True)
    hover_background el_ui_frame("button_hover", True)
    insensitive_background el_ui_frame("button_disabled", True)
    selected_background el_ui_frame("button_selected", True)
    selected_hover_background el_ui_frame("button_selected_hover", True)
    selected_insensitive_background el_ui_frame("button_disabled", True)
    xsize el_u(144)
    yminimum el_u(32)
    padding (el_u(20), el_u(8), el_u(14), el_u(9))
    activate_sound "audio/sfx_click.ogg"

style el_ui_button_text is el_ui_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5

screen el_ui_button(label, action, selected=None, sensitive=True, width=144, kind="button", font=None):
    $ _pad_l = el_u(7 if width < 75 else (10 if width < 140 else 20))
    $ _pad_r = el_u(7 if width < 75 else (10 if width < 140 else 14))
    $ _text_sz = 10 if width < 75 else (11 if width < 140 else 12)
    textbutton label:
        style "el_ui_button"
        text_style "el_ui_button_text"
        text_color el_ui_color()
        text_insensitive_color el_ui_color(1)
        text_size el_ui_font_size(_text_sz)
        text_font (font or el_ui_font())
        background el_ui_frame(kind + "_idle", True)
        hover_background el_ui_frame(kind + "_hover", True)
        insensitive_background el_ui_frame(kind + "_disabled", True)
        selected_background el_ui_frame(kind + "_selected", True)
        selected_hover_background el_ui_frame(kind + "_selected_hover", True)
        selected_insensitive_background el_ui_frame(kind + "_disabled", True)
        xsize el_u(width)
        yminimum el_u(32)
        padding (_pad_l, el_u(8), _pad_r, el_u(9))
        action action
        selected selected
        sensitive sensitive
        activate_sound "audio/sfx_click.ogg"

screen el_ui_continue():
    if el_ui_animate:
        add Animation(el_ui_path("continue_0"), .35, el_ui_path("continue_1"), .35,
                      el_ui_path("continue_2"), .35) nearest True
    else:
        add el_ui_path("continue_0") nearest True

screen el_ui_say(who, what):
    # Use Character("Name", screen="el_ui_say") to opt in.
    style_prefix "el_ui"
    window:
        id "window"
        background el_ui_frame("dialogue_wide")
        xpos el_u(16)
        ypos el_u(260)
        xanchor 0.0
        yanchor 0.0
        xsize el_u(608)
        ysize el_u(84)
        padding (el_u(20), el_u(14), el_u(32), el_u(12))
        text what:
            id "what"
            color el_ui_color()
            size el_ui_font_size(13)
            xmaximum el_u(556)
    if who is not None:
        frame:
            id "namebox"
            background el_ui_frame("nameplate")
            xpos el_u(28)
            ypos el_u(240)
            xminimum el_u(144)
            padding (el_u(12), el_u(5), el_u(12), el_u(7))
            text who:
                id "who"
                color el_ui_color()
                size el_ui_font_size(12)
    fixed:
        xpos el_u(586)
        ypos el_u(320)
        xsize el_u(12)
        ysize el_u(12)
        use el_ui_continue

screen el_ui_choices(items):
    # Use with `menu (screen="el_ui_choices"):` in your script.
    modal True
    vbox:
        xalign 0.5
        yalign 0.45
        spacing el_u(8)
        for item in items:
            use el_ui_button(item.caption, item.action, width=360, kind="choice")

screen el_ui_quick_menu():
    hbox:
        xalign 0.5
        ypos el_u(5)
        spacing el_u(3)
        for label, action, w in [("Riwayat", ShowMenu("el_ui_history"), 68),
                                 ("Simpan", ShowMenu("el_ui_save"), 68),
                                 ("Muat", ShowMenu("el_ui_load"), 62),
                                 ("Opsi", ShowMenu("el_ui_preferences"), 62),
                                 ("Menu Utama", MainMenu(), 88)]:
            use el_ui_button(_(label), action, width=w, kind="small_button")

screen el_ui_shell(title):
    modal True
    add Solid("#10182e")
    frame:
        xpos el_u(16)
        ypos el_u(16)
        xsize el_u(608)
        ysize el_u(328)
        background el_ui_frame("menu_panel")
        padding (el_u(20), el_u(16), el_u(20), el_u(16))
        text title style "el_ui_text" color el_ui_color() size el_ui_font_size(20)
    fixed:
        xpos el_u(508)
        ypos el_u(298)
        xsize el_u(92)
        ysize el_u(32)
        use el_ui_button(_("Kembali"), Return(), width=92)
    transclude

screen el_ui_slots(title, saving=True):
    use el_ui_shell(title):
        grid 3 2:
            xpos el_u(32)
            ypos el_u(65)
            spacing el_u(12)
            for i in range(6):
                $ slot = i + 1
                button:
                    id ("el_ui_slot_%d" % slot)
                    background el_ui_frame("save_slot_idle", True)
                    hover_background el_ui_frame("save_slot_hover", True)
                    xsize el_u(176)
                    ysize el_u(106)
                    padding (el_u(12), el_u(8), el_u(12), el_u(8))
                    action (FileSave(slot) if saving else FileLoad(slot))
                    key "save_delete" action FileDelete(slot)
                    vbox:
                        spacing el_u(3)
                        add FileScreenshot(slot) xsize el_u(128) ysize el_u(72) xalign 0.5
                        text FileTime(slot, format=_("%Y-%m-%d %H:%M"), empty=_("Slot kosong")):
                            style "el_ui_text"
                            size el_u(10)
                            color el_ui_color()
        hbox:
            xpos el_u(32)
            ypos el_u(298)
            spacing el_u(4)
            for page in range(1, 6):
                use el_ui_button(str(page), FilePage(page), selected=FileCurrentPage()==str(page), width=48, kind="small_button")

screen el_ui_save():
    tag menu
    use el_ui_slots(_("Simpan"))

screen el_ui_load():
    tag menu
    use el_ui_slots(_("Muat"), saving=False)

screen el_ui_bar(val, width=258, invert=False):
    bar:
        value val
        xsize el_u(width)
        ysize el_u(20)
        left_bar Frame(el_ui_path("slider_track_hover"), el_u(4), el_u(8), el_u(4), el_u(8), tile=True)
        right_bar Frame(el_ui_path("slider_track_idle"), el_u(4), el_u(8), el_u(4), el_u(8), tile=True)
        thumb el_ui_path("slider_thumb_idle")
        hover_thumb el_ui_path("slider_thumb_hover")
        thumb_shadow None
        bar_invert invert

screen el_ui_preferences():
    tag menu
    use el_ui_shell(_("Pengaturan")):
        if not main_menu:
            fixed:
                xpos el_u(36)
                ypos el_u(298)
                xsize el_u(110)
                ysize el_u(32)
                use el_ui_button(_("Menu Utama"), MainMenu(), width=110)
        vbox:
            xpos el_u(36)
            ypos el_u(60)
            spacing el_u(5)

            # --- BAGIAN ATAS: TEMA WARNA & PILIHAN FONT (1 BARIS) ---
            hbox:
                spacing el_u(14)
                yalign 0.5

                # Tema Warna
                hbox:
                    spacing el_u(6)
                    yalign 0.5
                    text _("Tema:") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5) yalign 0.5
                    for key, label, w in [("cream", _("Krem"), 60), ("sunset", _("Senja"), 60), ("midnight", _("Malam"), 66)]:
                        use el_ui_button(label, [SetVariable("el_ui_theme", key), SetField(persistent, "el_ui_theme", key)], selected=el_ui_theme==key, width=w)

                # Pilihan Font
                hbox:
                    spacing el_u(6)
                    yalign 0.5
                    text _("Font:") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5) yalign 0.5
                    use el_ui_button(_("Default (Fredoka)"), Function(set_game_font, "fredoka"), selected=(getattr(persistent, "game_font", "fredoka") == "fredoka"), width=138)
                    use el_ui_button(_("Pixel (Pixelify)"), Function(set_game_font, "pixel"), selected=(getattr(persistent, "game_font", "fredoka") == "pixel"), width=122)

            null height el_u(3)

            # --- DUA KOLOM: TAMPILAN (Kiri) & AUDIO/LEWATI (Kanan) ---
            hbox:
                spacing el_u(20)

                # KOLOM KIRI: Tampilan, Aksesibilitas, Kecepatan
                vbox:
                    spacing el_u(4)
                    xsize el_u(258)

                    text _("Mode Layar") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    hbox:
                        spacing el_u(6)
                        use el_ui_button(_("Jendela"), Preference("display", "window"), width=126)
                        use el_ui_button(_("Layar Penuh"), Preference("display", "fullscreen"), width=126)

                    null height el_u(1)
                    text _("Teks & Efek Visual") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    hbox:
                        spacing el_u(6)
                        use el_ui_button(_("Teks Besar"), ToggleVariable("el_ui_large_text"), selected=el_ui_large_text, width=126)
                        use el_ui_button(_("Animasi Penanda"), ToggleVariable("el_ui_animate"), selected=el_ui_animate, width=126)

                    null height el_u(1)
                    text _("Kecepatan Teks") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    use el_ui_bar(Preference("text speed"), width=258)

                    null height el_u(1)
                    text _("Waktu Maju Otomatis") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    use el_ui_bar(Preference("auto-forward time"), width=258)

                # KOLOM KANAN: Audio & Opsi Lewati
                vbox:
                    spacing el_u(4)
                    xsize el_u(258)

                    text _("Volume Musik") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    use el_ui_bar(Preference("music volume"), width=258)

                    null height el_u(1)
                    text _("Volume Efek Suara") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    use el_ui_bar(Preference("sound volume"), width=258)

                    null height el_u(2)
                    use el_ui_button(_("Bisukan Semua"), Preference("all mute", "toggle"), width=258)

                    null height el_u(1)
                    text _("Lewati Cerita (Skip)") style "el_ui_text" color el_ui_color() size el_ui_font_size(10.5)
                    hbox:
                        spacing el_u(6)
                        use el_ui_button(_("Belum Dibaca"), Preference("skip", "toggle"), width=126)
                        use el_ui_button(_("Setelah Pilihan"), Preference("after choices", "toggle"), width=126)

screen el_ui_history():
    tag menu
    use el_ui_shell(_("Riwayat")):
        viewport:
            xpos el_u(40)
            ypos el_u(66)
            xsize el_u(560)
            ysize el_u(220)
            mousewheel True
            draggable True
            vbox:
                spacing el_u(12)
                for entry in _history_list:
                    vbox:
                        if entry.who:
                            text entry.who style "el_ui_text" color el_ui_color(2)
                        text entry.what style "el_ui_text" color el_ui_color() size el_ui_font_size(12) substitute False

screen el_ui_confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#10182ecc")
    frame:
        background el_ui_frame("modal")
        xalign 0.5
        yalign 0.5
        xsize el_u(380)
        padding (el_u(20), el_u(20), el_u(20), el_u(20))
        vbox:
            spacing el_u(20)
            text message style "el_ui_text" color el_ui_color() xmaximum el_u(340)
            hbox:
                spacing el_u(12)
                use el_ui_button(_("Ya"), yes_action)
                use el_ui_button(_("Tidak"), no_action)
    key "game_menu" action no_action
