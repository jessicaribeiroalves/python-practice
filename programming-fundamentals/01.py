import random


def setting_range():
    start_range = input('Enter the start of the range: ')
    while (start_range.isalpha()) or (int(start_range) < 0):
        print('Please enter a valid number.')
        start_range = input('Enter the start of the range: ')
    end_range = input('Enter the end of the range: ')
    while (end_range.isalpha()) or (int(end_range) <= int(start_range)):
        print('Please enter a valid number.')
        end_range = input('Enter the end of the range: ')

    return (int(start_range), int(end_range))


ranges = setting_range()
random_number = random.randint(ranges[0], ranges[1])
guesses_counter = 0
user_guess = '0'
while int(user_guess) != random_number:
    user_guess = input('Guess a number: ')
    guesses_counter += 1
    if user_guess.isalpha():
        print('Please enter a valid number.')
        user_guess = '0'
        guesses_counter -= 1

if guesses_counter == 1:
    print('You guessed the number in 1 attempt')
else:
    print(f'You guessed the number in {guesses_counter} attempts')
