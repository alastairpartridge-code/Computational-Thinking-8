import random
random_player = ["Messi", "Ronaldo", "Doue", "Haaland", "Bellingham", "Yamal"]
hidden_player = random.choice(random_player)
for i in range (5):
    # Start of code
    guess_player = input ("ENTER PLAYER: ")
    if guess_player == hidden_player:
        print ("Good job, you win!")
        quit()
    else:
            print ("Wrong, guess again.")
    if hidden_player == "Messi":
         print ("They are from Argentina.")
    if hidden_player == "Ronaldo":
         print("They are from Portugal.")
    if hidden_player == "Doue":
         print("They are from France.")
    if hidden_player == "Haaland":
         print("They are from Norway.")
    if hidden_player == "Bellingham":
         print("They are from England.")
    if hidden_player == "Yamal":
         print("They are from spain.")
print ("You used all five guesses. You lose.")