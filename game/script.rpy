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

"""
Game globals
"""
transform star_closeup:
    xalign 0.5
    yalign -0.5
    easein 4 yalign 0.5
transform star_transform:
    xzoom -0.65
    yzoom 0.65
    ypos 200

transform xeno_transform:
    xzoom 0.55
    yzoom 0.55

init python:
    star_variations = ['starlet color 2 neutral', 'starlet color 3 neutral', 'starlet dress 2 neutral', 'starlet eye 2 neutral', 'starlet hairstyle 2 neutral', 'starlet hairstyle 3 neutral', 'starlet original neutral', 'starlet straps neutral']
    star_current_order = []
    star_current_index = -1
    star_rotations = 0
    star_current_skin = 'starlet original neutral'
    from random import choice
    def f():
        if len(star_variations) == len(star_current_order):
            return
        while True:
            sel = choice(star_variations)
            if sel not in star_current_order:
                star_current_order.append(sel)
                return
    def choose_a_star():
        global star_current_index
        f()
        if (star_current_index + 1) == len(star_current_order):
            star_current_index = 0
        else:
            star_current_index += 1
        return star_current_order[star_current_index]

# The game starts here.

label start:
    scene bg room

    #show starlet original neutral at left:
    #    xzoom 0.65
    #    yzoom 0.65

    # at the set
    #replace with producer
    show eileen happy
    
    pl "Ugh.. how much longer do I have to wait! It's not like my job is on the line here!"
    
    "This is a common occurence here."
    "You wonder what led up to this to this point. This has been your life for the past several years."
    "Your job is to assist the production of movies, but it seems all you do is chores for the talent."
    
    hide eileen happy
    show elieen happy at left
    show director at right:
        xzoom 0.65
        yzoom 0.65
    
    n_director "Where is she? We paid way too much for her appearance in this movie! GET HER HERE NOW!"

    pl "I'm still looking-"

    show bg room with hpunch

    n_director "NOW!!!!"

    "The Director waddles off. The search intensifies..."

    hide director 

    # after some time
    scene bg room with fade
    show elieen happy

    pl "I've tried everything.. she's not at the coffee shop ..."
    pl "... not at the lounge ..."
    pl "... the only place I haven't looked is her dressing room."
    pl "I don't have much of a choice. Ugh, I hate going in there! She goofs around in there more than anywhere else!"

    # at the dressing room door
    scene bg room with dissolve
    show eileen happy

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
    scene bg room 
    show elieen happy

    pl "Ow!"
    pl "My head h-"

    hide eileen happy with dissolve

    n_unknown "Oh man. Another one."
    show xeno neutral with fade
    "A creature is holding your lips sealed, dragging you across the floor."
    pl "Mmmm-"
    n_unknown "What a disaster. I just wanted to clean up the first mess!"
    pl "*Did they take The Starlet??*"
    n_unknown "I can't have this one leaking our secrets..."
    n_unknown "Well, capturing another subject is good too. Hopefully I can clean up all the evidence this time!"
    "The weird creature covers your face. The same strange sound from earlier returns, only this time its much louder."
    scene black with fade
    "You end up fainting."

    # after some time
    # at the xeno prison
    show bg room with fade
    show eileen happy

    pl "My head hurts, again..."
    "You look at your surroundings."
    "You're in a very spacious room. There doesn't seem to be any windows, but there's a large pantry stocked with food, bedding, and lots of books."
    "It appears luxurious - but it's unmistakeable - you are in a prison cell."
    pl "Hello?"
    pl "Hellooooooooo!"
    n_star "My love!!"
    pl "Huh?!"
    "The Starlet appears."
    hide eileen happy
    show elieen happy at right
    show starlet original neutral at left:
        xzoom -0.65
        yzoom 0.65
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

    hide starlet original neutral with dissolve
    "The Starlet bursts into a cloud of smoke..."

    n_unknown "Well, well, well..."
    "The weird creature reappears."
    show xeno neutral at left with fade:
        xzoom 0.55
        yzoom 0.55
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
        "I'm fine being a servant...":
            jump ending_serve
        "YES YES I'LL DO IT!":
            jump g1
    return

label instructions:
    n_xeno "Alright, this is how the experiment will go."
    n_xeno "You will sit right where you are; if you move, you won't ever leave."
    n_xeno "A version of your precious Starlet will come through this door."
    n_xeno "You have to choose, is she The Real Starlet, or you aren't sure and move on."
    n_xeno "You have many chances to look, but you can choose correctly only once."
    n_xeno "I advise you to look very closely, and use your belongings and memories for help."
    n_xeno "Do you understand?"
    menu:
        "Did I catch that?"
        "No, repeat that please!":
            jump instructions
            return
        "I got it.":
            scene black with fade
            jump g1
            $ star_current_skin = choose_a_star()
            return
    return

label g1:
    # Look at your inventory
    # Look at the Starlet
    # Decide
    scene bg room with fade
    # show the star
    $ renpy.show(name=star_current_skin, at_list=[star_transform])
    menu:
        "Look at your inventory":
            jump inventory
        "Look at the Starlet":
            jump star_look
        "Decide":
            jump decide
    return

"""
INVENTORY
"""
label inventory:
    menu:
        "Old Photo":
            jump oldphoto
        "Newspaper Clipping":
            jump newsclipping
        "Favorite Movie List":
            jump movielist
        "Notebook":
            jump notebook
        "Purse":
            jump purse
        "Return":
            jump g1
    return

