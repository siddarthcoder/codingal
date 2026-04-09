secret_number = 84

print("I'm thinking of a number between 1 and 100.")
print("guess my number")

guess = int(input("Guess 1: "))
if guess == secret_number:
    print(" Correct!")
else:
    print("Wrong!")

    
    guess = int(input("Guess 2: "))
    if guess == secret_number:
        print(" Correct!")
    else:
        print("Wrong!")

        
        guess = int(input("Guess 3: "))
        if guess == secret_number:
            print(" Correct!")
        else:
            print("wrong")
            print("Out of guesses! The number was", secret_number)
