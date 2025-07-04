label jun_2019_great_gatsby:

    transform fade:
        alpha 0.0
        linear 1.0 alpha 1.0

    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "Last Day Of School, June 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    scene bg alex_room

    show alex neutral at center
    show phone at right

    alex "(Damn can't believe its the end of the year already. I still want to see some of my friends before exams kill me. Maybe I’ll check if Clara’s around...)"

    play sound phone_ping
    alex "hey clara"

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "hey"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "how’s it going?"

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "busy. school’s kinda killing me lately"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "yeah, fair"
    
    pause
 
    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "hey, can I ask something?"
 
    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "yeah ofc"
 
    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "do you... actually like me?"

    clara "i’m asking because lately... it feels like you’ve been putting a lot of pressure on me"

    clara "being around you is fun, but sometimes it’s like you’re expecting something back"

    clara "so i need to know. is this just a crush thing? or do you really like me?"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    menu:
        "Confess honestly":
            jump alex_confess_real
        "Back off":
            jump alex_back_off

    label alex_confess_real:
 
        show alex blush at center
        play sound phone_ping
        alex "i do. i really like you clara"

        play sound phone_ping
        alex "i wasn’t trying to push you. i guess i just... got excited"
        
        play sound phone_ping
        alex "you’re smart and chill and funny and yeah i catch myself thinking about you a lot"

        scene bg clara_room_night

        show clara blush at center
        show phone at right

        show clara blush at center
        clara "(...)"

        play sound phone_ping
        clara "thanks for being honest"
        
        show clara neutral at center
        play sound phone_ping
        clara "i don’t know if i’m ready for anything right now"

        play sound phone_ping
        clara "but i’ll think about it. i just need space to figure things out"

        scene bg alex_room

        show alex neutral at center
        show phone at right

        play sound phone_ping
        alex "yeah. totally. take your time"

        jump scene_15b_clara_cafe

    # ──────────────────────
    # Back off branch
    # ──────────────────────

    label alex_back_off:
        play sound phone_ping
        alex "i’m sorry"
        play sound phone_ping
        alex "i didn’t mean to make you feel pressured"
        play sound phone_ping
        alex "i like hanging out with you, that’s all"
        play sound phone_ping
        alex "i’ll back off if it’s too much"

        scene bg clara_room_night

        show clara neutral at center
        show phone at right

        play sound phone_ping
        clara "thanks for saying that"

        play sound phone_ping
        clara "i just wanted to be honest"

        play sound phone_ping
        clara "we’re good"