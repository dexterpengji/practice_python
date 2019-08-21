print ('Welcome to the simplest game NumberGuess\n')
tempt = input("Could you guess my fortune number?\n")
guess = int(tempt)
if guess == 8:
    print("Yes, it is.\n")
else:
    print("No, it isn't.")
print("Game over, welcome back.")
