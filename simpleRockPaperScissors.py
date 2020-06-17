import random

def random_cpu():
    user_input = input()
    combo_list = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(combo_list)
    if user_input == cpu_choice:
        print(f"There is a draw ({user_input})")
    else:
        if user_input == "rock" and cpu_choice == "paper":
            print(f"Sorry, but computer chose {cpu_choice}")
        elif user_input == "paper" and cpu_choice == "scissors":
            print(f"Sorry, but computer chose {cpu_choice}")
        elif user_input == "scissors" and cpu_choice == "rock":
            print(f"Sorry, but computer chose {cpu_choice}")
        else:
            print(f"Well done. Computer chose {cpu_choice} and failed")
random_cpu()