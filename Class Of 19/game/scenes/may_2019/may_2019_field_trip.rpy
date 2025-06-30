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

    play music themepark

    scene bg theme_park

    show manias neutral at right
    show albert neutral at left
    show alex neutral at middle_left
    show tanish neutral at mid_left
    show clara neutral at mid_right
    show lia neutral at middle_right

    manias "Alright people, welcome to the physics field trip. I know you’re all thrilled to be here instead of in a windowless classroom doing actual work."

    manias "But don’t get too comfortable—this is still a graded assignment. You’ll be filling out your kinematics and dynamics worksheets using real rides."

    manias "Measure acceleration, force, time of motion... you know the drill."

    manias "You need data from at least two different rides. Roller coasters, drop towers, anything that makes your stomach leave your body."

    manias "Once you’re done, you’re free to enjoy the park—but remember, I want actual numbers, not napkin scribbles from the cotton candy stand."

    hide manias with moveoutright
    hide albert with moveoutleft
    hide clara with moveoutleft
    hide lia with moveoutleft

    show tanish neutral at left with move
    show alex neutral at right with move

    tanish "Yo you wanna team up for this?"

    alex "For sho, chigga"

    show tanish left at left

    tanish "Bruh you high or something? You don't sound right"

    show alex excited at right

    alex "Nah its all gucci, lets just get this little fucker over with"

    # Alex and Tanish working on data

    scene black
    with Pause(2)
    scene bg drop_tower

    show alex neutral at middle_left
    show tanish neutral at middle_right

    tanish "Okay... stopwatch ready. You’re counting the seconds when the ride drops."

    alex "KK. Just say when."

    tanish "Three... two... one... go!"

    pause

    tanish "And... stop."

    alex "3.4 seconds."

    tanish "Height is what—about 30 meters?"

    alex "That’s what the sign says."

    tanish "Okay... then acceleration is..."

    alex "Bruh did you forget the formula chigga?"

    tanish "It’s not forgetting. It’s... selectively outsourcing."

    alex "a = 2 * d / t². You’re welcome."

    tanish "You’d make a great calculator with a bad attitude."

    alex "And you’d make a decent partner if you didn't treat this dumbass worksheet like a game show."

    tanish "Coming up next: Two dumb teens miscalculate gravity!"

    alex "We’re doing science, not stand-up."

    tanish "You say that, but this worksheet is comedy gold."

    scene black
    with Pause(2)
    scene bg theme_park

    show tanish happy at right
    show alex excited at left

    tanish "Alright, that’s the worksheet done. Manias should give us full marks just for riding that death coaster twice."

    alex "Agreed. E-MOTIONAL - - DAMAGE."

    show tanish neutral at right

    tanish "Anyway, I gotta dip early — parents are picking me up at the gate."

    alex "All good. Catch you tomorrow?"

    tanish "Unless I’m still recovering from that loop."

    hide tanish with moveoutright

    # Alex alone at the park entrance

    show alex neutral at center with move
    pause

    alex "Alright... time to head out."

    alex "...Wait."

    alex "Is that Clara I see over in the distance?"


    menu:
        "Approach her":
            jump approach_clara
        "Don’t approach her":
            return

    label approach_clara:

    stop music
    play music chill

    alex "..."

    alex "Alright. Let’s go say hi."

    show clara happy at left with moveinleft

    alex "Hey."

    clara "Oh—hey. Weren’t you heading out?"

    alex "I was. Then I saw you standing here looking like you were waiting for a philosophical moment."

    clara "More like catching my breath after some of those rides."

    alex "The loop-de-loop one almost separated my soul from my body."

    clara "That’s physics for ya."

    alex "So... not heading back with anyone?"

    clara "Nah. Lia ditched me for Albert’s chaos squad. I was just gonna walk home."

    show alex blush at center
    alex "Same. You wanna walk together?"

    clara "Sure. Lead the way, stopwatch boy."

    scene black
    with Pause(2)

    scene bg park

    show alex excited at left
    show clara happy at right

    alex "This place gets so quiet sometimes."

    clara "Right? I like walking here in the morning to school, or late at night to destress after a long day."

    alex "You ever bring homework here or just vibes?"

    clara "Homework kills the vibes."

    alex "Good answer."

    pause

    clara "So... doing anything this weekend?"

    alex "Might study. Might not. What about you?"

    clara "Not sure. Might meet up with Lia. Or just draw."

    alex "If you’re down for something low effort, we could hang out."

    clara "Low effort is my love language. I’d be down."

    scene black
    with Pause(2)
    scene bg alex_house

    show alex neutral at left
    show clara neutral at right

    alex "Well... this is me."

    clara "Cute place. I’m guessing there’s at least one anime poster inside."

    show alex blush at left
    alex "That’s classified."

    clara "Uhh, do you keep secrets from everyone, or just TA girls?"


    show alex neutral at left
    alex "Depends. Wanna meet the rabbit I trust with everything?"

    show clara happy at right
    clara "There’s a rabbit involved?"

    alex "Wait here."

    # Bunny appears outside (offscreen or implied)

    show alex excited at left
    alex "Okay. Meet Bunny."

    show clara neutral at right
    clara "..."

    clara "You named your bunny... Bunny."

    alex "Listen, it’s minimalist."

    show clara blush at right
    clara "Yo its not even minilalist. It's anti-lore..."

    clara "Zero Creativity. Maximal Chaos. Like calling your future child \"Child\" or a dog \"Dog\"."

    alex "She responds to it. Sometimes."

    clara "Wow. Such a deep bond I guess."

    alex "Go ahead. You can pet her if she doesn’t run."

    show clara neutral at right
    clara "I swear if she bites me..."

    pause

    show clara happy at right
    clara "Okay, fine. She’s adorable."

    alex "Told you."

    clara "Still judging you for the name, though."

    show alex neutral at left
    alex "As expected."

    clara "You and Tanish should really co-author a book called \"Naming Things Is Hard: A Journey into Functional Nihilism\""

    alex "Why?"

    clara "Didn't Tanish name a bunch of files \'.png? Basically the same energy as you naming your bunny \"Bunny\"."

    show alex blush at left
    alex "Oh, of course Tanish... He'd definitely be the type to do that."

    show clara neutral at right
    clara "Anyways, gotta get going. Thanks for the walk though. And the bunny interaction."

    alex "Thanks for tolerating my animal naming skills."

    clara "See you at school?"

    alex "Definitely."

    clara "Cool. Bye, Alex."

    alex "Bye, Clara."

    return
