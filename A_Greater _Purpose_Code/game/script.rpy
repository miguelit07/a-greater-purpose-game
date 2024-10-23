# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define tT = Character("Time Tiller")

define me = Character("[mename]")

define epoch = Character("EPOCH")

define attack_flag = False

define fromFuture_flag = False

define fromLie_flag = False

define mission1_score = 0

define mission_failed = False

define saveTimeline = False

define ancientfemale = Character("Rainni")

define ancientmale = Character("Orvi")

define ancientmale2 = Character("Eso")

define dino1 = Character("Triceratops")

define dino2 = Character("T-Rex")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cronos_agency
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show historian default at center
    with zoominout

    # These display lines of dialogue.

    tT "Agent? .... Agent? .... AGENT!!! WAKE UP, THIS IS IMPORTANT!!!"

    "{i} Ah dang .... Looks like I fell asleep, first day on the job too. {/i}"

    $ mename = renpy.input("What's your name agent!? (type name)",length=32)

    me "It's [mename], sir."

    scene cronos_agency_blurred

    show historian default at center

    tT "You're about to enter the newest found anomaly! Do you even know what that means [mename]?! Are you sure you know everything?!"

    label choice1_prompt:
    menu:
        "I got it all boss.":
            jump choice_yesBoss
        "What's this anomaly?":
            jump choice_whatAnomaly
        "Where are we?":
            jump choice_whereAreWe
        "Who are you?":
            jump choice_whoAreYou
        "What is even the point of this?":
            jump choice_whatIsPoint
        
    label choice_yesBoss:
        tT "Great, glad you were paying attention."
        jump choice1_done
    
    label choice_whatAnomaly:
        tT "An anomaly is an alternate timeline to our own that has a distinct difference to mark it as a potential threat."
        tT "For example, one of the previous anomalies was a world where insects the size of cars, or another where every human grew horns. More questions [mename]?"
        jump choice1_prompt

    label choice_whereAreWe:
        tT "Did you even read the advertisement that brought you here? We are in the CA (Chronos Agency) headquarters. The Headquarters you are sitting in is not located on the familiar spatial plane."
        tT "We are in one that is in between almost all time variances and anomalies making it easy for us to travel amongst them. Anything else, [mename]?"
        jump choice1_prompt
    
    label choice_whoAreYou:
        tT "I am a Time Tiller, basically what you might call your immediate supervisor. I am in charge of assigning you missions and reporting whatever perceived success or failures you might achieve during your mission to the higher ups. Any other questions [mename]?"
        jump choice1_prompt
    
    label choice_whatIsPoint:
        tT "Our goal at the Chronos Agency is to remove any detrimental anomalies. If dangerous anomalies are allowed to remain they will start to impact our own in dangerous ways and could even lead to a total collapse of the proper timeline."
        tT "When we eliminate any anomaly we are able to eradicate all life forms there and keep every other world safe from implosion. Is that all, [mename]?"
        jump choice1_prompt

    label choice1_done:

    tT "Your first mission is an anomaly in the Triassic period, but somehow humans have appeared far too early. It's YOUR job to assess and eliminate this anomaly to save our own. DO NOT MESS THIS UP!"
    
    me "I won't let you down boss."

    tT "You better not, the Chronos Agency's council imposes strict deadlines."

    hide historian default
    with dissolve

    scene cronos_agency

    #show me default at left

    me "{i}Sheesh, good to know that my boss is an ass.{/i}"

    me "{i}Better head back to bed, I have a big day tomorrow.{/i}"

    #change to different scene
    #scene bg room

    me "{i}Well today is my big day ... my new life's purpose. If I mess this up ... no I got this! I will be successful.{/i}"

    me "{i}As I am making my way to the room I bump into a circular floating robotic creature.{/i}"

    hide me default 

    scene cronos_agency_blurred

    show epoch default at truecenter
    with dissolve

    epoch "PRESENCE DETECTED. AGENT RECOGNIZED ENGAGING CONVERSATION."

    epoch "Took you long enough! I am your personal Time Reviewer, EPOCH, and I will be making sure to report and grade your performance on this first mission. Try not to make this too hard on me."

    me "Uhh, so you'll be following me around my missions and critiquing me?"

    epoch "Exactly!"

    me "What if I do something wrong?"

    epoch "I will have to punish you accordingly."

    me "..."

    epoch "Just kidding! I can only act as observer throughout missions."

    me "A sarcastic robot to follow me around, nice. Let's turn down that humour setting by 40 percent"

    epoch "You are not authorized to change my settings. Jokes lighten the mood!"

    me "{i}This is going to be a long first day{/i}"

    epoch "Well come on let's get going, you do not want to be late."

    me "EPOCH started floating away before I could even get out a peep. I now am forced to jog quickly in order to keep up with my new 'best friend'."

    hide epoch default
    with ease

    show epoch default at topleft:
        blur 5
    
    show historian default at center
    with dissolve

    #show nurse default at right:
        #blur 5

    me "{i}We finally reach the anomaly room.{/i}"

    tT "You finally made it, [mename]. The transmission is ready for you to go."

    hide historian default

    scene cronos_agency_portal
    with dissolve

    me "{i}Before me was a strange looking portal, just like the one that brought me here but now, instead of the soft humming it felt as if a banshees were screaming at me to leave. My body was frozen in fear and all I can do is to try and further steel my nerves.{/i}"

    menu:
        "Alright, I'm gonna jump through":
            jump choice_portalDone
        "I need more time.":
            jump choice_needMoreTime
        "I don't think I can do this":
            jump choice_cantDoThis

    label choice_needMoreTime:
        tT "More time is not possible, this is an urgent anomaly [mename]."
        epoch "Don't worry, I'll be right beside you!"
        me "Alright, here goes nothing."
        jump choice_portalDone
    
    label choice_cantDoThis:
        tT "[mename], you are being given the sense of purpose to your previously meaningless life, do not waste this chance."
        epoch "You'll be fine [mename]! I'll be right beside you."
        me "Ughh... fine."
        jump choice_portalDone

    label choice_portalDone:
        tT "Goodluck agent."
        epoch "The past awaits us!"
        me "{i}What did I sign up for...{/i}"
        jump choice2_done

    label choice2_done:
    
    me "The smile staring back at me and the silent secret boss are my final images of the world I know and then I black out."

    scene triassic_background_trees
    with irisout

    me "{i}Holy... I've studied this period in the video books back in school, but to actually be here ... {/i}"

    scene triassic_background_trees_blurred

    show epoch default at topleft
    with dissolve

    epoch "VITALS DETECTED ... congratulations on not dying [mename]. So if you're done sleeping we have a job to do"

    me "I feel like I'm going to throw up."

    epoch "That is a common side effect of time travel, you'll be fine."

    epoch "Turning on invisibility cloak for the rest of mission. We will communicate through the headpiece in your ear, good luck."

    hide epoch default
    with dissolve

    me "{i}Ok ... I know that I am in a forested area right near a clearing and the CA were 'kind' enough to provide me with some supplies. Let's see ... some rations, medical supplies, and a more appropriate garment. Wait ... are those humans talking? I need to hide!{/i}"

    me "{i}I crouch down to lower myself, hidden amongst the ancient flora completely forgetting my uniform is white and stands out painfully.{/i}"

    scene triassic_background_trees
    with dissolve

    show ancientfemale default at left
    with dissolve

    show ancientmale default at right
    with dissolve

    ancientfemale "Did you find them?"

    ancientmale "No, how is it so hard to find creatures the size of 5 men?"

    me "{i}How can I understand them? We know the language of the past? What should I do?{/i}"

    menu:
        "Calmy approach them":
            jump choice_calm_entrance
        "Stay hidden":
            jump choice_stay_hidden

    label choice_stay_hidden:
        $ mission1_score+= 1
        epoch "Good choice, [mename]"
        ancientfemale "I think I see them! Let's go get them."
        me "{i}Who is 'them'?  Why are they running away from these two people? Too many questions and... they are running away.{/i}"
        me "{i}Huff {/i}... {i}huff {/i}... {i}huff{/i}. Who knew the people of the past could ... {i}huff{/i} ... really run huh."

        show triceratops default at center

        dino1 "ROOOAR!!!!!"
    
        me "{i}WHAT WAS THAT?! I don't even want to look past my tiny hiding spot{/i}"

        ancientmale "Glad to see you happy and safe [dino1]"

        dino2 "RAAEECHH!"

        me "{i}The blaring sound of a second creature caught me by surprise. In shock, I accidentally stepped on branch beneath me, emitting a CRRNCHH sound{/i}"

        me "Oh no ... I hope they didn't hear that."

        ancientfemale "What was that?!?"

        ancientmale "Sounded like it came from the bushes, let me investigate."

        epoch "He's coming straight towards us."

        me "{i}I can't move, I don't know what to do ... {/i}"

        ancientmale "{i}sniff, sniff, sniff{/i} I can smell you human, show yourself or my dinosaur companion will take care of you. "

        me "... I guess I have no choice."

        jump choice_dino_done
    

    label choice_calm_entrance:
        me "I'm going to engage with them, stay hidden and please be quiet EPOCH."
        epoch "You know this is against protocol, are you sure you still want to engage with them?"
        menu:
            "Yes, don't worry.":
                jump choice_calm_entrance_yes      
            "No, you're right.":
                jump choice_stay_hidden           
            
        
        label choice_calm_entrance_yes:
            $ mission1_score-= 1
            jump choice_dino_done
    

    label choice_dino_done:
    
    if mission1_score < 0:
        me "Hello ... I was wondering if you could help me?"
        me "{i}All heads whipped to the sound of my voice. The primitive human's expressions were now replaced with angry expressions and stone weapons raised to my head.{/i}"
        scene triassic_background_blurred
        show ancientfemale default at left
        show ancientmale default at right
        show triceratops default at center
        dino1 "ROARR!"
        me "{i}Is that ... a dinosaur ..."
        epoch "A Triceratops to be exact."
        me "{i}Oh god ...{/i}"

    else:
        me "Please don't hurt me."
        me "{i}All four heads whipped to the sound of my voice. The primitive human's expressions were now replaced with angry expressions and stone weapons raised to my head.{/i}"

    ancientfemale "Who are you and who sent you?"

    me "I'm from far away and ... I am very lost I was hoping you could help me find some food and water?"

    ancientmale "We have no reason to trust you. You are a stranger in strange clothes traveling by yourself. Explain to me stranger, why we should not just kill you where you stand?"

    me "What should I do?"   

    menu:
        "Attack and run":
            $ attack_flag = True
            jump choice_attack
        "Plead with them":
            $ mission1_score+= 2
            jump choice_plead
    
    label choice_attack:
        $ mission1_score-= 1
        me "{i}I try to throw a right hand before escaping, and in the blink of an eye the ancient human catches my fist with an immense strength.{/i}"
        show ancientmale close at center
        hide triceratops default
        with dissolve

        ancientmale "Ha ... You dare try to hit me with that weak of a punch?"
        epoch "That was a bad decison, [mename]. Your score is now [mission1_score]"

        ancientmale "My dinosaur hasn't ate today ... maybe I should feed you to him."

        me "Okay, okay ... please wait. I think we got off on a bad foot, let me explain himself."

        ancientfemale "Wait... I'm actually curious to see where this stranger is from."

        jump choice_plead

    
    label choice_plead:
    
    me "Please ... I am really just lost and looking for a- a place to rest and potentially gain supplies"

    me "{i}Please, please, please do not kill me. I can even hear the dinosaurs growling ready to trample me. My heart is about to burst just to make the decision.{/i}"
    
    ancientfemale "This stranger is no where near a threat to us, and I don't see any incentive to kill you ... yet."

    me "{i}Finally, both [ancientmale] and [ancientfemale] drop their weapons.{/i}"

    ancientmale "Stranger please tell me, what is your name and what is your business in this land?"

    menu:
        "Lie and give them a fake name":   
            jump choice_fakeName
        "Tell them your actual name":
            jump choice_realName
    
    label choice_fakeName:
        $ fakename = renpy.input("I am on a journey to explore the land, my name is (type fake name):",length=32)
        jump choiceNameDone
    
    label choice_realName:
        $ fakename = mename
        jump choiceNameDone
    
    label choiceNameDone:

    ancientmale "Alright [fakename], you may ride with us, but if you can't keep up you will be left behind."

    scene triassic_background_blurred

    show triceratops default at center
    me "{i}I GET TO RIDE A DINOSAUR! [ancientmale] has reached out their hand to me and up we go . The Parasaurolophus looks back at us, most likely not happy at the extra weight.{/i}"

    ancientmale "HUP"

    hide triceratops default

    me "{i}And off we go and surprisingly the ride is smooth, especially for being on a dinosaur. I guess the saddle is better designed than expected.{/i}"

    show ancientfemale close at left

    show ancientmale close at right

    ancientfemale "So [fakename], what's it like back where you're from?"

    menu:
        "Tell them about the future without revealing too much":
            jump choice_revealFuture
        "Make something up":
            jump choice_makeSomethingUp

    label choice_revealFuture:
        $ mission1_score-= 2
        $ fromFuture_flag = True
        me "So... I actually come from the future."
        epoch "You are revealing too much [mename]. Please keep the CA's policies in mind throughout the mission, or you will be demoted. Your score is now [mission1_score]"
        ancientfemale "The future?! How many years??"
        me "I would around 70 million years."
        ancientmale "Oh my..."
        ancientfemale "That explains your weird clothes."
        ancientmale "How is this possible?"
        me "In the future, we have developed technology to travel across time."
        me "My job requires to timetravel to prevent grave issues in the timeline, but due to a malfunction I was sent too far back to the past."
        ancientmale "I see.. "
        if attack_flag:
            me "Sorry for trying to attack you back there, many past eras of humans can be hostile, I feared for my life."
            ancientfemale "We aren't barbarians."
            ancientmale "Depending on instincts to survive is something we are familiar with, so it is understood."
        me "{i}They must have some sort of camp or base with others. If I can go there I will able to get the most intel and determine the outcome of this timeline."
        me "I just need somewhere to stay for a little, hopefully those back at job can identify the time period I am lost and come get me."
        ancientfemale "As long as you don't deem yourself as a threat or burden to us, you are welcome."
        ancientmale "You aren't off the hook yet though, you still have a lot of questions to answer once we get back to camp."
        me "{i}'Camp', okay nice I can finally get some more intel.{/i}"
        jump choice_whereFromDone
    
    label choice_makeSomethingUp:
        $ mission1_score+= 2
        $ fromLie_flag = True
        me "So... I actually come from a land from the other side of the world."
        epoch "Good choice [mename], your score is now [mission1_score]"
        ancientfemale "Other side... you mean you crossed the Mentile ocean?!"
        me "{i}They both looked at me with suprised faces, acting like this a great feat. I'll keep going with this lie and hope for the best.{/i}"
        me "Uhh... yeah"
        ancientmale "How? That journey is impossible. No one here has been able to venture to the other side."
        ancientfemale "Did you tame a Pterodactyl?"
        me "No, no. I actually used a boat."
        ancientmale "Boat? No boat can withstand the waters of the Mentile."
        me "With the materials from my land, we are able to make strong vessels."
        ancientmale "Based on your attire and demeanor, the other side must be a completely different world."
        ancientfemale "Yes, and what do your people call their land?"
        $ landname = renpy.input("We call our land (type name):",length=32)
        ancientfemale "[landname]... interesting."
        if attack_flag:
            ancientmale "So does everyone from [landname] attack strangers?"
            me "No we don't. Being in stranded in a new land I didn't know what I was dealing with. I expected the worse, sorry for that."
            ancientmale "Depending on instincts to survive is something we are familiar with, so it is understood."
        me "I was actually on an expedition with many others. There was a bad storm though.. I don't remember much.. our ship sank and I just remember waking up on shore alone."
        me "{i}They must have some sort of camp or base with others. If I can go there I will able to get intel and determine the outcome of this timeline."
        me "I just need somewhere to stay for a little, with some time hopefully I can find others who survived."
        ancientfemale "As long as you don't deem yourself as a threat or burden to us, you are welcome."
        ancientmale "You aren't off the hook yet though, you still have a lot of questions to answer once we get back to camp."
        me "{i}'Camp', okay nice I can finally get some more intel.{/i}"

        jump choice_whereFromDone

    label choice_whereFromDone:

    hide ancientfemale
    hide ancientmale
    
    me "{i}After some time traversing across the land, we finally arrive to their base camp.{i}"

    ancientmale "Okay, we have arrived [fakename]"

    scene triassic_background_trees_coveringsmoke
    with dissolve

    me "{i}I hop off the the dino and see smoke rising from the middle of the camp.{/i}"

    show ancientfemale close at center
    with dissolve

    ancientfemale "Stay close [fakename], the others might not approve of your arrival."

    hide ancientfemale
    with dissolve

    scene triassic_background_camp_far
    with irisout

    me "{i}As I walk closer to the camp, I am met with the confused and disapproving faces of several ancient humans and their dino companions."

    me "{i}I notice that dinosaurs are greatly integrated into their whole society, with even kids playing with dinos like they are dogs.{/i}"

    show epoch default at topleft
    with dissolve

    epoch "Don't be decieved [mename]. Despite them seeming to get along pretty well, it creates several implications in the future that must be prevented."

    hide epoch
    with dissolve

    show ancientmale2 default at center
    with dissolve

    ancientmale2 "Who is this stranger!?"

    show ancientmale default at left
    with dissolve

    ancientmale "Do not worry Eso, he is of no harm."
    
    show ancientmale2 close at center
    with dissolve

    show ancientfemale default at right
    with dissolve

    ancientmale2 "How are you so sure [ancientmale]? He does not look from this land."

    if fromFuture_flag:
        show ancientfemale close at right
        with dissolve

        ancientfemale "This might sound untrue, but he is from the future and he is lost."
        
        show ancientfemale default at right
        with dissolve

        ancientmale2 "The future?!?"
        me "{i}They all now look at me with perplexed faces{/i}"
        me "Hello everyone, I bring no harm. I am lost and just need a bit of help to get back home."
        ancientmale2 "So what bring you from the future [fakename]? I don't believe for one second that you came here for peace. You or whoever you belong to wants something from us."
        me "{i}I feel the tension rising. Many of those in the tribe close on me with their dinos, raising their weapons.{/i}"
        ancientmale2 "We might be from your time's past, but we are not naive. State your true purpose, and do not lie."
        menu:
            "Tell the truth":
                $ mission1_score-= 1
                jump choice_tellTruth
            "Keep lying":
                jump choice_keepLying
            "Run away":
                $ mission1_score-= 2
                jump choice_runAway


    if fromLie_flag:
        ancientfemale "Because he is not, he is from across the Mentile."
        ancientmale2 "The Mentile?"
        me "It is true. I come from [landname], it is much different from this land."
        me "I was able to cross by boat, but my crew and I got hit with a nasty storm. I need some help finding survivors."
        me "[ancientmale], who I assume has a position of leadership amongst the tribe, changes to a conflicted, surprised face."
        ancientfemale "What's wrong [ancientmale2]?"
        ancientmale2 "What is wrong... what is wrong is that YOU brought a liar to our home!"
        ancientmale "Liar?!"
        me "{i}I feel the tension rising. Many of those in the tribe close on me with their dinos, raising their weapons.{/i}"
        ancientmale2 "My people, there is something I have to tell you. A long time ago ... the land across the Mentile was very much explored."
        me "{i}They all gasp in shock.{/i}"
        epoch "[mename], for lack of a better term, you have gotten yourself in some 'deep shit'."
        ancientmale2 "The lands across the Mentile are much different than ours. The dinosaurs there are impossible to tame, very hostile, as almost if they are from a different world."
        ancientmale2 "Expeditions there have always been a disaster, killing dozens of our people. Me and other council members determined to erase any chance of our people going there. We are just not fit to survive there yet."
        ancientmale "You should have told us the truth [ancientmale2]"
        ancientmale2 "I will explain my reasons later, but now we have bigger problems to deal with."
        ancientmale2 "I have been to these lands, [landname] does not exist. You have not been truthful [fakename]"
        me "I think we've been caught Epoch..."
        ancientmale2 "I am giving you one last chance, state you true intention or die."
        menu:
            "Tell the truth":
                $ mission1_score-= 1
                jump choice_tellTruth
            "Keep lying":
                jump choice_keepLying
            "Run away":
                $ mission1_score-= 2
                jump choice_runAway
    

    label choice_keepLying:
        me "No.. I swear I am telling the truth. We must have confused locations, I swear I am from this world."
        ancientmale2 "I gave you a chance stranger. You think of us as idiots, believing in your false claims with your alien clothes and demeanor."
        ancientmale2 "You have had enough chances, prepare to be killed."
        epoch "Imminent threat detected, mission failure. Transported back to HQ,"
        me "{i}Everyone in the camp rushes towards me with their weapons, but before they get close a portal spawns in front of me and jump in.{/i}"
        $ mission_failed = True
        jump backToBase


    label choice_runAway:
        me "{i}I take a quick glance around the camp to find an exit path. I begin running as fast as I can.{/i}"
        ancientmale2 "You have chosen your fate [fakename], KIP"
        me "{i}As I run I sense the footsteps of dinosaurs behind me. I don't even think to look back.{/i}"
        me "EPOCH GET ME OUT OF HERE!"
        epoch "Imminent threat detected, mission failure. Transported back to HQ,"
        $ mission_failed = True
        jump backToBase
        
    
    label choice_tellTruth:
        me "Okay, Okay, I actually am from the future."
        me "I was sent by the CA, a company that takes monitors anomalies, events that should not happen, across different timelines."
        epoch "Revealing this much information can result in incursions, your score is now [mission1_score]"
        ancientmale2 "So there exists worlds beyong ours?!"
        me "Yes... and according to the CA some worlds must be taken care of."
        ancientmale2 "Ha..'taken care of'. You shall do nothing to our world."
        ancientfemale "What is this 'anomaly' in our world?"
        me "Dinosaurs are not supposed to be tamed by humans, let alone live in the same period as them."
        me "{i}Confused faces surrounded me. They couldn't process what I just said.{/i}"
        ancientmale2 "Who are you to determine what should or should not exist... to hell with you and your 'CA'!"
        epoch "Extreme tension detected. We have gotten enough intel to confirm our reports [mename], it is time to make the decision on this timeline."
        me "{i}I dont know what to do... It seems like this timeline is pretty stable to me, but I don't want to disappoint the CA, especially on my first mission. What should I do?{/i}"

        menu:
            "Terminate timeline":
                jump choice_terminateTimeline
            "Keep timeline":
                jump choice_keepTimeline

        label choice_terminateTimeline:
            me "I'm sorry... but I most do the greater good for the universe."
            epoch "Beginning timeline termination, good choice [mename]"
            ancientmale "You selfish scum.."
            me "{i}Everyone in the camp rushes towards me, but before they get close a portal spawns in front of me and jump in.{/i}"
            jump backToBase
        
        label choice_keepTimeline:
            me "But I don't agree with the CA's analysis on this timeline."
            epoch "Bad choice [mename], you are failing this mission."
            ancientmale2 "What do you mean?"
            me "From my experience here, this timeline is stable to me. Humans and dinosaurs living in unity was a surprise to me, but you guys seem to thrive with this bond."
            ancientfemale "If what you speak of is true [fakename], thank you."
            ancientmale2 "Begone stranger, you have already caused to much trouble."
            me "{i}As I take a final glance at this timeline, a portal spawns in front of me and jump in.{/i}"
            $ mission_failed = True
            $ saveTimeline = True
            jump backToBase
    
    label backToBase:
        scene cronos_agency
        with pixellate

        show historian default at center
        with dissolve

        tT "Welcome back [mename]. How did you do?"
        if mission_failed:
            me "Ummmm.. not so great."
            show epoch default at topleft
            with dissolve
            epoch "[mename] had a score of [mission1_score]. Did not terminate timeline."
            tT "I knew you weren't ready. You still have much to learn."
            me "Hey, atleast I got back in one piece, could have got eaten by a dinosaur back there."
            if saveTimeline:
                me "I just couldn't bring myself to get rid of that world. In a way it was beautiful."
                tT "Do not let empathy blind you. This choice might have seemed right but now many more will suffer."
            tT "Head back to your quarters, you have another mission tomorrow."
            hide epoch
            me "{i}I could definitely use some sleep.{i}"
            return
        me "Ummmm.. pretty good I think?"
        epoch "[mename] had a score of [mission1_score]. Successfuly gathered sufficient intel on anomaly and terminated timeline."
        tT "Well done [mename], you are fast learner."
        me "Could have gotten eaten by a dinosaur, what a wild job."
        tT "Head back to your quarters, you have another mission tomorrow."
        hide epoch
        me "{i}I could definitely use some sleep.{i}"
        return 


    # This ends the game.

    return
