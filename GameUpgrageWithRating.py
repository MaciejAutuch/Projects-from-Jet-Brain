import random

file = open("rating.txt", "a+")
user_name = input("Enter your name: ")
print("Hello " + user_name)
file.readlines()
if user_name not in file:
    file.writelines("\n" + user_name + " 0")
file.close()

score_dictionary = {}
with open("rating.txt") as f:
    for line in f:
        (key, val) = line.split()
        score_dictionary[key] = int(val)

score = score_dictionary.get(user_name)

def result(user, cpu):
    win_combo = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    global score
    if user == cpu:
        print(f'There is a draw ({user})')
        score += 50
    elif win_combo.get(user) == cpu:
        print(f'Well done. Computer chose {cpu} and failed')
        score += 100
    else:
        print(f'Sorry, but computer chose {cpu}')

options = ['rock', 'paper', 'scissors']

while True:
    player_input = input().lower()
    computer_choice = random.choice(options)
    if player_input in options:
        result(player_input, computer_choice)
    elif player_input == "!exit":
        print('Bye!')
        break
    elif player_input == "!rating":
        print("Your rating:", int(score))

    else:
        print('Invalid input')
