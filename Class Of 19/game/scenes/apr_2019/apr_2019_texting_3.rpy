label apr_2019_texting_3:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "A few days later..." with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music theme_music

    scene bg tanish_room_night

    show tanish neutral at center

    tanish "Ahh... just another boring weeknight. What should I do?"
    menu:
        "Text Cindy":
            $Ending9Condition1 = True
            $Ending7Eligible = False
            jump cindy_flirting
        "Watch Anime":
            return

    label cindy_flirting:
        show phone at mid_right

        play sound phone_ping
        tanish "yo, did you ever finish that drawing you were working on?"

        scene bg cindy_room
        show cindy neutral at center
        show phone at mid_right

        play sound phone_ping
        cindy "the monstera leaf one? yeah kinda. still sketchy tho"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right

        play sound phone_ping
        tanish "you gonna show me or are you gatekeeping your greatness?"

        scene bg cindy_room
        show cindy happy at center
        show phone at mid_right
        play sound phone_ping
        cindy "lol it’s not even greatness, it’s leaf with tiny faces"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "so… greatness"

        scene bg cindy_room
        show cindy blush at center
        show phone at mid_right
        play sound phone_ping
        cindy "fine. maybe I’ll send it later"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "deal. chunky the jade warrior needs a portrait anyway"

        scene bg cindy_room
        show cindy blush at center
        show phone at mid_right
        play sound phone_ping
        cindy "lmao he’s thriving on the windowsill btw. so powerful"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "what's next for the squad? any new plants on your wishlist?"

        scene bg cindy_room
        show cindy blush at center
        show phone at mid_right
        play sound phone_ping
        cindy "definitely want a calathea but i heard they’re drama queens"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "fitting for your vibe"

        scene bg cindy_room
        show cindy sideways at center
        show phone at mid_right
        play sound phone_ping
        cindy "rude"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "i mean that lovingly"

        scene bg cindy_room
        show cindy happy at center
        show phone at mid_right
        play sound phone_ping
        cindy "hm. you’re lucky chunky approves"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "blessed by the leaf gods"

        scene bg cindy_room
        show cindy neutral at center
        show phone at mid_right 
        play sound phone_ping
        cindy "but fr school is kinda drowning me lately"

        scene bg tanish_room_night
        show tanish neutral at center
        show phone at mid_right
        play sound phone_ping
        tanish "math?"
        pause
        scene bg cindy_room
        show cindy neutral at center
        show phone at mid_right
        play sound phone_ping
        cindy "math"

        scene bg tanish_room_night
        show tanish blush at center
        show phone at mid_right
        play sound phone_ping
        tanish "say less. you tryna study together this weekend?"
        pause
        scene bg cindy_room
        show cindy neutral at center
        show phone at mid_right
        play sound phone_ping
        cindy "at the library?"

        scene bg tanish_room_night
        show tanish blush at center
        show phone at mid_right
        play sound phone_ping
        tanish "yeah. snacks, notes, self-loathing"

        scene bg cindy_room
        show cindy happy at center
        show phone at mid_right
        play sound phone_ping
        cindy "honestly sounds perfect"

        scene bg tanish_room_night
        show tanish happy at center
        show phone at mid_right
        play sound phone_ping
        tanish "cool. I’ll bring something sugary and tragic"

        scene bg cindy_room
        show cindy happy at center
        show phone at mid_right
        play sound phone_ping
        cindy "i’ll bring chunky for moral support"

        scene bg clara_room_night

        show clara embarrassed at center
        pause
        clara "so now they’re texting."

        clara "figures."

        clara "I don’t know what’s going on with those two lately..."

        clara "they used to just be fun and cringe. now it’s like getting kinda annoying—"

        show clara neutral at center
        clara "Tanish is suddenly friendly with Cindy? Sweet, even."

        clara "is he for real? or just trying to mess around to get a rise out of me?"

        show clara sideways at center
        clara "ugh."

        clara "I need to stop thinking about this."

        return
