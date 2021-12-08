'''
Rock Paper Scissors
'''
import random

def player_input():
    while True:
        py_choice = input("what do you to choose?(rock/paper/scissors)\n")
        if py_choice.lower() not in ['rock','paper','scissors']:
            print("Invalid Choice!")
            continue
        else:
            break
    return py_choice.lower()

def comp_input():
    c_choice = random.choice(['rock','paper','scissors'])
    return c_choice

def win_cond():
    plyr = player_input()
    comp = comp_input()

    if plyr[0] == comp[0]:
        print(f"Your Choice -> {plyr}\nComputer -> {comp}")
        print("Its a TIE!")
    elif (plyr[0] == 'r' and comp[0] == 's') or (plyr[0] == 's' and comp[0] == 'p') or (plyr[0] == 'p' and comp[0] == 'r'):
        print(f"Your Choice -> {plyr}\nComputer -> {comp}")
        print("You won the game! CONGRATULATIONS!")
    else:
        print(f"Your Choice -> {plyr}\nComputer -> {comp}")
        print("You Lost the game! Better luck next time!")

def start():
    print("WELCOME TO RPS!")
    while True:
        win_cond()
        replay = input("Do you want to play again?(yes/no)\n")
        if replay.lower() == 'yes':
            continue
        else:
            print("THANKS PLAYING RPS!")
            break

if __name__ == '__main__':
    start()
