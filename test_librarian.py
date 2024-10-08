import pytest

from book import Book
from customer import Customer
from librarian import Librarian
from library import Library


def test_init(sample_library):
    andreas = Librarian('Andreas', sample_library)
    assert andreas._name == 'Andreas'
    assert andreas._library == sample_library


def test_buy_new_book(sample_library, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    book = sample_library.search_book_by_title('Test Titel')
    assert book.title == 'Test Titel'
    assert book.isbn == 'ABC-123'
    assert book.location is not None  # es muss ein String mit einem Ablageort hinterlegt sein.


def test_lend_book_by_title(sample_library, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    book = pit.lend_book_by_title('Test Titel')
    assert book.title == 'Test Titel'
    assert book.isbn == 'ABC-123'
    assert book.location is not None  # es muss ein String mit einem Ablageort hinterlegt sein.


def test_lend_unknown_book(capsys, sample_library, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    book = pit.lend_book_by_title('Das unbekannte Buch')
    assert book is None
    captured = capsys.readouterr()
    assert captured.out == 'Das angefragte Buch ist nicht vorhanden\n'


def test_get_a_book_from_customer(sample_library, pit):
    book = Book(title='Test', isbn='ABC-789')
    pit.take_back_book(book)
    book = sample_library.search_book_by_title('Test')
    assert book.title == 'Test'


def test_remind_customer(sample_library, pit, customer_max):
    pit.buy_new_book('Test Titel', 'ABC-123')
    book = customer_max.borrow_book_by_title('Test Titel')
    pit.remind_customer('Max')
    assert customer_max.reminded is True


def test_remove_book(sample_library, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    book = sample_library.search_book_by_title('Test Titel')
    assert book.title == 'Test Titel'
    pit.remove_book('Test Titel')
    book = sample_library.search_book_by_title('Test Titel')
    assert book is None


@pytest.fixture
def sample_library():
    return Library()


@pytest.fixture
def customer_max(pit, sample_library):
    return Customer('Max', pit, sample_library)


@pytest.fixture
def pit(sample_library):
    return Librarian('Pit', sample_library)
