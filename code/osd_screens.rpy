init python:
    osd_g = Gallery()
    osd_page = 0
    osd_g.transition = fade
    osd_g.locked_button = "osd/images/gui/save_load/main_menu/thumbnail_idle.png"
    osd_g.navigation = False

    osd_rows = 4
    osd_cols = 3
    osd_cells  = osd_rows * osd_cols

    osd_gallery_bg_list = [
    "osd_int_dining_hall_damaged", "osd_int_clubs_male_night_light", "osd_fireplace_5",
    "osd_ext_music_club_night", "osd_stars_1", "osd_ext_no_bus_pioneers",
    "osd_ext_bus_pioneers", "osd_int_bus_pioneers", "osd_int_dining_hall_sunset",
    "osd_ext_camp_plain_sight", "osd_ext_camp_empty_field", "osd_ext_sky", 'osd_nit_third_fight'
    ]

    for bg in osd_gallery_bg_list:
        osd_g.button(bg)
        osd_g.image(im.Crop("osd/images/bg/" + bg + ".png", (0, 0, 1920, 1080)))
        osd_g.unlock("bg " + bg)

    osd_music_box = {
        "God Is An Astronaut — All Is Violent, All Is Bright": osd_god_is_an_astronaut_all_is_violent_all_is_bright,
        "OSD — Escape From Reality": osd_escape_from_reality,
        "Nova: Covert Ops — Loading Screen": osd_novaco_loading,
        "Hearthstone — Boomsday": osd_boomsday,
        "Heroes Might and Magick 4 — Combat Theme": osd_heroes_of_might_and_magic_4_combat_theme_III,
        "OSD — Fireplace": osd_fireplace,
        "Painkiller — Forest": osd_painkiller_forest,
        "Skyrim — Tundra": osd_skyrim_tundra,
        "AlexRoma — Academy of Honor Guitar Cover": osd_academy_of_honor_guitar_cover,
        "April Rain — Soulmate": osd_soulmate,
        "Haimin — Mistakes": osd_haimin_mistakes,
        "OSD — Socialism": osd_socialism,
        "April Rain — In Spite Of": osd_having_lived,
        "God Is An Astronaut — When Everything Dies": osd_god_is_an_astronaut_when_everything_dies,
        "OSD — The Ancients": osd_the_ancients
    }

    osd_mr = MusicRoom(fadeout = 1.0)

    for music_name in osd_music_box.values():
        osd_mr.add(music_name)

screen osd_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "osd_main_menu_atl"
    
    if osd_main_menu_var:
        add "osd_logo"
            
        textbutton ["Начать игру"] at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 292
            action [Hide("osd_main_menu", Dissolve(1.5)), SetVariable("osd_lock_quit_game_main_menu_var", False), Start("osd_main_scenario")]
                
        textbutton "[osd_load_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 415
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_load_main_menu")]

        textbutton "[osd_extra_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 538
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_extra")]
            
        textbutton "[osd_preferences_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 662
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_preferences_main_menu")]
                
        textbutton ["Выход"] at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 785
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_quit_main_menu")]
            
        imagebutton:
            auto "osd_logowhite_%s"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")
        
