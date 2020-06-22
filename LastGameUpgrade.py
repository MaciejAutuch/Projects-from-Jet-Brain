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
        (key, val) = line.split(" ")
        score_dictionary[key] = int(val)

score = score_dictionary.get(user_name)

game_options = input()
if game_options == " " or game_options == "":
    options = ['rock', 'paper', 'scissors']
else:
    options = game_options.split(",")

print("Okay, let's start")

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

def more_complicated_game(user, cpu):
    global score
    num = int(options.index(user))
    after_list = options[num + 1:]
    before_list = options[:num]
    after_list.extend(before_list)
    n = int(len(after_list)) // 2
    win_combo = after_list[0:n]
    if user == cpu:
        print(f'There is a draw ({user})')
        score += 50
    elif num < n and cpu in win_combo:
        print(f'Sorry, but computer chose {cpu}')
    elif num >= n and cpu in win_combo:
        print(f'Sorry, but computer chose {cpu}')
    else:
        print(f'Well done. Computer chose {cpu} and failed')
        score += 100

while True:
    player_input = input().lower()
    computer_choice = random.choice(options)
    if player_input in options:
        if game_options == " " or game_options == "":
            result(player_input, computer_choice)
        else:
            more_complicated_game(player_input, computer_choice)
    elif player_input == "!exit":
        print('Bye!')
        break
    elif player_input == "!rating":
        print("Your rating:", int(score))
    else:
        print('Invalid input')
