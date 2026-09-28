# Lesson 9

import random

invalid = True
player = ''

while invalid:
    player = input('scissors, rock, paper\n').lower()

    if player in {'rock', 'paper', 'scissors'}:
        invalid = False

ai = random.choice(['scissors','rock','paper'])

if player == ai:
    print('Tie game')

else:
    if player == 'rock':
        if ai == 'paper':
            print('AI Wins')
        else:
            print('Player Wins')
    elif player == 'paper':
        if ai == 'scissors':
            print('AI Wins')
        else:
            print('Player Wins')
    else: #scissors
        if ai == 'rock':
            print('AI Wins')
        else:
            print('Player Wins')
