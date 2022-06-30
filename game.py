from random import *

menu_prompt = (
    '- Press A to PLAY\n'
    '- Press B to CHECK RECORD\n'
    '- Press Q to QUIT\n'
    '- Choose: '
)


def menu():
    user_input = ""
    wins = 0
    draws = 0
    losses = 0
    matches = 0

    while user_input.upper() != "Q":
        if user_input.upper() == 'A':
            wins, draws, losses, matches = game(wins, draws, losses, matches)
        elif user_input.upper() == 'B':
            record(wins, losses, draws, matches)
        user_input = input(menu_prompt)




def game(wins, draws, losses, matches):

    user_input = int(input("\nROCK = 1 \nPAPER = 2\nSCISSOR = 3\nQUIT = 0\n\nROCK, PAPER OR SCISSORS: "))
    enemy = randint(1, 3)
    enex = str(enemy)
    for rival in enex:
        int_rival = int(rival)
        while user_input > 0 and user_input < 4:

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




            return wins, draws, losses, matches


def record(wins, losses, draws, matches):

    print(f"YOUR RECORD\nWINS: {wins}\nLOSSES: {losses}\nDRAWS: {draws}\nTOTAL MATCHES: {matches}")


menu()




