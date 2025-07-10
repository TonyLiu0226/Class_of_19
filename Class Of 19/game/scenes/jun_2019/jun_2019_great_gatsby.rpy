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

    play music chiki

    scene bg classroom

    show bobby neutral at left
    show kyra neutral at right
    show alex neutral at mid_left
    show emma blush at mid_right
    show emily neutral at center

    emily "Alright, class. As part of our unit on modernism and disillusionment, we’ll be watching the 2013 adaptation of *The Great Gatsby*."

    emily "You’re expected to take notes on symbolism, tone, and how the film reflects Fitzgerald’s themes."

    emily "Phones away. Headphones out. Let’s begin."

    hide emily with moveoutleft
    hide alex with moveoutleft
    hide emma with moveoutright

    show bg classroom_dimmed at fade

    pause

    show bobby neutral at middle_left with moveinleft
    show kyra neutral at middle_right with moveinright

    bobby "You ever read the book or are you just here for DiCaprio?"

    kyra "I read it. Didn't love it. Gatsby’s a walking red flag."

    bobby "He’s literally the king of ignoring boundaries."

    kyra "And still people romanticize him. Wild."

    bobby "At least the soundtrack slaps."

    kyra "Okay, yeah. That part’s valid."

    # Steamy scene begins

    narrator "A steamy scene begins to play."

    menu:
        "Whisper to Kyra: 'This will be us in the future.'":
            $BobbyKyraBreakup = True
            jump bobby_inappropriate
        "Stay quiet and keep watching the movie.":
            jump bobby_respectful

    label bobby_inappropriate:

        stop music
        play music gatsby

        show bobby blush at middle_left

        bobby "This will be us in the future."

        show kyra angry at middle_right

        kyra "..."

        kyra "What the hell is wrong with you?"

        play sound slapping

        show bg classroom at fade

        show emily sad at center with moveinleft

        show bobby sad at mid_left with move
        show kyra angry at mid_right with move

        emily "Mister Singh... Is there a problem?"

        bobby "N-no, sorry—"

        emily "Then why did I just hear slapping?"

        bobby "Uhh,,, I—I need to go."

        hide bobby with moveoutleft

        emily "(sighs)"

        emily "Kyra, I'm going to need you to go to the principal's office to explain what happened."

        kyra "(sighs)"

        hide kyra with moveoutright

        scene splash

        show bobby sad at center with moveinleft

        pause

        bobby "God. What the hell was I thinking..."

        hide bobby with moveoutright

        scene bg classroom_dimmed

        show kyra sad at middle_right

        pause

        kyra "(I can’t believe he said that... in the middle of class.)"

        kyra "(I didn’t mean to slap him that hard... now we’re both humiliated.)"

        kyra "(On top of that, I have detention after school tomorrow, yet Bobby can just run away like nothing happened.)"

        # Movie ends. Class dismisses

        show bg classroom at fade

        show kyra sad at right with moveinright
        show alex neutral at left with moveinleft
        show emma blush at mid_left with moveinleft
        show emily neutral at mid_right with moveinright

        pause

        emily "Alright, that’s... enough for today."

        emily "I expect everyone to reflect on the film’s use of symbolism and tone in your responses."

        emily "You’re dismissed."

        hide kyra with moveoutright
        hide emma with moveoutleft

        # Alex is left with a choice

        menu:
            "Ask Emily a question about the movie":
                $Ending8Condition1 = True
                jump alex_talks_to_emily
            "Leave and save the question for next class":
                jump scene_12_end

                label alex_talks_to_emily:

                    alex "Hey, Ms. Emily? I had a question about that scene near the end... the green light?"

                    emily "Ah. Fitzgerald’s favorite metaphor. Hope, dreams, delusion. Classic."

                    alex "Makes sense. It kinda hit harder in the movie."

                    pause

                    alex "...Also, sorry about what happened earlier. That was... intense."

                    emily "Yeah. I’ve been teaching fifteen years. Never seen a student get slapped mid-Gatsby."

                    show emily happy at mid_right

                    emily "Still, I’m glad you’re handling it maturely."

                    show alex excited at left

                    alex "It was hard not to notice."

                    emily "Just remember—some people react to embarrassment by saying the worst possible thing. Others learn from it."

                    alex "Thanks. See you next class."

                return

                label scene_12_end:

                    # Alex leaves quietly
                    return

    # ────────────────────────────────
    # RESPECTFUL BRANCH
    # ────────────────────────────────

    label bobby_respectful:

        pause

        show bg classroom at fade

        show bobby neutral at left
        show kyra neutral at right
        show alex neutral at mid_left
        show emma blush at mid_right
        show emily neutral at center

        emily "Alright, let’s do a five-minute group discussion before you go."

        emily "Talk with the people near you—focus on themes, characterization, or anything that stood out."

        hide emily with moveoutleft

        bobby "So... Gatsby. Thoughts?"

        alex "Honestly? I liked it more than I expected."

        kyra "Same. I mean, it's a mess, but that was kind of the point."

        emma "Everyone was just emotionally wrecked and rich enough to ignore the consequences."

        bobby "I lowkey felt bad for Gatsby. He was chasing a fantasy that never existed."

        alex "And Daisy never really wanted to be caught. She just liked the attention."

        kyra "Exactly. He built this whole illusion for her, and she didn’t even ask for it."

        emma "Meanwhile, Tom’s just stomping around ruining lives."

        bobby "Tom might be the real villain here."

        alex "Nah, the villain is the American Dream."

        kyra "Woah. That’s deep."

        emma "That’s English class energy."

        # Bell rings

        hide emma with moveoutright
        hide alex with moveoutleft

        show bobby neutral at left
        show kyra happy at right

        kyra "Okay. Not bad. You actually held a decent conversation."

        show bobby blush at left

        bobby "Are you proud of me?"

        kyra "Mildly."

        bobby "Wanna walk out together?"

        kyra "Sure."

    return