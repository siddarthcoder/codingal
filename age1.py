try:
    age = int(input("Enter your age: "))

    if age % 2 == 0:
        print("Valid age. It is an EVEN number.")
    else:
        print("Valid age. It is an ODD number.")

except:
    print("Error: That is not a valid number!")
