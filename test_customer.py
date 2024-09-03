import pytest

from customer import Customer
from library import Library


def test_init(sample_library):
    hanna = Customer('Hanna', None, sample_library)
    assert hanna.name == 'Hanna'
    assert sample_library.search_customer('Hanna') == hanna


@pytest.fixture
def sample_library():
    return Library()
