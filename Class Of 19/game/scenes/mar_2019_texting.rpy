label mar_2019_texting:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "Late March, 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music lunchly

    scene bg tanish_room_night

    show tanish happy at center
    show phone at right

    play sound phone_ping
    tanish "{i}yo, i heard you’re a huge fan of Demon Slayer{/i}"

    pause
    
    scene bg clara_room_night

    show clara neutral at center
    show phone at left

    play sound phone_ping
    clara "{i}lol who told you that??{/i}"
    play sound phone_ping
    clara "{i}i’ve only seen like the first season 😭{/i}"

    scene bg tanish_room_night

    show tanish happy at center
    show phone at right

    play sound phone_ping
    tanish "{i}oh word? the way you were talking about Rengoku in class made it sound serious{/i}"

    scene bg clara_room_night

    show clara neutral at center
    show phone at left

    play sound phone_ping
    clara "{i}okay fair, he’s a legend{/i}"
    play sound phone_ping
    clara "{i}i cried on the train scene and everything{/i}"

    scene bg tanish_room_night

    show tanish happy at center
    show phone at right

    play sound phone_ping
    tanish "{i}you and half the country tbh{/i}"
    play sound phone_ping
    tanish "{i}dude really went out with flames AND wisdom{/i}"

    scene bg clara_room_night

    show clara neutral at center
    show phone at left

    play sound phone_ping
    clara "🔥🔥🔥"
    play sound phone_ping
    clara "{i}i respect that. 10/10 death monologue{/i}"

    scene bg tanish_room_night

    show tanish blush at center
    show phone at left

    tanish "She’s not obsessed with anime or anything, but she’s fun to talk to."
    tanish "Funny, kinda chaotic in a good way. Honestly… I like texting her."
    tanish "This might be a good moment. Should I turn the dial up just a bit?"

    menu:
        "Flirt a little":
            $ flirted_with_clara = True
            jump clara_flirt_path
        "Keep it light":
            $ flirted_with_clara = False
            jump clara_chill_path

    label clara_flirt_path:
    play sound phone_ping
    tanish "{i}not gonna lie{/i}"
    play sound phone_ping
    tanish "{i}talking to you kinda makes this break feel less boring{/i} 🫣"

    pause
    show tanish happy at center

    play sound phone_ping
    tanish "{i}might have to start calling u baeby now lmao{/i}"

    pause

    scene bg clara_room_night

    show clara happy at center
    show phone at left

    play sound phone_ping
    clara "{i}...omg{/i} 😳"
    play sound phone_ping
    clara "{i}ok baeby haha{/i}"

    scene bg tanish_room_night

    show tanish blush at center
    show phone at right

    tanish "That worked… sort of. Her reply’s cute, flirty even. Who knows what will happen from here."

    jump tanish_texts_alex

    label clara_chill_path:
     
        show tanish neutral at center
        play sound phone_ping
        tanish "{i}lol same{/i}"
        play sound phone_ping
        tanish "{i}i’ve been rewatching the Mugen Train arc, it still hits{/i}"

        scene bg clara_room_night

        show clara neutral at center
        show phone at left

        play sound phone_ping
        clara "{i}fr fr{/i}"
        play sound phone_ping
        clara "{i}might rewatch season 1 next week. i need to feel again lol{/i}"

        scene bg tanish_room_night

        show tanish neutral at center

        play sound phone_ping
        tanish "{i}nothing like anime trauma to keep u grounded{/i}"

        jump tanish_texts_alex

    label tanish_texts_alex:
        scene black with pixellate
        with Pause(1)

        tanish "{i}yo i’ve been talking to clara a lot lately{/i}"

        play sound phone_ping
        alex "{i}LMAO{/i}"
        play sound phone_ping
        alex "{i}u tryna bag the TA or what?{/i}"

        tanish "{i}bruh she’s not even MY TA{/i} 💀"

        play sound phone_ping
        alex "{i}still fair game{/i}"
        play sound phone_ping
        alex "{i}lowkey i’ve been thinking of messaging her too{/i} 👀"

        tanish "{i}don’t u dare lol{/i}"

        play sound phone_ping
        alex "{i}better shoot ur shot before i do{/i} 😎"

        scene black with pixellate
        with Pause(1)

    if flirted_with_clara:
        jump clara_response_scene
    else:
        return

    label clara_response_scene:

        scene bg tanish_room_night
        show tanish happy at center
        show phone at left

        play sound phone_ping
        tanish "{i}yo baeby{/i} 😘"
        play sound phone_ping
        tanish "{i}miss me yet or still crying over Rengoku?{/i}"
        play sound phone_ping

        tanish "{i}need a cuddle buddy for anime trauma recovery?{/i} 💀"

        scene bg clara_room_night
        show clara blush at center

        clara "..."

        clara "...he’s kinda cute when he says dumb stuff like that..."

        show clara neutral at center

        clara "...but this feels... extra?"
        clara "like he’s trying way too hard now."

        pause

    return
