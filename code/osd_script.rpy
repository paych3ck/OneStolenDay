init python:
    class OsdFunctionCallback(Action):
        def __init__(self,function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def osd_on_load_callback(slot):
        try:
            if persistent.osd_on_save_timeofday[slot]:
                persistent.timeofday = persistent.osd_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.osd_on_save_timeofday[slot][1]
                persistent.font_size = persistent.osd_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.osd_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.osd_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.osd_on_save_timeofday[slot][5]
        
        except:
            pass
    
    def osd_on_save_callback(slot):
        if not persistent.osd_on_save_timeofday:
            persistent.osd_on_save_timeofday = {}

        persistent.osd_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
        
    def osd_screens_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("osd_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def osd_screens_act():
        config.window_title = u"Один украденный день"
        config.name = "One_Stolen_Day"
        config.version = "2.0"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("osd_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненые данные?"

        renpy.free_memory()
        config.overlay_functions.append(osd_set_timeofday_cursor)
        config.main_menu_music = osd_god_is_an_astronaut_all_is_violent_all_is_bright
        config.linear_saves_page_size = None
        persistent._file_page = "osd_FilePage_1"

    def osd_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("osd_old_" + screen_name, None)]
          
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"

        renpy.free_memory()
        config.overlay_functions.remove(osd_set_timeofday_cursor)

        config.mouse_displayable = MouseDisplayable('images/misc/mouse/1.png', 0, 0)
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

        renpy.block_rollback()
        persistent._file_page = 1
        renpy.music.stop("ambience")
        renpy.music.stop("music")
        renpy.music.stop("sound")
        renpy.music.stop("sound_loop")
        renpy.play(music_list["blow_with_the_fires"], channel="music")

    def osd_screens_save_act():
        osd_screens_save()
        osd_screens_act()