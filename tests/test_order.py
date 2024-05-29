import json
import allure
import pytest
import requests
from data.static_data import OrderData, ResponseText
from helpers.endpoints import Endpoints
from helpers.urls import Urls


class TestCreateOrder:
    @allure.title('Order with correct data successfully created check')
    @allure.description('Request to create an order with correct data and any color, verify an answer')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]},
                                       {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {'Content-type': 'application/json'}
        data = OrderData.data
        data.update(color)
        data_dump = json.dumps(data)
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data_dump)
        assert response.status_code == 201 and ResponseText.track_in_order_list_response in response.text
