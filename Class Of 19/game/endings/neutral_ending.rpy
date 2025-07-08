transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits0():
    style_prefix "credits0"

    add "bg 00_neutral_ending"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "CONGRATULATIONS!" color "#ff52c0" size 60

            null height 150

            hbox:
                text "Alex and Tanish remained good friends from that day on, and both graduated from high school with honors."
            hbox:
                text "Tanish got an offer for Waterloo CS, while Alex got an offer for Engineering at U of T."
            hbox:
                if not TanishCindyBreakup:
                    text "They both became more confident in themselves, and attended prom with their respective dates - Alex with a Gr. 10 girl he met at a party, and Tanish with Cindy."
                else:
                    text "They both became more confident in themselves, and attended prom with their respective dates - Alex with a Gr. 10 girl he met at a party, and Tanish with a Gr. 12 girl he met in class."
            hbox:
                text "Clara let the entire Alex situation go, and in the end she got together with Albert, much to the dismay of Tanish and Alex when they found out."
            hbox:
                text "But by that point, the incident on July 11th, 2019 had long faded from their memories."
            hbox:
                text "Lia, after dumping Jacob, became much more happier and confident in herself."
            hbox:
                text "After all, high school is just a cringy phase that everyone has to use as a stepping stone to the responsibilities and challenges of the real world."
            

style credits0_hbox:
    spacing 100
    textalign 0.5
    xalign 0.5
    ysize 50

style credits0_text:
    xalign 0.5
    textalign 0.5
    spacing 10

style game_over_button0:
    xalign 0.5
    yalign 0.5
    color "#ff52c0"
    size 60

screen game_over_button0():

    add "bg 00_neutral_ending"
    textbutton _("Return to Main Menu") text_style "game_over_button0" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label neutral_ending:
    stop music
    window hide
    play music congratulations
    show screen credits0
    $ renpy.pause(60.0, hard=True)
    call screen game_over_button0
    return