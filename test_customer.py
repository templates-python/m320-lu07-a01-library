import pytest

from customer import Customer
from librarian import Librarian
from library import Library


def test_init(sample_library):
    hanna = Customer('Hanna', None, sample_library)
    assert hanna.name == 'Hanna'
    assert sample_library.search_customer('Hanna') == hanna

def test_borrow_book_by_title(customer_max, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    customer_max.borrow_book_by_title('Test Titel')
    book = customer_max.book
    assert book.title == 'Test Titel'

def test_borrow_unknown(capsys, customer_max, pit):
    pit.buy_new_book('Test Titel', 'ABC-123')
    customer_max.borrow_book_by_title('Unbekanntes Buch')
    assert customer_max.book is None
    captured = capsys.readouterr()
    assert captured.out == 'Das angefragte Buch ist nicht vorhanden\n'

@pytest.fixture
def sample_library():
    return Library()

@pytest.fixture
def pit(sample_library):
    return Librarian('Pit', sample_library)
@pytest.fixture
def customer_max(sample_library, pit):
    return Customer('Max', pit, sample_library)