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
    enemy = randint(1, 3)
    enex = str(enemy)

    while user_input.upper() != "Q":
        if user_input.upper() == 'A':
            wins, draws, losses, matches,  = game(wins, draws, losses, matches, enex)
        elif user_input.upper() == 'B':
            record(wins, losses, draws, matches)
        user_input = input(menu_prompt)




def game(wins, draws, losses, matches, enex):

    user_input = int(input("\nROCK = 1 \nPAPER = 2\nSCISSOR = 3\nQUIT = 0\n\nROCK, PAPER OR SCISSORS: "))
    for rival in enex:
        while user_input > 0 and user_input < 4:
            try:
                matches += 1

                if rival == "2":
                    losses += 1
                    print(f"YOU LOST")

                elif rival == "3":
                    wins += 1
                    print(f"YOU WON")

                elif rival == "1":
                    draws +=1
                    print(f"YOU DRAWN")

            except:
                ValueError(f" ONLY NUMBERS BETWEEN 1-3")
                continue



            return wins, draws, losses, matches
def record(wins, losses, draws, matches):
    print(f"YOUR RECORD\nWINS: {wins}\nLOSSES: {losses}\nDRAWS: {draws}\nTOTAL MATCHES: {matches}")

menu()





