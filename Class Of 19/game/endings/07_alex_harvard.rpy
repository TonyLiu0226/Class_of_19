transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits():
    style_prefix "credits"

    add "bg 07_alex_harvard"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "CONGRATULATIONS!" color "#52FF91" size 60

            null height 150

            hbox:
                text "Alex realized that it was more important to chase his dreams than chase around women. He stopped wasting time and started focusing—with real intensity."
            hbox:
                text "He studied like his life depended on it. Rewrote notes. Drilled problems. Pulled all-nighters not because he was behind, but because he wanted to get ahead."
            hbox:
                text "As a result, he aced all his exams that semester. 100s. On everything."
            hbox:
                text "The momentum continued into next year, where he scored over 95% on every single unit and final test, from AP Physics to English dash 1."
            hbox:
                text "Teachers stopped grading his work with red pens — they used it as the answer key. He got a 5 on every AP exam he wrote. When SAT season rolled around, he got a perfect 1600... on his first try."
            hbox:
                text "But he didn’t stop at academics."
            hbox:
                text "He spent his spare time learning to code in a variety of languages, and building impressive projects similar in scope to what university students typically did after years of studying."
            hbox:
                text "All the while, he was applying to Ivy League schools across the country. He was accepted to every single one he applied to... Harvard, Princeton, Yale, Stanford, you name it."
            hbox:
                text "When the Harvard offer came... he wasn't shocked. Because, deep down in his heart, he knew he earned it."
            

style credits_hbox:
    spacing 100
    textalign 0.5
    xalign 0.5
    ysize 50

style credits_text:
    xalign 0.5
    textalign 0.5
    spacing 10

style game_over_button:
    xalign 0.5
    yalign 0.5
    color "#52FF91"
    size 60

screen game_over_button():

    add "bg 07_alex_harvard"
    textbutton _("Return to Main Menu") text_style "game_over_button" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label alex_harvard:
    stop music
    window hide
    play music congratulations
    show screen credits
    $ renpy.pause(60.0, hard=True)
    hide screen credits
    call screen game_over_button
    return