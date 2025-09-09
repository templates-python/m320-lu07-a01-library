import pytest

from customer import Customer
from librarian import Librarian
from library import Library


def test_init(sample_library):
    hanna = Customer('Hanna', None, sample_library)
    assert hanna.name == 'Hanna'
    assert sample_library.search_customer('Hanna') == hanna


def test_no_library_attribute_stored(sample_library):
    """Test that Customer constructor does not store library as _library attribute."""
    customer = Customer('TestCustomer', None, sample_library)
    # Verify that the customer does not have a _library attribute
    assert not hasattr(customer, '_library')
    # Verify the customer is properly registered with the library
    assert sample_library.search_customer('TestCustomer') == customer


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


def test_reminded(customer_max):
    assert customer_max.reminded is False
    customer_max.reminded = True
    assert customer_max.reminded is True


def test_bring_back_a_book( customer_max, sample_library, pit):
    pit.buy_new_book('Test', 'ABC-123')
    customer_max.borrow_book_by_title('Test')
    customer_max.bring_back_book()
    book = sample_library.search_book_by_title('Test')
    assert book.title == 'Test'
    assert customer_max.book is None

@pytest.fixture
def sample_library():
    return Library()


@pytest.fixture
def pit(sample_library):
    return Librarian('Pit', sample_library)


@pytest.fixture
def customer_max(sample_library, pit):
    return Customer('Max', pit, sample_library)
