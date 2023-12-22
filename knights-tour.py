from random import randint
import pygame
import math

pygame.init()

N = 8

dx = [ 1,  2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2,  2,  1, -1, -2]

# Print Board
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def draw_board(move):

    # Set up constants
    WIDTH, HEIGHT = 400, 400
    CELL_SIZE = WIDTH // 8
    LINE_WIDTH = 2 # Adjust the line width as needed
    SQUARE_WIDTH = 1
    ARROW_SIZE = 8
    CIRCLE_RADIUS = 8

    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Knight's Tour")

    def draw_chessboard():
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLACK, rect, SQUARE_WIDTH)

    def draw_line(start_square, end_square):
        start_x = start_square[0] * CELL_SIZE + CELL_SIZE // 2
        start_y = start_square[1] * CELL_SIZE + CELL_SIZE // 2
        end_x = end_square[0] * CELL_SIZE + CELL_SIZE // 2
        end_y = end_square[1] * CELL_SIZE + CELL_SIZE // 2

        # Draw the line
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), LINE_WIDTH)
    
    def draw_line_arrow(start_square, end_square):
        start_x = start_square[0] * CELL_SIZE + CELL_SIZE // 2
        start_y = start_square[1] * CELL_SIZE + CELL_SIZE // 2
        end_x = end_square[0] * CELL_SIZE + CELL_SIZE // 2
        end_y = end_square[1] * CELL_SIZE + CELL_SIZE // 2

        # Draw the line
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), LINE_WIDTH)

        # Calculate angle and arrowhead points
        angle = math.atan2(end_y - start_y, end_x - start_x)
        arrowhead1 = (end_x - ARROW_SIZE * math.cos(angle - math.pi / 6),
                    end_y - ARROW_SIZE * math.sin(angle - math.pi / 6))
        arrowhead2 = (end_x - ARROW_SIZE * math.cos(angle + math.pi / 6),
                    end_y - ARROW_SIZE * math.sin(angle + math.pi / 6))

        # Draw the arrowhead
        pygame.draw.polygon(screen, BLACK, [arrowhead1, (end_x, end_y), arrowhead2])
    
    def draw_circle(square):
        x = square[0] * CELL_SIZE + CELL_SIZE // 2
        y = square[1] * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, BLACK, (x, y), CIRCLE_RADIUS)


    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Draw the board
        screen.fill(WHITE)
        draw_chessboard()

        # Draw an arrow line between the first and second squares
        for i in range(N * N):
            if i == 0:
                draw_circle(move[i])
            elif i == N * N - 1:
                draw_line_arrow(move[i][0], move[i][1])
            else:
                draw_line(move[i][0], move[i][1])
        

        # Update the display
        pygame.display.flip()

        # Set the frames per second
        pygame.time.Clock().tick(60)


# Function for if knight can visit a square
def can_visit(x, y, board):
    return x >= 0 and x < N and y >= 0 and y < N and board[y][x] == -1

# Get how many squares knight can jump to
def get_degree(x, y, board):
    degree = 0
    for i in range(N):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if can_visit(next_x, next_y, board):
            degree += 1
    
    return degree

# Get next move by picking square that has
# the smallest degree
def get_next_move(x, y, board, move):
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
    move[board[y][x]] = ((x, y), (next_x, next_y))

    return next_x, next_y

# Check if knight is in square of its original neighbours
def is_neighbour(x, y, start_x, start_y):
    for i in range(N):
        if x + dx[i] == start_x and y + dy[i] == start_y:
            return True
    return False

# Knights Tour Algorithm
def knights_tour(closed=True, start_x=0, start_y=0):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    move = [(0, 0)] * 64

    board[start_y][start_x] = 1

    x = start_x
    y = start_y
    for _ in range(N * N - 1):
        x, y = get_next_move(x, y, board, move)
        if x == -1 and y == -1:
            break

    if closed and not is_neighbour(x, y, start_x, start_y):
        return False
    
    print_board(board)
    draw_board(move)
    
    return True

if __name__ == '__main__':
    
    choice = max(0, min(1, int(input("Open or closed tour? (0 = open, 1 = closed tour): "))))
    start_x = max(0, min(7, int(input("Enter starting x position: "))))
    start_y = max(0, min(7, int(input("Enter starting y position: "))))

    while not knights_tour(choice, start_x, start_y):
        pass
