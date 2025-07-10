label jun_2019_gatsby_aftermath:

    stop music
    scene black with pixellate
    with Pause(1)

    play music sad

    scene bg school_hallway

    show cindy sad at center
    show gina neutral at middle_left
    show lia neutral at middle_right

    gina "Cindy? Hey—what’s wrong?"

    cindy "..."

    pause

    gina "I saw you walk out of class like you were about to cry."

    lia "Did something happen in English?"

    cindy "...Yeah. Bobby happened."

    gina "What did he do?"

    cindy "During the movie—during that steamy scene—he leaned over and whispered..."

    cindy "‘This will be us in the future.’"

    lia "...You're kidding."

    cindy "I froze. I didn’t know what to do. I slapped him."

    cindy "And then the teacher stopped the movie. Turned on the lights. Everyone stared."

    show gina angry at middle_left

    gina "What the hell was he thinking?"

    cindy "I don’t know. He just said it like it was a joke. Like we were in on it together."

    lia "You were just trying to watch a movie and this dude thinks he’s funny."

    cindy "It was so embarrassing. I didn’t want to make it a scene, but my body just reacted."

    show gina neutral at middle_left

    gina "No one blames you. He crossed a line."

    cindy "Still… I feel like the entire class was watching me for the rest of the period."

    lia "They were probably just shocked. You handled it way better than I would’ve."

    gina "You don’t need to explain anything. We’ve got your back."

    cindy "...Thanks. I just want this to go away."

    scene black
    show text "The next week" with dissolve
    with Pause(2)

    scene bg cafeteria_lunch

    show alex neutral at left
    show gina neutral at mid_left
    show cindy sad at center
    show lia neutral at mid_right
    show albert troll at right

    # Group is halfway through lunch

    albert "You guys realize Bobby hasn’t been here all week?"

    alex "Yeah. I've texted him twice. No response."

    lia "He’s probably buried himself in some corner of the school."

    albert "Library goblin arc?"

    gina "More like coward arc."

    cindy "..."

    pause

    alex "I guess he got pretty wrecked after what happened that day."

    lia "He should’ve been embarrassed."

    albert "What even possessed him to say that? Middle of Gatsby? Really?"

    gina "He thought it was funny. Or charming. Either way, it wasn’t."

    pause

    alex "Honestly, it was uncomfortable just being in the room."

    cindy "...I just wish he hadn’t made me part of it."

    gina "You didn’t do anything wrong."

    lia "Girl, you slapped him into another timeline. That was justified."

    cindy "Yeah, but everyone keeps looking at me in class like I'm radioactive."

    alex "People’ll forget. High school memory only lasts until the next hallway scandal."

    show albert neutral at right

    albert "Exactly. Wait till Jacob fails chem again and sets off the fire alarm. It'll blow over."

    show gina angry at mid_left
    pause

    gina "Still. He doesn’t get to just disappear."

    show lia sideways at mid_right

    lia "Gina—"

    gina "He humiliated Cindy and left her to deal with it alone. That’s not okay."

    alex "You gonna talk to him?"

    gina "I’m going to find him."

    show albert troll at right

    albert "Should we prepare a eulogy?"

    gina "Don’t be dramatic."

    hide gina with moveoutleft

    show alex excited at left

    alex "And there she goes. On a warpath of justice."

    show lia neutral at mid_right

    lia "Remind me to never cross her."

    show cindy neutral at center

    cindy "...Thanks, Gina."

    scene black
    with Pause(1)

    scene bg library

    show bobby sad at center

    bobby "(Why do I even come to school anymore... It's like I can't even look anyone in the eye without being reminded of what happened during that awful class again.)"

    bobby "(I'm so embarrassed. I can't believe I did that. I'm such a fool.)"

    show gina angry at left with moveinleft

    gina "I... Found You..."

    bobby "Gina... hey."

    gina "Don’t ‘hey’ me. You’ve been hiding out for days, not responding to anyone, not talking to anyone at school... We've all been wondering what the hell happened with you."

    bobby "I didn’t feel like seeing anyone."

    gina "Well if it wasn’t obvious, you made Cindy cry."

    bobby "...I know."

    gina "You embarrassed her in front of a whole class. What did you expect?"

    bobby "I messed up. I get it."

    gina "Then own it. Go apologize."

    show bobby angry at center

    bobby "I know! I know it's bad, and I'm sorry!"

    gina "Don't apologize to me, I'm not the one who got slapped!"

    bobby "But for real, where should I even start? Do I just go up to her and say \"Hey, I’m sorry I said something weird. I don’t remember what it was, so can you remind me? And if it’s that bad, I promise I’ll never talk to you again so it’s less awkward?\""

    gina "Are you serious right now?"

    gina "Bruh do you even hear yourself? You don’t even remember what you said, and somehow you’re still messing this up by acting like she owes you something?"

    gina "You don't sound sorry at all... You sound pathetic..."

    gina "Anyways, I'm going to leave you to it. You decide whether you want to actually apologize or not. But let me be clear, time is running out, and Cindy is still pissed."

    hide gina with moveoutleft

    menu:
        "Apologize to Cindy":
            jump bobby_apologizes
        "Refuse to apologize":
            $Ending3Triggered = True
            jump bobby_refuses

    label bobby_apologizes:

        show bobby neutral at center

        bobby "Okay. You're right."

        bobby "I’ll talk to her tomorrow. I owe her that much."

        show gina neutral at left with moveinleft

        gina "You owe her more, but yeah. Start there."

        bobby "Thanks... for coming to yell at me, I guess."

        gina "Don’t make me do it again."

        scene black
        with Pause(1)

        scene bg bobby_room_night

        show bobby sad at center
        show phone at right

        bobby "(Okay... here goes nothing.)"
    
        play sound phone_ping
        bobby "Hey. I just wanted to say I’m sorry for what I said during the movie."
        play sound phone_ping
        bobby "It was stupid and disrespectful. You didn’t deserve that."
        play sound phone_ping
        bobby "I was trying to be funny, but I wasn’t thinking at all. I’m sorry."

        scene bg cindy_room

        show cindy sad at center
        show phone at right

        play sound phone_ping
        cindy "Thanks for the apology."
        play sound phone_ping
        cindy "It doesn’t make it okay, but I appreciate that you owned up to it."
        play sound phone_ping
        cindy "We’re done, though. I’m not interested in picking this back up."
        play sound phone_ping
        cindy "Take care of yourself, alright?"

        scene bg bobby_room_night

        show bobby sad at center
        show phone at right

        bobby "(Yeah. I deserve that.)"

        play sound phone_ping
        bobby "ok... you too. Take care."
        pause
        bobby "(Screw it. Guess it's anime therapy hours again.)"

        bobby "(Time to change my username to 'hikkikomori_life'.)"

        return

    label bobby_refuses:

        return