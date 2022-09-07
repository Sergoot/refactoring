import requests
from decorators import mark_the_time
from service import save_to_json, get


@mark_the_time
def main() -> None:
    """ Отправляет и обрабатывает запросы на адреса из urls """
    urls = (
        'https://jsonplaceholder.typicode.com/users',
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/todos',
        'https://fakestoreapi.com/products',
        'https://fakestoreapi.com/carts',
        'https://fakestoreapi.com/users'
    )

    for idx in range(len(urls)):
        url_split = urls[idx].split("/")

        print(f'Отправка запроса на {urls[idx]}')
        response = get(urls[idx])
        print(f'Ответ сервера {response.status_code}')

        file_path = f'./results/{url_split[-2].split(".")[0]}_{url_split[-1]}.json'

        save_to_json(file_path, response)


if __name__ == '__main__':
    main()
