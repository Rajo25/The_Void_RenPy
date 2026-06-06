################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 0.15
    ypos -89
    
    xminimum 300   # Minimalna szerokość (dla krótkich imion)
    xsize None     # Zdejmujemy sztywny kaganiec szerokości! (Pudełko może rosnąć)
    ysize 100      # Wysokość zostaje sztywna
    
    # Używamy Frame. Cyferki (np. 15, 15) to marginesy lewy/prawy Twojego obrazka, 
    # których silnik ma NIE rozciągać (żeby nie zepsuć krawędzi ramki).
    background Frame("gui/namebox.png", 0, 0) 
    
    padding (30, 0) # Margines dla tekstu, żeby nie dotykał ramki

    #padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.2

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen history_menu(title, scroll=None, yinitial=0.0, spacing=0):
    
    # 1. TWOJE TŁO
    add "gui/main_menu.png"

    # 2. PRZYCISK RETURN W NOWYM MIEJSCU
    button:
        action Return()
        xalign 0.03
        yalign 0.96
        xysize (250, 70)
                    
        idle_background Transform("gui/Pause_Menu/Button.png", size=(250, 70))
        hover_background Transform("gui/Pause_Menu/Button.png", size=(250, 70), alpha=0.6)
                    
        text "Wróć":
            align (0.48, 0.5)
            size 40
            idle_color "#ffffff"
            hover_color "#ffffff60"

    frame:
        style "game_menu_content_frame"  
        
        viewport:
            yinitial yinitial
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            
            vbox:
                spacing spacing
                transclude


screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and not renpy.get_screen("choice"):

        hbox:

            xalign 0.93
            yalign 0.985
            spacing 10
            textbutton _("Cofnij"):
                action Rollback()
                xysize (100,50) 
                text_align (0.5, 0.5) 
                text_size 22
                text_idle_color "#ffffffff"
                text_hover_color "#ffffff60"
                
                
                idle_background Transform("gui/Pause_Menu/Button.png", size=(100,50))
                hover_background Transform("gui/Pause_Menu/Button.png", size=(100,50), alpha=0.7)
            # style_prefix "quick"
            #style "quick_menu"

            textbutton _("Historia"):
                action ShowMenu('history')
                xysize (100,50) 
                text_align (0.5, 0.5) 
                text_size 22
                text_idle_color "#ffffffff"
                text_hover_color "#ffffff60"
                
               
                idle_background Transform("gui/Pause_Menu/Button.png", size=(100,50))
                hover_background Transform("gui/Pause_Menu/Button.png", size=(100,50), alpha=0.7)
           
            textbutton _("Pomiń"):
                action Skip() alternate Skip(fast=True, confirm=True)
                xysize (100,50) 
                text_align (0.5, 0.5) 
                text_size 22
                text_idle_color "#ffffffff"
                text_hover_color "#ffffff60"
                
              
                idle_background Transform("gui/Pause_Menu/Button.png", size=(100,50))
                hover_background Transform("gui/Pause_Menu/Button.png", size=(100,50), alpha=0.7)

            textbutton _("Auto"):
                action Preference("auto-forward", "toggle")
                xysize (100,50) 
                text_align (0.5, 0.5) 
                text_size 22
                text_idle_color "#ffffffff"
                text_hover_color "#ffffff60"
                
              
                idle_background Transform("gui/Pause_Menu/Button.png", size=(100,50))
                hover_background Transform("gui/Pause_Menu/Button.png", size=(100,50), alpha=0.7)
        
            

            # textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("Auto") action Preference("auto-forward", "toggle")
            # textbutton _("Save") action ShowMenu('save')
            # textbutton _("Q.Save") action QuickSave()
            # textbutton _("Q.Load") action QuickLoad()
            # textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xalign 0.5
        yalign 0.7

        spacing gui.navigation_spacing

        if main_menu:
            imagebutton:
                idle "gui/New_game.png"
                hover Transform("gui/New_game.png", matrixcolor=TintMatrix("#8ac7ff9d"))
                action Start()
                at Transform(zoom=0.1)
                
                
            #textbutton _("Start") action Start()
            imagebutton:
                idle "gui/Continue.png"
                hover Transform("gui/Continue.png", matrixcolor=TintMatrix("#8ac7ff9d"))
                action ShowMenu("load")
                at Transform(zoom=0.2)
            imagebutton:
                idle "gui/Options.png"
                hover Transform("gui/Options.png", matrixcolor=TintMatrix("#8ac7ff9d"))
                action ShowMenu("preferences")
                at Transform(zoom=0.2)

        #     textbutton _("History") action ShowMenu("history")

        #     textbutton _("Save") action ShowMenu("save")

        # textbutton _("Load") action ShowMenu("load")

        # textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        imagebutton: 
            idle "gui/Info.png"
            hover Transform("gui/Info.png", matrixcolor=TintMatrix("#8ac7ff9d"))
            action ShowMenu("about")
            at Transform(zoom=0.2)

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton:
                idle "gui/Quit.png"
                hover Transform("gui/Quit.png", matrixcolor=TintMatrix("#8ac7ff9d"))
                action Quit(confirm=not main_menu)
                at Transform(zoom=0.1)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    add "gui/title.png":
        xalign 0.5  
        yalign 0.05
        zoom 0.15

    ## This empty frame darkens the main menu.
    #frame:
    #    style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:
