init -1 python:
    osd_gui_path = "osd/images/gui/"
    
    osd_link_font = osd_gui_path + "fonts/gothic.ttf"
    osd_header_font = osd_gui_path + "fonts/corbel.ttf"
    osd_main_font = "fonts/calibri.ttf"

    osd_load_text = "Загрузить игру"
    osd_preferences_text = "Настройки"
    osd_extra_text = "Дополнительно"
    osd_delete_text = "Удалить"
    osd_return_text = "Назад"
    osd_yes_text = "Да"
    osd_no_text = "Нет"
    osd_display_preferences_text = "Режим экрана"
    osd_display_preferences_fullscreen_text = "Во весь экран"
    osd_display_preferences_window_text = "В окне"
    osd_font_size_preferences_text = "Размер шрифта"
    osd_font_size_preferences_small_text = "Обычный"
    osd_font_size_preferences_large_text = "Крупный"
    osd_skip_preferences_text = "Пропускать"
    osd_skip_preferences_seen_text = "Виденное ранее"
    osd_skip_preferences_all_text = "Всё"
    osd_loading_text = "Загрузка"

    style.osd_button_none = Style(style.button)
    style.osd_button_none.background = None
    style.osd_button_none.hover_background = None
    style.osd_button_none.selected_background = None
    style.osd_button_none.selected_hover_background = None
    style.osd_button_none.selected_idle_background = None

    style.osd_text_style = Style(style.default)
    style.osd_text_style.color = "#ffdd7d"
    style.osd_text_style.drop_shadow = (2, 2)
    style.osd_text_style.drop_shadow_color = "#000"

    style.osd_titles_style = Style(style.default)
    style.osd_titles_style.font = osd_link_font
    style.osd_titles_style.color = "#fff"
    style.osd_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.osd_titles_style.drop_shadow_color = "#000"
    style.osd_titles_style.italic = False
    style.osd_titles_style.bold = False
    style.osd_titles_style.text_align = 0.5
    style.osd_titles_style.xmaximum = 0.8

    style.osd_log_button = Style(style.button)
    style.osd_log_button.child = None
    style.osd_log_button.focus_mask = None
    style.osd_log_button.background = None

    style.osd_save_load_button_main_menu = Style(style.button)
    style.osd_save_load_button_main_menu.background = osd_gui_path + "save_load/main_menu/thumbnail_idle.png"
    style.osd_save_load_button_main_menu.hover_background = osd_gui_path + "save_load/main_menu/thumbnail_hover.png"
    style.osd_save_load_button_main_menu.selected_background = osd_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.osd_save_load_button_main_menu.selected_hover_background = osd_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.osd_save_load_button_main_menu.selected_idle_background = osd_gui_path + "save_load/main_menu/thumbnail_selected.png"

    style.osd_save_load_button_day = Style(style.button)
    style.osd_save_load_button_day.background = osd_gui_path + "save_load/day/thumbnail_idle.png"
    style.osd_save_load_button_day.hover_background = osd_gui_path + "save_load/day/thumbnail_hover.png"
    style.osd_save_load_button_day.selected_background = osd_gui_path + "save_load/day/thumbnail_selected.png"
    style.osd_save_load_button_day.selected_hover_background = osd_gui_path + "save_load/day/thumbnail_selected.png"
    style.osd_save_load_button_day.selected_idle_background = osd_gui_path + "save_load/day/thumbnail_selected.png"

    style.osd_save_load_button_night = Style(style.button)
    style.osd_save_load_button_night.background = osd_gui_path + "save_load/night/thumbnail_idle.png"
    style.osd_save_load_button_night.hover_background = osd_gui_path + "save_load/night/thumbnail_hover.png"
    style.osd_save_load_button_night.selected_background = osd_gui_path + "save_load/night/thumbnail_selected.png"
    style.osd_save_load_button_night.selected_hover_background = osd_gui_path + "save_load/night/thumbnail_selected.png"
    style.osd_save_load_button_night.selected_idle_background = osd_gui_path + "save_load/night/thumbnail_selected.png"

    style.osd_save_load_button_prologue = Style(style.button)
    style.osd_save_load_button_prologue.background = osd_gui_path + "save_load/prologue/thumbnail_idle.png"
    style.osd_save_load_button_prologue.hover_background = osd_gui_path + "save_load/prologue/thumbnail_hover.png"
    style.osd_save_load_button_prologue.selected_background = osd_gui_path + "save_load/prologue/thumbnail_selected.png"
    style.osd_save_load_button_prologue.selected_hover_background = osd_gui_path + "save_load/prologue/thumbnail_selected.png"
    style.osd_save_load_button_prologue.selected_idle_background = osd_gui_path + "save_load/prologue/thumbnail_selected.png"

    style.osd_save_load_button_sunset = Style(style.button)
    style.osd_save_load_button_sunset.background = osd_gui_path + "save_load/sunset/thumbnail_idle.png"
    style.osd_save_load_button_sunset.hover_background = osd_gui_path + "save_load/sunset/thumbnail_hover.png"
    style.osd_save_load_button_sunset.selected_background = osd_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.osd_save_load_button_sunset.selected_hover_background = osd_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.osd_save_load_button_sunset.selected_idle_background = osd_gui_path + "save_load/sunset/thumbnail_selected.png"

    style.osd_centered_text_style = Style(style.default)
    style.osd_centered_text_style.font = osd_main_font
    style.osd_centered_text_style.size = 50
    style.osd_centered_text_style.color = "#ffdd7d"
    style.osd_centered_text_style.drop_shadow = (2, 2)
    style.osd_centered_text_style.drop_shadow_color = "#000"

    style.osd_base_font = Style(style.default)
    style.osd_base_font.font = osd_main_font
    style.osd_base_font.size = 28
    style.osd_base_font.line_spacing = 2

    style.osd_qte_text = Style(style.osd_base_font)
    style.osd_qte_text.font = osd_header_font
    style.osd_qte_text.size = 60
    style.osd_qte_text.kerning = 3
    style.osd_qte_text.color = "#cfd1d1"
    style.osd_qte_text.hover_color = "#ffffff"
    style.osd_qte_text.selected_color = "#ffffff"
    style.osd_qte_text.selected_idle_color = "#ffffff"
    style.osd_qte_text.selected_hover_color = "#ffffff"
    style.osd_qte_text.insensitive_color = "#ffffff"

    style.osd_settings_link = Style(style.osd_base_font)
    style.osd_settings_link.font = osd_link_font
    style.osd_settings_link.size = 60
    style.osd_settings_link.kerning = 3
    style.osd_settings_link.color = "#909ca3"
    style.osd_settings_link.hover_color = "#ffffff"
    style.osd_settings_link.selected_color = "#909ca3"
    style.osd_settings_link.selected_idle_color = "#909ca3"
    style.osd_settings_link.selected_hover_color = "#ffffff"
    style.osd_settings_link.insensitive_color = "#909ca3"

    style.osd_settings_link_main_menu = Style(style.osd_base_font)
    style.osd_settings_link_main_menu.font = osd_link_font
    style.osd_settings_link_main_menu.size = 60
    style.osd_settings_link_main_menu.kerning = 3
    style.osd_settings_link_main_menu.color = "#ffffff"
    style.osd_settings_link_main_menu.hover_color = "#ffffff"
    style.osd_settings_link_main_menu.selected_color = "#ffffff"
    style.osd_settings_link_main_menu.selected_idle_color = "#ffffff"
    style.osd_settings_link_main_menu.selected_hover_color = "#ffffff"
    style.osd_settings_link_main_menu.insensitive_color = "#ffffff"

    style.osd_settings_link_main_menu_preferences = Style(style.osd_base_font)
    style.osd_settings_link_main_menu_preferences.font = osd_link_font
    style.osd_settings_link_main_menu_preferences.size = 60
    style.osd_settings_link_main_menu_preferences.kerning = 3
    style.osd_settings_link_main_menu_preferences.color = "#d1d1d1"
    style.osd_settings_link_main_menu_preferences.hover_color = "#ffffff"
    style.osd_settings_link_main_menu_preferences.selected_color = "#d1d1d1"
    style.osd_settings_link_main_menu_preferences.selected_idle_color = "#d1d1d1"
    style.osd_settings_link_main_menu_preferences.selected_hover_color = "#ffffff"
    style.osd_settings_link_main_menu_preferences.insensitive_color = "#d1d1d1"

    style.osd_settings_header_main_menu_preferences = Style(style.osd_base_font)
    style.osd_settings_header_main_menu_preferences.font = osd_header_font
    style.osd_settings_header_main_menu_preferences.size = 60
    style.osd_settings_header_main_menu_preferences.color = "#d1d1d1"
    style.osd_settings_header_main_menu_preferences.hover_color = "#ffffff"
    style.osd_settings_header_main_menu_preferences.selected_color = "#ffffff"

    style.osd_settings_header_main_menu_preferences_locked = Style(style.osd_base_font)
    style.osd_settings_header_main_menu_preferences_locked.font = osd_header_font
    style.osd_settings_header_main_menu_preferences_locked.size = 60
    style.osd_settings_header_main_menu_preferences_locked.color = "#C0C0C0"
    style.osd_settings_header_main_menu_preferences_locked.hover_color = "#C0C0C0"
    style.osd_settings_header_main_menu_preferences_locked.selected_color = "#C0C0C0"

    style.osd_settings_header_main_menu_quit = Style(style.osd_base_font)
    style.osd_settings_header_main_menu_quit.font = osd_header_font
    style.osd_settings_header_main_menu_quit.size = 60
    style.osd_settings_header_main_menu_quit.color = "#d1d1d1"
    style.osd_settings_header_main_menu_quit.hover_color = "#ffffff"

    style.osd_settings_header_main_menu_preferences_inverse = Style(style.osd_base_font)
    style.osd_settings_header_main_menu_preferences_inverse.font = osd_header_font
    style.osd_settings_header_main_menu_preferences_inverse.size = 60
    style.osd_settings_header_main_menu_preferences_inverse.color = "#ffffff"
    style.osd_settings_header_main_menu_preferences_inverse.hover_color = "#ffffff"
    style.osd_settings_header_main_menu_preferences_inverse.selected_color = "#ffffff"

    style.osd_main_menu = Style(style.osd_base_font)
    style.osd_main_menu.font = osd_header_font
    style.osd_main_menu.size = 60
    style.osd_main_menu.kerning = 3
    style.osd_main_menu.color = "#ffffff"
    style.osd_main_menu.hover_color = "#ffffff"
    style.osd_main_menu.selected_color = "#ffffff"
    style.osd_main_menu.selected_idle_color = "#ffffff"
    style.osd_main_menu.selected_hover_color = "#ffffff"
    style.osd_main_menu.insensitive_color = "#ffffff"

    style.osd_main_menu_locked = Style(style.osd_base_font)
    style.osd_main_menu_locked.font = osd_header_font
    style.osd_main_menu_locked.size = 60
    style.osd_main_menu_locked.kerning = 3
    style.osd_main_menu_locked.color = "#C0C0C0"
    style.osd_main_menu_locked.hover_color = "#C0C0C0"
    style.osd_main_menu_locked.selected_color = "#C0C0C0"
    style.osd_main_menu_locked.selected_idle_color = "#C0C0C0"
    style.osd_main_menu_locked.selected_hover_color = "#C0C0C0"
    style.osd_main_menu_locked.insensitive_color = "#C0C0C0"

    style.osd_settings_header_day = Style(style.osd_base_font)
    style.osd_settings_header_day.font = osd_header_font
    style.osd_settings_header_day.size = 50
    style.osd_settings_header_day.color = "#4d2e19"
    style.osd_settings_header_day.hover_color = "#a27146"
    
    style.osd_settings_header_night = Style(style.osd_base_font)
    style.osd_settings_header_night.font = osd_header_font
    style.osd_settings_header_night.size = 50
    style.osd_settings_header_night.color = "#161d3d"
    style.osd_settings_header_night.hover_color = "#008193"

    style.osd_settings_header_prologue = Style(style.osd_base_font)
    style.osd_settings_header_prologue.font = osd_header_font
    style.osd_settings_header_prologue.size = 50
    style.osd_settings_header_prologue.color = "#161d3d"
    style.osd_settings_header_prologue.hover_color = "#008193"

    style.osd_settings_header_sunset = Style(style.osd_base_font)
    style.osd_settings_header_sunset.font = osd_header_font
    style.osd_settings_header_sunset.size = 50
    style.osd_settings_header_sunset.color = "#5a3525"
    style.osd_settings_header_sunset.hover_color = "#636840"

    style.osd_settings_text_day = Style(style.osd_settings_header_day)
    style.osd_settings_text_day.size = 36
    style.osd_settings_text_day.selected_color = "#4d2e19"
    style.osd_settings_text_day.hover_color = "#a27146"

    style.osd_settings_text_night = Style(style.osd_settings_header_night)
    style.osd_settings_text_night.size = 36
    style.osd_settings_text_night.selected_color = "#161d3d"
    style.osd_settings_text_night.hover_color = "#008193"

    style.osd_settings_text_prologue = Style(style.osd_settings_header_prologue)
    style.osd_settings_text_prologue.size = 36
    style.osd_settings_text_prologue.selected_color = "#161d3d"
    style.osd_settings_text_prologue.hover_color = "#008193"

    style.osd_settings_text_sunset = Style(style.osd_settings_header_sunset)
    style.osd_settings_text_sunset.size = 36
    style.osd_settings_text_sunset.selected_color = "#5a3525"
    style.osd_settings_text_sunset.hover_color = "#636840"

    style.osd_text_history = Style(style.osd_base_font)
    style.osd_text_history.color = "#ffdd7d"
    style.osd_text_history.drop_shadow = (2, 2)
    style.osd_text_history.drop_shadow_color = "#000"