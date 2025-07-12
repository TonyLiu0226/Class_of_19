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

    alex "(Damn can't believe its the end of the year already. I still want to see some of my friends before exams kill me. Maybe I’ll check if Gina’s around...)"

    play sound phone_ping
    alex "{i}hey Gina{/i}"

    scene bg gina_room_night

    show gina neutral at center
    show phone at right

    play sound phone_ping
    gina "{i}hey{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}how’s it going?{/i}"

    scene bg gina_room_night

    show gina neutral at center
    show phone at right

    play sound phone_ping
    gina "{i}busy. school’s kinda killing me lately{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}yeah, fair{/i}"
    
    pause
 
    scene bg gina_room_night

    show gina neutral at center
    show phone at right

    play sound phone_ping
    gina "{i}hey, can I ask something?{/i}"
 
    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}yeah ofc{/i}"
 
    scene bg gina_room_night

    show gina neutral at center
    show phone at right

    play sound phone_ping
    gina "{i}do you... actually like me?{/i}"

    play sound phone_ping
    gina "{i}i’m asking because lately... it feels like you’ve been putting a lot of pressure on me{/i}"

    play sound phone_ping
    gina "{i}being around you is fun, but sometimes it’s like you’re expecting something back{/i}"

    play sound phone_ping
    gina "{i}so i need to know. is this just a crush thing? or do you really like me?{/i}"

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
        alex "{i}i do. i really like you gina{/i}"

        play sound phone_ping
        alex "{i}i wasn’t trying to push you. i guess i just... got excited{/i}"
        
        play sound phone_ping
        alex "{i}you’re smart and chill and funny and yeah i catch myself thinking about you a lot{/i}"

        scene bg gina_room_night

        show gina blush at center
        show phone at right

        show gina blush at center
        gina "(...)"

        play sound phone_ping
        gina "{i}thanks for being honest{/i}"
        
        show gina neutral at center
        play sound phone_ping
        gina "{i}i don’t know if i’m ready for anything right now{/i}"

        play sound phone_ping
        gina "{i}but i’ll think about it. i just need space to figure things out{/i}"

        scene bg alex_room

        show alex neutral at center
        show phone at right

        play sound phone_ping
        alex "{i}yeah. totally. take your time{/i}"

        jump gina_cafe

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

        scene bg gina_room_night

        show gina neutral at center
        show phone at right

        play sound phone_ping
        gina "{i}thanks for saying that{/i}"

        play sound phone_ping
        gina "{i}i just wanted to be honest{/i}"

        play sound phone_ping
        gina "{i}we’re good{/i}"

        jump egbert_park

    label gina_cafe:
        scene black with pixellate
        with Pause(1)

        scene bg cafe

        show gina neutral at center
        show lia happy at right
        show emma blush at left

        lia "You told him?"

        gina "Yeah."

        emma "Finally. That’s been simmering for weeks."

        lia "How’d he take it?"

        show gina blush at center

        gina "Pretty well, actually. He was honest about it. Said he really likes me."

        emma "Did he ask you out?"

        gina "Kinda. But I told him I need time."

        lia "That’s fair. He’s been... kinda obsessed to say the least."

        emma "Yeah, like, sweet... but kind of constantly in orbit around you."

        show gina embarrassed at center

        gina "That’s what I told him. I felt like I was being observed. Texting a lot, chasing me around at lunch or before school, you know."

        show lia neutral at right

        lia "You're not wrong about that. Guy has resting ‘I’m silently in love with you’ face."

        gina "I don’t want to hurt him. He means well."

        emma "You’re not hurting him by telling the truth. You don’t owe anyone a yes."

        gina "I know. But I also don't want to just cut him off, you know?"

        show lia happy at right

        lia "Do you actually like him?"

        show gina neutral at center

        gina "Not gonna lie, I do a little. But I don't know if I'm ready for any commitments. Besides, what you told me the other week about his past... still kinda gives me a bit of a red flag."

        emma "Oh uhh... what?"

        lia "Well, I told her that Alex used to chase around the popular girls in middle school. It kinda got on their nerves, and he basically got told to piss off."

        emma "Oh, I didn't know that about him. But from what Gina is telling us, maybe we're seeing a similar kind of energy build up with Alex hovering over her."

        lia "Yea I guess Alex is a bit awkward, but I’ve seen worse. Remember Ben from our history class?"

        emma "He literally took pics of the substitute teacher's feet and sent them to the whole class."

        show gina blush at center

        gina "Hmm..?"

        show lia neutral at right

        lia "So in hindsight, Alex isn’t that bad. He's got potential."

        gina "That’s what makes this hard. If he was a jerk or a total perv, I could just walk away."

        emma "Take your time. Just don’t ghost him."

        show gina neutral at center

        gina "I won’t. I just needed to talk it out with people who aren’t... him."

        lia "That’s what we’re here for. Also, to remind you to eat something."

        emma "Seriously, go order something."

        show gina happy at center

        gina "I’m thinking!"

        show lia happy at right

        lia "Think with snacks in your mouth, Gina. It's how you stay grounded."

        gina "*sighs* Fine."

    label egbert_park:
        scene black with pixellate
        with Pause(1)

        scene bg park

        show alex neutral at left
        show egbert happy at right

        if Ending6Eligible == False:
            egbert "So? Did you shoot your shot?"
            alex "I did. Told her straight up."
            egbert "And?"
            alex "She said she needs time. I think I overwhelmed her a bit."
            egbert "Honestly? Could’ve been worse. She’s still talking to you, right?"
            alex "Yeah. Just... taking space."
            egbert "Then you're still in the game, my friend."

        else:
            egbert "So? Did you tell her how you feel?"
            alex "Kinda. She asked. But I backed off."
            egbert "Wait, you backed off?"
            alex "Yeah. She said I was pressuring her. I didn't want to make things worse."
            egbert "That’s mature... and also kinda tragic."
            alex "Whatever. I needed to hear it."

        egbert "Anyway, you missed it — Jacob is officially expelled."

        show alex excited at left

        alex "NANI?"

        egbert "And it's deja vu. Chem lab again. Guy literally set Ruby's hair on fire, because of some stupid drama with her friend group or something."

        alex "That man lives for catching chaos."

        egbert "Fire alarm was set off. Again."

        alex "Unreal."

        show egbert troll at right

        egbert "Also, I don't know, but Lia is definitely cheating on him too. Saw her walking with a guy after school yesterday."

        alex "Bruh after what happened, I'm not surprised. As Gina said it, Lia deserves someone with actual brain cells."

        egbert "Cheating on him all of a sudden kinda sounds slutty though not gonna lie."

        alex "Damn. I mean, her outfits though, screams sugar baby to a lot of guys."

        show egbert neutral at right

        egbert "Facts. Anyways, down for some food?"

        show alex neutral at left

        alex "Yep about time. I'm starving."

        egbert "Ok, let's go."

        return
