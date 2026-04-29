# 1) Take two integer inputs from the user and store them in `lower` and `upper`.

# (These represent the starting and ending range.)

# 2) Print a message showing the range: from `lower` to `upper`.

# 3) Use a loop to check every number `num` from `lower` to `upper` (inclusive).

# 4) For each `num`, first check if it is greater than 1.

# (Because prime numbers are always greater than 1.)

# 5) If `num` is greater than 1, test if it is prime:

# a) Try dividing `num` by every number `i` from 2 to `num - 1`.

# b) If `num` is divisible by any `i` (remainder is 0), it is NOT prime → stop checking (break).

# 6) If the loop finishes without finding any divisor (no break happened),

# then `num` is prime → print `num`.

lower = int(input("enter a low number:"))
upper = int(input("enter a higher number:"))
print("prime numbers between",lower,"and",upper, "are:")
for i in range (lower , upper + 1):
    if i > 1:
        for j in range (2,i):
            if ( i % j) == 0:
                break
        else:     
                print(i)


         

