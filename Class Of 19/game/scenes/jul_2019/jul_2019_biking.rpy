label jul_2019_biking:

    stop music
    scene black
    show text "Meanwhile..." with dissolve
    $renpy.pause(1.5, hard=True)

    play music turtle

    scene bg cafe

    show alex neutral at left
    show albert happy at right

    albert "Man, this burger is actually insane."

    alex "Yeah, it's good."

    albert "You’ve barely touched yours."

    alex "Just... not that hungry."

    albert "Still Clara?"

    alex "Still Clara."

    pause

    show albert troll at right

    albert "So... what happened at Clara's house on June 24th?"

    show alex excited at left
    alex "Bruh... how did you know?"

    albert "Of course I know. Don't ask how."

    show alex neutral at left
    alex "But we talked for a bit. She was upset at first, but it didn’t explode. She said we should take space. Be honest."

    show albert happy at right

    albert "Dude. That's not even bad. Sounds like you handled it."

    alex "I guess. But after that? Nothing. No messages. Total silence."

    albert "You think she meant it when she said you could stay friends?"

    alex "I don’t know anymore. Every time I try to say something chill, it feels like I’m just annoying her."

    pause

    albert "Okay, but like... finals are over now. The pressure’s gone."

    alex "Yeah?"

    albert "Yeah. So maybe this is the perfect time to talk again. For real. In person."

    alex "You mean go back to her house?"

    show albert troll at right

    albert "Why not? No school stress. No deadlines. Just show up, be calm, and straighten things out."

    alex "...I don’t know, man."

    albert "What do you mean?"

    alex "The first time I went to her place, she was already weirded out. I saw it in her face. She literally asked me why I was there. I almost felt she was about to call the cops on me."

    albert "But you didn’t do anything wrong. You called her first, remember?"

    alex "I know. But still — I feel like if I do it again, it’ll just make things worse."

    alex "(But what if I’m overthinking it?)"

    alex "(What if this is the last chance I get to actually fix things?)"

    show albert happy at right

    albert "Look. If she really didn't want to talk to you, she would’ve blocked you already. She didn't. That’s something."

    albert "Sometimes people just need a little push. Don’t let fear talk you out of doing what might actually fix things."

    alex "I know, but... I just don't want to mess things up again."

    albert "Bruh... just do what you feel is right. Worst that can happen is she'll be mad at you, and you'll be able to move on."

    alex "(I need to decide on this soon...)"

    pause
    menu:
        "Bike to Clara's house":
            $Ending1Triggered = True
            jump alex_bikes_to_clara_postfinals
            
        "Leave it alone":
            return

    label alex_bikes_to_clara_postfinals:

        stop music
        play music theme

        scene bg 108_night

        show alex neutral at center

        alex "(Okay. Just be calm. She might not even be home. Just talk. That's all I want.)"

        alex "(I'll give her a call, I guess.)"

        pause

        alex "(Here goes nothing...)"

        alex "(Let me just grab my phone—)"

        stop music
        play music sirens

        pause

        alex "(...What the?)"

        show cop at left with moveinleft

        cop "HANDS UP WHERE I CAN SEE THEM, NOW!"

        show alex sad at center

        alex "Wait, what—? I live down the street! I’m just here to—"

        cop "PUT YOUR HANDS BEHIND YOUR BACK!"

        alex "I wasn’t— I was just gonna call her—"

        cop "NOW!!!"

        show cop at mid_left with move

        play sound handcuffs

        cop "You’re under arrest for trespassing. You have the right to remain silent, but anything you say can and will be used against you in a court of law."

        pause

        alex "(...This can’t be happening.)"

        scene black

        return
