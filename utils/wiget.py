import json


def json_reader():
    """
    Функция читает json файл с данными об операциях
    :return: список словарей
    """
    with open('../operations.json') as file:
        return json.load(file)
