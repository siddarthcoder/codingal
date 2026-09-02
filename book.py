lib = ["bobb","diary of a wimpy kid","bhagavad gita","eagle","ramayanam"]
user = input("what book do you want?")
found = False
for i in lib:
    if i == user:
        print("book available")
        found = True
        break
if found == False:
    print('Book not available')