#
#        vbox:
#            style "main_menu_vbox"
#
#            text "[config.name!t]":
#               style "main_menu_title"
#
#            text "[config.version]":
#                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yscrollbar=True):
    tag menu

    add "gui/game_menu.png":
        xalign 0.5
        yalign 0.5

    if title == "Save":
        add "gui/save.png" xalign 0.5 yalign 0.05
    elif title == "Load":
        add "gui/load.png" xalign 0.5 yalign 0.05
    elif title == "Preferences":
        add "gui/opcje.png" xalign 0.5 yalign 0.05
    elif title == "About":
        add "gui/credits.png" xalign 0.5 yalign 0.05
    button:
        action Return()
        xalign 0.2
        yalign 0.87
        xysize (250, 70)
                    
        idle_background Transform("gui/Pause_Menu/Button.png", size=(250, 70))
        hover_background Transform("gui/Pause_Menu/Button.png", size=(250, 70), alpha=0.6)
                    
        text "Wróć":
            align (0.48, 0.5)
            size 40
            idle_color "#ffffff"
            hover_color "#ffffff60"

    frame:
        xalign 0.5
        yalign 0.53
        background None
        padding (0, 0)
        margin (0, 0)

        if scroll:
            viewport:
                scrollbars scroll
                vscrollbar_unscrollable "hide"
                mousewheel True
                draggable True
                has vbox
                transclude
        else:
            transclude

# screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

#     style_prefix "game_menu"

#     if main_menu:
#         add gui.main_menu_background
#     else:
#         add gui.game_menu_background
#         xalign 0.5
#         yalign 0.5

#     frame:
#         style "game_menu_outer_frame"
#         background None

#         hbox:

#             ## Reserve space for the navigation section.
#             frame:
#                 style "game_menu_navigation_frame"

#             frame:
#                 style "game_menu_content_frame"

#                 if scroll == "viewport":

#                     viewport:
#                         yinitial yinitial
#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         vbox:
#                             spacing spacing

#                             transclude

#                 elif scroll == "vpgrid":

#                     vpgrid:
#                         cols 1
#                         yinitial yinitial

#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         spacing spacing

#                         transclude

#                 else:

#                     transclude

#     #use navigation

#     button:
#         action Return()
#         xalign 0.1
#         yalign 0.95 
#         xysize (250, 70)
                    
#         idle_background Transform("gui/Pause_Menu/Button.png", size=(250, 70))
#         hover_background Transform("gui/Pause_Menu/Button.png", size=(250, 70), alpha=0.6)
                    
