# Lesson 11

x = int(input())
y = int(input())

if x == 0 and y == 0:
    exit()

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')

'''
all = input()
point = point.slip(' ')
point = list(map(int, point))
x, y = point

'''