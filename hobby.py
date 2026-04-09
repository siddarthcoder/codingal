print("what is your hobby? ")
print("1.skating")
print("2.games")
choice = int(input("1 or 2? "))

if choice == 1:
    print("1.skateboard")
    print("2.scooter")
    choice2 = int(input("1 or 2? "))
    if choice2 == 1:
        print("you have selected skateboard.")
    else:
        print("you have chosen scooter. ")

elif choice == 2:
    print("1.video games")
    print("2. board games")
    choice3 = int(input("1 or 2? "))
    if choice3 == 1:
        print("you have selected video games")
    else:
        print("you have selected board games")
else: 
    print("invalid option")



