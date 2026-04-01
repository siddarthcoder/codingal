# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.

# 2) Calculate the average of `a`, `b`, and `c`:
#    - Add them and divide by 3
#    - Store the result in `avg`
#    - Print `avg`

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
#    - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
#    - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
#    - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
#    - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
#    - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
#    - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
#    - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
d = (a+b+c)/3
print(d)
if d>a and d>b and d>c:
    print("%d is higher than %d, %d, %d" %(d,a,b,c))
elif d>a and d>b  :
    print("%d is higher than %d, %d" %(d,a,b))
elif d>a and d>c:
    print("%d is higher than %d, %d" %(d,a,c))
elif  d>b and d>c:
    print("%d is higher than %d, %d" %(d,b,c))
elif d>a :
    print("%d is higher than %d" %(d,a))
elif  d>b :
    print("%d is higher than %d" %(d,b))
elif  d>c:
    print("%d is higher than %d" %(d,c))