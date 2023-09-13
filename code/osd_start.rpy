init python:
    mods["osd_start"] = u"{font=[osd_link_font]}{size=40}Один украденный день{/font}{/size}"

    try:
        modsImages["osd_start"] = ("osd/images/gui/misc/osd_tabular_list_preview.png", False)

    except:
        pass

label osd_start:
    $ osd_onload("lock")
    $ osd_screens_save_act()
    #$ osd_set_null_cursor()
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard = True)
    scene osd_sky_day
    show osd_intro_logo:
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    $ renpy.pause(0.5, hard = True) 
    play sound osd_intro_sample
    $ renpy.pause(8, hard = True)
    scene bg black with Dissolve(2)
    $ osd_loading_screen()
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard = True)
    $ persistent.timeofday = "day"
    $ osd_set_mode_adv()
    $ osd_onload("unlock")
    #$ osd_set_main_menu_cursor()
    $ renpy.transition(Dissolve(2))