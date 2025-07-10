label jul_2019_aftermath:

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

    screen countdown2:
        timer 0.1 repeat True action If(time2 > 0, true=SetVariable('time2', time2 - 0.1), false=[Hide('countdown2'), Jump(timer_jump2)])
        bar value time2 range timer_range2 xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

    scene black with pixellate
    $renpy.pause(1.0, hard=True)

    scene bg bobby_room_night

    show bobby neutral at center

    play music ring

    $ time = 3.0
    $ timer_range = 3.0
    $ timer_jump = 'menus'

    show screen countdown

    bobby "(Ugh... someone's calling me this late?)"

    label menus:

    hide screen countdown

    $ time2 = 5.0
    $ timer_range2 = 5.0
    $ timer_jump2 = 'bobby_dont_answer_alex'

    show screen countdown2

    menu:
        "Pick up the phone":
            hide screen countdown2
            jump bobby_answers_alex
        "Don't pick up" if time2 > 0:
            hide screen countdown2
            jump bobby_dont_answer_alex

    label bobby_answers_alex:

    stop music
    play music floater

    show phone at right

    bobby "(Hello?)"

    alex "Bobby... it’s me."

    bobby "Bruh What's up?"

    alex "She blocked me."

    bobby "...Gina?"

    alex "Yeah. Discord. Text. Everything. I was just casually checking discord and saw 'Unknown User'... and then I checked my texts..."

    bobby "Bruh."

    alex "I didn’t even do anything. I didn’t even go to her house this time."

    bobby "Wait — this time?"

    alex "No, I mean... I *thought* about it. But I didn’t. I really didn’t."

    bobby "Okay chill out bro. Just tell me what happened."

    pause

    alex "I was feeling low, right? I just wanted to talk to someone, especially during and after finals. I messaged her a few times — light stuff, nothing weird."

    alex "She replied... but slower. Less and less. I felt it. So I asked Albert what I should do."

    bobby "Well I know he said to give her some space, but guess you didn't take that advice on that day."

    alex "Yep so I biked to her house a couple weeks back. We talked for a bit, she said she wasn't mad at me but needed some space, and from then on I gave it to her."

    alex "Nothing happened for the rest of finals season. I was thinking everything was in the clear and I can talk to her again."

    bobby "So why didn't you just text her?"

    alex "I wasn't sure. Should I still give her space and wait for her to come to me? Or should I be more proactive? I went to Albert for advice, and boy did his advice change."

    bobby "So this man now decides to tell you to bike to her house? What a goddamn troll."

    alex "Yeah. I ended up not taking his advice again and just left her alone. But now I just end up getting blocked."

    bobby "I'm not sure what was going on in her head. Why did she block you after you guys talked it out if nothing happened afterwards?"

    alex "Exactly. I’m sitting here wondering if doing nothing just made her decide I wasn’t worth the effort."

    pause

    bobby "Nah, man. In all honesty you did the right thing by not going. Seriously."

    bobby "You respected her space, and that matters. But blocking you... that’s on her. Not you."

    alex "Still hurts."

    if BobbyCindyBreakup:

        bobby "I get that. Trust me, I’ve been there."

        alex "Yeah... with Cindy?"

        bobby "Yeah. When that all fell apart, I kept second guessing everything. But sometimes... people just move on."

    pause

    alex "So what do I do now?"

    bobby "Honestly? Let it all go. Take the L, learn from it... and then start figuring out who *you* want to be next."

    pause 1.0

    alex "...Thanks, man."

    bobby "Anyways let's grind some CSGO to get your mind off it, I gotta get some of those juicy cases to sell on the marketplace."

    alex "Lol sure let's go."

    stop music

    return

label bobby_dont_answer_alex:
    $Ending2Triggered = True
    stop music

    scene black with pixellate
    $renpy.pause(1.0, hard=True)

    return