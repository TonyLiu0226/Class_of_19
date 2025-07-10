transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits1():
    style_prefix "credits1"

    add "bg 01_alex_arrested"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "GAME OVER!" color "#52FF91" size 60

            null height 150

            hbox:
                text "As Alex was shoved into the back of the police cruiser, panic set in."
            hbox:
                text "He tried to explain that he hadn’t meant any harm, but the officers ignored him."
            hbox:
                text "At the station, he was booked, fingerprinted, and locked in a holding cell for the night — alone, cold, and terrified."
            hbox:
                text "The next morning, the charges were read: criminal trespassing, stalking, and harrassment."
            hbox:
                text "When the case went to trial, the judge showed no leniency. Alex was sentenced to three months in adult prison."
            hbox:tan
                text "Alex was now isolated from his old life. No friends, no relationships, and a bleak future - marked by a record he couldn’t erase."
            

style credits1_hbox:
    spacing 100
    textalign 0.5
    xalign 0.5
    ysize 50

style credits1_text:
    xalign 0.5
    textalign 0.5
    spacing 10

style game_over_button1:
    xalign 0.5
    yalign 0.5
    color "#52FF91"
    size 60

screen game_over_button1():

    add "bg 01_alex_arrested"
    textbutton _("Return to Main Menu") text_style "game_over_button1" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label alex_arrested:
    window hide
    show screen credits1
    $ renpy.pause(60.0, hard=True)
    hide screen credits1
    call screen game_over_button1
    return