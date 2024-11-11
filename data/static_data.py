
class OrderData:
    data = {
        'firstname': "Степан",
        'lastname': 'Штоков',
        'address': 'г. Самара',
        'metroStation': 1,
        'phone': '+7 917 157 00 00',
        'rentTime': 3,
        'deliveryDate': '2024-05-20',
        'comment': 'Lets roll'
    }


class ResponseText:
    courier_successful__operation_response = '{"ok":true}'
    same_login_usage_response = 'Этот логин уже используется'
    insufficient_reg_data_response = 'Недостаточно данных для создания учетной записи'
    invalid_id_deletion_response = 'Курьера с таким id нет'
    null_id_deletion_response = 'invalid input syntax'
    track_in_order_list_response = "track"
    profile_not_found_response = 'Учетная запись не найдена'
    insufficient_login_data_response = 'Недостаточно данных для входа'
