import random
import sqlite3

account = []

print("""1. Create an account
2. Log into account
0. Exit""")

def altElement(a):
    return a[::2]

def otherElement(b):
    return b[1::2]

def database_creation():
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS card (
                                id INTEGER PRIMARY KEY,
                                number TEXT NOT NULL,
                                pin text NOT NULL,
                                balance INTEGER DEFAULT 0);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()

database_creation()

def insert_to_database(id, card_number, pin, balance):
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()

        cursor.execute("INSERT INTO card (id, number, pin, balance) values (?, ?, ?, ?)",
                    (id, card_number, pin, balance))
        sqliteConnection.commit()
        print("Record inserted successfully into card table ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

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

def transfer_possibility(card_number):
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()
        for row in cursor.execute("SELECT balance FROM card WHERE number = ?", (card_number,)):
            card_balance = row[0]
            return int(card_balance)
        else:
            card_balance = 0
            return card_balance
    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def balance_check(card_number):
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT balance FROM card WHERE number = ?", card_number)
        sqliteConnection.commit()
        print("Record accessed")
        balance = cursor.fetchone()
        print(balance)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def add_income(card_number):
    extra_money = int(input("Enter income:\n"))
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()
        update_querry = """UPDATE card SET balance = balance + ? WHERE number = ?"""
        data = (extra_money, card_number)
        cursor.execute(update_querry, data)
        sqliteConnection.commit()
        print("Income was added!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def do_transfer(card_number):
    print("Transfer")
    money_destination = input("Enter card number:\n")
    number_check = money_destination[:15]
    if int(money_destination[0]) != 4:
        print("Such a card does not exist.")
    elif str(luhn_algorithm(number_check)) != money_destination:
        print("Probably you made mistake in the card number. Please try again!")
    elif str(luhn_algorithm(number_check)) == money_destination:
        amount_transfered = int(input("Enter how much money you want to transfer:\n"))
        result = transfer_possibility(card_number)
        if result is None:
            result = 0
        if result < amount_transfered:
            print("Not enough money!")
        else:
            try:
                sqliteConnection = sqlite3.connect('card.s3db')
                cursor = sqliteConnection.cursor()
                cursor.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount_transfered, money_destination))  # I might have a mistake here as well...
                cursor.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount_transfered, card_number))
                sqliteConnection.commit()
                print("Success!")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
    else:
        print("Such a card does not exist.")

def close_account(card_number):
    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()

        cursor.execute("DELETE FROM card WHERE number = ?", (card_number,))
        sqliteConnection.commit()
        print("You have deleted your account!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def baking_menu(input_card):
    print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")
    while True:
        user_input = int(input())
        if user_input == 0:
            print("Bye")
            quit()
        elif user_input == 1:
            balance_check(input_card)
        elif user_input == 2:
            add_income(input_card)
        elif user_input == 3:
            do_transfer(input_card)
        elif user_input == 4:
            close_account(input_card)
        elif user_input == 5:
            print("You have logged out from your account!")
            continue

def menu_function():
    while True:
        user_option = int(input())
        if user_option == 0:
            break
        elif user_option == 1:
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
            card_id = random.randint(1, 100000)
            balance = 0
            insert_to_database(card_id, str(luhn_algorithm(new_card_number)), new_pin, balance)
        elif user_option == 2:
            input_card = input("Enter your card number:\n")
            input_pin = input("Enter your PIN:\n")
            if input_card in account:
                n = input_card.index(input_card)
                if input_pin == account[n + 1]:
                    print("You have successfully logged in!")
                    baking_menu(input_card)
                else:
                    print("Wrong card number or PIN!")
            else:
                print("Wrong card number or PIN!")

menu_function()


