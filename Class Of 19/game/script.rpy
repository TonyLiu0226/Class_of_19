# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define clara = Character("Clara")
define tanish = Character("Tanish")
define alex = Character("Alex")
define cindy = Character("Cindy")
define mcdonald = Character("McDonald")
define phone = Character("Phone")

# define sounds
define door_open = "audio/sfx/door_open.mp3"
define typing = "audio/sfx/typing.mp3"
define whistle = "audio/sfx/whistle.mp3"
define phone_ping = "audio/sfx/phone_ping.mp3"
define yooo = "audio/sfx/yooo.mp3"

# define music
define cpen = "audio/CPEN.mp3"
define theme_music = "audio/theme.mp3"
define chiki = "audio/c.mp3"
define distance = "audio/distance.mp3"
define chill = "audio/chill.mp3"
define lunchly = "audio/lunchly.mp3"

# define scenes
image bg computer_lab = "images/backgrounds/computer_lab.png"
image bg 108_night = "images/backgrounds/108_night.png"
image splash = "images/backgrounds/school.png"
image bg library = "images/backgrounds/library.png"
image bg tanish_room_night = "images/backgrounds/tanish_room.png"
image bg clara_room_night = "images/backgrounds/clara_room.png"

init python:

    # Ending 8: Alex dates Ms. Neuheimer
    Ending8Condition1 = False
    Ending8Condition2 = False
    Ending8Condition3 = False

    # Ending 9: Tanish and Cindy Prom
    Ending9Condition1 = False
    Ending9Condition2 = False

    # Ending 6: Tanish harvard university
    Ending7Eligible = True
# The game starts here.
label start:
    call feb_2019_cs_lab
    call mar_2019_volunteering
    call mar_2019_texting
    return