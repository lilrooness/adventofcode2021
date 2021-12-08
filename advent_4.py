def read_data(filename):
    
    numbers = []
    boards = []

    with open(filename) as file:
        lines = file.readlines()
        first_line = True
        start = True

        for line in lines:
            if first_line:
                numbers = get_numbers(line, ",")
                first_line = False
            else:
                if line.strip() == "" or start:
                    boards.append([])
                    start = False
                else:
                    boards[-1] = boards[-1] + get_numbers(line)
    
    return numbers, boards

def get_numbers(line, delim=" "):
    parts = line.strip().split(delim)
    numbers = []
    for part in parts:
        if part.strip() != '':
            numbers.append(int(part))

    return numbers

def has_complete_row(numbers, board, dim=5):
    for y in range(dim):
        start_idx = y*dim
        complete_row = True
        indexes = []
        x_pos = 0
        for x in board[start_idx:start_idx+dim]:
            indexes.append(start_idx+x_pos)
            x_pos += 1
            if x not in numbers:
                complete_row = False

        if complete_row:
            return (True, indexes)
    return (False, [])

def has_complete_column(numbers, board, dim=5):
    for x in range(5):
        complete_column = True
        indexes = []
        for y in range(dim):
            n = board[y*dim+x]
            indexes.append(y*dim+x)
            if n not in numbers:
                complete_column = False
            
        if complete_column:
            return (True, indexes)
        
    return (False, [])

def get_winning_score(numbers, boards):

    called = []
    for n in numbers:
        called.append(n)
        for board in boards:
            (row_win, row_indexes) = has_complete_row(called, board)
            (col_win, col_indexes) = has_complete_column(called, board)
            if row_win:
                sum = get_unmarked_sum(board, get_marked_indexes(board, called))
                return sum * called[-1]
            elif col_win:
                sum = get_unmarked_sum(board, get_marked_indexes(board, called))
                return sum * called[-1]

def get_loosing_score(numbers, boards):
    winning_boards_info = []
    
    for i in range(len(boards)):
        for j in range(len(numbers)):
            (row_win, row_indexes) = has_complete_row(numbers[:j+1], boards[i])
            (col_win, col_indexes) = has_complete_column(numbers[:j+1], boards[i])

            if row_win or col_win:
                # boardidx, numberidx
                winning_boards_info.append((i, j))
                break
    
    max_number_idx = -1
    last_board_idx = -1

    for board_idx, number_idx in winning_boards_info:
        if number_idx > max_number_idx:
            max_number_idx = number_idx
            last_board_idx = board_idx
    
    sum = get_unmarked_sum(boards[last_board_idx], get_marked_indexes(boards[last_board_idx], numbers[:max_number_idx+1]))
    return sum * numbers[max_number_idx]


def get_marked_indexes(board, numbers):
    indexes = []
    for i in range(len(board)):
        if board[i] in numbers:
            indexes.append(i)
    
    return indexes

def get_unmarked_sum(board, marked):
    sum=0
    for i in range(len(board)):
        if i not in marked:
            sum += board[i]
    return sum

def test():
    assert (True, [10, 11, 12, 13, 14]) == has_complete_row([1,2,3,4,5], [0,9,3,6,1, 1,0,5,3,7, 1,5,4,3,2,  8,6,3,5,6, 0,0,5,1,7])
    assert (True, [0, 5, 10, 15, 20]) == has_complete_column([1,2,3,4,5], [1,5,6,7,5, 2,5,6,4,3, 3,6,5,7,5, 4,7,9,6,4, 5,7,5,3,1])
    numbers, boards = read_data("test_input_4")
    winning_score = get_winning_score(numbers, boards)
    assert 4512 == winning_score

    loosing_score = get_loosing_score(numbers, boards)
    assert 1924 == loosing_score

if __name__ == "__main__":
    test()
    print("tests passed")
    numbers, boards = read_data("input_4")
    winning_score = get_winning_score(numbers, boards)
    print("winning score: {}".format(winning_score))

    loosing_score = get_loosing_score(numbers, boards)
    print("loosing score: {}".format(loosing_score))
