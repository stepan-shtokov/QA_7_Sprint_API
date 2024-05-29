import allure
import requests
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseText


class TestOrderList:
    @allure.title('Get orders list check')
    @allure.description('Get orders list, verify an answer')
    def test_get_list_of_orders(self):
        response = requests.get(f'{Urls.SCOOTER_URL}{Endpoints.order_list}')
        assert response.status_code == 200
        assert ResponseText.track_in_order_list_response in response.text
