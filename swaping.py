a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

print("before swapping:")
print("a =", a, "b =", b, "c =", c )

temp = a

a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)