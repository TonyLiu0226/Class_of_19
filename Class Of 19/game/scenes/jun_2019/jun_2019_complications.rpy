label jun_2019_complications:

    stop music
    scene black
    with Pause(1)

    play music gatsby

    scene bg alex_room

    show alex neutral at center

    alex "(Everyone’s buried in finals...)"

    alex "(I just feel like I’m floating through all this alone.)"

    alex "(But Clara and I are still friends, right?)"

    alex "(It’s not weird to check in.)"

    show phone at right

    play sound phone_ping
    alex "{i}hey clara, want to study together sometime this week?{/i}"

    play sound phone_ping
    alex "{i}we could invite the others too{/i}"

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}hey, sorry. i’m swamped with chem right now{/i}"

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}ah yeah i get it. gl on it{/i}"

    alex "(...Maybe I’ll try again tomorrow.)"

    scene black
    show text "The Next Day" with dissolve
    with Pause(1)

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}yo i finally got back into PUBG. still cracked at sniping{/i}"

    scene black
    show text "A few hours later" with dissolve
    with Pause(1)

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}lol nice{/i}"

    scene black
    show text "The next day" with dissolve
    with Pause(1)

    scene bg alex_room

    show alex neutral at center
    show phone at right

    play sound phone_ping
    alex "{i}found this anime called 'Seraph’s Echo'{/i}"

    play sound phone_ping
    alex "{i}kinda your vibe. soft drama, gorgeous animation{/i}"

    scene black
    show text "18 hours later" with dissolve
    with Pause(1)

    scene bg clara_room_night

    show clara neutral at center
    show phone at right

    play sound phone_ping
    clara "{i}cool{/i}"

    scene bg alex_room

    show alex sad at center
    show phone at right

    pause

    alex "(Okay... something’s off.)"

    play sound phone_ping
    alex "{i}remember this? lol{/i}"
    play sound phone_ping
    alex "\[attaches cringy meme here\]"

    scene black
    show text "Literally after like forever..." with dissolve
    with Pause(1)

    scene bg clara_room_night

    show clara angry at center
    show phone at right

    play sound phone_ping
    clara "{i}lmao{/i}"

    scene bg alex_room

    show alex sad at center
    alex "(...)"

    alex "(I just need to stop.)"

    alex "(Maybe I just need to talk this out with someone who isn't her.)"

    show phone at right
    play sound dial
    $renpy.pause(6.0, hard=True)
    albert "Yo yo. What’s up?"

    alex "Hey. Can I vent for a second?"

    albert "Always. What’s going on?"

    alex "Clara’s going cold. Like, she still responds, but it’s robotic. It feels like she’s pulling away."

    albert "Yeah... that’s rough."

    alex "I don’t know if I should say something or just... wait it out."

    albert "Honestly? Wait it out."

    alex "What?"

    albert "Dude, it’s finals. Everyone’s stressed. You don’t want to be that guy blowing up her notifications when she’s trying to cram for chem."

    alex "...So just do nothing?"

    albert "Give it space. Let her miss you, if she will. If not, summer’s around the corner. New energy. New people. Focus on your grind."

    alex "Hmm..."

    albert "Trust me. Chasing too hard just makes it worse."

    pause

    alex "(...Maybe.)"

    alex "(Let's talk to Tanish. Haven't heard from him in a while.)"

    play sound dial
    $renpy.pause(6.0, hard=True)

    scene bg tanish_room_night

    show tanish neutral at center
    show phone at right

    tanish "Alex? What’s up?"

    alex "Clara."

    tanish "...Oof. Yeah."

    alex "I don’t know what to do. She’s still replying, but it’s like... one-word replies, huge delays. I feel like I’m clinging to something that’s slipping."

    tanish "Man, I’ve been there."

    alex "With Cindy?"

    tanish "Yeah. Back when I said that dumb line during the Gatsby screening? Things tanked after that. I thought it was over."

    alex "I remember. You disappeared for like a week."

    tanish "I didn’t know how to talk to her without making it worse. But eventually I did. I apologized. I explained myself. I gave her space — but I also gave her clarity."

    alex "So you think I should reach out?"

    tanish "If you care, yeah. Don’t ghost her out of pride. And don’t keep throwing half-hearted texts either."

    alex "But what if it makes her more uncomfortable?"

    tanish "Then let her say that. But let it be clear. Like... tell her how you feel, and ask her straight if she still wants to keep talking."

    alex "It feels scary."

    tanish "So is guessing forever. At least this way, it’s honest. That’s what worked with Cindy. Even if it was awkward."

    alex "And if it doesn’t work?"

    tanish "Then at least you gave it a shot. You won’t be stuck wondering ‘what if’ all summer."

    pause

    scene bg alex_room

    show alex neutral at center
    show phone at right
    alex "(Albert says wait it out. Tanish says be honest.)"

    alex "(I don’t know what’s right anymore.)"

    alex "(Maybe I'll go on a bike ride tomorrow to clear my head.)"

    scene black
    with Pause(1)

    scene bg park

    show alex bike at center

    alex "(Just a quick bike ride. Breathe. Think.)"

    alex "(...)"

    alex "(Wait... isn’t this close to where Clara lives?)"

    # Player choice

    menu:
        "Bike to Clara’s house":
            $ AlexBikedToClara = True
            jump alex_bikes_to_clara
        "Let it go and go home":
            jump alex_goes_home

    label alex_bikes_to_clara:

        stop music
        play music theme
        alex "(...I just want to talk.)"

        alex "(Maybe... just maybe, she'll understand.)"

        return

    label alex_goes_home:

        alex "(...No. This isn’t right.)"

        alex "(I need to give her space. Pushing more won’t fix anything.)"

        alex "(Just go back home and study, man.)"

        return
