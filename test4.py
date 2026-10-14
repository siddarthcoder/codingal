user = input("what book do you want? ")
title = ("wimpy kid")
if user != title :
    print("book unavaliable , please come back another time")
else:
    print("thank you for borrowing a book , please return in a week")
class library:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class borrowed:
    def borrow(self):
        print("bye")



