number = int(input("Enter a number: "))

# Handle negative numbers
if number < 0:
    number = -number

count = 0

# Special case for 0
if number == 0:
    count = 1

while number > 0:
    number = number // 10
    count += 1

print("The number has", count, "digits.")