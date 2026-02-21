class Book:
    """A simple Book class representing a printed book.

    Parameters
    ----------
    title : str
        The book title.
    author : str
        The book author.
    year : int
        The publication year.
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self):
        """Return the age of the book assuming current year is 2025."""
        return 2025 - self.year


class EBook(Book):
    """EBook represents a digital book and extends :class:`Book`.

    Parameters
    ----------
    title : str
        The book title.
    author : str
        The book author.
    year : int
        The publication year.
    file_size : int
        File size in megabytes.
    """

    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        parent = super().__str__()
        return f"{parent} ({self.file_size} MB)"


if __name__ == '__main__':
    # Quick manual check
    b = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(b)
    print("Age:", b.get_age())

    e = EBook("Dune", "Frank Herbert", 1965, 5)
    print(e)
    print("EBook Age:", e.get_age())
