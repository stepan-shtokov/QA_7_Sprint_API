import allure
import pytest
import requests
from helpers.helper_data import CourierData, Courier
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseText


class TestCourierLogin:
    @allure.title('Courier with valid data login check')
    @allure.description('Request to login a courier, verify an answer, delete new courier')
    def test_courier_login(self, courier):
        courier_data = courier
        response = Courier().login_and_get_courier_id(courier_data['data'])
        assert response['status_code'] == 200
        assert response.get('id')
        Courier().delete_courier(response["id"])

    @allure.title('Login without login/password failed with error check')
    @allure.description('Request for a login without login/password, verify an answer')
    @pytest.mark.parametrize('courier_data', [CourierData.invalid_data_without_login,
                             CourierData.invalid_data_without_password])
    def test_courier_login_params_missing(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)
        assert response.status_code == 400
        assert ResponseText.insufficient_login_data_response in response.text

    @allure.title('Login with invalid data failed with error check')
    @allure.description('Request for a login with invalid data, verify an answer')
    def test_courier_login_null_data(self):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.login_courier}', data=CourierData.null_courier_data)
        assert response.status_code == 404
        assert ResponseText.profile_not_found_response in response.text
