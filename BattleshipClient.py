import socket

#   TODO clean up any other input errors or other types of errors that could awry from people being stupid

host = "Place your server here"
port = 5051
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
num = s.recv(1024)
num = num.decode("utf-8")

def setup():
    if num == "p2":
        play2()
    elif num == "p1":
        play1()
    else:
        print("\nWasn't assigned\n")


board = []
board2 = []
row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for x in range(1, 11):
    board2.append(["Q"] * 10)


def print_board2(board2):
    print("  1 2 3 4 5 6 7 8 9 10")
    for r in range(len(row)):
        print(row[r] + " " + " ".join(board2[r]))


for x in range(1, 11):
    board.append(["O"] * 10)


def print_board(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for r in range(len(row)):
        print(row[r] + " " + " ".join(board[r]))


def ship5_place():
    while True:
        print("\nPlacing the Aircraft Carrier: 5 piece\n")
        print("\nStarting Position of Boat\n")
        ship_row = input("Ship Row: ")
        ship_col = input("Ship Column: ")
        if ship_col.isdigit() == True:
            ship_col = int(ship_col) - 1
        else:
            print("\nColumn wasn't a number\n")
        if ship_row.lower() == "a":
            ship_row = 0
        elif ship_row.lower() == "b":
            ship_row = 1
        elif ship_row.lower() == "c":
            ship_row = 2
        elif ship_row.lower() == "d":
            ship_row = 3
        elif ship_row.lower() == "e":
            ship_row = 4
        elif ship_row.lower() == "f":
            ship_row = 5
        elif ship_row.lower() == "g":
            ship_row = 6
        elif ship_row.lower() == "h":
            ship_row = 7
        elif ship_row.lower() == "i":
            ship_row = 8
        elif ship_row.lower() == "j":
            ship_row = 9
        else:
            print("\nRow wasn't a letter between A and J\n")

        if ship_row not in range(10) or ship_col not in range(10):
            print("\nLand Ho!\n")
        elif board[ship_row][ship_col] == 'S':
            print("\nShip Collision\n")
        else:
            an = input("\nPlace the rest of the ship on that row(r) or column(c): ")
            if an.lower() == "row" or an.lower() == "r":
                an2 = input("\nGo to the right(r) or the left(l) on the row: ")
                if an2.lower() == "left" or an2.lower() == "l":
                    if (ship_row - 4) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col - 1] = 'S'
                        board[ship_row][ship_col - 2] = 'S'
                        board[ship_row][ship_col - 3] = 'S'
                        board[ship_row][ship_col - 4] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an2.lower() == "right" or an2.lower() == "r":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col + 1] = 'S'
                        board[ship_row][ship_col + 2] = 'S'
                        board[ship_row][ship_col + 3] = 'S'
                        board[ship_row][ship_col + 4] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")

            elif an.lower() == "column" or an.lower() == "c":
                an3 = input("\nGo up(u) or down(d) the column: ")
                if an3.lower() == "up" or an3 == "u":
                    if (ship_row - 4) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row - 1][ship_col] = 'S'
                        board[ship_row - 2][ship_col] = 'S'
                        board[ship_row - 3][ship_col] = 'S'
                        board[ship_row - 4][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an3.lower() == "down" or an3 == "d":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row + 1][ship_col] = 'S'
                        board[ship_row + 2][ship_col] = 'S'
                        board[ship_row + 3][ship_col] = 'S'
                        board[ship_row + 4][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")
            else:
                print("\nSomethings not right\n")


def ship4_place():
    while True:
        print("\nPlacing the Battleship: 4 piece\n")
        print("\nStarting Position of Boat\n")
        ship_row = input("Ship Row: ")
        ship_col = input("Ship Column: ")
        if ship_col.isdigit() == True:
            ship_col = int(ship_col) - 1
        else:
            print("\nColumn wasn't a number\n")
        if ship_row.lower() == "a":
            ship_row = 0
        elif ship_row.lower() == "b":
            ship_row = 1
        elif ship_row.lower() == "c":
            ship_row = 2
        elif ship_row.lower() == "d":
            ship_row = 3
        elif ship_row.lower() == "e":
            ship_row = 4
        elif ship_row.lower() == "f":
            ship_row = 5
        elif ship_row.lower() == "g":
            ship_row = 6
        elif ship_row.lower() == "h":
            ship_row = 7
        elif ship_row.lower() == "i":
            ship_row = 8
        elif ship_row.lower() == "j":
            ship_row = 9
        else:
            print("\nRow wasn't a letter between A and J\n")
        if ship_row not in range(10) or ship_col not in range(10):
            print("\nLand Ho!\n")
        elif board[ship_row][ship_col] == 'S':
            print("\nShip Collision\n")
        else:
            an = input("\nPlace the rest of the ship on that row(r) or column(c): ")
            if an.lower() == "row" or an.lower() == "r":
                an2 = input("\nGo to the right(r) or the left(l) on the row: ")
                if an2.lower() == "left" or an2.lower() == "l":
                    if (ship_row - 3) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col - 1] = 'S'
                        board[ship_row][ship_col - 2] = 'S'
                        board[ship_row][ship_col - 3] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an2.lower() == "right" or an2 == "l":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col + 1] = 'S'
                        board[ship_row][ship_col + 2] = 'S'
                        board[ship_row][ship_col + 3] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")

            elif an.lower() == "column" or an.lower() == "c":
                an3 = input("\nGo up(u) or down(d) the column: ")
                if an3.lower() == "up" or an3.lower() == "u":
                    if (ship_row - 3) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row - 1][ship_col] = 'S'
                        board[ship_row - 2][ship_col] = 'S'
                        board[ship_row - 3][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an3.lower() == "down" or an3.lower() == "d":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row + 1][ship_col] = 'S'
                        board[ship_row + 2][ship_col] = 'S'
                        board[ship_row + 3][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")
            else:
                print("\nSomethings not right\n")


def ship3_place():
    while True:
        print("\nPlacing the Cruiser: 3 piece\n")
        print("\nStarting Position of Boat\n")
        ship_row = input("Ship Row: ")
        ship_col = input("Ship Column: ")
        if ship_col.isdigit() == True:
            ship_col = int(ship_col) - 1
        else:
            print("\nColumn wasn't a number\n")
        if ship_row.lower() == "a":
            ship_row = 0
        elif ship_row.lower() == "b":
            ship_row = 1
        elif ship_row.lower() == "c":
            ship_row = 2
        elif ship_row.lower() == "d":
            ship_row = 3
        elif ship_row.lower() == "e":
            ship_row = 4
        elif ship_row.lower() == "f":
            ship_row = 5
        elif ship_row.lower() == "g":
            ship_row = 6
        elif ship_row.lower() == "h":
            ship_row = 7
        elif ship_row.lower() == "i":
            ship_row = 8
        elif ship_row.lower() == "j":
            ship_row = 9
        else:
            print("\nRow wasn't a letter between A and J\n")
        if ship_row not in range(10) or ship_col not in range(10):
            print("\nLand Ho!\n")
        elif board[ship_row][ship_col] == 'S':
            print("\nShip Collision\n")
        else:
            an = input("\nPlace the rest of the ship on that row(r) or column(c): ")
            if an.lower() == "row" or an.lower() == "r":
                an2 = input("\nGo to the right(r) or the left(l) on the row: ")
                if an2 == "left" or an2.lower() == "l":
                    if (ship_row - 2) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col - 1] = 'S'
                        board[ship_row][ship_col - 2] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an2.lower() == "right" or an2.lower() == "r":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col + 1] = 'S'
                        board[ship_row][ship_col + 2] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")

            elif an.lower() == "column" or an.lower() == "c":
                an3 = input("\nGo up(u) or down(d) the column: ")
                if an3.lower() == "up" or an3.lower() == "u":
                    if (ship_row - 2) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row - 1][ship_col] = 'S'
                        board[ship_row - 2][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an3.lower() == "down" or an3.lower() == "d":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("Land Ho!")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row + 1][ship_col] = 'S'
                        board[ship_row + 2][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")
            else:
                print("\nSomethings not right\n")


def ship32_place():
    while True:
        print("\nPlacing the Submarine: 3 piece\n")
        print("\nStarting Position of Boat\n")
        ship_row = input("Ship Row: ")
        ship_col = input("Ship Column: ")
        if ship_col.isdigit() == True:
            ship_col = int(ship_col) - 1
        else:
            print("\nColumn wasn't a number\n")
        if ship_row.lower() == "a":
            ship_row = 0
        elif ship_row.lower() == "b":
            ship_row = 1
        elif ship_row.lower() == "c":
            ship_row = 2
        elif ship_row.lower() == "d":
            ship_row = 3
        elif ship_row.lower() == "e":
            ship_row = 4
        elif ship_row.lower() == "f":
            ship_row = 5
        elif ship_row.lower() == "g":
            ship_row = 6
        elif ship_row.lower() == "h":
            ship_row = 7
        elif ship_row.lower() == "i":
            ship_row = 8
        elif ship_row.lower() == "j":
            ship_row = 9
        else:
            print("\nRow wasn't a letter between A and J\n")
        if ship_row not in range(10) or ship_col not in range(10):
            print("\nLand Ho!\n")
        elif board[ship_row][ship_col] == 'S':
            print("\nShip Collision\n")
        else:
            an = input("\nPlace the rest of the ship on that row(r) or column(c): ")
            if an.lower() == "row" or an.lower() == "r":
                an2 = input("\nGo to the right(r) or the left(l) on the row: ")
                if an2.lower() == "left" or an2.lower() == "l":
                    if (ship_row - 2) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col - 1] = 'S'
                        board[ship_row][ship_col - 2] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an2.lower() == "right" or an2.lower() == "r":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col + 1] = 'S'
                        board[ship_row][ship_col + 2] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")

            elif an.lower() == "column" or an.lower() == "c":
                an3 = input("\nGo up(u) or down(d) the column: ")
                if an3.lower() == "up" or an3.lower() == "u":
                    if (ship_row - 2) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row - 1][ship_col] = 'S'
                        board[ship_row - 2][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an3.lower() == "down" or an3.lower() == "d":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row + 1][ship_col] = 'S'
                        board[ship_row + 2][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")
            else:
                print("\nSomethings not right\n")


def ship2_place():
    while True:
        print("\nPlacing the Aircraft Destroyer: 2 piece\n")
        print("\nStarting Position of Boat\n")
        ship_row = input("Ship Row: ")
        ship_col = input("Ship Column: ")
        if ship_col.isdigit() == True:
            ship_col = int(ship_col) - 1
        else:
            print("\nColumn wasn't a number\n")
        if ship_row.lower() == "a":
            ship_row = 0
        elif ship_row.lower() == "b":
            ship_row = 1
        elif ship_row.lower() == "c":
            ship_row = 2
        elif ship_row.lower() == "d":
            ship_row = 3
        elif ship_row.lower() == "e":
            ship_row = 4
        elif ship_row.lower() == "f":
            ship_row = 5
        elif ship_row.lower() == "g":
            ship_row = 6
        elif ship_row.lower() == "h":
            ship_row = 7
        elif ship_row.lower() == "i":
            ship_row = 8
        elif ship_row.lower() == "j":
            ship_row = 9
        else:
            print("Row wasn't a letter between A and J")
        if ship_row not in range(10) or ship_col not in range(10):
            print("\nLand Ho!\n")
        elif board[ship_row][ship_col] == 'S':
            print("\nShip Collision\n")
        else:
            an = input("\nPlace the rest of the ship on that row(r) or column(c): ")
            if an.lower() == "row" == an.lower() == "r":
                an2 = input("\nGo to the right(r) or the left(l) on the row: ")
                if an2.lower() == "left" or an2.lower() == "l":
                    if (ship_row - 1) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col - 1] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an2.lower() == "right" or an2.lower() == "r":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row][ship_col + 1] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")

            elif an.lower() == "column" or an.lower() == "c":
                an3 = input("\nGo up(u) or down(d) the column: ")
                if an3.lower() == "up" or an3.lower() == "u":
                    if (ship_row - 1) < 0:
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row - 1][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                elif an3.lower() == "down" or an3.lower() == "d":
                    if ship_row not in range(10) or ship_col not in range(10):
                        print("\nLand Ho!\n")
                    else:
                        board[ship_row][ship_col] = 'S'
                        board[ship_row + 1][ship_col] = 'S'
                        print("\nShip Placed\n")
                        print_board(board)
                        print("")
                        break
                else:
                    print("\nSomethings not right\n")
            else:
                print("\nSomethings not right try again\n")

def play1():
    print("\nYour Player One: You go First\n")
    print_board(board)
    print("")
    ship5_place()
    ship4_place()
    ship3_place()
    ship32_place()
    ship2_place()
    ships = 0
    ships2 = 0
    while ships < 15 or ships < 15:
        while True:
            print("")
            print_board2(board2)
            print("")
            guess_row = input("Guess Row: ")
            guess_col = input("Guess Col: ")
            if guess_col.isdigit() == True:
                guess_col = int(guess_col) - 1
            else:
                print("\nColumn wasn't a number\n")
            if guess_row.lower() == "a":
                guess_row = 1
            elif guess_row.lower() == "b":
                guess_row = 2
            elif guess_row.lower() == "c":
                guess_row = 3
            elif guess_row.lower() == "d":
                guess_row = 4
            elif guess_row.lower() == "e":
                guess_row = 5
            elif guess_row.lower() == "f":
                guess_row = 6
            elif guess_row.lower() == "g":
                guess_row = 7
            elif guess_row.lower() == "h":
                guess_row = 8
            elif guess_row.lower() == "i":
                guess_row = 9
            elif guess_row.lower() == "j":
                guess_row = 10
            else:
                print("\nRow wasn't a letter between A and J\n")

            s.send(("p1|" + str(guess_row)).encode("utf-8"))
            s.send(("p1|" + str(guess_col)).encode("utf-8"))
            data = s.recv(1024)
            data = data.decode("utf-8")
            print("\n" + data + "\n")
            if not data:
                break
            if data == "miss":
                board2[int(guess_row) - 1][int(guess_col) - 1] = "X"
                print("")
                print_board2(board2)
                print("")
                break
            elif data == "hit":
                board2[int(guess_row) - 1][int(guess_col) - 1] = "S"
                print("")
                print_board2(board2)
                print("")
                ships2 = ships2 + 1
                print("\nYou get to go again\n")
            else:
                print("\nDA FAQ\n")

        while True:
            p2guess_row = s.recv(1024)
            p2guess_col = s.recv(1024)
            p2guess_col = p2guess_col.decode("utf-8")
            p2guess_row = p2guess_row.decode("utf-8")
            p2guess_col = int(p2guess_col) - 1
            p2guess_row = int(p2guess_row) - 1
            if board[int(p2guess_row)][int(p2guess_col)] == "X":
                print("\nThey already hit that location idiots.\n")
            elif board[int(p2guess_row)][int(p2guess_col)] == 'S':
                print("\nThey sank your battleship!\n")
                board[int(p2guess_row)][int(p2guess_col)] = "X"
                ships = ships + 1
                s.send("p1|hit".encode("utf-8"))
                print("")
                print_board(board)
                print("\nThey get to go again\n")
            else:
                board[int(p2guess_row)][int(p2guess_col)] = "X"
                print("\nThey missed your battleship!\n")
                s.send("p1|miss".encode("utf-8"))
                print("")
                print_board(board)
                print("")
                break
    print("\nGame Over\n")

def play2():
    print("\nYou are Player Two: You go Second\n")
    print_board(board)
    print("")
    ship5_place()
    ship4_place()
    ship3_place()
    ship32_place()
    ship2_place()
    ships = 0
    ships2 = 0
    while ships < 15 or ships2 < 15:
        while True:
            print("")
            print_board2(board2)
            print("")
            p2guess_row = s.recv(1024)
            p2guess_col = s.recv(1024)
            p2guess_col = p2guess_col.decode("utf-8")
            p2guess_row = p2guess_row.decode("utf-8")
            p2guess_col = int(p2guess_col) - 1
            p2guess_row = int(p2guess_row) - 1
            if board[p2guess_row][p2guess_col] == "X":
                print("\nThey already hit that location idiots.\n")
            elif board[p2guess_row][p2guess_col] == 'S':
                print("\nThey sank your battleship!\n")
                board[p2guess_row][p2guess_col] = "X"
                ships = ships + 1
                s.send("p2|hit".encode("utf-8"))
                print("")
                print_board(board)
                print("\nThey get to go again\n")
            else:
                board[p2guess_row][p2guess_col] = "X"
                print("\nThey missed your battleship!\n")
                s.send("p2|miss".encode("utf-8"))
                print("")
                print_board(board)
                print("")
                break

        while True:
            guess_row = input("Guess Row: ")
            guess_col = input("Guess Col: ")
            if guess_col.isdigit() == True:
                guess_col = int(guess_col) - 1
            else:
                print("\nColumn wasn't a number\n")
            if guess_row.lower() == "a":
                guess_row = 1
            elif guess_row.lower() == "b":
                guess_row = 2
            elif guess_row.lower() == "c":
                guess_row = 3
            elif guess_row.lower() == "d":
                guess_row = 4
            elif guess_row.lower() == "e":
                guess_row = 5
            elif guess_row.lower() == "f":
                guess_row = 6
            elif guess_row.lower() == "g":
                guess_row = 7
            elif guess_row.lower() == "h":
                guess_row = 8
            elif guess_row.lower() == "i":
                guess_row = 9
            elif guess_row.lower() == "j":
                guess_row = 10
            else:
                print("Row wasn't a letter between A and J")

            s.send(("p2|" + str(guess_row)).encode("utf-8"))
            s.send(("p2|" + str(guess_col)).encode("utf-8"))
            data = s.recv(1024)
            data = data.decode("utf-8")
            print("\n" + data + "\n")
            if not data:
                break
            if data == "miss":
                board2[int(guess_row) - 1][int(guess_col) - 1] = "X"
                print("")
                print_board2(board2)
                print("")
                break
            elif data == "hit":
                board2[int(guess_row) - 1][int(guess_col) - 1] = "S"
                print("")
                print_board2(board2)
                print("\nYou get to go again\n")
                ships2 = ships2 + 1
            else:
                print("\nDA FAQ\n")
    print("\nGame Over\n")

def main():
    setup()

if __name__ == "__main__":
    main()