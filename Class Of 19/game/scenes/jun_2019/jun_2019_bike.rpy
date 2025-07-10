label jun_2019_bike:

    scene black with pixellate

    $renpy.pause(1.5, hard=True)

    scene bg clara_street

    show alex bike at center

    alex "(Okay. Just... breathe.)"

    alex "(No door-knocking. No weird ambush. I’ll call her first.)"

    show phone at right

    play sound dial
    $renpy.pause(6.0, hard=True)

    scene bg clara_room_day

    show clara neutral at center

    clara "(Huh?)"

    clara "(Is that... Alex?)"

    clara "(Why is he in my neighborhood?)"

    show clara angry at center

    clara "(No way. Please don’t tell me...)"

    play sound ring
    clara "(He’s calling me. Of course.)"

    scene bg clara_street
    show alex bike at left
    show phone at center

    clara "Are you serious? You’re across the street?!"

    alex "I didn’t want to just show up and ring your doorbell. I thought calling would be better."

    clara "Alex—this is not cool. This is exactly what I was afraid of."

    alex "I know. I messed up. I didn’t mean to come off like a stalker or anything, I just—"

    clara "Bruh"

    alex "I didn’t know how else to say it. Things felt off. You were going cold, and I didn’t know if I should back off or say something."

    pause

    clara "Look... I get it. I’ve been distant. Finals, family stuff... and yeah, I was unsure about you."

    clara "But this? This is the behavior I was afraid of especially when others have mentioned your past tendencies in middle school."

    alex "...Yeah. I know."

    clara "But I also know you’re not Bobby. You actually bothered to call and commnuicate your feelings."

    alex "I didn’t want to make things worse. I just wanted to understand where we stand."

    clara "Then let’s talk."

    $renpy.pause(0.5, hard=True)
    scene bg 108_day

    show clara neutral at right
    show alex neutral at left

    clara "It’s not that I hate you. I don’t."

    alex "That’s... a relief."

    clara "But I’ve felt boxed in. Like if I didn’t reply to a message, I was a villain."

    alex "I wasn’t trying to pressure you."

    clara "I know. But pressure doesn't always need intent. It’s about how it lands."

    alex "Then what now?"

    clara "We take space. But we stay honest. No assumptions. No ghosting. No more unnecessary bike trips."

    alex "Fair."

    pause

    clara "Anyways, thanks for calling first."

    alex "Thanks for hearing me out."

    clara "How is studying for physics going?"

    show alex excited at left

    alex "Oh god... When Manias told the class what was going to be on the final, everyone groaned. And I don't think I'm ready at all."

    clara "Lia told me she’s not even believing him in the slightest, because Manias knows he can't make the whole class fail."

    alex "Honestly... That's a good way of looking at it."

    show clara happy at right

    clara "But... If you fail, I’m not tutoring you again."

    alex "You say that every time."

    clara "And every time you end up sending me blurry pics of your worksheet at 11PM."

    alex "Guilty."

    show clara neutral at right

    clara "Alright. You should head home."

    show alex neutral at left

    alex "Yeah... good luck with the studying."

    clara "You too."

    hide alex with moveoutleft

    $renpy.pause(1.5, hard=True)

    show clara neutral at left with move
    show albert happy at right with moveinright

    albert "Was that Alex you were talking to?"

    show clara blush at left

    clara "Umm... were you spying on us the whole time?"

    show albert troll at right

    albert "Totally wasn't. Anyways, everything good?"

    show clara embarrassed at center with move

    clara "Define \"good.\""

    show albert neutral at left with move
    albert "What happened?"

    clara "He biked to my house. Called me from across the street."

    albert "Bold."

    clara "Desperate, more like."

    albert "Did you send him packing?"

    show clara neutral at center

    clara "We talked. It wasn’t as bad as I thought it would be."

    albert "So...?"

    clara "So, we’re still figuring it out. But at least we’re doing it like people, not a CW drama."

    albert "Proud of you."

    clara "Shut up and let's grab some ice cream. I'm craving it."

    hide clara with moveoutright
    hide albert with moveoutright

    return
