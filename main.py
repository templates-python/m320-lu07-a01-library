""" Provides the main routine for the Library application."""
from customer import Customer
from librarian import Librarian
from library import Library


def main():
    """
    Bibliothek-Applikation
    """
    print('Bibliotheks-Anwendung\n=====================\n')
    library = Library()
    pit = Librarian('Pit', library)
    moritz = Customer('Moritz', pit, library)
    ursula = Customer('Ursula', pit, library)
    library.print_customers()

    pit.buy_new_book(title='Ich bin dann mal weg', isbn='3-345-678')
    pit.buy_new_book(title='im Westen nichts neues', isbn='6-444-856')
    pit.buy_new_book(title='Das Omen', isbn='3-3345-678-X')
    pit.buy_new_book(title='Harry Potter, die neue Welt', isbn='3-4321-334')
    pit.buy_new_book(title='die schönsten Zugreisen', isbn='3-2123-554')
    library.print_inventory()

    ursula.borrow_book_by_title('Das Omen')
    moritz.borrow_book_by_title('Ich bin dann mal weg')
    library.print_inventory()

    ursula.bring_back_book()
    library.print_inventory()

    # Moritz wird gemahnt
    # Teil 5
    # TODO

    # Pit löscht ein Buch aus der Bibliothek
    # TODO

    # Ursula will ein Buch, das es nicht gibt.
    # TODO

    pass


if __name__ == '__main__':
    main()
