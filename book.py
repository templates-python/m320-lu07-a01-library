""" Provides the class Book for the Library application."""
from dataclasses import dataclass, field


@dataclass
class Book:
    """
    Defines a book identified by the title, with an ISBN-number and a location.

    The location will be assigned by the librarian who shelves the book in the library.

    Attributes
    ----------
    title: str
        the unique title of the book
    isbn: str
        the ISBN-13 number of this book
    location: str
        the shelf in the library this book is placed upon, will be assigned by the librarian
    """

    title: str
    isbn: str
    location: str = field(init=False)  # will be assigned by the librarian

    def __post_init__(self):
        self.location = None

    def __str__(self):
        """
        Returns a human-readable representation of the book.
        """
        return f'ISBN : {self.isbn} / Titel: {self.title}  / Ablage : {self.location}'

    @property
    def title(self):
        """ Gets the title of this book. """
        return self._title

    @title.setter
    def title(self, value):
        """ Sets the title of this book."""
        self._title = value

    @property
    def isbn(self):
        """ Gets the isbn-number of this book. """
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        """ Sets the isbn-number of this book. """
        self._isbn = value

    @property
    def location(self):
        """ Gets the location of this book. """
        return self._location

    @location.setter
    def location(self, value):
        """ Sets the location of this book. """
        self._location = value
