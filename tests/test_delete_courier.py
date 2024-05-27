import allure
from helpers.helper_data import Courier


class TestDeleteCourier:
    @allure.title('Courier deletion check')
    @allure.description('Request to delete a courier, verify an answer')
    def test_courier_delete_success(self, courier_delete):
        courier_id = courier_delete
        response = Courier().delete_courier(courier_id['id'])
        assert response["status_code"] == 200
        assert response["response_text"] == '{"ok":true}'

    @allure.title('Courier with invalid id deletion error check')
    @allure.description('Request to delete a courier with invalid id, verify an answer')
    def test_courier_with_invalid_id_deletion_failed(self):
        invalid_id = '111111'
        response = Courier().delete_courier(invalid_id)
        assert response['status_code'] == 404
        assert 'Курьера с таким id нет' in response['response_text']

    @allure.title('Courier without id deletion error check')
    @allure.description('Request to delete a courier without id, verify an answer')
    def test_delete_courier_without_id_failed(self):
        courier_id = None
        response = Courier().delete_courier(courier_id)
        assert response['status_code'] == 500
        assert 'invalid input syntax' in response['response_text']
        