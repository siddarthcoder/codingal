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
    else:
        print("you wantt a spicy meal. ")
    s =(input("do you want it really spicy or just mild:"))

elif f == 2:
    print("1.cold")
    print("2. hot")
    choice3 = int(input("1 or 2? "))
    if choice3 == 1:
        print("you want a cold snack")
    else:
        print("you want a hot snack")
else: 
    print("invalid option")



