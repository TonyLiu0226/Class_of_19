label feb_2019_cs_lab:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "February 2019" with dissolve
    play sound yooo
    $ renpy.pause(10, hard=True)

    scene black with pixellate
    with Pause(1)

    play music cpen
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg computer_lab
    

    show bobby neutral at left
    show alex excited at right

    alex "You seriously still haven't finished Mob Psycho season two?"

    show bobby happy at left

    bobby "I'm pacing myself, okay? You gotta savor good animation like that. It's like gourmet anime."

    alex "Gourmet? You binge-watched Black Clover like it was a bag of Doritos."

    bobby "And I regret nothing."

    alex "You think Reigen could talk a compiler into working?"

    bobby "He'd charge it $500 an hour and still forget the semicolon."

    play sound door_open
    pause

    show chatjippity neutral at center with moveinleft
    chatjippity "Alex. Bobby. I assume your animated discussion is directly related to linked lists?"

    show bobby neutral at left
    show alex neutral at right
    bobby "Oh! Uh, technically… Mob Psycho does have arcs..."

    chatjippity "The only arcs I care about are binary trees. Assignment is due tomorrow, remember?"

    alex "We… totally knew that."

    chatjippity "I'd be less worried if you didn't say it like a question."

    hide chatjippity with moveoutleft
    pause

    show bobby left at left
    show alex sideways at right
    bobby "Dude. We're so behind."

    alex "How did we forget? Didn't he literally write it on the whiteboard in all caps?"

    bobby "I was distracted. Gina was standing in front of the board."

    alex "Wow. So brave of you to admit that out loud."

    play sound typing
    pause

    alex "What the hell is a 'null pointer exception'? And why is it yelling at me?"

    bobby "You dereferenced a dead variable. Like a ghost. You made a ghost mad."

    alex "So helpful, thanks."

    bobby "We could ask Gina for help?"

    alex "You sure? Isn't she assigned to the 100-level class?"

    bobby "Yeah, but she knows stuff. She helped Jimin fix that recursion bug last week. Remember?"

    play sound whistle
    pause

    show bobby happy at left

    bobby "Hey Gina, got a sec?"

    show gina happy at center with moveinleft
    gina "Sure! What's up?"

    alex "We're, uh… hitting a wall with this data structures thing. Think you could take a look?"

    gina "Oof. Yeah, that one's tricky. But I actually haven't finished it yet—I'm only assigned to help the first-years."

    bobby "Darn. You seemed like our last hope."

    gina "Sorry! But hey, the hint on the assignment page? It's more useful than it looks. Read the hint."

    alex "Got it."

    gina "You guys got this. Probably."

    hide gina with moveoutleft
    play sound typing
    pause

    show bobby left at left
    show alex blush at right
    alex "Okay but real talk… Gina's kinda cute."

    bobby "I knew it. You were paying more attention to her than the whiteboard too."

    alex "Can you blame me?"

    pause
    hide bobby with moveoutleft
    show gina left at left with moveinleft

    # [Class winds down. Students begin to leave. Gina stays behind, organizing papers.]
    # [Alex hesitates, then walks over to her solo.]

    alex "Hey—uh, thanks again for earlier. Even if you couldn't help, it… helped. Y'know?"

    gina "Of course. You guys are fun."

    alex "Do you, uh... use Discord? Maybe we could trade memes. Or debugging pain."

    gina "Memes and suffering? Sounds like my kind of chat. Here—add me."

    # [They exchange phones. SFX: Discord notification ping.]

    alex "Nice. I'll start with something cursed. Test your threshold."

    gina "Bring it on. But no JoJo memes. I've seen everything."

    alex "You're gonna regret saying that."

    return 