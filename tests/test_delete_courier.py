import allure
from helpers.helper_data import Courier
from data.static_data import ResponseText


class TestDeleteCourier:
    @allure.title('Courier deletion check')
    @allure.description('Request to delete a courier, verify an answer')
    def test_courier_delete_success(self, courier):
        courier_id = courier
        courier_login = Courier().login_and_get_courier_id(courier_id["data"])
        response = Courier().delete_courier(courier_login["id"])
        assert response["status_code"] == 200
        assert ResponseText.courier_successful__operation_response in response['response_text']

    @allure.title('Courier with invalid id deletion error check')
    @allure.description('Request to delete a courier with invalid id, verify an answer')
    def test_courier_with_invalid_id_deletion_failed(self):
        invalid_id = '111111'
        response = Courier().delete_courier(invalid_id)
        assert response['status_code'] == 404
        assert ResponseText.invalid_id_deletion_response in response['response_text']

    @allure.title('Courier without id deletion error check')
    @allure.description('Request to delete a courier without id, verify an answer')
    def test_delete_courier_without_id_failed(self):
        courier_id = None
        response = Courier().delete_courier(courier_id)
        assert response['status_code'] == 500
        assert ResponseText.null_id_deletion_response in response['response_text']
        