import time


def mark_the_time(func):
    def wrapper():
        start = time.monotonic()
        result = func()
        end = time.monotonic() - start

        print(f'Время выполнения: {end}')

        return result

    return wrapper