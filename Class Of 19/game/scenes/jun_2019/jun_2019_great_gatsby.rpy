label jun_2019_great_gatsby:

    transform fade:
        alpha 0.0
        linear 1.0 alpha 1.0

    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "June 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music calc_studying

    scene bg classroom

    show tanish neutral at left
    show cindy neutral at right
    show alex neutral at mid_left
    show nicole blush at mid_right
    show neuheimer neutral at center

    neuheimer "Alright, class. As part of our unit on modernism and disillusionment, we’ll be watching the 2013 adaptation of *The Great Gatsby*."

    neuheimer "You’re expected to take notes on symbolism, tone, and how the film reflects Fitzgerald’s themes."

    neuheimer "Phones away. Headphones out. Let’s begin."

    hide neuheimer with moveoutleft
    hide alex with moveoutleft
    hide nicole with moveoutright

    show bg classroom_dimmed at fade

    pause

    show tanish neutral at middle_left with moveinleft
    show cindy neutral at middle_right with moveinright

    tanish "You ever read the book or are you just here for DiCaprio?"

    cindy "I read it. Didn't love it. Gatsby’s a walking red flag."

    tanish "He’s literally the king of ignoring boundaries."

    cindy "And still people romanticize him. Wild."

    tanish "At least the soundtrack slaps."

    cindy "Okay, yeah. That part’s valid."

    # Steamy scene begins

    narrator "A steamy scene begins to play."

    menu:
        "Whisper to Cindy: 'This will be us in the future.'":
            jump tanish_inappropriate
        "Stay quiet and keep watching the movie.":
            jump tanish_respectful

    label tanish_inappropriate:

        stop music
        play music gatsby

        show tanish blush at middle_left

        tanish "This will be us in the future."

        show cindy angry at middle_right

        cindy "..."

        cindy "*What the hell is wrong with you?*"

        play sound slapping

        show bg classroom at fade

        show neuheimer sad at center with moveinleft

        show tanish sad at mid_left with move
        show cindy angry at mid_right with move

        neuheimer "Mister Shah... Is there a problem?"

        tanish "N-no, sorry—"

        neuheimer "Then why did I just hear slapping?"

        tanish "Uhh,,, I—I need to go."

        hide tanish with moveoutleft

        scene splash

        show tanish sad at center with moveinleft

        pause

        tanish "God. What the hell was I thinking..."

        hide tanish with moveoutright

        scene bg classroom_dimmed

        show cindy sad at middle_right

        pause

        cindy "(I can’t believe he said that... in the middle of class.)"

        cindy "(I didn’t mean to slap him that hard... now we’re both humiliated.)"

        # Movie ends. Class dismisses

        show bg classroom at fade

        show cindy sad at right with moveinright
        show alex neutral at left with moveinleft
        show nicole blush at mid_left with moveinleft
        show neuheimer neutral at mid_right with moveinright

        pause

        neuheimer "Alright, that’s... enough for today."

        neuheimer "I expect everyone to reflect on the film’s use of symbolism and tone in your responses."

        neuheimer "You’re dismissed."

        hide cindy with moveoutright
        hide nicole with moveoutleft

        # Alex is left with a choice

        menu:
            "Ask Neuheimer a question about the movie":
                jump alex_talks_to_neuheimer
            "Leave and save the question for next class":
                jump scene_12_end

                label alex_talks_to_neuheimer:

                    alex "Hey, Ms. Neuheimer? I had a question about that scene near the end... the green light?"

                    neuheimer "Ah. Fitzgerald’s favorite metaphor. Hope, dreams, delusion. Classic."

                    alex "Makes sense. It kinda hit harder in the movie."

                    pause

                    alex "...Also, sorry about what happened earlier. That was... intense."

                    neuheimer "Yeah. I’ve been teaching fifteen years. Never seen a student get slapped mid-Gatsby."

                    show neuheimer happy at mid_right

                    neuheimer "Still, I’m glad you’re handling it maturely."

                    show alex excited at left

                    alex "It was hard not to notice."

                    neuheimer "Just remember—some people react to embarrassment by saying the worst possible thing. Others learn from it."

                    alex "Thanks. See you next class."

                return

                label scene_12_end:

                    # Alex leaves quietly
                    return

    # ────────────────────────────────
    # RESPECTFUL BRANCH
    # ────────────────────────────────

    label tanish_respectful:

        pause

        show bg classroom at fade

        show tanish neutral at left
        show cindy neutral at right
        show alex neutral at mid_left
        show nicole blush at mid_right
        show neuheimer neutral at center

        neuheimer "Alright, let’s do a five-minute group discussion before you go."

        neuheimer "Talk with the people near you—focus on themes, characterization, or anything that stood out."

        hide neuheimer with moveoutleft

        tanish "So... Gatsby. Thoughts?"

        alex "Honestly? I liked it more than I expected."

        cindy "Same. I mean, it's a mess, but that was kind of the point."

        nicole "Everyone was just emotionally wrecked and rich enough to ignore the consequences."

        tanish "I lowkey felt bad for Gatsby. He was chasing a fantasy that never existed."

        alex "And Daisy never really wanted to be caught. She just liked the attention."

        cindy "Exactly. He built this whole illusion for her, and she didn’t even ask for it."

        nicole "Meanwhile, Tom’s just stomping around ruining lives."

        tanish "Tom might be the real villain here."

        alex "Nah, the villain is the American Dream."

        cindy "Woah. That’s deep."

        nicole "That’s English class energy."

        # Bell rings

        hide nicole with moveoutright
        hide alex with moveoutleft

        show tanish neutral at left
        show cindy happy at right

        cindy "Okay. Not bad. You actually held a decent conversation."

        show tanish blush at left

        tanish "Are you proud of me?"

        cindy "Mildly."

        tanish "Wanna walk out together?"

        cindy "Sure."

    return