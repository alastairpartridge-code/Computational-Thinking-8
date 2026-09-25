name = input("Hi my name is Robert, what's your name? ")
print(f"Nice to meet you {name}.")
mood = input("How are you feeling today? ")
print(f"Oh, I'm also feeling {mood}.")
print(f"Hey {name} I have a question?")
input("")
school_feeling = input("How was school? ")
answer = input(f"Why was it {school_feeling}?" )
if answer == "I don't know" or answer == "idk" or answer == "i don't know":
    print("Ok.")
else:
    print("Thats nice.")
answer2 = input(f"Hay {name} what is your favorite class? ")
if answer2 == "PE" or answer2 == "pe":
    print("No way PE is my favorite too!")
else:
    print("That's cool.")
print(f"Goodbye {name} see you later.")