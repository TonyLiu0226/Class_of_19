label jun_2019_alex_rejected:

    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "Exams, June 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music cpen

    scene bg school_hallway

    show alex neutral at center

    alex "(God I am not looking forward to the CS exam today...)"

    alex "(Why is Tanish still not responding to my messages? Is he even gonna show up today?)"

    alex "(Also, Clara is not responding to my messages... great)"

    show clara neutral at left with moveinleft

    clara "Hey."

    alex "Hey. How was the bio final?"

    clara "It was brutal. I hope we get curved"

    alex "I’m sure you did fine."

    clara "Thanks."

    clara "So... I’ve been thinking. About us."

    pause

    clara "I don’t think I’m ready. And honestly, I just don’t see it working out."

    alex "...Right."

    show clara happy at left

    clara "But... I still want us to be friends. Hope that's okay with you."

    alex "Yeah. Friends."

    hide clara with moveoutleft

    show alex sad at center

    alex "(Hmm... Friends... No big deal, It's okay...)"

    alex "(...Why does it feel like I got kicked in the ribs.)"

    # Transition to outside

    scene black with pixellate
    with Pause(1)

    scene splash

    show alex sad at center

    alex "(Damn I just need to clear my head... I can't afford to fail CS because of this.)"

    # Drug dealer approaches

    show dealer at left with moveinleft

    dealer "Yo."

    alex "...Hi?"

    dealer "You look like you got dumped or failed bio. Or both."

    show alex neutral at center

    alex "What do you want?"

    dealer "Chill, man. Just saying—you look like you could use a little lift."

    dealer "Got some edibles. Real mellow. Help you forget the world for a while."

    menu:
        "Take the edibles":
            $Ending5Triggered = True
            jump alex_accepts_drugs
        "Refuse and walk away":
            jump alex_refuses_drugs

    # ──────────────────────
    # Bad Ending
    # ──────────────────────

    label alex_accepts_drugs:

    alex "...Screw it. Why not."

    dealer "Good man. Enjoy."

    hide dealer with moveoutleft

    play sound smoke

    pause

    scene black
    with Pause(1)

    return

    # ──────────────────────
    # Refusal branch
    # ──────────────────────

    label alex_refuses_drugs:

    alex "No thanks. I’m good."

    dealer "Suit yourself. More for the depressed band kids, I guess."

    hide dealer with moveoutleft

    alex "(Yeah... that would’ve been stupid.)"

    alex "(Anyways... I got a goddamn CS exam to pass)"

    return
