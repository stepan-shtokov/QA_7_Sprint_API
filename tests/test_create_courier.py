import allure
import pytest
import requests
from helpers.helper_data import CourierData
from helpers.endpoints import Endpoints
from helpers.urls import Urls


class TestCourierCreate:
    @allure.title('Create courier check')
    @allure.description('Request to create a courier,verify an answer')
    def test_registration_success(self, courier):
        courier_data = courier
        assert courier_data['status_code'] == 201
        assert courier_data['response_text'] == '{"ok":true}'

    @allure.title('Two same couriers registration error check')
    @allure.description('Second request to create a courier, verify expected error and delete new courier')
    def test_double_registration_failed(self, courier):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])
        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.text

    @allure.title('Courier without login/password registration error check')
    @allure.description('Request to create a courier without login/password and verify an answer')
    @pytest.mark.parametrize('courier_data', [CourierData.invalid_data_without_login,
                             CourierData.invalid_data_without_password])
    def test_registration_without_params_failed(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text
