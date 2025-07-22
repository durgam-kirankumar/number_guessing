import os
os.system('cls')
# ======================================
from random import shuffle
   
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
# result = shuffle_list(list)
# print(result)

def player_guess():
    guess = ''
    while guess not in['1','2','3','4']:
        guess = input('Pick a number (1-4) >')
    return int(guess)
# result = player_guess()
# print(result) 


def check_guess(my_list,guess):
    if my_list[guess] == 'O':
        print('Correct')
    else:
        print('Wrong Guess !')
        print(my_list)

# intial list 
my_list = ['','O','','']   

# shuffle list
mixed_list = shuffle_list(my_list)

# player_guess

guess = player_guess()

# check_guess
       
check_guess(mixed_list,guess)
    
    