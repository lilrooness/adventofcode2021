def read_input_data(filename):
    lines = []
    max_x = 0
    max_y = 0


    with open(filename) as file:
        file_lines = file.readlines()

        for line in file_lines:
            points = line.split("->")
            p1_x = int(points[0].split(",")[0].strip())
            p1_y = int(points[0].split(",")[1].strip())

            p2_x = int(points[1].split(",")[0].strip())
            p2_y = int(points[1].split(",")[1].strip())

            max_x = max(max_x, max(p1_x, p2_x))
            max_y = max(max_y, max(p1_y, p2_y))

            lines.append(((p1_x, p1_y), (p2_x, p2_y)))
        
    return lines, max_x, max_y


def count_overlap_points(lines, max_x, max_y, include_diagonals=False):
    board = []
    for y in range(max_y+1):
        board.append([])
        for x in range(max_x+1):
            board[y].append(0)
    
    for line in lines:
        if include_diagonals or is_not_diagonal(line[0], line[1]):
            line_points = get_line_points(line[0], line[1])
            for (x, y) in line_points:
                board[y][x] += 1
    
    intersections = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 1:
                intersections += 1
    
    return intersections

def get_line_points(a, b):
    points = []
    if a[0] == b[0]:
        for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
            points.append((a[0], y))
    elif a[1] == b[1]:
        for x in range(min(a[0], b[0]), max(a[0], b[0])+1):
            points.append((x, a[1]))
    else:
        dx = a[0] - b[0]
        dy = a[1] - b[1]

        x_increment = int(dx / abs(dx))
        y_increment = int(dy / abs(dy))

        for x in range(abs(dx)+1):
            points.append((b[0] + x_increment*x, b[1] + y_increment*x))
        
    return points

def is_not_diagonal(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return True
    else:
        return False


def test():

    lines, max_x, max_y = read_input_data("test_input_5")
    assert max_y == 9
    assert max_x == 9

    for line in lines:
        print("{} -> {}".format(line[0], line[1]))
    count = count_overlap_points(lines, max_x, max_y)
    assert 5 == count

    count_with_diagonals = count_overlap_points(lines, max_x, max_y, include_diagonals=True)
    assert 12 == count_with_diagonals

if __name__ == "__main__":
    test()
    print("tests passed")

    lines, max_x, max_y = read_input_data("input_5")
    intersections = count_overlap_points(lines, max_x, max_y)
    print("streight intersections: {}".format(intersections))

    all_intersections = count_overlap_points(lines, max_x, max_y, include_diagonals=True)
    print("all intersections: {}".format(all_intersections))

