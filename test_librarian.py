import pytest

from librarian import Librarian
from library import Library


def test_init(sample_library):
    andreas = Librarian('Andreas', sample_library)
    assert andreas._name == 'Andreas'
    assert andreas._library == sample_library


@pytest.fixture
def sample_library():
    return Library()
