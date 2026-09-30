class myclass:
    __privatevar = 37;

    def __privemeth(self):
        print("i am inside my class")

    def hello(self):
        print("private variable value",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__privemeth()
