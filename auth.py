class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

book1 = Book("harry potter", "Jk rowling", 310)
book2 = Book("wimpy kid", "jeff kinney", 217)

