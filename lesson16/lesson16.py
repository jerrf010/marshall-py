# Lesson 16
fizz = False
buzz = False
for i in range(50):
    i += 1
    if i % 3 == 0:
        fizz = True
    if i % 5 == 0:
        buzz = True

    if fizz == True and buzz == True:
        print('FizzBuzz')
    elif fizz == True and buzz == False:
        print('Fizz')
    elif fizz == False and buzz == True:
        print('Buzz')
    else:
        print(i)

    buzz = False
    fizz = False