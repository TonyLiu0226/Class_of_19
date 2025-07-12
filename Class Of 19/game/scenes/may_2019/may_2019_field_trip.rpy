label may_2019_field_trip:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "May 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music turtle

    scene bg theme_park

    show qwen neutral at right
    show egbert neutral at left
    show alex neutral at middle_left
    show bobby neutral at mid_left
    show gina neutral at mid_right
    show lia neutral at middle_right

    qwen "Alright people, welcome to the physics field trip. I know you’re all thrilled to be here instead of in a windowless classroom doing actual work."

    qwen "But don’t get too comfortable—this is still a graded assignment. You’ll be filling out your kinematics and dynamics worksheets using real rides."

    qwen "Measure acceleration, force, time of motion... you know the drill."

    qwen "You need data from at least two different rides. Roller coasters, drop towers, anything that makes your stomach leave your body."

    qwen "Once you’re done, you’re free to enjoy the park—but remember, I want actual numbers, not napkin scribbles from the cotton candy stand."

    hide qwen with moveoutright
    hide egbert with moveoutleft
    hide gina with moveoutleft
    hide lia with moveoutleft

    show bobby neutral at left with move
    show alex neutral at right with move

    bobby "Yo you wanna team up for this?"

    alex "For sho, chigga"

    show bobby left at left

    bobby "Bruh you high or something? You don't sound right"

    show alex excited at right

    alex "Nah its all gucci, lets just get this little fucker over with"

    # Alex and Bobby working on data

    scene black
    with Pause(2)
    scene bg drop_tower

    show alex neutral at middle_left
    show bobby neutral at middle_right

    bobby "Okay... stopwatch ready. You’re counting the seconds when the ride drops."

    alex "KK. Just say when."

    bobby "Three... two... one... go!"

    pause

    bobby "And... stop."

    alex "3.4 seconds."

    bobby "Height is what—about 30 meters?"

    alex "That’s what the sign says."

    bobby "Okay... then acceleration is..."

    alex "Bruh did you forget the formula chigga?"

    bobby "It’s not forgetting. It’s... selectively outsourcing."

    alex "a = 2 * d / t². You’re welcome."

    bobby "You’d make a great calculator with a bad attitude."

    alex "And you’d make a decent partner if you didn't treat this dumbass worksheet like a game show."

    bobby "Coming up next: Two dumb teens miscalculate gravity!"

    alex "We’re doing science, not stand-up."

    bobby "You say that, but this worksheet is comedy gold."

    scene black
    with Pause(2)
    scene bg theme_park

    show bobby happy at right
    show alex excited at left

    bobby "Alright, that’s the worksheet done. Qwen should give us full marks just for riding that death coaster twice."

    alex "Agreed. E-MOTIONAL - - DAMAGE."

    show bobby neutral at right

    bobby "Anyway, I gotta dip early — parents are picking me up at the gate."

    alex "All good. Catch you tomorrow?"

    bobby "Unless I’m still recovering from that loop."

    hide bobby with moveoutright

    # Alex alone at the park entrance

    show alex neutral at center with move
    pause

    alex "Alright... time to head out."

    alex "...Wait."

    alex "Is that Gina I see over in the distance?"


    menu:
        "Approach her":
            jump approach_gina
        "Don’t approach her":
            return

    label approach_gina:

    stop music
    play music bunny

    alex "..."

    alex "Alright. Let’s go say hi."

    show gina happy at left with moveinleft

    alex "Hey."

    gina "Oh—hey. Weren’t you heading out?"

    alex "I was. Then I saw you standing here looking like you were waiting for a philosophical moment."

    gina "More like catching my breath after some of those rides."

    alex "The loop-de-loop one almost separated my soul from my body."

    gina "That’s physics for ya."

    alex "So... not heading back with anyone?"

    gina "Nah. Lia ditched me for Egbert’s chaos squad. I was just gonna walk home."

    show alex blush at center
    alex "Same. You wanna walk together?"

    gina "Sure. Lead the way, stopwatch boy."

    scene black
    with Pause(2)

    scene bg park

    show alex excited at left
    show gina happy at right

    alex "This place gets so quiet sometimes."

    gina "Right? I like walking here in the morning to school, or late at night to destress after a long day."

    alex "You ever bring homework here or just vibes?"

    gina "Homework kills the vibes."

    alex "Good answer."

    pause

    gina "So... doing anything this weekend?"

    alex "Might study. Might not. What about you?"

    gina "Not sure. Might meet up with Lia. Or just draw."

    alex "If you’re down for something low effort, we could hang out."

    gina "Low effort is my love language. I’d be down."

    scene black
    with Pause(2)
    scene bg alex_house

    show alex neutral at left
    show gina neutral at right

    alex "Well... this is me."

    gina "Cute place. I’m guessing there’s at least one anime poster inside."

    show alex blush at left
    alex "That’s classified."

    gina "Uhh, do you keep secrets from everyone, or just TA girls?"


    show alex neutral at left
    alex "Depends. Wanna meet the rabbit I trust with everything?"

    show gina happy at right
    gina "There’s a rabbit involved?"

    alex "Wait here."

    hide alex with moveoutleft

    pause

    show alex excited at left with moveinleft
    show bunny at center with moveinleft
    alex "Okay. Meet Bunny."

    show gina neutral at right
    gina "..."

    gina "You named your bunny... Bunny."

    alex "Listen, it’s minimalist."

    show gina blush at right
    gina "Yo its not even minilalist. It's anti-lore..."

    gina "Zero Creativity. Maximal Chaos. Like calling your future child \"Child\" or a dog \"Dog\"."

    alex "She responds to it. Sometimes."

    gina "Wow. Such a deep bond I guess."

    alex "Go ahead. You can pet her if she doesn’t run."

    show gina neutral at right
    gina "I swear if she bites me..."

    pause

    show gina happy at right
    gina "Okay, fine. She’s adorable."

    alex "Told you."

    gina "Still judging you for the name, though."

    show alex neutral at left
    alex "As expected."

    gina "You and Bobby should really co-author a book called \"Naming Things Is Hard: A Journey into Functional Nihilism\""

    alex "Why?"

    gina "Didn't Bobby name a bunch of files \'.png? Basically the same energy as you naming your bunny \"Bunny\"."

    show alex blush at left
    alex "Oh, of course Bobby... He'd definitely be the type to do that."

    show gina neutral at right
    gina "Anyways, gotta get going. Thanks for the walk though. And the bunny interaction."

    alex "Thanks for tolerating my animal naming skills."

    gina "See you at school?"

    alex "Definitely."

    gina "Cool. Bye, Alex."

    alex "Bye, Gina."

    scene black
    with Pause(2)

    scene bg 108_day

    show gina neutral at right

    gina "..."

    gina "Okay, that was... unexpectedly nice."

    gina "And he seriously named his bunny 'Bunny.' I still can't believe that."

    # Gina reaches her doorstep, sees Lia waiting

    show lia neutral at left with moveinleft

    pause

    gina "Wait—Lia?"

    lia "Hey."

    gina "What are you doing here?"

    lia "I felt bad about ditching you earlier. So... I came to offer peace snacks."

    show gina sideways at right

    gina "Did you actually bring snacks or are you lying again?"

    show lia blush at left

    lia "Emotionally, yes. Spiritually, I brought chips."

    gina "That’ll do."

    lia "Sooo. I saw you walking with Alex on the way home...?"

    show gina embarrassed at right
    gina "...Yeah."

    lia "You two looked... cozy."

    gina "We just talked. Walked home. That’s it."

    lia "Uh huh."

    gina "Okay, fine. It was nice."

    show lia neutral at left

    lia "He's not awful. But can I be real for a sec?"

    show gina neutral at right
    gina "Always."

    lia "You remember at lunch a couple weeks ago? He was acting kind of weird."

    gina "Weird how?"

    lia "Like... super quiet, staring at everyone but not really talking. Gave me ‘trying to analyze the table dynamic’ vibes."

    gina "Maybe he was just nervous?"

    lia "Maybe. But also during the physics study group — he was definitely staring at you while you were explaining stuff."

    gina "...Oh."

    lia "And I’m not trying to be petty, but in middle school? He used to follow some of the popular girls around a little too often."

    gina "Seriously?"

    lia "Yeah. Like, not 'call-the-counselor' level, but definitely hovering. Whispery hallway kid energy."

    gina "...Damn."

    pause

    lia "Look, I’m not saying he’s a red flag bouquet or anything. Just... don’t rush into trusting the vibe too quick. Also don't shut him out, he might actually be figuring things out."

    gina "Got it. Yeah I guess, he chases me around a bit. But not in an annoying way. He's definitely not as try-hard as Bobby."

    lia "Bobby...?"

    gina "Yeah, that guy called me \"babe\" like the week we met"

    lia "Screams pretty try-hard to me."

    gina "Exactly. Bobby is all try-hard energy. Like he’s performing. Alex is... quieter. More himself."

    show lia blush at left

    lia "Hmm okay... Well let me know if you need me to start planning the wedding"

    show gina blush at right

    gina "Liaaaaa, noooo, its not anything like that yet"

    lia "Too late. I already picked the bunny as ring bearer."

    gina "You're actually insane."

    lia "Only for you."

    gina "Okay for real though, next time, don’t ditch me."

    lia "Deal."
    
    return
