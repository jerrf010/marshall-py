# Lesson 7

import random

dc = int(input('DC: '))

if playernum > 20 or playernum < 1:
    exit()

rannum = random.randint(1,20)

if rannum >= dc:
    print('You shall pass')
else: 
    print('You failed')