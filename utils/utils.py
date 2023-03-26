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

            if len(operation) != 0 and operation.get("state") == "EXECUTED":
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


def masking_card(card_info: str):
    """
    :param card_info: строка с именем и номером карты/счета
    :return: имя карты/счета и ее замаскированный номер
    """
    card_number = card_info.split()[-1]
    card_name = ' '.join(card_info.split()[:-1])

    if len(card_number) == 16 and card_number.isdigit():
        card_number = card_number[4:6] + '** **** ' + card_number[-4:]

    elif len(card_number) == 20 and card_number.isdigit():
        card_number = '**' + card_number[-4:]

    return f'{card_name} {card_number}'


def output_money(operation_amount: dict):
    """
    :param operation_amount: словарь с данными
    :return: количество денег и валюту в нужном формате
    """
    if "amount" in operation_amount.keys() and "currency" in operation_amount.keys():
        amount = operation_amount.get("amount")
        currency = operation_amount.get("currency").get("name")
        return f'{amount} {currency}'
