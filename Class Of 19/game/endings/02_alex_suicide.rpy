transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits2():
    style_prefix "credits2"

    add "bg 02_alex_suicide"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "GAME OVER!" color "#52FF91" size 60

            null height 150

            hbox:
                text "In the early hours of July 12th, Alex wandered the empty streets, his mind a whirlwind of rejection, shame, and unbearable loneliness."
            hbox:
                text "The silence pressed against him, broken only by the distant rumble of a train."
            hbox:
                text "He found himself near the tracks, staring into the distance, where the faint glow of headlights began to emerge."
            hbox:
                text "Thoughts swirled—memories of being ignored, of always falling short, of desperately trying to be seen and always ending up invisible."
            hbox:
                text "He thought about Gina. About everyone. About how no one had called him back."
            hbox:
                text "The train horn wailed, long and hollow. And as the light grew brighter, something inside him snapped."
            hbox:
                text "He took a deep breath, clenched his jaw—and ran."
            hbox:
                text "Toward the rails. Toward the end."
            

style credits2_hbox:
    spacing 100
    textalign 0.5
    xalign 0.5
    ysize 50

style credits2_text:
    xalign 0.5
    textalign 0.5
    spacing 10

style game_over_button2:
    xalign 0.5
    yalign 0.5
    color "#52FF91"
    size 60

screen game_over_button2():

    add "bg 02_alex_suicide"
    textbutton _("Return to Main Menu") text_style "game_over_button2" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label alex_suicide:
    window hide
    show screen credits2
    $ renpy.pause(60.0, hard=True)
    call screen game_over_button2
    return