label mar_2019_texting:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "Late March, 2019" with dissolve
    play sound yooo
    with Pause(10)

    scene black with pixellate
    with Pause(1)

    play music lunchly

    scene bg tanish_room_night

    show tanish happy at center
    show phone at right

    tanish "yo, i heard you’re a huge fan of Demon Slayer"

    pause
    
    play sound phone_ping
    clara "lol who told you that??"
    play sound phone_ping
    clara "i’ve only seen like the first season 😭"

    tanish "oh word? the way you were talking about Rengoku in class made it sound serious"

    play sound phone_ping
    clara "okay fair, he’s a legend"
    play sound phone_ping
    clara "i cried on the train scene and everything"

    tanish "you and half the country tbh"
    tanish "dude really went out with flames AND wisdom"

    play sound phone_ping
    clara "🔥🔥🔥"
    play sound phone_ping
    clara "i respect that. 10/10 death monologue"

    show tanish blush at center
    show phone at left
    pause

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

    tanish "not gonna lie"
    tanish "talking to you kinda makes this break feel less boring 🫣"

    pause
    show tanish happy at center

    tanish "might have to start calling u baeby now lmao"

    pause

    play sound phone_ping
    clara "...omg 😳"
    play sound phone_ping
    clara "ok baeby haha"

    tanish "That worked… sort of. Her reply’s cute, flirty even. Who knows what will happen from here."

    jump tanish_texts_alex

    label clara_chill_path:

        tanish "lol same"
        tanish "i’ve been rewatching the Mugen Train arc, it still hits"

        clara "fr fr"
        clara "might rewatch season 1 next week. i need to feel again lol"

        tanish "nothing like anime trauma to keep u grounded"

        jump tanish_texts_alex

    label tanish_texts_alex:
        scene black with pixellate
        with Pause(1)

        tanish "yo i’ve been talking to clara a lot lately"

        play sound phone_ping
        alex "LMAO"
        play sound phone_ping
        alex "u tryna bag the TA or what?"

        tanish "bruh she’s not even MY TA 💀"

        play sound phone_ping
        alex "still fair game"
        play sound phone_ping
        alex "lowkey i’ve been thinking of messaging her too 👀"

        tanish "don’t u dare lol"

        play sound phone_ping
        alex "better shoot ur shot before i do 😎"

        scene black with pixellate
        with Pause(1)

    if flirted_with_clara:
        jump clara_response_scene
    else:
        return

    label clara_response_scene:

        scene bg tanish_room_night

        tanish "yo baeby 😘"
        tanish "miss me yet or still crying over Rengoku?"

        tanish "need a cuddle buddy for anime trauma recovery? 💀"

        scene bg clara_room_night
        show clara blush at center

        clara "..."

        clara "...he’s kinda cute when he says dumb stuff like that..."

        show clara neutral at center

        clara "...but this feels... extra?"
        clara "like he’s trying way too hard now."

        pause

    return
