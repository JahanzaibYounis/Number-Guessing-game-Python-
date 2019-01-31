
from random import randint
number = randint(1, 100)
guess = list()
while True:
    x = int(input('Guess the number \n'))
    guess.append(x)
    if x not in range(1, 101):
        print('OUT OF BOUND \nThe number should be between 1 and 100')
    elif x in range(number-10, number+11) and x != number:
        if len(guess) != 1:
            if abs(number-x) <= abs(number-guess[-2]):
                print('warmer')
            elif abs(number-x) > abs(number-guess[-2]):
                print('colder')
        else:
            print('warm')
    elif x not in range(number-10, number+11):
        print('cold')
    elif x == number:
        print('jackpot')
        print('You have guessed the right number in', len(guess), 'tries')
        exit()




