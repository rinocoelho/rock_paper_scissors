from random import *
import os

menu_prompt = (
    '- Press A to PLAY\n'
    '- Press B to CHECK RECORD\n'
    '- Press Q to QUIT\n'
    '- Choose: '
)


def menu():
    menu_input = ""
    wins = 0
    draws = 0
    losses = 0
    matches = 0

    while menu_input.upper() != "Q":
        if menu_input.upper() == 'A':
            wins, draws, losses, matches = game(wins, draws, losses, matches)
        elif menu_input.upper() == 'B':
            record(wins, losses, draws, matches)
        menu_input = input(menu_prompt)


def game(wins, draws, losses, matches):

    enemy = randint(1, 3)
    enex = str(enemy)
    for rival in enex:
        int_rival = int(rival)
        user_input = ask_input()
        #while user_input > 0 and user_input < 4:
            #user_input = int(input("\n ROCK = 1 \n PAPER = 2\n SCISSOR = 3\n\n ROCK, PAPER OR SCISSORS: "))

        matches += 1

        if int_rival == user_input:
            draws +=1
            print(f"YOU DRAWN")

        elif int_rival == 2 and user_input != 3:
            losses += 1
            print(f"YOU LOST")

        elif int_rival == 3 and user_input != 1:
            losses += 1
            print(f"YOU LOST")

        elif int_rival == 1 and user_input != 2:
            losses += 1
            print(f"YOU LOST")

        else:
            wins += 1
            print(f"YOU WON")


        #user_input = ask_input()

        return wins, draws, losses, matches





def record(wins, losses, draws, matches):

    print(f"YOUR RECORD\nWINS: {wins}\nLOSSES: {losses}\nDRAWS: {draws}\nTOTAL MATCHES: {matches}")

def ask_input():

    user_input = 0
    while user_input < 1 or user_input > 3:
        try:
            user_input = int(input("\nROCK = 1\nPAPER = 2\nSCISSOR = 3\n\nROCK, PAPER OR SCISSORS: "))
        except:
            ValueError
            print("Invalid input! Only numbers from 1 to 3")
    return user_input









menu()