screen osd_quit_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "Вы действительно хотите выйти?":
            font osd_link_font
            size 80
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton "[osd_yes_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [Hide("osd_quit_main_menu"), (Function(osd_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "[osd_no_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [SetVariable("osd_main_menu_var", True), Hide("osd_quit_main_menu"), ShowMenu("osd_main_menu")]
        
screen osd_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "[osd_preferences_text]":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        text "[osd_display_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 200
            
        textbutton "[osd_display_preferences_fullscreen_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton "[osd_display_preferences_window_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 280

            if not _preferences.fullscreen:
                text_style "osd_settings_header_main_menu_preferences_inverse"

            else:
                text_style "osd_settings_header_main_menu_preferences"

            action Preference("display", "window")

        text "[osd_font_size_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 360
                
        textbutton "[osd_font_size_preferences_small_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "[osd_font_size_preferences_large_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "[osd_skip_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "[osd_skip_preferences_seen_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[osd_skip_preferences_all_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "[osd_skip_preferences_seen_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[osd_skip_preferences_all_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")    
            
        text ["Громкость музыки"]:
            font osd_header_font
            size 60
            xpos 430
            ypos 820

        bar:
            value Preference("music volume")
            right_bar "osd_main_menu_bar_null"
            left_bar "osd_main_menu_bar_full"
            thumb "osd_main_menu_thumb"
            xpos 975
            ypos 813
            xmaximum 400
            ymaximum 85

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [SetVariable("osd_main_menu_var", True), Hide("osd_preferences_main_menu"), ShowMenu("osd_main_menu")]
        
screen osd_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "[osd_loading_text]":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [SetVariable("osd_main_menu_var", True), Hide("osd_load_main_menu"), ShowMenu("osd_main_menu")]
                    
        textbutton "[osd_load_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            ypos 970
            action (OsdFunctionCallback(osd_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))
                 
        textbutton "[osd_delete_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.9
            ypos 970
            action FileDelete(selected_slot, confirm = False)
            
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "osd_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + "Пусто") + "\n" + FileSaveName(i)):
                                style "osd_text_save_load_main_menu"
                                xpos 15
                                ypos 15
        
screen osd_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var: 
        add "osd_main_menu_frame"
        
        text "[osd_extra_text]":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton ["Музыка"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.3
            action [Hide("osd_extra"), ShowMenu("osd_music_room")]

        textbutton ["Галерея"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.5
            action [Hide("osd_extra"), ShowMenu("osd_background_gallery")]

        textbutton ["Достижения"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.7
            action [Hide("osd_extra"), ShowMenu("osd_achievements")]

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [SetVariable("osd_main_menu_var", True), Hide("osd_extra"), ShowMenu("osd_main_menu")]

screen osd_achievements():
    modal True

    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var: 
        add "osd_main_menu_frame"
        
        text "Достижения":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        add osd_gui_path + "achievements/frame.png" xpos 1105 ypos 160

        if persistent.osd_achievements["osd_old_story"]:
            add "osd_old_story" xalign 0.75 yalign 0.2

        else:
            add "osd_locked" xalign 0.75 yalign 0.2

        if persistent.osd_achievements["osd_our_world"]:
            add "osd_our_world" xalign 0.75 yalign 0.35

        else:
            add "osd_locked" xalign 0.75 yalign 0.35

        if persistent.osd_achievements["osd_perfect_gear"]:
            add "osd_perfect_gear" xalign 0.75 yalign 0.5

        else:
            add "osd_locked" xalign 0.75 yalign 0.5

        if persistent.osd_achievements["osd_as_before"]:
            add "osd_as_before" xalign 0.75 yalign 0.65

        else:
            add "osd_locked" xalign 0.75 yalign 0.65
                
        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [Hide('osd_achievements'), ShowMenu('osd_extra')]

screen osd_background_gallery():
    modal True

    if not osd_main_menu_var:
        add "osd_main_menu_frame"

        $ osd_gallery_table = osd_gallery_bg_list

        $ osd_len_table = len(osd_gallery_bg_list)

        text "Галерея":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [Hide('osd_background_gallery'), ShowMenu('osd_extra')]

        grid osd_rows osd_cols xpos 0.09 ypos 0.18:
            $ osd_bg_displayed = 0
            $ osd_next_page = osd_page + 1

            if osd_next_page > int(osd_len_table / osd_cells):
                $ osd_next_page = 0

            for n in range(osd_len_table):
                if n < (osd_page + 1) * osd_cells and n >= osd_page * osd_cells:
                    $ _osd_t = im.Crop("osd/images/bg/" + osd_gallery_table[n] + ".png", (0, 0, 1920, 1080))
                            
                    $ _osd_img_scaled = im.Scale(_osd_t, 320, 180)

                    $ osd_img = im.Composite((336, 196), (8, 8), im.Alpha(_osd_img_scaled, 0.9), (0, 0), im.Image(osd_gui_path + "/save_load/main_menu/thumbnail_idle.png"))
                    $ osd_imgh = im.Composite((336, 196), (8, 8), _osd_img_scaled, (0, 0), im.Image(osd_gui_path + "/save_load/main_menu/thumbnail_hover.png"))

                    add osd_g.make_button(osd_gallery_table[n], get_image("gui/gallery/blank.png"), None, osd_imgh, osd_img , style = "blank_button", bottom_margin = 50, right_margin = 50)

                    $ osd_bg_displayed += 1

                    if n + 1 == osd_len_table:
                        $ osd_next_page = 0

            for j in range(0, osd_cells - osd_bg_displayed):
                null

        if osd_page != 0:
            imagebutton:
                auto 'osd_gallery_previous_%s'
                yalign 0.5 
                xalign 0.04 
                action [SetVariable("osd_page", osd_page - 1), ShowMenu("osd_background_gallery")]

        if osd_page != int(osd_page_counter(osd_len_table, osd_cells)) - 1:
            imagebutton: 
                auto 'osd_gallery_next_%s'
                yalign 0.5 
                xalign 0.96 
                action [SetVariable("osd_page", osd_next_page), ShowMenu("osd_background_gallery")]

screen osd_music_room():
    modal True

    if not osd_main_menu_var: 
        frame background "osd_main_menu_frame":
            side "c r":
                area (0.15, 0.22, 0.8, 0.73)

                viewport:
                    id "osd_music_box"
                    draggable True
                    mousewheel True
                    scrollbars None
                    
                    grid 1 len(osd_music_box):
                        for name, track in sorted(osd_music_box.iteritems()):
                            textbutton name:
                                style "osd_button_none"
                                text_style "music_link"
                                # style "osd_button_none"
                                # text_style "osd_settings_header_main_menu_preferences"
                                xalign 0.5
                                action osd_mr.Play(track)

                vbar:
                    value YScrollValue("osd_music_box")
                    bottom_bar 'osd_main_menu_vbar_null'
                    top_bar 'osd_main_menu_vbar_full'
                    thumb "images/misc/none.png"
                    xmaximum 52

        text "Музыка":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [Hide('osd_music_room'), ShowMenu('osd_extra')]

        on "replaced" action Play("music", osd_god_is_an_astronaut_all_is_violent_all_is_bright)
        
screen osd_preferences():
    tag menu
    modal True
    
    $ osd_bar_null = Frame((osd_gui_path + "preferences/" + persistent.timeofday + "/osd_bar_null.png"), 36, 36)
    $ osd_bar_full = Frame((osd_gui_path + "preferences/" + persistent.timeofday + "/osd_bar_full.png"), 36, 36)

    window background osd_gui_path + "preferences/" + persistent.timeofday + "/preferences_bg.jpg":
        text "[osd_preferences_text]": 
            style "osd_settings_link"
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "[osd_return_text]": 
            style "osd_log_button" 
            text_style "osd_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 16 xfill True spacing 15

                text "[osd_display_preferences_text]":
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_display_preferences_fullscreen_text]": 
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_display_preferences_window_text]": 
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action Preference("display", "window")

                text "[osd_skip_preferences_text]":
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_skip_preferences_all_text]": 
                            style "osd_log_button" 
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_skip_preferences_seen_text]": 
                            style "osd_log_button" 
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action Preference("skip", "seen")

                text ["Громкость"]:
                    style "osd_settings_header_" + persistent.timeofday + ""                    
                    xalign 0.5

                grid 2 1 xfill True:
                    textbutton ["Музыка"]: 
                        style "osd_log_button"
                        text_style "osd_settings_text_" + persistent.timeofday + ""
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("music volume")
                        left_bar osd_bar_full 
                        right_bar osd_bar_null 
                        thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        hover_thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Звуки"]: 
                        style "osd_log_button"
                        text_style "osd_settings_text_" + persistent.timeofday + ""
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("sound volume") 
                        left_bar osd_bar_full 
                        right_bar osd_bar_null 
                        thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        hover_thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Эмбиент"]: 
                        style "osd_log_button"
                        text_style "osd_settings_text_" + persistent.timeofday + ""
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("voice volume") 
                        left_bar osd_bar_full 
                        right_bar osd_bar_null 
                        thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        hover_thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                text ["Скорость текста"]:
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                bar: 
                    value Preference("text speed") 
                    left_bar osd_bar_full 
                    right_bar osd_bar_null 
                    thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                    hover_thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text ["Автопереход"]:
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Включить"]: 
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Выключить"]: 
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text ["Время автоперехода"]:
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                bar: 
                    value Preference("auto-forward time") 
                    left_bar osd_bar_full 
                    right_bar osd_bar_null 
                    thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                    hover_thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text "[osd_font_size_preferences_text]":
                    style "osd_settings_header_" + persistent.timeofday + ""
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_font_size_preferences_small_text]":
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add osd_gui_path + "preferences/" + persistent.timeofday + "/osd_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "[osd_font_size_preferences_large_text]": 
                            style "osd_log_button"
                            text_style "osd_settings_text_" + persistent.timeofday + ""
                            action SetField(persistent, "font_size", "large")

            bar: 
                value XScrollValue("preferences") 
                left_bar "images/misc/none.png" 
                right_bar "images/misc/none.png" 
                thumb "images/misc/none.png" 
                hover_thumb "images/misc/none.png"

            vbar: 
                value YScrollValue("preferences") 
                bottom_bar "images/misc/none.png" 
                top_bar "images/misc/none.png" 
                thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_vthumb.png" 
                thumb_offset -12

screen osd_save():
    tag menu
    modal True
    
    window background osd_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text ["Сохранение"]: 
            style "osd_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "[osd_return_text]": 
            style "osd_log_button" 
            text_style "osd_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Сохранить"]: 
            style "osd_log_button" 
            text_style "osd_settings_link"
            yalign 0.92 
            xalign 0.5 
            action (OsdFunctionCallback(osd_on_save_callback,selected_slot), FileSave(selected_slot))

        textbutton "[osd_delete_text]": 
            style "osd_log_button" 
            text_style "osd_settings_link" 
            yalign 0.92 
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "osd_save_load_button_" + persistent.timeofday + ""
                        has fixed
                        text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + translation_new["Empty_slot"]) + "\n" + FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15
    
