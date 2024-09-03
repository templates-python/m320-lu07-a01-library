""" Provides the class Customer for the Library application."""


class Customer:
    """
    Defines a customer of our library who,
    * borrows [ borrow_book_by_title() ] or
    * returns [ bring_back_book() ]
    a book.
    Each customer may only borrow one book at a time.

    Attributes
    ----------
    name: str
        The full name of this customer.
    reminded: bool (Default: false)
        Has this customer been reminded to return an overdue book.
    librarian: Librarian
        A reference to a librarian of our library.
    book: Book (Default: None)
        The book currently borrowed by this customer. None=no book borrowed
    """

    def __init__(self, name, librarian, library):
        """
        Creates a customer object, sets the reference to the librarian
        and registers the client with the library.
        :param name: Full name of this customer.
        :param librarian: A reference to the librarian.
        :param library: A reference to the library.
        """
        self._name = name
        self._reminded = False
        self._librarian = librarian
        self._book = None
        library.add_customer(self)

    def __str__(self):
        """
        Gibt den Namen des Kunden aus.
        """
        return f'Kunde: {self.name}'

    def borrow_book_by_title(self, title):
        """
        Borrows a book identified by the title from the librarian.
        If the book is available, the reference to the book will be set.
        Otherwise, an error message is printed.

        :param title: The title of the book.
        """

        print(f'{self.name} hat das Buch "{self.book.title}" erhalten.')

    def bring_back_book(self):
        """
        Returns the book to the librarian.
        The reference to the book will be set to None.
        """

        print(f'{self.name} hat das Buch "{self.book.title}" zurückgebracht')

    @property
    def name(self):
        """
        Gets the name of this customer.
        :return: Name des Kunden
        """
        return self._name

    @property
    def book(self):
        """
        Gets the name of the borrowed book.
        :return: Referenz zum ausgeliehenen Buch
        """
        return self._book

    @property
    def reminded(self):
        """
        Gets the status of the reminder.
        :return: Status der Mahnung true/false
        """
        # TODO

    @reminded.setter
    def reminded(self, value):
        """
        Sets the status of the reminder.
        """

        print(f'Das Buch "{self._book.title}" ist noch ausstehend')
