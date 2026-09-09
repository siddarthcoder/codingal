class pet:
    type = " mammal"

    def __init__(self,name,age):
        self.name = name
        self.age = age

woof = pet("woof",4)
meow = pet("meow",9)

print("woof is {}".format(woof.type))
print("meow is {}".format(meow.type))

print("{} is {}".format(woof.name,woof.age))
print("{} is {}".format(meow.name,meow.age))


