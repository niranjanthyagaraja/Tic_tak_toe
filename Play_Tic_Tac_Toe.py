#gloabal_variables
game = 0
list1 = []
a_size = 0
value_col = 0
count2 = 0
count1 = 0
p = 0
count3 = 0
counter = 0
counter1 = 0

#start main()
def main():
    print("WELCOME TO TIC_TAC_TOE")
    count = 0
#evaluating player1 name
    while True:
        name1 = input("Enter Player1 name:")
        if name1.isalpha():
            break
        else:
            print("Enter only alphabets")

#evaluating player2 name
    while True:
        name2 = input("Enter Player2 name:")
        if name2.isalpha():
            break
        else:
            print("Enter only alphabets")

#forcing the user to enter only odd numbers
    while True:
        bsize = int(input("Please enter the size of the board:"))
        n = bsize % 2
        if n == 0:
            print("Please enter an odd number ")
        else:
            break

    print("Let's start the Game!")
    print(name1 + " can only use 'X' and " + name2 + " can only use 'O'")

    # create the board
    for x in range(bsize):
        list1.append(["-"] * bsize)

    # end create board

    # check top diagonal elememnts
    def check_top_dig_win(bsize, counter, counter1):
        for i in range(bsize):
            if list1[i][i] == "X":
                counter += 1
                if counter == bsize:
                    print("Game Over!! " + name1 + " Wins")
                    list1[:] = []
                    main()
            elif list1[i][i] == "O":
                counter1 += 1
                if counter1 == bsize:
                    print("Game Over!! " + name2 + " Wins")
                    list1[:] = []
                    main()
            else:
                break

    # check bottom diagonal elements
    def check_bottom_dig_win(bsize, counter, counter1):
        j = bsize
        for i in range(bsize):
            if list1[i][j - 1] == "X":
                counter += 1
                j = j - 1
                if counter == bsize:
                    print("Game Over!!  " + name1 + "  Wins")
                    list1[:] = []
                    main()
            elif list1[i][j - 1] == "O":
                counter1 += 1
                j = j - 1
                if counter1 == bsize:
                    print("Game Over!!  " + name2 + "  Wins")
                    list1[:] = []
                    main()
            else:
                break

    # check each row element for  " + name1 + "
    def check_row_win_player1(bsize, counter):
        i = 0
        j = 0
        while i < bsize:
            counter = 0
            for j in range(bsize):
                if list1[i][j] == "X":
                    counter += 1
                    if counter == bsize:
                        print("Game Over!!  " + name1 + "  Wins")
                        list1[:] = []
                        main()
                else:
                    break
            i += 1

    # check each row element for player2
    def check_row_win_player2(bsize,counter):
        i = 0
        j = 0
        while i < bsize:
            counter = 0
            for j in range(bsize):
                if list1[i][j] == "O":
                    counter += 1
                    if counter == bsize:
                        print("Game Over!!  " + name2 + "  Wins")
                        list1[:] = []
                        main()
                else:
                    break
            i += 1

    # check each column element for player1
    def check_col_win_player1(bsize, counter):
        i = 0
        j = 0
        while i < bsize:
            counter = 0
            for j in range(bsize):
                if list1[j][i] == "X":
                    counter += 1
                    if counter == bsize:
                        print("Game Over!!  " + name1 + "  Wins")
                        list1[:] = []
                        main()
                else:
                    break
            i += 1

    # check each column element from player2
    def check_col_win_player2(bsize, counter):
        i = 0
        j = 0
        while i < bsize:
            counter = 0
            for j in range(bsize):
                if list1[j][i] == "O":
                    counter += 1
                    if counter == bsize:
                        print("Game Over!!  " + name2 + "  Wins")
                        list1[:] = []
                        main()
                else:
                    break
            i += 1

    # display the board
    def print_board(list1):
        for row in list1:
            print(" ".join(row))

    # end display

    print_board(list1)

    # getting player input
    def play_test1(count):
        print(name1 + "'s turn")
        value_row = int(input("Enter Row number: "))
        value_col = int(input("Enter Column number: "))
        count1 = player1_turn(value_row, value_col, bsize, count)
        check_top_dig_win(bsize, counter, counter1)
        check_bottom_dig_win(bsize, counter, counter1)
        check_row_win_player1(bsize, counter)
        check_col_win_player1(bsize, counter)
        return count1

    def play_test2(count):
        print(name2 + "'s turn")
        value_row1 = int(input("Enter Row number: "))
        value_col1 = int(input("Enter Column number: "))
        count1 = player2_turn(value_row1, value_col1, bsize, count)
        check_top_dig_win(bsize, counter, counter1)
        check_bottom_dig_win(bsize, counter, counter1)
        check_row_win_player2(bsize, counter)
        check_col_win_player2(bsize, counter)
        return count1

    # end of player input

    # evaulating the board and populating values
    def player1_turn(value_row, value_col, bsize, count):
        if (value_row < 0 or value_row >= bsize) or (value_col < 0 or value_col >= bsize):
            print("Co-ordinates does not exist")
            return count
        elif list1[value_row][value_col] == "X" or list1[value_row][value_col] == "O":
            print("You already have X/O in this position")
            return count
        else:
            list1[value_row][value_col] = "X"
            count += 1
            print_board(list1)
        return count

    def player2_turn(value_row1, value_col1, bsize, count):
        if (value_row1 < 0 or value_row1 >= bsize) or (value_col1 < 0 or value_col1 >= bsize):
            print("Co-ordinates does not exist")
            return count
        elif list1[value_row1][value_col1] == "O" or list1[value_row1][value_col1] == "X":
            print("You already have O/X in this position")
            return count
        else:
            list1[value_row1][value_col1] = "O"
            count += 1
            print_board(list1)
        return count

    # end of evaluation and population

    a_size = bsize ** 2
    count = 0
    while 0 < bsize:

        count2 = play_test1(count)
        count = count2
        if count2 == a_size:
            print("Game Over!!")
            list1[:] = []
            main()

        count2 = play_test2(count)
        count = count2
        if count2 == a_size:
            print("Game Over!!")
            list1[:] = []
            main()
#end main()

#invoking the main()
main()