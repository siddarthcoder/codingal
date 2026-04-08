# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"


print("which vehicle do you want to take? ")
print("1.bike")
print("2.car")
choice = int(input("1 or 2? "))

if choice == 1:
    print("1.scooty")
    print("2.scooter")
    choice2 = int(input("1 or 2? "))
    if choice2 == 1:
        print("you have selected scooty.")
    else:
        print("you have chosen scooter. ")

elif choice == 2:
    print("1.xuv")
    print("2.sedan")
    choice3 = int(input("1 or 2? "))
    if choice3 == 1:
        print("you have selected xuv")
    else:
        print("you have selected sedan")
else: 
    print("invalid option")



