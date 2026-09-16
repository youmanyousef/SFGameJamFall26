# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

"""
Define characters here
"""
define pl = Character("The Producer")
define n_star = Character("The Starlet")
define n_xeno = Character("The Xeno")
define n_unknown = Character("???")
define n_director = Character("The Director")

"""
Define sprites here
"""

# The game starts here.

label start:

    scene bg room

    show eileen happy

    # at the set

    pl "Ugh.. how much longer do I have to wait! It's not like my job is on the line here!"
    
    "This is a common occurence here."
    "You wonder what led up to this to this point. This has been your life for the past several years."
    "Your job is to assist the production of movies, but it seems all you do is chores for the talent."
    
    n_director "Where is she? We paid way too much for her appearance in this movie! GET HER HERE NOW!"

    pl "I'm still looking-"

    n_director "NOW!!!!"

    "The Director waddles off. The search intensifies..."

    # after some time

    pl "I've tried everything.. she's not at the coffee shop ..."
    pl "... not at the lounge ..."
    pl "... the only place I haven't looked is her dressing room."
    pl "I don't have much of a choice. Ugh, I hate going in there! She goofs around in there more than anywhere else!"

    # at the dressing room door

    pl "Open the door!"
    "*crickets*"
    pl "Come on!! Open the damn door!"
    "*crickets intensify*"
    "..."
    "Suddenly, a strange sound emanates from inside."
    pl "What was that?! Is she playing with the outlets again?!"
    pl "That's it! I'm coming in!"
    "You brace yourself, and prepare to break in the door."
    "However, the door opens as soon as you charge, and you end up falling to the floor."

    # inside the dressing room

    pl "Ow!"
    pl "My head h-"
    n_unknown "Oh man. Another one."
    "A creature is holding your lips sealed, dragging you across the floor."
    pl "Mmmm-"
    n_unknown "What a disaster. I just wanted to clean up the first mess!"
    pl "*Did they take The Starlet??*"
    n_unknown "I can't have this one leaking our secrets..."
    n_unknown "Well, capturing another subject is good too. Hopefully I can clean up all the evidence this time!"
    "The weird creature covers your face. The same strange sound from earlier returns, only this time its much louder."
    "You end up fainting."

    # after some time
    # at the xeno prison
    
    pl "My head hurts, again..."
    "You look at your surroundings."
    "You're in a very spacious room. There doesn't seem to be any windows, but there's a large pantry stocked with food, bedding, and lots of books."
    "It appears luxurious - but it's unmistakeable - you are in a prison cell."
    pl "Hello?"
    pl "Hellooooooooo!"
    n_star "My love!!"
    pl "Huh?!"
    "The Starlet appears."
    n_star "Isn't this place nice? I should definitely get a place like this!"
    pl "*sobbing*"
    n_star "What's the matter, dear?"
    pl "What's wrong with you! I was worried sick about you!"
    n_star "I've only stepped out for a couple of hours..."
    pl "THAT DOESN'T MATTER! LOOK AT THIS PLACE!"
    n_star "Yeah it looks nice, doesn't it?"
    n_star "Come here, you..."
    "The Starlet comes close for a hug, and you oblige."
    "Instinctively, you wince, but you find that she's rather plesant today."
    "As a matter of fact, you wonder why she smells tolerable today."
    pl "How come you aren't wearing your perfume today?"
    n_star "Pardon? I'm not sure I understand?"
    "The Starlet is always overzealous in her application of perfumes and makeup."
    "What's more scary is the fact that she is speaking formally, and asking for clarity."
    pl "Wait a minute..."
    n_star "What's wrong!"
    pl "You're a fraud! You aren't The Real Starlet!"
    n_star "..."
    "The Starlet bursts into a cloud of smoke..."
    n_unknown "Well, well, well..."
    "The weird creature reappears."
    n_unknown "It seem's you have caught on fast! I have much to learn from a human like you!"
    pl "What?!"
    n_unknown "I've been studying humans for a long time, I thought I mastered their ways. I haven't been caught in my human suit this fast in decades."
    pl "Who are you?"
    n_unknown "I don't have one. Your people call me a Xeno."
    pl "What do you want from me?"
    n_xeno "I don't *want* anything, I *need* you to work for me. You will help me enslave your species."
    pl "I will do no such thing!"
    n_xeno "Oh yeah? And what about your precious Starlet? What would happen to her if you refused?"
    pl "..."
    n_xeno "That's what I thought."
    n_xeno "I have a game for you."
    n_xeno "I want to study how your brain works, it would make for great data!"
    n_xeno "If you can pick out The Real Starlet - that is, you can pick her over me in the disguise - you both get to go home. If you don't..."
    n_xeno "I keep you two as service pets!"
    pl "*gulp*"
    n_xeno "Do you have what it takes?"
    menu:
        "What should I do?"
        "I'm fine being a servant.":
            jump ending_serve
        "YES YES I'LL DO IT!":
            jump g1
    return

label g1:
    "g1"
    return

label ending_serve:
    "ending_serve"
    return

