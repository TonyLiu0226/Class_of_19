label jun_2019_gatsby_aftermath:

    stop music
    scene black with pixellate
    with Pause(1)

    play music sad

    scene bg school_hallway

    show cindy sad at center
    show clara neutral at middle_left
    show lia neutral at middle_right

    clara "Cindy? Hey—what’s wrong?"

    cindy "..."

    pause

    clara "I saw you walk out of class like you were about to cry."

    lia "Did something happen in English?"

    cindy "...Yeah. Tanish happened."

    clara "What did he do?"

    cindy "During the movie—during that steamy scene—he leaned over and whispered..."

    cindy "‘This will be us in the future.’"

    lia "...You're kidding."

    cindy "I froze. I didn’t know what to do. I slapped him."

    cindy "And then the teacher stopped the movie. Turned on the lights. Everyone stared."

    show clara angry at middle_left

    clara "What the hell was he thinking?"

    cindy "I don’t know. He just said it like it was a joke. Like we were in on it together."

    lia "You were just trying to watch a movie and this dude thinks he’s funny."

    cindy "It was so embarrassing. I didn’t want to make it a scene, but my body just reacted."

    show clara neutral at middle_left

    clara "No one blames you. He crossed a line."

    cindy "Still… I feel like the entire class was watching me for the rest of the period."

    lia "They were probably just shocked. You handled it way better than I would’ve."

    clara "You don’t need to explain anything. We’ve got your back."

    cindy "...Thanks. I just want this to go away."

    scene black
    show text "The next week" with dissolve
    with Pause(2)

    scene bg cafeteria_lunch

    show alex neutral at left
    show clara neutral at mid_left
    show cindy sad at center
    show lia neutral at mid_right
    show albert troll at right

    # Group is halfway through lunch

    albert "You guys realize Tanish hasn’t been here all week?"

    alex "Yeah. I've texted him twice. No response."

    lia "He’s probably buried himself in some corner of the school."

    albert "Library goblin arc?"

    clara "More like coward arc."

    cindy "..."

    pause

    alex "I guess he got pretty wrecked after what happened that day."

    lia "He should’ve been embarrassed."

    albert "What even possessed him to say that? Middle of Gatsby? Really?"

    clara "He thought it was funny. Or charming. Either way, it wasn’t."

    pause

    alex "Honestly, it was uncomfortable just being in the room."

    cindy "...I just wish he hadn’t made me part of it."

    clara "You didn’t do anything wrong."

    lia "Girl, you slapped him into another timeline. That was justified."

    cindy "Yeah, but everyone keeps looking at me in class like I'm radioactive."

    alex "People’ll forget. High school memory only lasts until the next hallway scandal."

    show albert neutral at right

    albert "Exactly. Wait till Jacob fails chem again and sets off the fire alarm. It'll blow over."

    show clara angry at mid_left
    pause

    clara "Still. He doesn’t get to just disappear."

    show lia sideways at mid_right

    lia "Clara—"

    clara "He humiliated Cindy and left her to deal with it alone. That’s not okay."

    alex "You gonna talk to him?"

    clara "I’m going to find him."

    show albert troll at right

    albert "Should we prepare a eulogy?"

    clara "Don’t be dramatic."

    hide clara with moveoutleft

    show alex excited at left

    alex "And there she goes. On a warpath of justice."

    show lia neutral at mid_right

    lia "Remind me to never cross her."

    show cindy neutral at center

    cindy "...Thanks, Clara."

    scene black
    with Pause(1)

    scene bg library

    show tanish sad at center

    tanish "(Why do I even come to school anymore... It's like I can't even look anyone in the eye without being reminded of what happened during that awful class again.)"

    tanish "(I'm so embarrassed. I can't believe I did that. I'm such a fool.)"

    show clara angry at left with moveinleft

    clara "I... Found You..."

    tanish "Clara... hey."

    clara "Don’t ‘hey’ me. You’ve been hiding out for days, not responding to anyone, not talking to anyone at school... We've all been wondering what the hell happened with you."

    tanish "I didn’t feel like seeing anyone."

    clara "Well if it wasn’t obvious, you made Cindy cry."

    tanish "...I know."

    clara "You embarrassed her in front of a whole class. What did you expect?"

    tanish "I messed up. I get it."

    clara "Then own it. Go apologize."

    show tanish angry at center

    tanish "I know! I know it's bad, and I'm sorry!"

    clara "Don't apologize to me, I'm not the one who got slapped!"

    tanish "But for real, where should I even start? Do I just go up to her and say \"Hey, I’m sorry I said something weird. I don’t remember what it was, so can you remind me? And if it’s that bad, I promise I’ll never talk to you again so it’s less awkward?\""

    clara "Are you serious right now?"

    clara "Do you even hear yourself, Tanish? You don’t even remember what you said, and somehow you’re still messing this up by acting like she owes you something?"

    clara "You don't sound sorry at all... You sound pathetic..."

    clara "Anyways, I'm going to leave you to it. You decide whether you want to actually apologize or not. But let me be clear, time is running out, and Cindy is still pissed."

    hide clara with moveoutleft

    menu:
        "Apologize to Cindy":
            jump tanish_apologizes
        "Refuse to apologize":
            $Ending3Triggered = True
            jump tanish_refuses

    label tanish_apologizes:

        show tanish neutral at center

        tanish "Okay. You're right."

        tanish "I’ll talk to her tomorrow. I owe her that much."

        show clara neutral at left with moveinleft

        clara "You owe her more, but yeah. Start there."

        tanish "Thanks... for coming to yell at me, I guess."

        clara "Don’t make me do it again."

        return

    label tanish_refuses:

        return