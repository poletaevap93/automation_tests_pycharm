import requests   # импортируем сначала библиотеку

url = "https://api.chucknorris.io/jokes/random"

result = requests.get(url)
print(result.status_code)
assert 200 == result.status_code   # это наша проверка. цифра 200 это то, что мы ожидаем, == это сравнение
if result.status_code == 200:
    print("Успешно")
else: print("запрос ошибочный")

result.encoding = 'utf-8'   # эта строка желательна, лучше ее вставлять, чтобы был понятный формат
print(result.text)