#         text "Return":
#             align (0.48, 0.5)
#             size 40
#             idle_color "#FEEDC4"
#             hover_color "#ffffff67"

    #label title
    # if title == "Save":
    #             add "gui/save.png":
    #                 xalign 0.5
    #                 yalign 0.05 # Lekki margines od góry
    # elif title == "Load":
    #             add "gui/load.png":
    #                 xalign 0.5
    #                 yalign 0.05
    # elif title == "Preferences":
    #             add "gui/load.png":
    #                 xalign 0.5
    #                 yalign 0.05

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu

    use game_menu("About"):
        
        # Główny kontener
        vbox:
            xalign 0.5
            yalign 0.1  
            spacing 20
            xmaximum 1000  

    
            text "Barbara Skowron\nMichał Chojak\nIzabela Olszewska\nOskar Mroziewicz" size 50 xalign 0.5 text_align 0.5 color "#ffffff" #font "gui/twoj_font.ttf"
            null height 40

            
            #text "[config.name!t]" size 45 xalign 0.5 text_align 0.5 color "#FEEDC4" #font "gui/twoj_font.ttf"
            text _("Wersja [config.version!t]") size 30 xalign 0.5 text_align 0.5 color "#ffffff" #font "gui/twoj_font.ttf"
            
            if gui.about:
                text "[gui.about!t]" size 30 xalign 0.5 text_align 0.5 color "#ffffff"# font "gui/twoj_font.ttf"
            
            # Ten długi tekst licencji teraz automatycznie się zawinie dzięki xmaximum w vboxie
            text _("Stworzono w Ren'Py [renpy.version_only].\n\n[renpy.license!t]") size 30 xalign 0.5 text_align 0.5 color "#ffffff" #font "gui/twoj_font.ttf"
# screen about():

#     tag menu

#     ## This use statement includes the game_menu screen inside this one. The
#     ## vbox child is then included inside the viewport inside the game_menu
#     ## screen.
#     use game_menu(_("About"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             label "[config.name!t]"
#             text _("Version [config.version!t]\n")

#             ## gui.about is usually set in options.rpy.
#             if gui.about:
#                 text "[gui.about!t]\n"

#             text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Strona {}"), auto=_("Automatyczny zapis"), quick=_("Szybki zapis"))

    
    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                yalign 0.8
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
                    color "#ffffff"            
                    #font "gui/twoj_font.ttf"   
                    size 35                    

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("pusty slot")):
                            style "slot_time_text"
                            idle_color "#ffffff"

                        text FileSaveName(slot):
                            style "slot_name_text"
                            idle_color "#ffffff"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.9
                #spacing 50

                hbox:
                    xalign 0.5
                    yalign 0.5
                    #spacing 30

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious():
                        text_idle_color "#ffffff"
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            action FilePage("auto")
                            text_idle_color "#ffffff"

                    if config.has_quicksave:
                        textbutton _("{#szybkie_zapisy}Q"):
                            action FilePage("quick")
                            text_idle_color "#ffffff"

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 5):
                        textbutton "[page]":
                            action FilePage(page)
                            text_idle_color "#ffffff"

                    textbutton _(">")action FilePageNext(max=4):
                        text_idle_color "#ffffff"
                    key "save_page_next" action FilePageNext(max=4)

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Wgraj Sync"):
                            action UploadSync()
                            text_idle_color "#ffffff"
                            xalign 0.5
                    else:
                        textbutton _("Pobierz Sync"):
                            action DownloadSync()
                            text_idle_color "#ffffff"
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu("Preferences"):

        vbox:
            

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        
                   

                        style_prefix "radio"
                        label _("Wyświetlanie") 
                        textbutton _("Okno"):
                            action Preference("display", "window")
                            text_idle_color "#ffffff"
                        textbutton _("Pełen ekran"):
                            action Preference("display", "fullscreen")
                            text_idle_color "#ffffff"

                vbox:
                    style_prefix "check"
                    label _("Pomiń")
                    textbutton _("Nieczytany tekst"):
                        action Preference("skip", "toggle")
                        text_idle_color "#ffffff"
                    textbutton _("Po wyborach"):
                        action Preference("after choices", "toggle")
                        text_idle_color "#ffffff"
                    textbutton _("Przejścia"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        text_idle_color "#ffffff"

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Szybkość tekstu")

                    bar value Preference("text speed")

                    label _("Czas autoodtwarzania")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Głośność muzyki")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Głośność dźwięków")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    # if config.has_voice:
                    #     label _("Voice Volume")

                    #     hbox:
                    #         bar value Preference("voice volume")

                    #         if config.sample_voice:
                    #             textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Wycisz wszystko"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            text_idle_color "#ffffff"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False
    

    use history_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


