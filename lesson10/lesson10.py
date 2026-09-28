# Lesson 10

first = int(input())
second = int(input())
third = int(input())
four = int(input())

if first >= 8:
    if second == third:
        if four >= 8:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')