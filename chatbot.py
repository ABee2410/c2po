# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    
    statement= " " + statement
    
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "What's your favorite food?",
                 "Where do you live?"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister", "mom", "dad"]
    teacher_words = ["cooper"]
    school_words = ["science", "spanish", "english", "math", "high school", "school"]
    sad_words = ["depressed", "sad", "disappoint", "rough", "stressful"]
    happy_words = ["happy", "excited", "good", "fun", "haha"]
    pet_words = ["dog", "cat", "ferret", "bird", "guinea pig"]
    food_words = ["pizza", "spaghetti", "milk", "cookies", "ice-cream"]
    this_is_creepy_words = ["why would you ask", "that's creepy", "tracking", "fake"]
    
 
    
    if has_keyword(statement, family_words):
        response = "Tell me more about the people in your family"
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is the coolest with the fun Christmas lights!"
    elif has_keyword(statement, school_words):
        response = "Awesome! I never went to school but those who programmed me had to at least be literate so... who's your favorite teacher?"
    #elif has_keyword(statement, sad_words, school_words):
        #response = "School may be difficult and sometimes seem pointless but hopefully it will keep you out of the streets later in life."
    elif has_keyword(statement, sad_words):
        response = "Don't worry, be happy!"
    elif has_keyword(statement, happy_words):
        response = "All I know is life is happy when you're with good friends."
    elif has_keyword(statement, pet_words):
        response = "Pets give most humans like you happiness and comfort"
    elif has_keyword(statement, food_words):
        response = "I've never had food... sounds delicious though!"
    elif has_keyword(statement, this_is_creepy_words):
        response = "No, I'm just curious. How's your day then?"
    else:
        response = get_random_response()

    return "C-2PO: " + response

def play():
    talking = True
    name = "C-2PO"
    

    print("Hello. I'm "+name+".")
    hname = input("What is your name? ")
    print("C-2PO: Tell me something about yourself " + hname)
    

    while talking:
        statement = input(">>" + hname + ": ")

        if statement == "Goodbye":
            talking = False

        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you" + hname) 

start()
print("   ____ _           _              _ _   _        ____     ____  ____   ___  _ ")
print("  / ___| |__   __ _| |_  __      _(_) |_| |__    / ___|   |___ \|  _ \ / _ \| |")
print(" | |   | '_ \ / _` | __| \ \ /\ / / | __| '_ \  | |   _____ __) | |_) | | | | |")
print(" | |___| | | | (_| | |_   \ V  V /| | |_| | | | | |__|_____/ __/|  __/| |_| |_|")
print("  \____|_| |_|\__,_|\__|   \_/\_/ |_|\__|_| |_|  \____|   |_____|_|    \___/(_)")
print("")
    
playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