screen pause_menu():
    
    #transform hover_tint:
    #    matrixcolor TintMatrix("#0b412f7c")

    tag menu # Mówi silnikowi, że to jest menu i ma zatrzymać grę

    # 1. Czarne, półprzezroczyste tło przyciemniające grę
    add Solid("#000000a7")

    # 2. Kwadrat na środku ekranu

    add "gui/Pause_Menu/Pause_Menu.png":
        xalign 0.5
        yalign 0.5
        zoom 0.5
       
    vbox:
        xalign 0.5
        yalign 0.57
        spacing 20

        button:
            action Return()
            xysize (260, 80)
            
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Powrót":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 40
                idle_color "#ffffff"
                hover_color "#ffffff"
        button:
            action ShowMenu("save")
            xysize (260, 80)
       
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Zapisz":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff"
        button:
            action ShowMenu("load")
            xysize (260, 80)
            
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Wczytaj":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 35
                idle_color"#ffffff"
                hover_color "#ffffff"

        button:
            action ShowMenu("preferences")
            xysize (260, 80)
        
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Opcje":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff"

        button:
            action MainMenu()
            xysize (260, 80)
         
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Menu główne":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff"

        
        button:
            action Quit(confirm=True)
            xysize (260, 80)
    
            idle_background Transform("gui/Pause_Menu/Button.png", size=(260, 80))
            hover_background Transform("gui/Pause_Menu/Button.png", size=(260, 80), alpha=0.6)
            
            text "Wyjdź":
                align (0.48, 0.5)
                #font "gui/twoj_font.ttf"
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff"

screen diary_page():

    add "bg book"

    # LEWA STRONA
    frame:
        background None

        xpos 200
        ypos 120
        xsize 520
        ysize 700

        vbox:
            spacing 18

            text "Dziennik Alysii Wpis 001":
                size 50
                color "#000000"

            text "Dla moich uczniów":
                size 34
                color "#000000"

            text "Jeśli czytacie te słowa, to wiecie już, że jestem w miejscu, do którego nikt nie powinien wchodzić.":
                size 30
                color "#000000"

            text "On… mówił mi, żebym tego nie robiła.":
                size 30
                color "#f5f0e8"

            text "Że nie wszystko jest do odkrycia.":
                size 30
                color "#f5f0e8"

            text "Że niektóre tajemnice istnieją tylko po to, by pozostać tajemnicami.":
                size 30
                color "#f5f0e8"

            text "Ale jeśli świat ma sens, to musi istnieć jego źródło.":
                size 30
                color "#f5f0e8"

            text "A jeśli go nie ma…":
                size 30
                color "#f5f0e8"

            text "…to chcę wiedzieć dlaczego.":
                size 30
                color "#f5f0e8"


    # PRAWA STRONA
    frame:
        background None

        xpos 1000
        ypos 140
        xsize 520
        ysize 700

        vbox:
            spacing 18

            text "Nie idę tam jako bohaterka.":
                size 30
                color "#f5f0e8"

            text "Idę jako nauczycielka, która nie potrafi znieść niewiedzy.":
                size 30
                color "#f5f0e8"

            text "Chcę wiedzieć, co się stało z moimi rodzicami.":
                size 30
                color "#f5f0e8"

            text "I nie jestem sama.":
                size 30
                color "#f5f0e8"

            text "Nie martwcie się.":
                size 30
                color "#f5f0e8"

            text "{b}On się mną zaopiekuje.{/b}":
                size 30
                color "#f5f0e8"




screen end_game_menu():
    
    modal True 

   
    add "images/bg end.png"

    
    vbox:
        xalign 0.5
        yalign 0.87
        spacing 30

        button:
            action MainMenu()
            xysize (400, 120)
         
            idle_background Composite(
                (400, 120),                                                   
                (0, 0), Solid("#141414"),                                     
                (0, 0), Transform("gui/Pause_Menu/Button.png", size=(400, 120)) 
            )

            hover_background Composite(
                (400, 120),                                                   
                (0, 0), Solid("#141414"),                                     
                (0, 0), Transform("gui/Pause_Menu/Button.png", size=(400, 120), alpha=0.6) 
            )

            
            text "Zagraj ponownie":
                align (0.48, 0.5)           
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff60"

        button:
            action MainMenu()
            xysize (400, 120)
         
            idle_background Composite(
                (400, 120),                                                   
                (0, 0), Solid("#141414"),                                     
                (0, 0), Transform("gui/Pause_Menu/Button.png", size=(400, 120)) 
            )

            hover_background Composite(
                (400, 120),                                                   
                (0, 0), Solid("#141414"),                                     
                (0, 0), Transform("gui/Pause_Menu/Button.png", size=(400, 120), alpha=0.6) 
            )
            
            text "Menu główne":
                align (0.48, 0.5)
                size 35
                idle_color "#ffffff"
                hover_color "#ffffff60"