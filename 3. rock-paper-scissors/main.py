import os
import random
import drawings


def right_input(char):
    if char == "0" or char == "1" or char == "2":
        return True
    else:
        return False


def unit_generator(number):
    if number == "0":
        print(drawings.rock)
    if number == "1":
        print(drawings.paper)
    if number == "2":
        print(drawings.scissors)


def winner(human, comp):
    if human == comp:
        return "Standoff"
    if human == "0" and comp == "1":
        return "Computer Wins!"
    if human == "0" and comp == "2":
        return "You Wins!"
    if human == "1" and comp == "2":
        return "Computer Wins!"
    if human == "1" and comp == "0":
        return "You Wins!"
    if human == "2" and comp == "0":
        return "Computer Wins!"
    if human == "2" and comp == "1":
        return "You Wins!"


repeat_game = True
while repeat_game:
    os.system('cls')
    print("Why do you choose? Type 0 fo Rock, 1 for paper, 2 for Scissors")
    flag = True
    human_choice = 0
    list1 = []

    while flag:
        human_choice = input()
        if right_input(human_choice):
            flag = False
        else:
            print("Type 0, 1 or 2")

    unit_generator(human_choice)

    print("Computer chose:")

    comp_choice = random.randint(0, 2)

    unit_generator(str(comp_choice))

    print(winner(human_choice, str(comp_choice)))

    game_over = input("Do you want to play again? Y/N ")

    if game_over.lower() == "n":
        exit()