screen osd_load():
    tag menu
    modal True
    
    window background osd_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text "[osd_loading_text]": 
            style "osd_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "[osd_return_text]": 
            style "osd_log_button" 
            text_style "osd_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Загрузить"]: 
            style "osd_log_button" 
            text_style "osd_settings_link" 
            yalign 0.92 
            xalign 0.5 
            action (OsdFunctionCallback(osd_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))
        
        textbutton "[osd_delete_text]": 
            style "osd_log_button" 
            text_style "osd_settings_link"
            yalign 0.92
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "osd_save_load_button_" + persistent.timeofday + ""
                        has fixed
                        text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15                  
                                
screen osd_say(what, who):    
    window background None id "window":
        if persistent.font_size == "large":
            add osd_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday + '/hide_%s.png' 
                xpos 1508 
                ypos 883 
                action HideInterface()

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday + "/save_%s.png"
                xpos 1567
                ypos 883
                action ShowMenu('osd_save')

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday + "/menu_%s.png"
                xpos 1625 
                ypos 883 
                action ShowMenu('osd_game_menu_selector')

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday + "/load_%s.png"
                xpos 1682 
                ypos 883 
                action ShowMenu('osd_load')

            imagebutton:
                auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 924 
                action ShowMenu("osd_text_history")

            if not config.skipping:
                imagebutton:
                    auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            else:
                imagebutton: 
                    auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 914 
                xmaximum 1541 
                size 30
                line_spacing 1

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 877 
                    size 35 
                    line_spacing 1

        elif persistent.font_size == "small":
            add osd_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos 174 ypos 916

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday + "/hide_%s.png"
                xpos 1508
                ypos 933
                action HideInterface()

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday+"/save_%s.png"
                xpos 1567
                ypos 933
                action ShowMenu('osd_save')

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday+"/menu_%s.png"
                xpos 1625
                ypos 933
                action ShowMenu('osd_game_menu_selector')

            imagebutton:
                auto osd_gui_path + 'dialogue_box/' + persistent.timeofday+"/load_%s.png"
                xpos 1682
                ypos 933
                action ShowMenu('osd_load')

            imagebutton:
                auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 949 
                action ShowMenu("osd_text_history")

            if not config.skipping:
                imagebutton:
                    auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            else:
                imagebutton:
                    auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 964 
                xmaximum 1541 
                size 25
                line_spacing 2

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 931 
                    size 28 
                    line_spacing 2

