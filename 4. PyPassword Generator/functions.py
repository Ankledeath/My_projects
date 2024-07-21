import random

import initial_data


def random_letters(number):
    random_letters_list = []
    for i in range(number):
        random_letters_list.append(initial_data.letters[random.randint(0, 52)])
    return random_letters_list


def random_symbols(number):
    random_symbols_list = []
    for i in range(number):
        random_symbols_list.append(initial_data.symbols[random.randint(0, 8)])
    return random_symbols_list


def random_numbers(number):
    random_numbers_list = []
    for i in range(number):
        random_numbers_list.append(initial_data.numbers[random.randint(0, 9)])
    return random_numbers_list


def make_password(total_list):
    passwd = ""
    random.shuffle(total_list)
    for i in range(len(total_list)):
        passwd += total_list[i]
    return passwd
