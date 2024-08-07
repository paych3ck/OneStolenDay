init python:
    import time
    from os import path
    
    for file_name in renpy.list_files():
        if "osd" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("osd/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("osd/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("osd/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("osd/sounds/"):
                globals()[file_path] = file_name

    osd_std_set_for_preview = {}
    osd_std_set = {}
    store.osd_colors = {}
    store.osd_names = {}
    store.osd_names_list = []
    osd_speaker_color = "speaker_color"

    store.osd_names_list.append("osd_narrator")

    store.osd_names_list.append("osd_th")

    osd_colors["osd_third"] = {"speaker_color": "#004979"}
    osd_names["osd_third"] = "Третий"
    store.osd_names_list.append("osd_third")

    osd_colors["osd_hall"] = {"speaker_color": "#551313"}
    osd_names["osd_hall"] = "Халл"
    store.osd_names_list.append("osd_hall")

    osd_colors["osd_nit"] = {"speaker_color": "#9f9393"}
    osd_names["osd_nit"] = "Ниточник"
    store.osd_names_list.append("osd_nit")

    osd_colors["osd_pi2"] = {"speaker_color": "#ffcc66"}
    osd_names["osd_pi2"] = "Пионер"
    store.osd_names_list.append("osd_pi2")

    osd_colors["osd_nit_voice"] = {"speaker_color": "#9f9393"}
    osd_names["osd_nit_voice"] = "Голос"
    store.osd_names_list.append("osd_nit_voice")

    osd_colors["osd_sl"] = {"speaker_color": "#ffd200"}
    osd_names["osd_sl"] = "Славя"
    store.osd_names_list.append("osd_sl")

    def osd_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global osd_store
        global osd_speaker_color
        osd_gl = globals()
        
        if character_name == "osd_narrator":
            if is_nvl:
                osd_gl["osd_narrator"] = Character(None, kind=nvl, what_style="osd_text_style")
            
            else:
                osd_gl["osd_narrator"] = Character(None, what_style="osd_text_style")
            
            return
        
        if character_name == "osd_th":
            if is_nvl:
                osd_gl["osd_th"] = Character(None, kind=nvl, what_style="osd_text_style", what_prefix="~ ", what_suffix=" ~")
            
            else:
                osd_gl["osd_th"] = Character(None, what_style="osd_text_style", what_prefix="~ ", what_suffix=" ~")
            
            return
        
        if is_nvl:
            osd_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.osd_colors[character_name][osd_speaker_color], kind=nvl, what_style="osd_text_style", who_suffix=":")
            osd_gl["%s_name" % character_name] = store.osd_names[character_name]
        
        else:
            osd_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.osd_colors[character_name][osd_speaker_color], what_style="osd_text_style")
            osd_gl["%s_name" % character_name] = store.osd_names[character_name]

    def osd_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global osd_store
        
        for character_name in store.osd_names_list:
            osd_char_define(character_name)

    def osd_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global osd_narrator
        global osd_th
        osd_narrator_nvl = osd_narrator
        th_nvl = osd_th
        
        global osd_store
        
        for character_name in store.osd_names_list:
            osd_char_define(character_name, True)

    def osd_reload_names():
        global osd_store
        
        for character_name in store.osd_names_list:
            osd_char_define(character_name)

    osd_reload_names()

    def osd_page_counter(n, k):
        l = float(n) / float(k)
        
        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    if persistent.osd_achievements == None:
        persistent.osd_achievements = {}

    persistent.osd_achievements.setdefault('osd_old_story', False)
    persistent.osd_achievements.setdefault('osd_our_world', False)
    persistent.osd_achievements.setdefault('osd_perfect_gear', False)
    persistent.osd_achievements.setdefault('osd_as_before', False)
    persistent.osd_achievements.setdefault('osd_wind_of_changes', False)
    persistent.osd_achievements.setdefault('osd_calm', False)

    def osd_get_achievement(achievement_name):
        renpy.pause(1, hard=True)

        if not persistent.osd_achievements[achievement_name]:
            persistent.osd_achievements[achievement_name] = True
            osd_show_titles()
            renpy.play(sfx_achievement, channel='sound')
            renpy.show(achievement_name + '_hover', at_list=[osd_achievements_pos])
            renpy.with_statement(moveinright)
            renpy.pause(4, hard=True)
            renpy.hide(achievement_name + '_hover')
            renpy.with_statement(dissolve)

    def osd_show_titles():
        renpy.show('osd_titles_frame')
        renpy.with_statement(dissolve)
        renpy.show_screen("osd_titles_overlay", _layer="overlay")
        renpy.show("osd_titles_style osd_titles", at_list=[osd_titles_anim])
        renpy.pause(42, hard=True)
        renpy.hide('osd_titles_frame')
        renpy.with_statement(dissolve)
        renpy.hide_screen('osd_titles_overlay', layer="overlay")

    def osd_show_centered_text(text, transition = None):
        renpy.show("text", what=Text(text, slow=True, style=style.osd_centered_text_style, xalign=0.5, yalign=0.5))
        renpy.with_statement(transition)
        renpy.pause()

    def osd_hide_centered_text(transition=None):
        renpy.hide("text")
        renpy.with_statement(transition)

    def osd_frame_animation(image_name, frames_quantity, retention, loop, transition, start=1, **properties):
        if image_name:
            anim_args = []
            
            for i in xrange(start, start + frames_quantity):
                anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
                
                if loop:
                    anim_args.append(retention)
                    anim_args.append(transition)
            
            return anim.TransitionAnimation(*anim_args, **properties)
        return None

    def osd_heartbeat_animation(image_name, power, zoom2):
        renpy.show(image_name, at_list=[osd_heartbeat_anim(image_name, power, zoom2)], tag=image_name + "_2")
        
    def osd_stop_skipping():
        renpy.config.skipping = None

    def osd_onload(type):
        global osd_lock_quit
        global osd_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            osd_lock_quit = True
            osd_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            osd_lock_quit = False
            osd_lock_quick_menu = False
            config.allow_skipping = True

    def osd_portal_using(after_portal_use_bg):
        before_portal_use_bg = renpy.get_attributes('bg')[0]
        renpy.play(osd_portal_use, channel="sound")
        renpy.scene()
        renpy.show(before_portal_use_bg, at_list=[osd_portal_using_zoom])
        renpy.pause(0.035, hard=True)
        renpy.scene()
        renpy.show("bg white")
        renpy.transition(osd_portal_use_transition)
        renpy.pause(1.2, hard=True)
        renpy.show(after_portal_use_bg)
        renpy.transition(flash)
        renpy.pause(1.3, hard=True)

    def osd_set_main_menu_cursor():
        config.mouse_displayable = MouseDisplayable(osd_gui_path + 'misc/osd_cursor.png', 0, 0)

    osd_set_main_menu_cursor_curried = renpy.curry(osd_set_main_menu_cursor)

    def osd_set_timeofday_cursor():
        global osd_set_timeofday_cursor_var

        if osd_set_timeofday_cursor_var:
            config.mouse_displayable = MouseDisplayable(osd_gui_path + 'dialogue_box/' + persistent.timeofday + '/cursor.png', 0, 0)

    osd_set_timeofday_cursor_curried = renpy.curry(osd_set_timeofday_cursor)

    def osd_set_null_cursor():
        config.mouse_displayable = MouseDisplayable(osd_gui_path + 'misc/osd_none.png', 0, 0)

    osd_set_null_cursor_curried = renpy.curry(osd_set_null_cursor)

    class OsdDust(renpy.Displayable, NoRollback):   
        def __init__(self, particle):
            super(OsdDust, self).__init__()
            self.particle = renpy.displayable(particle)           
            self.parts_cache = []
            
            if self.parts_cache:
                self.__init__()
            
            self.max_parts = 125
            self.oldst = None                    
        
        def osd_dust_create_cache(self):     
            self.parts_cache = [self.osd_dust_get_anim() for i in xrange(self.max_parts)]
        
        def osd_dust_get_anim(self):
            part = self.particle
            pos = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            pos2 = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            dist = [pos2[0] - pos[0], pos2[1] - pos[1]]
            speed = random.uniform(45, 55)
            alpha = random.uniform(.25, 1.0)
            zoom = random.uniform(.25, .75)
            time = math.sqrt(dist[0] ** 2 + dist[1] ** 2) / speed
            elapsed_time = time
            birth_time = time - random.uniform(.5, 3.5)
            death_time = random.uniform(.5, 3.5)
            current_zoom = .0
            current_alpha = .0
            return [part, pos, pos2, dist, speed, alpha, zoom, time, elapsed_time, birth_time, death_time, current_zoom, current_alpha]      
        
        def osd_dust_visit(self):
            return [i[0] for i in self.parts_cache]
        
        def osd_dust_update(self, st):            
            if self.oldst == None:
                self.oldst = st
            
            self.tick = st - self.oldst
            self.oldst = st     
            
            for part in self.parts_cache:   
                if part[8] <= part[7]:
                    part[8] -= self.tick
                
                else:
                    part[8] = 0
                    self.tick = 0     
                
                if part[8] <= .0:
                    upd_val = self.osd_dust_get_anim()

                    for i in xrange(1, 13):
                        part[i] = upd_val[i]

                try:        
                    path_progress = part[8] / part[7]           
                    xdist_now = part[3][0] * path_progress
                    part[1][0] = part[2][0] - xdist_now
                    
                    ydist_now = part[3][1] * path_progress
                    part[1][1] = part[2][1] - ydist_now
                    
                    alpha_time = part[7] - part[9]
                    alpha_el_time = alpha_time
                    alpha_el_time -= self.tick
                    alpha_progress = alpha_el_time / alpha_time
                    alpha_now = part[5] * (1.0 - alpha_progress)
                    zoom_now = part[6] * (1.0 - alpha_progress)
                    
                    if part[8] >= part[9]:
                        if part[12] < part[5] and part[11] < part[6]:
                            part[12] += alpha_now
                            part[11] += zoom_now
                        
                        elif part[12] > part[5] and part[11] > part[6]:
                            part[12] = part[5]
                            part[11] = part[6]
                    
                    if part[8] <= part[10]:
                        if part[12] > .0 and part[11] > .0:
                            part[12] -= alpha_now
                            part[11] -= zoom_now
                        
                        elif part[12] <= .001 and part[11] <= .001:
                            part[12] = .0
                            part[11] = .0
                
                except ZeroDivisionError:
                    pass
        
        def render(self, width, height, st, at):               
            if not self.parts_cache:
                self.osd_dust_create_cache()
            
            renderObj = renpy.Render(config.screen_width, config.screen_height)
            
            for part in self.parts_cache:
                xpos, ypos = part[1]
                alpha, zoom = part[12], part[11]
                t = Transform(child=part[0], zoom=zoom, alpha=alpha)
                cp_render = renpy.render(t, width, height, st, at)
                renderObj.blit(cp_render, (xpos, ypos))
            
            self.osd_dust_update(st)              
            renpy.redraw(self, 0)
            return renderObj

