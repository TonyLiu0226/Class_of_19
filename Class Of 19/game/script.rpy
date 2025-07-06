# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define clara = Character("Clara")
define tanish = Character("Tanish")
define alex = Character("Alex")
define cindy = Character("Cindy")
define mcdonald = Character("McDonald")
define phone = Character("Phone")
define albert = Character("Albert")
define lia = Character("Lia")
define sandwich1 = Character("Sandwich1")
define sandwich2 = Character("Sandwich2")
define chunky = Character("Chunky")
define manias = Character("Manias")
define bunny = Character("Bunny")
define neuheimer = Character("Neuheimer")
define nicole = Character("Nicole")
define dealer = Character("Dealer")

# define sounds
define door_open = "audio/sfx/door_open.mp3"
define typing = "audio/sfx/typing.mp3"
define whistle = "audio/sfx/whistle.mp3"
define phone_ping = "audio/sfx/phone_ping.mp3"
define yooo = "audio/sfx/yooo.mp3"
define flipping_page = "audio/sfx/flipping_page.mp3"
define laugh = "audio/sfx/laugh.mp3"
define eating = "audio/sfx/eating.mp3"
define ohno = "audio/sfx/ohno.mp3"
define kiss = "audio/sfx/kiss.mp3"
define slapping = "audio/sfx/slap.mp3"
define tv_static = "audio/sfx/tv_static.mp3"
define smoke = "audio/sfx/smoke.mp3"
define dial = "audio/sfx/dial.mp3"

# define music
define cpen = "audio/CPEN.mp3"
define theme_music = "audio/theme.mp3"
define chiki = "audio/c.mp3"
define distance = "audio/distance.mp3"
define chill = "audio/chill.mp3"
define lunchly = "audio/lunchly.mp3"
define TS = "audio/TS.mp3"
define study = "audio/c.mp3"
define chiggajockey = "audio/chiggajockey.mp3"
define dfd = "audio/dfd.mp3"
define calc_studying = "audio/calc_studying.mp3"
define library = "audio/library.mp3"
define themepark = "audio/themepark.mp3"
define bunny = "audio/chau_bunny.mp3"
define gatsby = "audio/gatsby.mp3"
define sad = "audio/sad.mp3"
define congratulations = "audio/congratulations.mp3"

# define scenes
image bg computer_lab = "images/backgrounds/computer_lab.png"
image bg 108_day = "images/backgrounds/108_day.png"
image bg 108_night = "images/backgrounds/108_night.png"
image splash = "images/backgrounds/school.png"
image bg library = "images/backgrounds/library.png"
image bg tanish_room_night = "images/backgrounds/tanish_room.png"
image bg clara_room_night = "images/backgrounds/clara_room.png"
image bg school_hallway = "images/backgrounds/hallway.png"
image bg alex_room = "images/backgrounds/alex_room.png"
image bg cindy_room = "images/backgrounds/cindy_room.png"
image bg classroom = "images/backgrounds/english.png"
image bg classroom_dimmed = "images/backgrounds/english_dimmed.png"
image bg cafeteria_lunch = "images/backgrounds/cafeteria.png"
image bg public_library = "images/backgrounds/public_library.png"
image bg library_shelf = "images/backgrounds/library_shelf.png"
image bg cafe = "images/backgrounds/cafe.png"
image bg cafe_night = "images/backgrounds/cafe_night.png"
image bg theme_park = "images/backgrounds/theme_park.png"
image bg drop_tower = "images/backgrounds/drop_tower.png"
image bg park = "images/backgrounds/park.png"
image bg alex_house = "images/backgrounds/alex_house.png"

# ending scenes
image bg 03_tanish_deported = "images/backgrounds/03_tanish_deported.png"
image bg 05_alex_overdose = "images/backgrounds/05_overdose.png"
image bg 07_alex_harvard = "images/backgrounds/07_alex_harvard.png"

define far_left = Position(xalign=0.1, yalign=1.0)
define far_right = Position(xalign=0.9, yalign=1.0)
define mid_left = Position(xalign=0.25, yalign=1.0)
define mid_right = Position(xalign=0.75, yalign=1.0)
define middle_left = Position(xalign=0.365, yalign=1.0)
define middle_right = Position(xalign=0.635, yalign=1.0)

define table_right = Position(xalign=0.6, yalign=0.3)
define table_center = Position(xalign=0.5, yalign=0.3)
define table_left = Position(xalign=0.4, yalign=0.3)

init python:

    # Ending 8: Alex dates Ms. Neuheimer
    Ending8Condition1 = False
    Ending8Condition2 = False
    Ending8Condition3 = False

    # Ending 9: Tanish and Cindy Prom
    Ending9Condition1 = False
    Ending9Condition2 = False

    # Ending 7: Tanish waterloo cs
    Ending7Eligible = True

    #Ending 6: Alex harvard university
    Ending6Eligible = True

    # Tanish and Cindy breakup
    TanishCindyBreakup = False

    # Tanish deported ending
    Ending3Triggered = False

    # Alex overdose ending
    Ending05Triggered = False

    # Alex biked to Clara's house
    AlexBikedToClara = False

# The game starts here.
label start:
    call feb_2019_cs_lab
    call mar_2019_volunteering
    call mar_2019_texting
    call apr_2019_studying
    call apr_2019_texting_2
    call apr_2019_lunch
    call apr_2019_texting_3

    if Ending9Condition1:
        call may_2019_library_date

    call may_2019_field_trip

    if Ending9Condition1:
        call jun_2019_great_gatsby

        if TanishCindyBreakup:
            call jun_2019_gatsby_aftermath

            if Ending3Triggered:
                call tanish_deported

        if Ending9Condition1 and not TanishCindyBreakup:
            call jun_2019_squid_game
    
    call jun_2019_alex_confession

    if Ending6Eligible == False:
        call jun_2019_alex_rejected

        if Ending05Triggered:
            call alex_overdose
    else:
        call alex_harvard
    
    call jun_2019_complications
    
    return