from requests.models import Response
import requests


def save_to_json(file: str, response: Response) -> None:
    """ Сохраняет данные в файл """
    if response.status_code == 200:
        with open(file, 'w') as file:
            file.write(str(response.json()))
    else:
        print(f'Ошибка {response.text}')


def get(url: str) -> Response:
    """ Отправляет get запрос на адрес """
    return requests.get(url)
