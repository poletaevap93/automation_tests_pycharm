import requests    #  импортируем библиотеку

class Test_new_location():
    """Работа с новой локацией в гугл мэпс"""

    def create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com" # базовая URL для всех запросов
        key = "?key=qaclick123"     # параметр для всех запросов


        """СОЗДАНИЕ НОВОЙ ЛОКАЦИИ. POST"""
        post_resource = "/maps/api/place/add/json"     # ресурс метода POST
        post_url = base_url + post_resource + key

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"}

        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print("Статус код: " + str(result_post.status_code))
        assert 200 == result_post.status_code  # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
        if result_post.status_code == 200:
            print("Успешно")
        else:
            print("запрос ошибочный")

        # проверка на прихождение верного статуса
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа: "+ check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")

        # получение id места нового
        place_id = check_post.get("place_id")
        print("ID места равен: "+ place_id)


        """ПРОВЕРКА СОЗДАНИЯ НОВОЙ ЛОКАЦИИ. """

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)

        result_get = requests.get(get_url)  # выполняем гет запрос на проверку созданного места
        print(result_get.text) # выглядеть должен также, как пример в документации от разрабов

        # теперь проверка статус кода ответа
        print("Статус код: " + str(result_get.status_code))
        assert 200 == result_get.status_code  # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
        if result_get.status_code == 200:
            print("Успешно. Проверка создания нового места прошла успешно")
        else:
            print("запрос ошибочный")


        """ИЗМЕНЕНИЕ НОВОЙ ЛОКАЦИИ. (positive test) """
        print("______________")

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_new_location = {
                "place_id": place_id,
                "address": "100 Lenina street, RU",
                "key": "qaclick123"
            }
        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)
        print("Статус код: " + str(result_put.status_code))
        assert 200 == result_put.status_code  # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
        if result_put.status_code == 200:
            print("Успешно. Проверка изменения нового места прошла успешно")
        else:
            print("запрос ошибочный")

        # теперь проверка сообщения ответа позитивного теста
        check_put = result_put.json()
        check_info_put = check_put.get("msg")
        assert check_info_put == "Address successfully updated"
        print("Сообщение верно")


        """ИЗМЕНЕНИЕ НОВОЙ ЛОКАЦИИ. (negative test) """
        print("______________")

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_new_location = {
                "place_id": 5555, # вставляем кривой ID места
                "address": "100 Lenina street, RU",
                "key": "qaclick123"
            }
        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)
        print("Статус код: " + str(result_put.status_code))
        assert 404 == result_put.status_code
        if result_put.status_code == 404:
            print("Отработано успешно. Место не изменено ")
        else:
            print("запрос ошибочный")


        """УДАЛЕНИЕ НОВОЙ ЛОКАЦИИ """
        print("______________")

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        json_for_delete_new_location = {
                "place_id": place_id,
            }
        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print (result_delete.text)

        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
             print("Удаление новой локации прошло успешно")
        else:
             print("Удаление новой локации не произошло")

        # теперь проверка сообщения ответа теста
        check_delete = result_delete.json()
        check_info_delete = check_delete.get("status")
        assert check_info_delete == "OK"
        print("Сообщение верно")


        """ПРОВЕРКА УДАЛЕНИЯ НОВОЙ ЛОКАЦИИ.  """
        print("______________")

        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код: " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно. Проверка удаления нового места прошла успешно")
        else:
            print("запрос ошибочный")

        # теперь проверка сообщения ответа теста
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Сообщение верно")

        print()
        print("Тестирование Test_new_location завершено успешно")


new_place = Test_new_location()
new_place.create_new_location()

