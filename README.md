# Финальный проект 7 спринта(Тестирование API)

## Описание тестов: 
* test_create_courier.py - проверка создания курьера
* test_delete_courier.py - проверка удаления курьера
* test_login_courier.py - проверка авторизации курьера 
* test_order.py - проверка создания заказа
* test_order_list.py - проверка получения полного списка заказов

## Для работы с репозиторием
* Установите зависимости:
``` shell
pip3 install -r requirements.txt
```
* Запустить все тесты из директории tests:
```shell
pytest tests --alluredir=allure_results
```
* Просмотр результатов тестирования в веб-версии отчета:
``` shell
allure serve allure_results
```