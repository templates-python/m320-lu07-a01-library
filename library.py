""" Provides the class Library for the Library application."""
import random


class Library:
    """
    Defines the library that provides informations about the stored books.
    It offers services for:
      * adding new books to the library
      * removing books from the library
      * lending and returning books
      * registering customers
      * print the inventory of all available books
      * print a list of all customers

    Attributes
    ----------
    _booklist: List
        A list of all books in the library.
    _customerlist: List
        A list of all customers.
    """

    def __init__(self):
        """
        Creates a library object.
        Defines lists for books and customers.
        """
        self._booklist = []
        self._customers = []

    def add_customer(self, customer):
        """
        Adds a customer to the customer-list.
        :param customer: The customer to add.
        """
        self._customers.append(customer)

    def search_customer(self, name):
        """
        Searches a customer by his name.
        :param name: Name of the customer.
        :return: Customer-object or None=not found
        """
        for customer in self._customers:
            if customer.name == name:
                return customer
        return None

    def print_customers(self):
        """
        Prints a list of all customers on stdout.
        """
        print('Kunden:')
        for customer in self._customers:
            print(customer)
        print('---')

    def add_book(self, book):
        """
        Adds a book to a random shelf in the library.
        Returns the location (shelf) of the book.
        :param book: The book to add to the library.
        :return: The location of the book.
        """
        self._booklist.append(book)
        return chr(random.randint(65, 68)) + str(random.randint(1, 10))

    def remove_book(self, book):
        """
        Removes a book from the library.
        :param book: The book to be removed.
        """
        self._booklist.remove(book)

    def print_inventory(self):
        """
        Prints all available books on stdout
        """
        print('Inventar:')
        for book in self._booklist:
            print(book)
        print('---')

    def search_book_by_title(self, title):
        """
        Searches a book identified by its title in the library.
        :param title: The title of the book.
        :return: Book-object or None=not found
        """
        for book in self._booklist:
            if book.title == title:
                return book
        return None

    def lend_book(self, location):
        """
        Lends a book identified by its location from the library.
        Removes the book from the book-list.
        :param location: The shelf the book sits upon.
        :return: Book-object
        :raise: LookupError when there is no book at the location specified.
        """
        for book in self._booklist:
            if book.location == location:
                self._booklist.remove(book)
                return book
        raise LookupError

    def reshelve_book(self, borrowed_book):
        """
        Puts a book back on its shelf. The shelf is set in the attribute 'location' of the book.
        :param borrowed_book: The book object to be put back on its shelf.
        """
        self._booklist.append(borrowed_book)
