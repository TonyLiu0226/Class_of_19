transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -1080

## Credits screen.

screen credits():
    style_prefix "credits"

    add "bg 05_alex_overdose"

    frame at credits_scroll(60.0):
        background None
        xalign 0.01

        vbox:
            null height 20

            text "GAME OVER!" color "#52FF91" size 60

            null height 150

            hbox:
                text "Alex thought he could handle it. Just one edible to take the edge off—maybe clear his mind before the exam."
            hbox:
                text "He hadn’t studied much, but when he sat down for his computer science final, it felt like everything was finally clicking. The first few questions were easy."
            hbox:
                text "For the first time in weeks, he actually felt… okay."
            hbox:
                text "And then it all went black."
            hbox:
                text "The next thing he knew, he was waking up in the ICU, tubes in his arms, his parents at his bedside with fear etched into their faces."
            hbox:
                text "The edible had been spiked with carfentanyl. He had overdosed — right there in the middle of the exam room."
            hbox:
                text "Mr. McDonald had called an ambulance, as Alex had collapsed in front of everyone."
            hbox:
                text "Alex spent days in the hospital, his life hanging in the balance. When he was finally discharged, his parents didn’t even let him say goodbye."
            hbox:
                text "They pulled him out of school immediately, said it wasn’t safe anymore. He was to complete Grade 12 online, at home, under their watchful eyes."
            hbox:
                text "Luckily, Justice was there to help him. The dealer who gave him the edible? Arrested that same week — charged with drug trafficking and sentenced to twelve years in prison."
            hbox:
                text "Sometimes he replayed that moment—sitting in the exam room, feeling like he had it all under control. But he didn’t. And he lost everything in the space of a heartbeat."
            

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

    add "bg 03_tanish_deported"
    textbutton _("Return to Main Menu") text_style "game_over_button" action Return() xalign 0.5 yalign 0.5

## Show credits screen.

label alex_overdose:
    window hide
    show screen credits
    $ renpy.pause(60.0, hard=True)
    hide screen credits
    call screen game_over_button
    return