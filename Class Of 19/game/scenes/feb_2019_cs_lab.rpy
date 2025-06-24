label feb_2019_cs_lab:
    stop music
    scene black
    with Pause(1)

    show splash with pixellate
    show text "February 2019" with dissolve
    with Pause(2)

    scene black with pixellate
    with Pause(1)

    play music cpen
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg computer_lab
    

    show tanish neutral at left
    show alex excited at right

    alex "You seriously still haven't finished Mob Psycho season two?"

    show tanish happy at left

    tanish "I'm pacing myself, okay? You gotta savor good animation like that. It's like gourmet anime."

    alex "Gourmet? You binge-watched Black Clover like it was a bag of Doritos."

    tanish "And I regret nothing."

    alex "You think Reigen could talk a compiler into working?"

    tanish "He'd charge it $500 an hour and still forget the semicolon."

    play sound door_open
    pause

    show mcdonald neutral at center
    mcdonald "Alex. Tanish. I assume your animated discussion is directly related to linked lists?"

    show tanish neutral at left
    show alex neutral at right
    tanish "Oh! Uh, technically… Mob Psycho does have arcs..."

    mcdonald "The only arcs I care about are binary trees. Assignment is due tomorrow, remember?"

    alex "We… totally knew that."

    mcdonald "I'd be less worried if you didn't say it like a question."

    hide mcdonald
    pause

    show tanish left at left
    show alex sideways at right
    tanish "Dude. We're so behind."

    alex "How did we forget? Didn't he literally write it on the whiteboard in all caps?"

    tanish "I was distracted. Clara was standing in front of the board."

    alex "Wow. So brave of you to admit that out loud."

    play sound typing
    pause

    alex "What the hell is a 'null pointer exception'? And why is it yelling at me?"

    tanish "You dereferenced a dead variable. Like a ghost. You made a ghost mad."

    alex "So helpful, thanks."

    tanish "We could ask Clara for help?"

    alex "You sure? Isn't she assigned to the 100-level class?"

    tanish "Yeah, but she knows stuff. She helped Jimin fix that recursion bug last week. Remember?"

    play sound whistle
    pause

    show tanish happy at left

    tanish "Hey Clara, got a sec?"

    show clara happy at center
    clara "Sure! What's up?"

    alex "We're, uh… hitting a wall with this data structures thing. Think you could take a look?"

    clara "Oof. Yeah, that one's tricky. But I actually haven't finished it yet—I'm only assigned to help the first-years."

    tanish "Darn. You seemed like our last hope."

    clara "Sorry! But hey, the hint on the assignment page? It's more useful than it looks. Read the hint."

    alex "Got it."

    clara "You guys got this. Probably."

    hide clara
    play sound typing
    pause

    show tanish left at left
    show alex blush at right
    alex "Okay but real talk… Clara's kinda cute."

    tanish "I knew it. You were paying more attention to her than the whiteboard too."

    alex "Can you blame me?"

    pause
    hide tanish
    show clara left at left

    # [Class winds down. Students begin to leave. Clara stays behind, organizing papers.]
    # [Alex hesitates, then walks over to her solo.]

    alex "Hey—uh, thanks again for earlier. Even if you couldn't help, it… helped. Y'know?"

    clara "Of course. You guys are fun."

    alex "Do you, uh... use Discord? Maybe we could trade memes. Or debugging pain."

    clara "Memes and suffering? Sounds like my kind of chat. Here—add me."

    # [They exchange phones. SFX: Discord notification ping.]

    alex "Nice. I'll start with something cursed. Test your threshold."

    clara "Bring it on. But no JoJo memes. I've seen everything."

    alex "You're gonna regret saying that."

    # This ends the game.

    return 