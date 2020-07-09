cell_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
i = 0
x = "XXX"
o = "OOO"

win_places = (cell_list[0:3], cell_list[3:6], cell_list[6:9], cell_list[0:7:3],
        cell_list[1:8:3], cell_list[2:9:3], cell_list[0:9:4], cell_list[2:7:2])

def check_for_win(input_list):
    row1 = input_list[0] + " " + input_list[1] + " " + input_list[2]
    row2 = input_list[3] + " " + input_list[4] + " " + input_list[5]
    row3 = input_list[6] + " " + input_list[7] + " " + input_list[8]
    column1 = input_list[0] + " " + input_list[3] + " " + input_list[6]
    column2 = input_list[1] + " " + input_list[4] + " " + input_list[7]
    column3 = input_list[2] + " " + input_list[5] + " " + input_list[8]
    cross1 = input_list[0] + " " + input_list[4] + " " + input_list[8]
    cross2 = input_list[6] + " " + input_list[4] + " " + input_list[2]
    O_win = row1.count("O") == 3 or row2.count("O") == 3 or row3.count("O") == 3 \
            or column1.count("O") == 3 or column2.count("O") == 3 or column3.count("O") == 3 \
            or cross1.count("O") == 3 or cross2.count("O") == 3
    X_win = row1.count("X") == 3 or row2.count("X") == 3 or row3.count("X") == 3 \
            or column1.count("X") == 3 or column2.count("X") == 3 or column3.count("X") == 3 \
            or cross1.count("X") == 3 or cross2.count("X") == 3

    if O_win:
        return 1
    elif X_win:
        return 2
    elif int(input_list.count("X")) + int(input_list.count("O")) == 9:
        return 3
    else:
        return 0


print("---------")
print("| " + cell_list[0] + " " + cell_list[1] + " " + cell_list[2] + " |")
print("| " + cell_list[3] + " " + cell_list[4] + " " + cell_list[5] + " |")
print("| " + cell_list[6] + " " + cell_list[7] + " " + cell_list[8] + " |")
print("---------")

def coordinates(x, y):
    if x == 1:
        if y == 1:
            return 6
        elif y == 2:
            return 3
        elif y == 3:
            return 0
    elif x == 2:
        if y == 1:
            return 7
        elif y == 2:
            return 4
        elif y == 3:
            return 1
    elif x == 3:
        if y == 1:
            return 8
        elif y == 2:
            return 5
        elif y == 3:
            return 2
    else:
        return 100

def game_play_x():
    global cell_list
    global i
    numbers = [1, 2, 3]
    user_coordinates = input("Enter the coordinates:\n")
    num1, num2 = user_coordinates.split()
    if int(num1) > 3 or int(num1) < 0 or int(num2) > 3 or int(num2) < 0:
        print("Coordinates should be from 1 to 3!")
    elif int(num1) and int(num2) not in numbers:
        print("You should enter numbers!")
    elif coordinates(int(num1), int(num2)) != 100:
        if cell_list[coordinates(int(num1), int(num2))] == "X" or cell_list[
            coordinates(int(num1), int(num2))] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            cell_list[coordinates(int(num1), int(num2))] = 'X'
            i += 1
            print("---------")
            print("| " + cell_list[0] + " " + cell_list[1] + " " + cell_list[2] + " |")
            print("| " + cell_list[3] + " " + cell_list[4] + " " + cell_list[5] + " |")
            print("| " + cell_list[6] + " " + cell_list[7] + " " + cell_list[8] + " |")
            print("---------")

def game_play_o():
    global cell_list
    global i
    numbers = [1, 2, 3]
    user_coordinates = input("Enter the coordinates:\n")
    num1, num2 = user_coordinates.split()
    if int(num1) > 3 or int(num1) < 0 or int(num2) > 3 or int(num2) < 0:
        print("Coordinates should be from 1 to 3!")
    elif int(num1) and int(num2) not in numbers:
        print("You should enter numbers!")
    elif coordinates(int(num1), int(num2)) != 100:
        if cell_list[coordinates(int(num1), int(num2))] == "X" or cell_list[coordinates(int(num1), int(num2))] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            i += 1
            cell_list[coordinates(int(num1), int(num2))] = 'O'
            print("---------")
            print("| " + cell_list[0] + " " + cell_list[1] + " " + cell_list[2] + " |")
            print("| " + cell_list[3] + " " + cell_list[4] + " " + cell_list[5] + " |")
            print("| " + cell_list[6] + " " + cell_list[7] + " " + cell_list[8] + " |")
            print("---------")

def loop_game():
    global cell_list
    global i
    while check_for_win(cell_list) == 0:  # change this loop and the code will be completed
        if i % 2 == 0:
            game_play_x()
        elif i % 2 != 0:
            game_play_o()
    if check_for_win(cell_list) == 2:
        print("X wins!")
    elif check_for_win(cell_list) == 1:
        print("O wins!")
    elif check_for_win(cell_list) == 3:
        print("Draw!")
loop_game()