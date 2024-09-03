import pytest

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

@pytest.fixture
def sample_library():
    return Library()

@pytest.fixture
def pit(sample_library):
    return Librarian('Pit', sample_library)