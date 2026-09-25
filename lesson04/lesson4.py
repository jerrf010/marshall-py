# Lesson 4

import math

sec1 = len(input('Sec 1: '))
sec2 = len(input('Sec 2: '))
sec3 = len(input('Sec 3: '))

totalCans = sec1 + sec2 + sec3

amtDozens = math.ceil(totalCans / 12) #The amount of dozens needed

costCans = 14.95 * amtDozens
leftOver = totalCans - amtDozens * 12

print(f'The cost would be ${costCans} and there would be {leftOver} leftover, with {totalCans} cans needed.')