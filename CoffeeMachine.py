money = 550
disposable_cups = 9
water = 400
milk = 540
coffee_beans = 120
loop_ = 1

while loop_ > 0:
    action = input("Write action (buy, fill, take, remaining, exit): \n")
    if action == "buy":
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if choice == "1" and water >= 250 and coffee_beans >= 16 and disposable_cups >= 1:
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4
            print("I have enough resources, making you a coffee!")
        elif choice == "2" and water >= 300 and milk >= 75 and coffee_beans >= 20 and disposable_cups >= 1:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7
            print("I have enough resources, making you a coffee!")
        elif choice == "3" and water >= 200 and milk >= 100 and coffee_beans >= 12 and disposable_cups >= 1:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6
            print("I have enough resources, making you a coffee!")
        elif choice == "back":
            continue
        else:
            if water < 300:
                print("Sorry, not enough water" )
                continue
            elif coffee_beans < 20:
                print("Sorry, not enough coffee")
                continue
            elif milk < 100:
                print("Sorry, not enough coffee")
                continue
            else:
                print("Sorry, not enough cups")
                continue

    elif action == "fill":
        water += int(input("Write how many ml of water do you want to add: \n"))
        milk += int(input("Write how many ml of milk do you want to add: \n"))
        coffee_beans += int(input("Write how many grams of coffee beans do you want to add: \n"))
        disposable_cups += int(input("Write how many disposable cups of coffee do you want to add: \n"))

    elif action == "take":
        print("I gave you", money)
        money = 0

    elif action == "remaining":
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(coffee_beans, "of coffee beans")
        print(disposable_cups, "of disposable cups")
        print(money, "of money")

    else:
        print("Good Bye :-)")
        break
