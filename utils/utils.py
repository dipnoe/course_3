import json


def json_reader(file_name):
    """
    Функция читает json файл с данными об операциях
    :return: список словарей
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_by_date(data):
    """
    :param data: json файл с операциями
    :return: список выполненных операций, отсортированных по дате
    """
    sorted_list = []

    for operation in data:

        if "state" in operation.keys():

            if len(operation) != 0 and operation["state"] == "EXECUTED":
                sorted_list.append(operation)

    sorted_list.sort(key=lambda x: x.get('date'), reverse=True)
    return sorted_list


def change_date_format(date: str):
    """
    :param date: строка с датой и временем
    :return: строку с датой в нужном формате
    """
    date = date.split('T')[0].split('-')
    return '.'.join(date[::-1])
