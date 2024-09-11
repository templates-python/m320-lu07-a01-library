import pytest

from customer import Customer
from library import Library


def test_add_and_print_customers(sample_library, customer_max, customer_moritz, capsys):
    sample_library.print_customers()
    captured = capsys.readouterr()
    assert captured.out == 'Kunden:\nKunde: Max\nKunde: Moritz\n---\n'


def test_search_customer(sample_library, customer_max, customer_moritz):
    sample_library.add_customer(customer_max)
    sample_library.add_customer(customer_moritz)
    customer = sample_library.search_customer('Moritz')
    assert customer is customer_moritz


def test_search_customer_failed(sample_library, customer_max, customer_moritz):
    sample_library.add_customer(customer_max)
    sample_library.add_customer(customer_max)
    customer = sample_library.search_customer('Julian')
    assert customer is None


@pytest.fixture
def sample_library():
    return Library()


@pytest.fixture
def customer_max(sample_library):
    return Customer('Max', None, sample_library)


@pytest.fixture
def customer_moritz(sample_library):
    return Customer('Moritz', None, sample_library)
