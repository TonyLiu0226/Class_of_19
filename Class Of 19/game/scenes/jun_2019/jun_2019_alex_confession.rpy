label jun_2019_alex_confession:

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

    play music chiggajockey

    scene bg alex_room

    show alex neutral at center
    show phone at right

    alex "(Damn can't believe its the end of the year already. I still want to see some of my friends before exams kill me. Maybe I’ll check if Clara’s around...)"

    play sound phone_ping
    alex "{i}hey clara{/i}"

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}hey{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}how’s it going?{/i}"

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}busy. school’s kinda killing me lately{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}yeah, fair{/i}"
    
    pause
 
    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}hey, can I ask something?{/i}"
 
    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}yeah ofc{/i}"
 
    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}do you... actually like me?{/i}"

    play sound phone_ping
    clara "{i}i’m asking because lately... it feels like you’ve been putting a lot of pressure on me{/i}"

    play sound phone_ping
    clara "{i}being around you is fun, but sometimes it’s like you’re expecting something back{/i}"

    play sound phone_ping
    clara "{i}so i need to know. is this just a crush thing? or do you really like me?{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    menu:
        "Confess honestly":
            $Ending6Eligible = False
            jump alex_confess_real
        "Back off":
            jump alex_back_off

    label alex_confess_real:
 
        show alex blush at center
        play sound phone_ping
        alex "{i}i do. i really like you clara{/i}"

        play sound phone_ping
        alex "{i}i wasn’t trying to push you. i guess i just... got excited{/i}"
        
        play sound phone_ping
        alex "{i}you’re smart and chill and funny and yeah i catch myself thinking about you a lot{/i}"

        scene bg clara_room_night

        show clara blush at center
        show phone at right

        show clara blush at center
        clara "(...)"

        play sound phone_ping
        clara "{i}thanks for being honest{/i}"
        
        show clara neutral at center
        play sound phone_ping
        clara "{i}i don’t know if i’m ready for anything right now{/i}"

        play sound phone_ping
        clara "{i}but i’ll think about it. i just need space to figure things out{/i}"

        scene bg alex_room

        show alex neutral at center
        show phone at right

        play sound phone_ping
        alex "{i}yeah. totally. take your time{/i}"

        jump clara_cafe

    # ──────────────────────
    # Back off branch
    # ──────────────────────

    label alex_back_off:
        play sound phone_ping
        alex "{i}i’m sorry{/i}"
        play sound phone_ping
        alex "{i}i didn’t mean to make you feel pressured{/i}"
        play sound phone_ping
        alex "{i}i like hanging out with you, that’s all{/i}"
        play sound phone_ping
        alex "{i}i’ll back off if it’s too much{/i}"

        scene bg clara_room_night

        show clara neutral at center
        show phone at right

        play sound phone_ping
        clara "{i}thanks for saying that{/i}"

        play sound phone_ping
        clara "{i}i just wanted to be honest{/i}"

        play sound phone_ping
        clara "{i}we’re good{/i}"

        jump albert_park

    label clara_cafe:
        scene black with pixellate
        with Pause(1)

        scene bg cafe

        show clara neutral at center
        show lia happy at right
        show nicole blush at left

        lia "You told him?"

        clara "Yeah."

        nicole "Finally. That’s been simmering for weeks."

        lia "How’d he take it?"

        show clara blush at center

        clara "Pretty well, actually. He was honest about it. Said he really likes me."

        nicole "Did he ask you out?"

        clara "Kinda. But I told him I need time."

        lia "That’s fair. He’s been... kinda obsessed to say the least."

        nicole "Yeah, like, sweet... but kind of constantly in orbit around you."

        show clara embarrassed at center

        clara "That’s what I told him. I felt like I was being observed. Texting a lot, chasing me around at lunch or before school, you know."

        show lia neutral at right

        lia "You're not wrong about that. Guy has resting ‘I’m silently in love with you’ face."

        clara "I don’t want to hurt him. He means well."

        nicole "You’re not hurting him by telling the truth. You don’t owe anyone a yes."

        clara "I know. But I also don't want to just cut him off, you know?"

        show lia happy at right

        lia "Do you actually like him?"

        show clara neutral at center

        clara "Not gonna lie, I do a little. But I don't know if I'm ready for any commitments. Besides, what you told me the other week about his past... still kinda gives me a bit of a red flag."

        nicole "Oh uhh... what?"

        lia "Well, I told her that Alex used to chase around the popular girls in middle school. It kinda got on their nerves, and he basically got told to piss off."

        nicole "Oh, I didn't know that about him. But from what Clara is telling us, maybe we're seeing a similar kind of energy build up with Alex hovering over her."

        lia "Yea I guess Alex is a bit awkward, but I’ve seen worse. Remember Ben from our history class?"

        nicole "He literally took pics of the substitute teacher's feet and sent them to the whole class."

        show clara blush at center

        clara "Hmm..?"

        show lia neutral at right

        lia "So in hindsight, Alex isn’t that bad. He's got potential."

        clara "That’s what makes this hard. If he was a jerk or a total perv, I could just walk away."

        nicole "Take your time. Just don’t ghost him."

        show clara neutral at center

        clara "I won’t. I just needed to talk it out with people who aren’t... him."

        lia "That’s what we’re here for. Also, to remind you to eat something."

        nicole "Seriously, go order something."

        show clara happy at center

        clara "I’m thinking!"

        show lia happy at right

        lia "Think with snacks in your mouth, Clara. It's how you stay grounded."

        clara "*sighs* Fine."

    label albert_park:
        scene black with pixellate
        with Pause(1)

        scene bg park

        show alex neutral at left
        show albert happy at right

        if Ending6Eligible == False:
            albert "So? Did you shoot your shot?"
            alex "I did. Told her straight up."
            albert "And?"
            alex "She said she needs time. I think I overwhelmed her a bit."
            albert "Honestly? Could’ve been worse. She’s still talking to you, right?"
            alex "Yeah. Just... taking space."
            albert "Then you're still in the game, my friend."

        else:
            albert "So? Did you tell her how you feel?"
            alex "Kinda. She asked. But I backed off."
            albert "Wait, you backed off?"
            alex "Yeah. She said I was pressuring her. I didn't want to make things worse."
            albert "That’s mature... and also kinda tragic."
            alex "Whatever. I needed to hear it."

        albert "Anyway, you missed it — Jacob is officially expelled."

        show alex excited at left

        alex "NANI?"

        albert "And it's deja vu. Chem lab again. Guy literally set Ruby's hair on fire, because of some stupid drama with her friend group or something."

        alex "That man lives for catching chaos."

        albert "Fire alarm was set off. Again."

        alex "Unreal."

        show albert troll at right

        albert "Also, I don't know, but Lia is definitely cheating on him too. Saw her walking with a guy after school yesterday."

        alex "Bruh after what happened, I'm not surprised. As Clara said it, Lia deserves someone with actual brain cells."

        albert "Cheating on him all of a sudden kinda sounds slutty though not gonna lie."

        alex "Damn. I mean, her outfits though, screams sugar baby to a lot of guys."

        show albert neutral at right

        albert "Facts. Anyways, down for some food?"

        show alex neutral at left

        alex "Yep about time. I'm starving."

        albert "Ok, let's go."

        return