screen osd_nvl(items, dialogue):
    window background Frame((osd_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10

                if persistent.font_size == "large":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 35

                    text what:
                        id what_id 
                        size 35

                elif persistent.font_size == "small":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 28

                    text what:
                        id what_id 
                        size 28

        if items:
            vbox:
                id "menu"

                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"

    imagebutton:
        auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
        xpos 38 
        ypos 924
        action ShowMenu("osd_text_history")

    if not config.skipping:
        imagebutton:
            auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            auto osd_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

screen osd_game_menu_selector():
    tag menu
    modal True

    if osd_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

        add osd_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5

        imagemap:
            auto osd_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_%s.png" xalign 0.5 yalign 0.5

            hotspot (0, 83, 660, 65) focus_mask None clicked [yn_set_main_menu_cursor_curried(), MainMenu(confirm=False)]

            hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu("osd_save")

            hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu("osd_load")

            hotspot (0, 278, 660, 65) focus_mask None clicked ShowMenu("osd_preferences")

            hotspot (0, 343, 660, 65) focus_mask None action [(Function(osd_screens_diact)), ShowMenu("main_menu")]

screen osd_quit():
    tag menu
    modal True

    if osd_lock_quit:
        timer 0.01 action Return()

    elif osd_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm=False)

    else:
        add osd_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
            
        text ["Вы действительно \nхотите выйти?"]:
            font osd_link_font
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton "[osd_yes_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [(Function(osd_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "[osd_no_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [Hide("osd_quit"), Return()]

screen osd_yesno_prompt(yes_action, message, no_action):
    modal True

    add osd_gui_path + "yes_no/" + persistent.timeofday + "/yes_no.png"

    text _(message):
        font osd_header_font
        text_align 0.5 
        yalign 0.46 
        xalign 0.5

        if persistent.timeofday == "day":
            color "#64483c"

        elif persistent.timeofday == "night":
            color "#161d3d"

        elif persistent.timeofday == "prologue":
            color "#008193"

        elif persistent.timeofday == "sunset":
            color "#5a3525"

        size 30

    textbutton "[osd_yes_text]": 
        text_size 60 
        style "osd_log_button" 
        text_style "osd_settings_link" 
        yalign 0.65 
        xalign 0.3 
        action yes_action

    textbutton "[osd_no_text]": 
        text_size 60 
        style "osd_log_button" 
        text_style "osd_settings_link" 
        yalign 0.65 
        xalign 0.7 
        action no_action

screen osd_text_history():
    tag menu

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "small":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(osd_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "osd_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what:
                    text_size history_text_size
                    style "osd_log_button" 
                    text_style "osd_text_history" 
                    xpos 100                    
                    xmaximum xmax

                    if persistent.timeofday == "day":
                        text_hover_color "#40e138"

                    elif persistent.timeofday == "night":
                        text_hover_color "#008193"

                    elif persistent.timeofday == "prologue":
                        text_hover_color "#00c6ff"

                    elif persistent.timeofday == "sunset":
                        text_hover_color "#636840"
                    
                    action RollbackToIdentifier(h.rollback_identifier) 
        
        vbar value YScrollValue("osd_text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb osd_gui_path + "preferences/" + persistent.timeofday + "/osd_vthumb.png" xoffset 1700  

screen osd_choice(items):
    modal True
    
    python:
        osd_choice_colors = {
        "day": "#466123",
        "night": "#145644",
        "sunset": "#69652f",
        "prologue": "#496463"
                            }

        osd_choice_colors_hover = {                        
        "day": "#9dcd55",
        "night": "#3ccfa2",
        "sunset": "#dcd168",
        "prologue": "#98d8da"
                            }

        osd_choice_colors_selected = {                        
        "day": "#2a3b15",
        "night": "#0b3027",
        "sunset": "#42401e",
        "prologue": "#2d3d3d"
                            }

    window background Frame(("osd/images/gui/choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color osd_choice_colors_selected[persistent.timeofday] hover_color osd_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5
                            
                        else:
                            text caption font header_font size 37 hover_size 37 color osd_choice_colors[persistent.timeofday] hover_color osd_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color osd_choice_colors[persistent.timeofday] hover_color osd_choice_colors_hover[persistent.timeofday] xalign 0.5

            else:
                if persistent.licensed:
                    text caption font header_font size 60 color osd_choice_colors[persistent.timeofday] text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color osd_choice_colors[persistent.timeofday] xalign 0.5 text_align 0.5 xcenter 0.5

screen osd_help():
    tag menu
    modal True
    
    add osd_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
    
    text ["Информация"]:
        font osd_link_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
            
    textbutton ["Группа VK"]:
        style "osd_log_button" 
        text_style "osd_settings_header_main_menu_quit"
        xalign 0.5
        ypos 350
        action OpenURL("https://vk.com/public176281709")
            
    textbutton ["Бессонница"]:
        style "osd_log_button" 
        text_style "osd_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1636163628")    
            
    textbutton ["Петля времени"]:
        style "osd_log_button" 
        text_style "osd_settings_header_main_menu_quit"
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")        
            
    imagebutton:
        idle osd_gui_path + "logowhite_hover.png"
        hover osd_gui_path + "logowhite_hover.png"
        xpos 1520
        ypos 890
        action NullAction()

    textbutton "[osd_return_text]": 
        style "osd_log_button" 
        text_style "osd_settings_link" 
        xalign 0.015 
        yalign 0.92 
        action Return()

screen osd_fight_with_nit(osd_x1_time):  
    tag game
    modal True

    use osd_bar1(osd_x1_time)
   
    textbutton ["Напролом"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 400
        action [Hide("osd_fight_with_nit"), Jump("osd_fight_ahead1")]

    textbutton ["Использовать Смещение"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 600
        action [Hide ("osd_fight_with_nit"), Jump("osd_fight_parallax1")]

screen osd_fight_ahead2(osd_x2_time):  
    tag game
    modal True

    use osd_bar2(osd_x2_time)
   
    textbutton ["По дуге"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 400
        action [Hide("osd_fight_ahead2"), Jump("osd_fight_arc")]

    textbutton ["По прямой"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 600
        action [Hide("osd_fight_ahead2"), Jump("osd_fight_straight")]

screen osd_fight_parallax2(osd_x2_time):  
    tag game
    modal True

    use osd_bar2(osd_x2_time)
   
    textbutton ["Переместиться самому"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 400
        action [Hide("osd_fight_parallax2"), Jump("osd_fight_self_parallax")]

    textbutton ["Бросить снаряд через разлом"]:
        style "osd_log_button" 
        text_style "osd_qte_text" 
        xalign 0.5
        ypos 600
        action [Hide ("osd_fight_parallax2"), Jump("osd_fight_projectile_parallax")]

screen osd_bar1(osd_x1_time):
    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    key "K_SCROLLOCK":
        action NullAction()
        
    key "mouseup_3":
        action NullAction()
        
    key "mouseup_4":
        action NullAction()
        
    key "K_PAGEUP":
        action NullAction()
    
    key "repeat_K_PAGEUP":
        action NullAction()
    
    key "K_AC_BACK":
        action NullAction()

    key "mouseup_2":
        action NullAction()

    key "h":
        action NullAction()

    key "K_RETURN":
        action NullAction()

    key "K_SPACE":
        action NullAction()

    key "K_KP_ENTER":
        action NullAction()
        
    key "K_SELECT":
        action NullAction()
    
    bar:
        keyboard_focus False
        left_bar osd_gui_path + "misc/osd_fight_bar_null.png"
        right_bar osd_gui_path + "misc/osd_fight_bar_full.png"
        thumb osd_gui_path + "misc/osd_none.png"
        xpos 62
        ypos 186
        ysize 34
        xmaximum 1796

        value AnimatedValue(old_value = 1.0, value = 0.0, range = 1.0, delay = osd_x1_time)

    timer osd_x1_time action [Hide ("osd_bar1"), Jump("osd_death1")]

screen osd_bar2(osd_x2_time):
    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    key "K_SCROLLOCK":
        action NullAction()
        
    key "mouseup_3":
        action NullAction()
        
    key "mouseup_4":
        action NullAction()
        
    key "K_PAGEUP":
        action NullAction()
    
    key "repeat_K_PAGEUP":
        action NullAction()
    
    key "K_AC_BACK":
        action NullAction()

    key "mouseup_2":
        action NullAction()

    key "h":
        action NullAction()

    key "K_RETURN":
        action NullAction()

    key "K_SPACE":
        action NullAction()

    key "K_KP_ENTER":
        action NullAction()
        
    key "K_SELECT":
        action NullAction()
    
    bar:
        keyboard_focus False
        left_bar osd_gui_path + "misc/osd_fight_bar_null.png"
        right_bar osd_gui_path + "misc/osd_fight_bar_full.png"
        thumb osd_gui_path + "misc/osd_none.png"
        xpos 62
        ypos 186
        ysize 34
        xmaximum 1796

        value AnimatedValue(old_value = 1.0, value = 0.0, range = 1.0, delay = osd_x2_time)

    timer osd_x2_time action [Hide("osd_bar2"), Jump("osd_death2")]

screen osd_titles_overlay():
    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    key "K_SCROLLOCK":
        action NullAction()
        
    key "mouseup_3":
        action NullAction()
        
    key "mouseup_4":
        action NullAction()
        
    key "K_PAGEUP":
        action NullAction()
    
    key "repeat_K_PAGEUP":
        action NullAction()
    
    key "K_AC_BACK":
        action NullAction()

    key "mouseup_2":
        action NullAction()

    key "h":
        action NullAction()

    key "mouseup_1":
        action NullAction()

    key "K_RETURN":
        action NullAction()

    key "K_SPACE":
        action NullAction()

    key "K_KP_ENTER":
        action NullAction()

    key "K_SELECT":
        action NullAction()

    key "K_LCTRL":
        action NullAction()

    key "K_RCTRL":
        action NullAction() 
        
    key "joy_holdskip":
        action NullAction()

    key "K_TAB":
        action NullAction() 
        
    key "joy_toggleskip":
        action NullAction()

    key ">":
        action NullAction()