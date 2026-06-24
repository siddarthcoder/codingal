try:
    num1 , num2 = eval(input("enter two numbers, seperated by a coma:"))
    result = num1 / num2
    print(result)
except:
    print("division by zero is  error")

else:
    print("n0 exceeptions")
finally:
    print("i am in finally")