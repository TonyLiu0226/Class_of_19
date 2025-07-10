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

    scene bg bobby_room_night

    show bobby happy at center
    show phone at right

    play sound phone_ping
    bobby "{i}yo, i heard you’re a huge fan of Demon Slayer{/i}"

    pause
    
    scene bg gina_room_night

    show gina neutral at center
    show phone at left

    play sound phone_ping
    gina "{i}lol who told you that??{/i}"
    play sound phone_ping
    gina "{i}i’ve only seen like the first season 😭{/i}"

    scene bg bobby_room_night

    show bobby happy at center
    show phone at right

    play sound phone_ping
    bobby "{i}oh word? the way you were talking about Rengoku in class made it sound serious{/i}"

    scene bg gina_room_night

    show gina neutral at center
    show phone at left

    play sound phone_ping
    gina "{i}okay fair, he’s a legend{/i}"
    play sound phone_ping
    gina "{i}i cried on the train scene and everything{/i}"

    scene bg bobby_room_night

    show bobby happy at center
    show phone at right

    play sound phone_ping
    bobby "{i}you and half the country tbh{/i}"
    play sound phone_ping
    bobby "{i}dude really went out with flames AND wisdom{/i}"

    scene bg gina_room_night

    show gina neutral at center
    show phone at left

    play sound phone_ping
    gina "🔥🔥🔥"
    play sound phone_ping
    gina "{i}i respect that. 10/10 death monologue{/i}"

    scene bg bobby_room_night

    show bobby blush at center
    show phone at left

    bobby "She’s not obsessed with anime or anything, but she’s fun to talk to."
    bobby "Funny, kinda chaotic in a good way. Honestly… I like texting her."
    bobby "This might be a good moment. Should I turn the dial up just a bit?"

    menu:
        "Flirt a little":
            $ flirted_with_gina = True
            $Ending7Eligible = False
            jump gina_flirt_path
        "Keep it light":
            $ flirted_with_gina = False
            jump gina_chill_path

    label gina_flirt_path:
    play sound phone_ping
    bobby "{i}not gonna lie{/i}"
    play sound phone_ping
    bobby "{i}talking to you kinda makes this break feel less boring{/i} 🫣"

    pause
    show bobby happy at center

    play sound phone_ping
    bobby "{i}might have to start calling u baeby now lmao{/i}"

    pause

    scene bg gina_room_night

    show gina happy at center
    show phone at left

    play sound phone_ping
    gina "{i}...omg{/i} 😳"
    play sound phone_ping
    gina "{i}ok baeby haha{/i}"

    scene bg bobby_room_night

    show bobby blush at center
    show phone at right

    bobby "That worked… sort of. Her reply’s cute, flirty even. Who knows what will happen from here."

    jump bobby_texts_alex

    label gina_chill_path:
     
        show bobby neutral at center
        play sound phone_ping
        bobby "{i}lol same{/i}"
        play sound phone_ping
        bobby "{i}i’ve been rewatching the Mugen Train arc, it still hits{/i}"

        scene bg gina_room_night

        show gina neutral at center
        show phone at left

        play sound phone_ping
        gina "{i}fr fr{/i}"
        play sound phone_ping
        gina "{i}might rewatch season 1 next week. i need to feel again lol{/i}"

        scene bg bobby_room_night

        show bobby neutral at center

        play sound phone_ping
        bobby "{i}nothing like anime trauma to keep u grounded{/i}"

        jump bobby_texts_alex

    label bobby_texts_alex:
        scene black with pixellate
        with Pause(1)

        bobby "{i}yo i’ve been talking to Gina a lot lately{/i}"

        play sound phone_ping
        alex "{i}LMAO{/i}"
        play sound phone_ping
        alex "{i}u tryna bag the TA or what?{/i}"

        bobby "{i}bruh she’s not even MY TA{/i} 💀"

        play sound phone_ping
        alex "{i}still fair game{/i}"
        play sound phone_ping
        alex "{i}lowkey i’ve been thinking of messaging her too{/i} 👀"

        bobby "{i}don’t u dare lol{/i}"

        play sound phone_ping
        alex "{i}better shoot ur shot before i do{/i} 😎"

        scene black with pixellate
        with Pause(1)

    if flirted_with_gina:
        jump gina_response_scene
    else:
        return

    label gina_response_scene:

        scene bg bobby_room_night
        show bobby happy at center
        show phone at left

        play sound phone_ping
        bobby "{i}yo baeby{/i} 😘"
        play sound phone_ping
        bobby "{i}miss me yet or still crying over Rengoku?{/i}"
        play sound phone_ping

        bobby "{i}need a cuddle buddy for anime trauma recovery?{/i} 💀"

        scene bg gina_room_night
        show gina blush at center

        gina "..."

        gina "...he’s kinda cute when he says dumb stuff like that..."

        show gina neutral at center

        gina "...but this feels... extra?"
        gina "like he’s trying way too hard now."

        pause

    return
