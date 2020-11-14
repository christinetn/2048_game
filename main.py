from utilities import place_random, print_board

DEV_MODE = False


def merge_left(game_board):
    for i in range(4):  # row (0-3)
        changed = [False, False, False, False] #default false
        for j in range(1, 4):  # column (1-3)

            for k in range(j):  # number of hops
                if game_board[i][j - 1 - k] == 0: #shifts to left
                    game_board[i][j - 1 - k] = game_board[i][j - k]
                    game_board[i][j - k] = 0
                if game_board[i][j - k] == game_board[i][j - 1 - k]:
                    if (changed[j - k - 1] or changed[j - k]): #checks if value is already changed
                        pass                                   #if changed already pass, else merge
                    else:
                        game_board[i][j - k - 1] = game_board[i][j - k] * 2
                        game_board[i][j - k] = 0
                        changed[j - k - 1] = True


def merge_right(game_board):
    for i in range(4):  # row
        changed = [False, False, False, False]
        for j in range(2, -1, -1):

            for k in range(3 - j):  # number of hops
                if game_board[i][j + 1 + k] == 0:
                    game_board[i][j + 1 + k] = game_board[i][j + k]
                    game_board[i][j + k] = 0
                if game_board[i][j + k] == game_board[i][j + 1 + k]:
                    if (changed[j + k] or changed[j + k + 1]):
                        pass
                    else:
                        game_board[i][j + k + 1] = game_board[i][j + k + 1] * 2
                        game_board[i][j + k] = 0
                        changed[j + k + 1] = True


def merge_up(game_board):
    for i in range(4):  # column
        changed = [False, False, False, False]
        for j in range(1, 4):

            for k in range(j):  # number of hops
                if game_board[j - 1 - k][i] == 0:
                    game_board[j - 1 - k][i] = game_board[j - k][i]
                    game_board[j - k][i] = 0
                if game_board[j - k][i] == game_board[j - 1 - k][i]:
                    if (changed[j - k - 1] or changed[j - k]):
                        pass
                    else:
                        game_board[j - k - 1][i] = game_board[j - k][i] * 2
                        game_board[j - k][i] = 0
                        changed[j - k - 1] = True


def merge_down(game_board):
    for i in range(4):  # row
        changed = [False, False, False, False]
        for j in range(2, -1, -1):

            for k in range(3 - j):  # number of hops
                if game_board[j + 1 + k][i] == 0:
                    game_board[j + 1 + k][i] = game_board[j + k][i]
                    game_board[j + k][i] = 0
                if game_board[j + k][i] == game_board[j + 1 + k][i]:
                    if (changed[j + k] or changed[j + k + 1]):
                        pass
                    else:
                        game_board[j + k + 1][i] = game_board[j + k + 1][i] * 2
                        game_board[j + k][i] = 0
                        changed[j + k + 1] = True


def game_over(game_board: [[int, ], ]) -> bool:
    #case 1: empty space does not equal game over
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == 0:
                return False

    #case 2: check for horizontal valid moves
    for i in range(4):
        for j in range(3):
            if game_board[i][j] == game_board[i][j + 1]:
                return False
    #case:3 check for vertical valid moves
    for i in range(3):
        for j in range(4):
            if game_board[i][j] == game_board[i + 1][j]:
                return False

    #game is over
    return True

def main(game_board: [[int, ], ]) -> [[int, ], ]:

    #retrieve random number
    def random():
        random_value = place_random(game_board)
        row = random_value['row']
        column = random_value['column']
        target = random_value['value']
        game_board[row][column] = target

    random()

    while True:
        #reset user input
        direction = '0'

        #tests
        if DEV_MODE:
            # This line of code handles the input of the develop mode.
            column, row, value = (int(i) for i in input("column,row,value:").split(','))
            game_board[row - 1][column - 1] = value

        else:
            random()
            pass

        #check if game is over
        game_over(game_board)

        print_board(game_board)

        #user input
        direction = input('What is your move? A: move left, D: move right, W: move up, S: move down \n')

        #check for valid keys
        if direction == 'a':
            merge_left(game_board)
        elif direction == 'd':
            merge_right(game_board)
        elif direction == 'w':
            merge_up(game_board)
        elif direction == 's':
            merge_down(game_board)
        elif direction == 'q': #if quit, terminate
            break


        # Check if the user wins (2048)
        for i in range(4):
            for j in range(4):
                if game_board[i][j] == 2048:
                    return True

    return game_board


if __name__ == "__main__":
    main([[0, 4, 2, 2],
          [2, 2, 4, 2],
          [0, 2, 0, 0],
          [0, 0, 0, 0]])
