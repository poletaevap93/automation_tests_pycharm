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


new_place = Test_new_location()
new_place.create_new_location()
