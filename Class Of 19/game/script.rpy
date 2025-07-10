﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define gina = Character("Gina")
define bobby = Character("Bobby")
define alex = Character("Alex")
define kyra = Character("Kyra")
define chatjippity = Character("Chatjippity")
define phone = Character("Phone")
define albert = Character("Albert")
define lia = Character("Lia")
define sandwich1 = Character("Sandwich1")
define sandwich2 = Character("Sandwich2")
define chunky = Character("Chunky")
define qwen = Character("Qwen")
define bunny = Character("Bunny")
define emily = Character("Emily")
define nicole = Character("Nicole")
define dealer = Character("Dealer")
define cop = Character("Cop")

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
define ring = "audio/sfx/ring.mp3"
define drinking = "audio/sfx/drinking.mp3"
define handcuffs = "audio/sfx/handcuffs.mp3"

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
define distance = "audio/distance.mp3"
define turtle = "audio/turtle.mp3"
define sirens = "audio/sirens.mp3"
define block = "audio/block.mp3"
define error = "audio/error.mp3"
define floater = "audio/floater.mp3"

# define scenes
image bg computer_lab = "images/backgrounds/computer_lab.png"
image bg 108_day = "images/backgrounds/108_day.png"
image bg 108_night = "images/backgrounds/108_night.png"
image splash = "images/backgrounds/school.png"
image bg library = "images/backgrounds/library.png"
image bg bobby_room_night = "images/backgrounds/bobby_room.png"
image bg gina_room_night = "images/backgrounds/gina_room.png"
image bg gina_room_day = "images/backgrounds/gina_room_day.png"
image bg school_hallway = "images/backgrounds/hallway.png"
image bg alex_room = "images/backgrounds/alex_room.png"
image bg kyra_room = "images/backgrounds/kyra_room.png"
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
image bg gina_street = "images/backgrounds/street.png"
image bg bar = "images/backgrounds/bar.png"

# ending scenes
image bg 00_neutral_ending = "images/backgrounds/00_neutral_ending.png"
image bg 01_alex_arrested = "images/backgrounds/01_alex_arrested.png"
image bg 02_alex_suicide = "images/backgrounds/02_alex_suicide.png"
image bg 03_bobby_deported = "images/backgrounds/03_bobby_deported.png"
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

    # Ending 8: Alex dates Ms. Emily
    Ending8Condition1 = False
    Ending8Condition2 = False
    Ending8Condition3 = False

    # Ending 9: bobby and Kyra Prom
    Ending9Condition1 = False
    Ending9Condition2 = False

    # Ending 7: bobby waterloo cs
    Ending7Eligible = True

    #Ending 6: Alex harvard university
    Ending6Eligible = True

    # bobby and Kyra breakup
    BobbyKyraBreakup = False

    # bobby deported ending
    Ending3Triggered = False

    # Alex overdose ending
    Ending5Triggered = False

    # Alex biked to Gina's house
    AlexBikedToGina = False

    # Gina calls cops on Alex
    Ending1Triggered = False

    #Alex commits suicide
    Ending2Triggered = False

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

        if BobbyKyraBreakup:
            call jun_2019_gatsby_aftermath

            if Ending3Triggered:
                call bobby_deported
                return

        if Ending9Condition1 and not BobbyKyraBreakup:
            call jun_2019_squid_game
    
    call jun_2019_alex_confession

    if Ending6Eligible == False:
        call jun_2019_alex_rejected

        if Ending5Triggered:
            call alex_overdose
            return
    else:
        call alex_harvard
        return
    
    call jun_2019_complications

    if AlexBikedToGina:
        call jun_2019_bike
    else:
        call alex_harvard
        return

    call jul_2019_bar_night
    call jul_2019_biking

    if Ending1Triggered:
        call alex_arrested
        return
    else:
        call jul_2019_gina_block
        call jul_2019_aftermath
        if Ending2Triggered:
            call alex_suicide
            return

    call neutral_ending

    return