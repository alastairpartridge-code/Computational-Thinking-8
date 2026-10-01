answer1 = input("You wake up. Will you go to school or stay home? ")
if answer1 == "stay home" or answer1 == "Stay home" or  answer1 == "Stay home." or answer1 == "skip":
    choice1 = input("Will you go to sleep or watch TV and play video games? ")
    if choice1 == "sleep" or choice1 == "Sleep":
        print("Ok, good night.")
    elif choice1 == "play video games and watch TV" or choice1 == "TV and video games" or choice1 == "tv and video games":
        choice2 = input("Will you play Fc 27 or Fortnite? ")
        if choice2 == "Fc 27" or choice2 == "FC 27" or choice2 == "fc 27":
            team1 = input("will you be Liverpool or Real Madrid? ")
            if team1 == "liverpool" or team1 == "Liverpool":
                print("Great Choice!")
            elif team1 == "Real madrid" or team1 == "real madrid" or team1 == "Real Madrid":
                print("Ok.")
        elif choice2 == "Fortnite" or choice2 == "fortnite":
            print ("good choice.")
        else:
                print ("Pick one of the options.")
    else:
            print("Pick one of the options")
            
elif answer1 == "Go to school" or answer1 == "go to school":
    choice3 = input("You have arrived at school. Will you go to your first class or skip?")
    if choice3 == "skip" or choice3 == "Skip" or choice3 == "skip class":
        choice4 =("You haved skiped class, now you have time will you get food or go to sleep")
        if choice4 == "sleep" or choice4 == "Sleep" or choice4 == "go to sleep" or choice4 == "Go to sleep":
             print("Good night.")
    elif choice3 == "Go to class" or choice3 == "go to class":
        choice5 = input("You are really tierd and really bored.")