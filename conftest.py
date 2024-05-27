import pytest
from helpers.helper_data import Courier


@pytest.fixture()
def courier():
    courier_create = Courier().registration_and_get_courier_data()
    courier_login = Courier().login_and_get_courier_id(courier_create["data"])
    yield courier_create
    Courier().delete_courier(courier_login["id"])


@pytest.fixture()
def courier_delete():
    courier_create = Courier.registration_and_get_courier_data()
    print(courier_create['data'])
    courier_login = Courier().login_and_get_courier_id(courier_create["data"])
    yield courier_login
