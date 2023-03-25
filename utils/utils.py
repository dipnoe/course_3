import json


def json_reader():
    """
    Функция читает json файл с данными об операциях
    :return: список словарей
    """
    with open('../operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_by_date(data):
    """
    :param data: json файл с операциями
    :return: список выполненных операций, отсортированных по дате
    """
    executed_list = []
    for operation in data:
        if "state" in operation.keys():
            if len(operation) != 0 and operation["state"] == "EXECUTED":
                executed_list.append(operation)

    executed_list.sort(key=lambda x: x.get('date'), reverse=True)
    return executed_list
