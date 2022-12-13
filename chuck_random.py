import requests  # импортируем сначала библиотеку

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def Test_create_new_random_joke(self):
        """Создание случайной шутки"""
        url = "https://api.chucknorris.io/jokes/random"

        result = requests.get(url)
        print(result.status_code)
        assert 200 == result.status_code  # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
        if result.status_code == 200:
            print("Успешно")
        else:
            print("запрос ошибочный")


######  тест на проверку, что значение ключа Категории равен нулю

        result.encoding = 'utf-8'  # эта строка желательна, лучше ее вставлять, чтобы был понятный формат
        print(result.text)
        check = result.json()  # здесь в чек мы сохраняем результат в виде джэйсона, чтобы проверить его на наличие нужных нам элементов
        check_info = check.get("categories")  # вытаскиваем именно значение ключа ""категории", хотим посмотреть, что там пустота
        print(check_info)
        assert check_info == []   # проверка на то, что ключ занчения Категории равен нулю
        print("категория верна")


################ тест на содержание слово ЧАК в каждой рандомной шутке

        check2 = result.json()  # здесь в чек мы сохраняем результат в виде джэйсона, чтобы проверить его на наличие нужных нам элементов
        check_info2 = check2.get(
            "value")  # вытаскиваем именно значение ключа ""value", хотим посмотреть, что там
        print(check_info2)
        name = "Chuck" # сохраняем в нэйм то слово, которое должно находиться в наших всех шутках
        if name in check_info2:
            print("слово чак содержится в шутке")
        else: print("чака в шутке нет")


######   получение рандомной штуки из категории спорт

    def Test_create_new_random_categories_joke(self):
        """Создание случайной шутки в категории спорт"""

        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category

        result3 = requests.get(url)
        print(result3.status_code)
        assert 200 == result3.status_code  # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
        if result3.status_code == 200:
            print("Успешно")
        else:
            print("запрос ошибочный")
        result3.encoding = 'utf-8'  # эта строка желательна, лучше ее вставлять, чтобы был понятный формат
        print(result3.text)
        check3 = result3.json()
        check_info3 = check3.get("categories")  # вытаскиваем именно значение ключа ""категории", хотим посмотреть, что там
        print(check_info3)
        assert check_info3 == ["sport"]  # проверка на то, что ключ занчения Категории равен sport
        print("категория верна")

sport_joke = Test_new_joke()
sport_joke.Test_create_new_random_categories_joke()