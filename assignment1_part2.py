class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    b1 = Book("Liu Cixin", "The Three-Body Problem")
    b2 = Book("George Orwell", "1984")

    b1.display()
    b2.display()