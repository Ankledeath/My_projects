# Password Generator Project
import os
from time import sleep

import drawings
import functions

while True:
    os.system('cls||clear')
    # print("Welcome to the PyPassword Generator!")
    print(drawings.welcome)
    sleep(2)
    os.system('cls||clear')
    nr_letters = int(input("How many letters would you like in your password?\n\n > "))
    os.system('cls||clear')
    nr_symbols = int(input(f"How many symbols would you like?\n\n > "))
    os.system('cls||clear')
    nr_numbers = int(input(f"How many numbers would you like?\n\n > "))

    total_list = []
    total_list += functions.random_letters(nr_letters)
    total_list += functions.random_symbols(nr_symbols)
    total_list += functions.random_numbers(nr_numbers)

    password = functions.make_password(total_list)

    os.system('cls||clear')
    print(drawings.finish)
    print("\n" * 5)
    print("Your password is: ", password)
    print("\n" * 5)
    finish = input("Do you want to generate your password again? y/n \n\n > ")
    if finish.lower() == "n":
        exit()
