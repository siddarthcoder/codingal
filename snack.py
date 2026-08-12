import array

box1 = {'fries','hershey','gummy bears','fries'}
box2 = {'carrot','cucumber','strawberry','carrot','gummy bears'}
# print(box1)
# print(box2)

box1.add('orange')
# print(box1)
box2.add('orange')
# print(box2)

# for i in  box1:
#     print(i)

# for j in  box2:
#     print(j)
    
for i in box1:
    print('================')
    print('i = ', i)
    print('================')
    for j in box2:
        print('j = ',j)
        if i == j:
            print('common snack', i)

snack_count = [box1,box2]
snack_count.count(snack_count)
print (snack_count)

snack_count.reverse()
print(snack_count)