# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define clara = Character("Clara")
define tanish = Character("Tanish")
define alex = Character("Alex")
define cindy = Character("Cindy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show clara happy at left
    show alex sad at right
    # These display lines of dialogue.

    clara "Hi, I'm Clara"   
    alex "Hi, I'm Alex"
    clara "I'm a student at the University of California, Los Angeles"
    alex "I'm a student at the University of California, Los Angeles"

    show cindy happy at center
    cindy "Hi, I'm Cindy"
    alex "Hi, I'm Alex"
    clara "Hi, I'm Clara"
    cindy "Hi, I'm Cindy"

    # This ends the game.

    return