label oldphoto:
    pl "This is an old photo of The Starlet."
    pl "She always gets so flustered thinking about this time in her life."
    pl "It's almost as if she's done a full-180 since this was taken."
    pl "It's unbelivable..."
    jump g1

label newsclipping:
    "EXCLUSIVE INTERVIEW: The Starlet of Hollywood - Bad Blood with Co-Star?"
    "The Interviewer: I love your long, blonde hair!"
    "The Starlet: Thank you!"
    "The Interviewer: But I was wondering if you had any thoughts on your co-star, The Diva?"
    "The Starlet: She did really well, but honestly I wish she could take off the brunette wig."
    "The Interviewer: Are you saying you don't like that color?"
    "The Starlet: OF COURSE NOT! It's just, ew, you know?"
    jump g1

label movielist:
    pl "This is her list of favorite movies..."
    pl "There's no rhyme or reason for the choices on the list..."
    pl "They just seem to be all like her, blondes, in elaborate and fancy dresses."
    pl "Hmmm... none of these dresses have straps. Come to think of it, I've never seen her in a dress with straps."
    jump g1

label notebook:
    "March XX, 20XX"
    pl "This was a while ago"
    "I cut my hair short today. NONONONO! I hated it!"
    "Never again. The Director said it looked good on me, he's really funny!"
    pl ".. sure .. *flips to the last page*"
    "September XX, 20XX"
    pl "This was yesterday!"
    "I had my BFF run some errands for me, but I totally forgot my flat iron!"
    "The main character for this movie had straight hair, I hope the techs have one for me."
    jump g1

label purse:
    "The purse is purple."
    pl "One thing I can give her, she has a great fashion sense."
    pl "Or her assistants do. I don't know."
    pl "Her outfits always come together, always paired with color or texture."
    jump g1
    

"""
CLOSE UP OF THE STARLET
"""
label star_look:
    scene black with fade
    "Press H to show or hide the dialogue box."
    scene bg room with fade
    window hide
    $ renpy.show(name=star_current_skin, at_list=[star_closeup])
    pause 4
    "Press any key to continue"
    jump g1
    return

"""
DECIDE
"""
label decide:
    menu:
        "Shes The Real Starlet.":
            jump reveal
        "I can't tell. Next one...":
            $ star_rotations += 1
            $ star_current_skin = choose_a_star()
            jump g1
    return

label reveal:
    #determine ending
    return

label good_ending:
    # at the dressing room
    "You wake up and see that you are back in the dressing room."
    "You look around, and the entire place is a mess."
    pl "*Did we crash land here?*"
    n_star "WHERE IS MY PHONE!!!"
    pl "Here we go again..."
    n_star "WHY DID YOU HAVE TO PICK THE REAL ME! I LOVED IT OVER THERE!"
    pl "Get over yourself! Don't you still want to make movies? Be seen? Your fans would have missed you!"
    n_star "Who cares about them! My friend had an all you can eat buffet..."
    pl "You became friends with that thing?? And you need to watch what you eat..."
    "The Starlet begins pouting."
    pl "Come on, stop doing that."
    pl "What about your pet dog?"
    n_star "FLUFFY!!! YOU'RE SO RIGHT!"
    "The Starlet begins to cry."
    n_star "How could I be so cruel!! I was having so much fun that I forgot about my poor baby."
    pl "I'm sorry to cut you off, but you have been holding your phone in your hand this whole time."
    n_star "Oh... silly me!"
    pl "Come on and get ready!"
    
    # at the set
    pl "Sir, I've brought the talent. I'm so sorry for the delay!"
    n_director "About time! We have been waiting for hours!"
    n_director "We are hungry, the techs are pissed, the execs are breathing down my neck!"
    pl "..."
    n_director "Do you have anything to say?!"
    n_star "I was the only one that was late!"
    n_director "Huh?"
    n_star "You should be mad at me, sir! I was the one who dragged her out to a space ship!"
    "The Director is visibly confused."
    n_director "Uhh...."
    n_director "..."
    n_star "..."
    n_director "Oh, how could I ever be mad at you, my dear."
    n_star "You're so sweet!"
    pl "..."
    n_director "You're lucky this time. Don't disappoint me again!"
    pl "Yes sir..."
    "Good End. (The are 3 more endings! Replay for more!)"
        
    return

label ending_serve:
    # "ending_serve"
    "It's a sorry sight."
    "You ended up serving The Xeno and its ship. Your tasks involve maintance and helping it understand human langauge and culture."
    "The Xeno studies its subjects diligently, and is quite pleased with their work."
    "You, however, are still doing the same things you were doing back on Earth."
    "The Starlet is perched up on her xeno-made throne, and she's staring down at her assistant."
    n_star "It's so great here! I love it here!"
    "You are on the floor mopping up an oil spil."
    pl "... that's easy enough for you to say ..."
    n_xeno "Hmm, the maid-type seems to sound angry at princess-type. But she is using neutral words. I'm gonna have to write this down."
    n_xeno "What is this phenomenon called?"
    pl "Don't call me a maid! And it's called sarcasm!"
    n_xeno "Human, please refrain from yelling at me. If you don't cease this behavior, you will be made to do more work."
    pl "Oh my days..."
    
    "This disfunctional crew continued on for a long time... while their friends at home were worried about them, they were in the sky, up to no good..."
    "Bad End. (There are 3 more endings! Replay for more!)"
    
    return