init:
    $ osd_titles = '''{b}Большое спасибо за прохождение этого мода!{/b}\n\nВся наша команда провела не один десяток часов в созвонах, рисовании, написании текста и душевном общении, чтобы в конце концов создать нечто особенное.\n\nИ, если история вам понравилась, то своей цели мы достигли. А если нет, то отпишите нам в комментариях, что именно вам не понравилось и как бы ВЫ сделали этот мод лучше.\n\nЗдесь все работают за чашку чая, которую они покупают себе сами, так что ваши комментарии «Хороший мод, жду нового!» - всё, что у нас есть.\n\nНад модом работали:\nSeeker - автор идеи, сценарист, код.\n\nАндрей Катаев - основой код, дизайн интерфейса.\n\nДаниил Бухичевский - помощь с текстом.\n\nЕгорыч - работа над визуальной составляющей.\n\nДарья Исаева - помощь с визуальной составляющей и вычитка текста.\n\nD_SMILE - фон пустого лагеря.\n\nwhale dream - арт боя Третьего и Ниточника.\n\nОтдельная благодарность:\nАлександр Ларин, Никита Стрельцов и Рина Анисимова - за то, что помогли запустить этот мод давным давно, в самый первый раз \n\nТем, кто поддерживал нас финансово\n\nLaimer_\n\nБезумный шаурма\n\nILNikolaevich\n\nZabib\n\nTom Anderson\n\nBy Vensedor\n\nАлександр Милютин\n\nИгорь Шарапов\n\nЮрий Борисов\n\nЕгор Быстров\n\nИван Киселев\n\nGamzaly Yaraliev\n\nВладимир Иванов\n\nДанила Люлин\n\nВалерий Хакимов\n\n Саня Гуляев\n\n Даниил Тихонов \n\n Евгений Портов \n\nТак или иначе, спасибо за уделённое нам время! Этот мод - лишь начало. Мы не собираемся останавливаться. Следите за анонсами. С уважением, Zero Impact.'''

    $ osd_set_timeofday_cursor_var = False

    image osd_blank_skip = renpy.display.behavior.ImageButton(Null(1920, 1080), Null(1920, 1080), clicked=[Jump('osd_after_intro')])

    image osd_titles_style = ParameterizedText(style="osd_titles_style", size=40, xalign=0.5)

    image osd_loading_text = Text("Загрузка", size=65, font="osd/images/gui/fonts/gothic.ttf")

    $ osd_lamp_anim_frequency = renpy.random.randint(1, 5)

    $ osd_main_menu_var = True
    $ osd_lock_quit_game_main_menu_var = True
    $ osd_lock_quit = False
    $ osd_lock_quick_menu = False

    $ osd_portal_use_transition = ImageDissolve("osd/images/gui/misc/osd_transition2.png", 0.3, 16)

    image osd_main_menu_atl:
        "osd_sky_day" with Dissolve(4)
        pause 6.0
        "osd_sky_sunset" with Dissolve(4)
        pause 6.0
        "osd_sky_night" with Dissolve(4)
        pause 6.0
        repeat

    image osd_dust = OsdDust("osd/images/gui/effects/osd_dust/particle.png")

    image bg osd_stars_anim = osd_frame_animation("osd/images/bg/osd_stars_anim/osd_stars", 2, 1.5, True, Dissolve(1.5))
    image osd_blood_anim = osd_frame_animation("osd/images/gui/effects/osd_blood/osd_blood", 4, 0.5, True, dspr)
    image bg osd_fireplace_anim = osd_frame_animation("osd/images/bg/osd_fireplace_anim/osd_fireplace", 10, 1.8, True, Dissolve(1.2))
    image bg osd_ext_camp_entrance_anim = osd_frame_animation("osd/images/bg/osd_ext_camp_entrance_anim/osd_ext_camp_entrance", 3, 1.0, True, Dissolve(1.0))
    image osd_lamp_anim = osd_frame_animation("osd/images/bg/osd_lamp_anim/osd_semen_room_lamp", 2, osd_lamp_anim_frequency, True, dspr)

    image osd_lamp_anim_blurred_1 = im.Blur("osd/images/bg/osd_lamp_anim/osd_semen_room_lamp_1.png", 1.5)
    image osd_lamp_anim_blurred_2 = im.Blur("osd/images/bg/osd_lamp_anim/osd_semen_room_lamp_2.png", 1.5)

    image osd_lamp_anim_1 = "osd/images/bg/osd_lamp_anim/osd_semen_room_lamp_1.png"
    image osd_lamp_anim_2 = "osd/images/bg/osd_lamp_anim/osd_semen_room_lamp_2.png"

    image bg osd_lamp_anim:
        "osd_lamp_anim_1" with dspr
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_2" with Dissolve(2)
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_1" with dissolve
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_2" with dspr
        pause osd_lamp_anim_frequency
        repeat

    image bg osd_lamp_anim_blurred:
        "osd_lamp_anim_blurred_1" with dspr
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_blurred_2" with Dissolve(2)
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_blurred_1" with dissolve
        pause osd_lamp_anim_frequency
        "osd_lamp_anim_blurred_2" with dspr
        pause osd_lamp_anim_frequency
        repeat

    image bg osd_ext_road_day_full_nit:
        contains:
            "bg osd_ext_road_day_full"
            ypos -1080

        contains:
            "osd_nit smil3_r"
            xalign 0.5

    $ osd_quest1 = 0
    $ osd_quest2 = 0
    $ osd_quest3 = 0
    $ osd_quest4 = 0
    $ osd_quest5 = 0
    $ osd_end_of_secrets = False
    $ osd_expl_death = False

    image silhouette osd_far = im.MatrixColor("osd/images/sprites/pi/far/osd_pi normal far.png", im.matrix.tint(0, 0, 0))
    image osd_dv silhouette = im.MatrixColor('osd/images/sprites/dv/far/osd_dv normal far.png', im.matrix.tint(0, 0, 0))

    transform osd_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.05

    transform osd_nit_center():
        xpos 300
        xanchor 0.5
        yanchor 0.0

    transform osd_titles_anim():
        xalign 0.5
        ypos 1.1
        linear 48 ypos -4.0

    transform osd_moveinbottom():
        linear 0.8 ypos 1300

    transform osd_full_rotate_repeat(l, z, x, y):
        parallel:
            zoom z
            xalign x
            yalign y 
            rotate_pad True
            rotate 0
            linear l rotate 360
            repeat

    transform osd_achievements_pos():
        xpos 1535
        ypos 600

    transform osd_portal_using_zoom():
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.5 zoom 2 xalign 0.5 yalign 0.5

    transform osd_bus_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat

    transform osd_buttons_transition():
        on hover:
            alpha 1.0
            linear 0.4 alpha 0.0
            
        on idle:
            alpha 0.0
            linear 0.4 alpha 1.0

    transform osd_vertigo():
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1 zoom 1.05

        parallel:
            ease 1 xalign 0.48
            ease 1 xalign 0.52
            repeat

        parallel:
            ease 1.5 rotate 1.5 zoom 1.05
            ease 1.5 rotate -1.05 zoom 1.035
            repeat

    transform osd_heartbeat_anim(image_name, power, zoom2):
        contains:
            image_name
            alpha 0.0
            zoom power
            xanchor 0.5 
            yanchor 0.5 
            xpos 0.5 
            ypos 0.5

            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0

            parallel:
                ease 0.75 zoom 1.10

            repeat

        contains:
            image_name
            alpha 0.0
            zoom power
            xanchor 0.5 
            yanchor 0.5 
            xpos 0.5 
            ypos 0.5

            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0

            parallel:
                ease 0.75 zoom zoom2

            repeat