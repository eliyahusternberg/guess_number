import random

print('---------------------------------')
print('    GUESS THAT NUMBER GAME  ')
print('---------------------------------')
print()

the_number = random.randint(0, 100)

guess =-1
guesses = 0
number_of_guesses = 5

name = input('Player what is your name? ')


while guesses < 5 and guess != the_number  :
    print('You have {} guesses left'.format(number_of_guesses))
    guess_text = input('{} guess a number between 0 and 100:'.format(name.upper()))
    guess = int(guess_text)
    guesses = guesses + 1
    number_of_guesses = number_of_guesses -1


    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW'.format(name,guess))

    elif guess > the_number:
        print('Sorry {}, your guess of {} was too High'.format(name,guess))



    else:
        print('Excellent work {}, you won it was {}!'.format(name,guess))

if guess != the_number:
    print('Sorry {}, you are out of guesses, the correct number was {}'.format(name,the_number))

