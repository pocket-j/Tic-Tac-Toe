def save_list(user_input_list):
    temp_list = []
    li = []
    for ele in range(len(user_input_list)):
        temp_list.append(user_input_list[ele])
        if len(temp_list) == 3:
            li.append(temp_list)
            temp_list = []
    return li


def print_board(output_lists):
    print("---------")
    for rr in range(0, 3):
        print(f'| {output_lists[rr][0]} {output_lists[rr][1]} {output_lists[rr][2]} |')
    print("---------")


def check_row_win(ol):
    li = ''
    for row in range(len(ol)):
        if '_' in (ol[row][0], ol[row][1], ol[row][2]):
            continue
        elif len({ol[row][0], ol[row][1], ol[row][2]}) == 1:
            li = ol[row][0]
            print(f'{li} wins')
    return li


def check_column_win(ol):
    li = ''
    for column in range(len(ol)):
        if '_' in (ol[0][column], ol[1][column], ol[2][column]):
            continue
        elif len({ol[0][column], ol[1][column], ol[2][column]}) == 1:
            li[0] += 1
            li = ol[0][column]
            print(f'{li} wins')
    return li


def check_diagonal_win(ol):
    li = False
    if (len({ol[0][0], ol[1][1], ol[2][2]}) == 1 or len({ol[0][2], ol[1][1], ol[2][0]}) == 1) and ol[1][1] != '_':
        li = ol[1][1]
        print(f'{li} wins')
    return li


def game_check(ol):
    row = check_row_win(ol)
    column = check_column_win(ol)
    diagonal = check_diagonal_win(ol)
    if any([row, column, diagonal]):
        return True
    else:
        return False


user_list = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
output_list = save_list(user_list)
print_board(output_list)
player = True
flag = True
count = 0


while count < 9:
    (x, y) = (input('Enter the coordinates: ')).split()
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)
        if 1 <= x <= 3 and 1 <= y <= 3:
            ii = 3 - y
            jj = x - 1
            if output_list[ii][jj] == '_':
                count += 1
                if player:
                    output_list[ii][jj] = 'X'
                    player = False
                else:
                    output_list[ii][jj] = 'O'
                    player = True
                print_board(output_list)
                if game_check(output_list):
                    flag = False
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

if count == 9 and flag:
    print("Draw")
