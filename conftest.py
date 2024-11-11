import pytest
from helpers.helper_data import Courier


@pytest.fixture()
def courier():
    courier_create = Courier().registration_and_get_courier_data()
    yield courier_create

