label jun_2019_bike:

    scene black with pixellate

    $renpy.pause(1.5, hard=True)

    scene bg gina_street

    show alex bike at center

    alex "(Okay. Just... breathe.)"

    alex "(No door-knocking. No weird ambush. I’ll call her first.)"

    show phone at right

    play sound dial
    $renpy.pause(6.0, hard=True)

    scene bg gina_room_day

    show gina neutral at center

    gina "(Huh?)"

    gina "(Is that... Alex?)"

    gina "(Why is he in my neighborhood?)"

    show gina angry at center

    gina "(No way. Please don’t tell me...)"

    play sound ring
    gina "(He’s calling me. Of course.)"

    scene bg gina_street
    show alex bike at left
    show phone at center

    gina "Are you serious? You’re across the street?!"

    alex "I didn’t want to just show up and ring your doorbell. I thought calling would be better."

    gina "Alex—this is not cool. This is exactly what I was afraid of."

    alex "I know. I messed up. I didn’t mean to come off like a stalker or anything, I just—"

    gina "Bruh"

    alex "I didn’t know how else to say it. Things felt off. You were going cold, and I didn’t know if I should back off or say something."

    pause

    gina "Look... I get it. I’ve been distant. Finals, family stuff... and yeah, I was unsure about you."

    gina "But this? This is the behavior I was afraid of especially when others have mentioned your past tendencies in middle school."

    alex "...Yeah. I know."

    gina "But I also know you’re not Bobby. You actually bothered to call and commnuicate your feelings."

    alex "I didn’t want to make things worse. I just wanted to understand where we stand."

    gina "Then let’s talk."

    $renpy.pause(0.5, hard=True)
    scene bg 108_day

    show gina neutral at right
    show alex neutral at left

    gina "It’s not that I hate you. I don’t."

    alex "That’s... a relief."

    gina "But I’ve felt boxed in. Like if I didn’t reply to a message, I was a villain."

    alex "I wasn’t trying to pressure you."

    gina "I know. But pressure doesn't always need intent. It’s about how it lands."

    alex "Then what now?"

    gina "We take space. But we stay honest. No assumptions. No ghosting. No more unnecessary bike trips."

    alex "Fair."

    pause

    gina "Anyways, thanks for calling first."

    alex "Thanks for hearing me out."

    gina "How is studying for physics going?"

    show alex excited at left

    alex "Oh god... When Qwen told the class what was going to be on the final, everyone groaned. And I don't think I'm ready at all."

    gina "Lia told me she’s not even believing him in the slightest, because Qwen knows he can't make the whole class fail."

    alex "Honestly... That's a good way of looking at it."

    show gina happy at right

    gina "But... If you fail, I’m not tutoring you again."

    alex "You say that every time."

    gina "And every time you end up sending me blurry pics of your worksheet at 11PM."

    alex "Guilty."

    show gina neutral at right

    gina "Alright. You should head home."

    show alex neutral at left

    alex "Yeah... good luck with the studying."

    gina "You too."

    hide alex with moveoutleft

    $renpy.pause(1.5, hard=True)

    show gina neutral at left with move
    show albert happy at right with moveinright

    albert "Was that Alex you were talking to?"

    show gina blush at left

    gina "Umm... were you spying on us the whole time?"

    show albert troll at right

    albert "Totally wasn't. Anyways, everything good?"

    show gina embarrassed at center with move

    gina "Define \"good.\""

    show albert neutral at left with move
    albert "What happened?"

    gina "He biked to my house. Called me from across the street."

    albert "Bold."

    gina "Desperate, more like."

    albert "Did you send him packing?"

    show gina neutral at center

    gina "We talked. It wasn’t as bad as I thought it would be."

    albert "So...?"

    gina "So, we’re still figuring it out. But at least we’re doing it like people, not a CW drama."

    albert "Proud of you."

    gina "Shut up and let's grab some ice cream. I'm craving it."

    hide gina with moveoutright
    hide albert with moveoutright

    return
