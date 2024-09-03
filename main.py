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

    # pit kauft 5 neue Bücher, die er der Bibliothek beifügt.
    # Danach wird das Inventar der Bibliothek ausgegeben.
    # Teil 2
    # TODO

    # Ursula und Moritz leihen sich ein Buch aus
    # Teil 3
    # TODO

    # Ursula bringt ihr Buch zurück
    # Teil 4
    # TODO

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
