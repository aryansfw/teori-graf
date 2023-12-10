from random import randint

N = 8

dx = [ 1,  2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2,  2,  1, -1, -2]

def can_visit(x, y, board):
    return x >= 0 and x < N and y >= 0 and y < N and board[y][x] == -1

def get_degree(x, y, board):
    degree = 0
    for i in range(N):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if can_visit(next_x, next_y, board):
            degree += 1
    
    return degree

def get_next_move(x, y, board):
    min_degree_index = -1
    min_degree = N + 1
    next_x = 0
    next_y = 0 

    start = randint(0, 1000) % N
    for cnt in range(0, N):
        i = (start + cnt) % N
        next_x = x + dx[i]
        next_y = y + dy[i]
        degree = get_degree(next_x, next_y, board)

        if can_visit(next_x, next_y, board) and degree < min_degree:
            min_degree_index = i
            min_degree = degree
    
    if min_degree_index == -1:
        return -1, -1
    
    next_x = x + dx[min_degree_index]
    next_y = y + dy[min_degree_index]

    board[next_y][next_x] = board[y][x] + 1

    return next_x, next_y

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_neighbour(x, y, start_x, start_y):
    for i in range(N):
        if x + dx[i] == start_x and y + dy[i] == start_y:
            return True
    return False

def knights_tour(closed=True):
    board = [[-1 for _ in range(N)] for _ in range(N)]

    start_x = 0
    start_y = 0
    board[start_y][start_x] = 1

    x = start_x
    y = start_y
    for _ in range(N * N - 1):
        x, y = get_next_move(x, y, board)
        if x == -1 and y == -1:
            break

    if closed and not is_neighbour(x, y, start_x, start_y):
        return False
    
    print_board(board)
    return True

if __name__ == '__main__':
    while not knights_tour(closed=True):
        pass
