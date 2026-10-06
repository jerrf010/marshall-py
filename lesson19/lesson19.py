# Lesson 19

n = int(input())

if n < 3:
    print('Not Prime')
    exit()

start = 2

for i in range(n):
    if start == n:
        break
    if n % start == 0:
        print('Not Prime')
        exit()
    start += 1

print('Prime')