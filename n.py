base = int(input("Enter number: "))
n = int(input("Enter power: "))

result = 1

for i in range(n):
    result = result * base

print("Answer is:", result)