transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits3():
    style_prefix "credits3"

    add "bg 03_bobby_deported"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "GAME OVER!" color "#ff52c0" size 60

            null height 150

            hbox:
                text "Bobby never apologized. Maybe he didn't know how. After everything that happened with Cindy, he just disappeared."
            hbox:
                text "He stopped showing up to school, stopped talking to anyone. His grades dropped to zero, and he let them."
            hbox:
                text "He didn't even check the portal anymore — because what was the point? When the school finally withdrew him, his parents lost it."
            hbox:
                text "At first, they were furious. Then, they just looked at him like he wasn't even there. A few weeks later, they gave him the news: they were moving back to India."
            hbox:
                text "No discussion. No choice. Just boxes, plane tickets, and silence."
            hbox:
                text "He didn't fight it. He didn't have the energy to. He left behind everything — his room, his friends, his mistakes — and got on the plane like a ghost boarding his own exile."
            hbox:
                text "As he watched the city disappear through the tiny oval window, something twisted in his chest."
            hbox:
                text "It wasn't regret exactly — more like a quiet ache for the person he could've been if he had done things differently."
            hbox:
                text "He thought maybe the distance would help him forget. But deep down, he knew he wasn't leaving his problems behind. He was carrying them, 35,000 feet above everything he ruined."

style credits3_hbox:
    spacing 100
    textalign 0.5
    xalign 0.5
    ysize 50

style credits3_text:
    xalign 0.5
    textalign 0.5
    spacing 10

style game_over_button3:
    xalign 0.5
    yalign 0.5
    color "#ff52c0"
    size 60

screen game_over_button3():

    add "bg 03_bobby_deported"
    textbutton _("Return to Main Menu") text_style "game_over_button3" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label bobby_deported:
    window hide
    show screen credits3
    $ renpy.pause(60.0, hard=True)
    call screen game_over_button3
    return