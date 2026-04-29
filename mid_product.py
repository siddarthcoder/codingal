# 1) Take an integer input from the user and store it in `num`.

# Also copy the same value into `t` for digit counting.

# 2) Initialize `numLen = 0` to count the number of digits.

# 3) Count the digits using a loop:

# a) Repeat while `t > 0`

# b) Increase `numLen` by 1 each time

# c) Remove the last digit of `t` using `t = int(t/10)`

# 4) Check if the number has at least 4 digits:

# If `numLen >= 4`, continue to find the middle digits.

# Otherwise, print: "It's not a 4 or more than 4-digit number!"

# 5) If the number has 4 or more digits:

# a) Set `numLen = int(numLen/2)` to locate the middle positions

# b) Initialize `chk = 0` to track the digit index while extracting digits

# 6) Extract digits from right to left:

# a) Repeat while `num > 0`

# b) Get the last digit using `rem = num % 10`

# c) If `chk == numLen`, store this digit as `midOne`

# d) Else if `chk == (numLen - 1)`, store this digit as `midTwo`

# e) Remove the last digit using `num = int(num/10)`

# f) Increase `chk` by 1

# 7) Multiply the two middle digits:

# `prod = midOne * midTwo`

# 8) Print the product in the required format:

# "Product of Mid digits (midOne * midTwo) = prod"

num = int(input("Enter the number : "))
t = num
numLen = 0
while t>0: 
  numLen = numLen+1
  t = int(t/10)
if numLen>=4: #condition 1
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    rem = num%10
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)
else:
  print("\nIt's not a 4 or more than 4-digit number!")
        

