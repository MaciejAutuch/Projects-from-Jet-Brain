import random

print("""1. Create an account
2. Log into account
0. Exit""")


def altElement(a):
    return a[::2]


def otherElement(b):
    return b[1::2]


def luhn_algorithm(card_to_check):
    sum_of_the_odd = 0
    sum_of_the_rest = 0
    card_list = [int(d) for d in str(card_to_check)]  # making the 15 digit string an int list
    only_odd_digits = altElement(card_list)
    rest_of_the_digits = otherElement(card_list)

    for i in only_odd_digits:
        new_num = int(i) * 2
        if new_num > 9:
            new_num -= 9
        sum_of_the_odd += new_num

    for g in rest_of_the_digits:
        sum_of_the_rest += g
    sum_of_numbers = sum_of_the_odd + sum_of_the_rest

    if sum_of_numbers % 10 == 0:
        card_number = str(card_to_check) + "0"
        return int(card_number)

    else:
        for x in range(0, 10):
            if (sum_of_numbers + x) % 10 == 0:
                m = str(x)
                card_number = str(card_to_check) + m
                return int(card_number)

def menu_function():
    account = []
    while True:
        user_input = int(input())
        if user_input == 0:
            break
        elif user_input == 1:
            new_card_number = str(random.randint(400000100000000,400000999999999))
            new_pin = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 4)])
            card_number = str(luhn_algorithm(new_card_number))
            account.append(card_number)
            account.append(new_pin)
            print("Your card has been created")
            print("Your card number:")
            print(str(luhn_algorithm(new_card_number)))
            print("Your card PIN:")
            print(new_pin)
        elif user_input == 2:
            input_card = input("Enter your card number:\n")
            input_pin = input("Enter your PIN:\n")
            if input_card in account:
                n = input_card.index(input_card)
                if input_pin == account[n + 1]:
                    print("You have successfully logged in!")
                else:
                    print("Wrong card number or PIN!")
            else:
                print("Wrong card number or PIN!")

menu_function()
