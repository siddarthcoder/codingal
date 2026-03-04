height = int(input("enter a number"))
weight = int(input("enter a number"))
BMI = weight/(height/100)**2
if BMI <= 18.4 :
    print("you are under weight")
elif BMI <= 24.9 :
    print("you are healthy")
elif BMI <= 29.9 :
    print("you are over weight")
elif BMI <= 34.9 :
    print("you are severly over weight")
elif BMI <= 39.9 :
    print("you are obease")
else:
    print("you are serverly obease")