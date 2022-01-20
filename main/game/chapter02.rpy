label chapter02:

    "{i}Waking up is such a pain. Maybe something interesting will happen today! That's how I should be thinking, but for some reason…{/i}"
    
    #scene MC house

    "TV" "Another person has gone missing from Asteroth Academy while a missing person in a related case has just been found heavily injured and was recently taken to hospital via helicopter for urgent medical care"
    "{i}I can't let this happen to one of my classmates. I can't handle the regret knowing I could've at least tried to do something. Wait. What time is it? Oh no, I'm going to be late for school! I guess I'll have to skip breakfast to make it there on time.{/i}"

    #scene MC classroom

    mch "That, must be, a new record, for me."
    mch "No one in the class says a word during the lecture, the atmosphere morbid, like a funeral for an insignificant human"

    "outside of classroom" "~Nyofuuuu~"

    menu:

        #if statement (has not met Nyofu i.e. ch111 or ch121 or ch122)
        "{i}What was that? I'm curious to know what kind of animal makes that sound!{/i}":
            jump ch211
        #else statement (has met Nyofu i.e. ch131 or 132)
        "Is that Nyofu? What is she doing here? I should go and talk to her.":
            jump ch211

        #if statement (met Soleil i.e. ch121 or ch122)
        "I should try to find Soleil/(that girl yesterday), maybe she knows something useful? It's lunch break so she will probably be at the cafeteria.":
            jump ch221
        #if statement (met Soleil + clue i.e. ch122)
        "{i}I should go and investigate the teachers office afterschool, I don't have enough time right now.{/i}":
            jump ch231
        #if statement (met Nyofu + clue i.e. ch131)
        "{i}Nyofu told me that there was someone suspicious hanging around afterschool at the old school buildings, I'll go and check them out after classes end today.{/i}":
            jump ch241

label ch211:
label ch221:
label ch231:
label ch241: