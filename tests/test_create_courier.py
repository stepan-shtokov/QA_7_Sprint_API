import allure
import pytest
import requests
from helpers.helper_data import CourierData, Courier
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseText


class TestCourierCreate:
    @allure.title('Create courier check')
    @allure.description('Request to create a courier,verify an answer')
    def test_registration_success(self, courier):
        courier_data = courier
        assert courier_data['status_code'] == 201
        assert ResponseText.courier_successful__operation_response in courier_data['response_text']
        courier_login = Courier().login_and_get_courier_id(courier_data["data"])
        Courier().delete_courier(courier_login["id"])

    @allure.title('Two same couriers registration error check')
    @allure.description('Second request to create a courier, verify expected error and delete new courier')
    def test_double_registration_failed(self, courier):
        courier_data = courier
        first_courier_id = Courier().login_and_get_courier_id(courier_data["data"])
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data["data"])
        assert response.status_code == 409
        assert ResponseText.same_login_usage_response in response.text
        Courier().delete_courier(first_courier_id["id"])

    @allure.title('Courier without login/password registration error check')
    @allure.description('Request to create a courier without login/password and verify an answer')
    @pytest.mark.parametrize('courier_data', [CourierData.invalid_data_without_login,
                             CourierData.invalid_data_without_password])
    def test_registration_without_params_failed(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert ResponseText.insufficient_reg_data_response in response.text
