print("would you like a meal or just a snack?")
print("1.meal")
print("2.snack")
f = int(input("1 or 2? "))

if f == 1:
    print("1.sweet")
    print("2.spicy")
    choice2 = int(input("1 or 2? "))
    if choice2 == 1:
        print("you want a sweet meal.")
        print("i recommend payasm")
    else:
        print("you wantt a spicy meal. ")
    s =(input("do you want it really spicy or just mild:"))
    print("i recommend the spicy chicken legs.")

elif f == 2:
    print("1.cold")
    print("2. hot")
    choice3 = int(input("1 or 2? "))
    if choice3 == 1:
        print("you want a cold snack")
        print("i recommend icecream")
    else:
        print("you want a hot snack")
        print("i reccomend stuffed mushrooms")
else: 
    print("invalid option")



