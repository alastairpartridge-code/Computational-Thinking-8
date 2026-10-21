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
print ("You used all five guesses. You lose.")