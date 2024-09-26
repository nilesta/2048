from random import randint

def print_help() -> None:
    print("""
    Use WASD to push items in the given direction:
    W : Up
    A : Left
    S : Down
    D : Right
    """)

def make_grid() -> list[list]:
    return [[0 for _ in range(4)] for _ in range(4)]

def print_grid(matrix: list[list]) -> None:
    print('-----------------------------')
    for c in matrix:
        print('|', ' | '.join(str(i).rjust(4) for i in c), '|')
    print('-----------------------------')

# Check for any "blank" (0) items:
def check_blanks(matrix: list[list]) -> bool:
    for c in matrix:
        if 0 in c:
            return True
    return False

# Check for win:
def check_win(matrix: list[list]) -> bool:
    for c in matrix:
        if 2048 in c:
            return True
    return False

# Random 2:
def place_2(matrix: list[list]) -> list:
    c = randint(0, 3)
    r = randint(0, 3)
    while matrix[c][r] != 0:
        c = randint(0, 3)
        r = randint(0, 3)
    matrix[c][r] = 2
    return matrix

# Reverse rows
def reverse(matrix: list[list]) -> list:
    new = []
    for i in range(4):
        new.append(matrix[i][::-1])
    return new

# Switch cols and rows
def transpose(matrix: list[list]) -> list:
    new = []
    for c in range(4):
        new.append([])
        for r in range(4):
            new[c].append(matrix[r][c])
    return new

# Push all rows to the left
def push(matrix: list[list]) -> list:
    new = []
    for c in range(4):
        new.append([0,0,0,0])
        i = 0 # Position of last 0
        for r in range(4):
            if matrix[c][r] != 0:
                new[c][i] = matrix[c][r]
                i += 1
    return new

# Double numbers
def double(matrix: list[list]) -> list:
    for c in range(4):
        for r in range(4):
            if matrix[c][r] != 0 and r != 3:
                if matrix[c][r] == matrix[c][r+1]:
                    matrix[c][r] = matrix[c][r] * 2
                    matrix[c][r+1] = 0
    return matrix

def move_left(matrix: list[list]) -> list:
    return push(
        double(
            push(matrix)
        )
    )

def move_right(matrix: list[list]) -> list:
    return reverse(
        push(
            double(
                push(reverse(matrix))
            )
        )
    )

def move_up(matrix: list[list]) -> list:
    return transpose(
        push(
            double(
                push(transpose(matrix))
            )
        )
    )

def move_down(matrix: list[list]) -> list:
    return transpose(
        reverse(
            push(
                double(
                    push(reverse(transpose(matrix)))
                )
            )
        )
    )

grid = make_grid()
todo = ''

while True:
    match todo.lower():
        case 'w':
            grid = move_up(grid)
        case 'a':
            grid = move_left(grid)
        case 's':
            grid = move_down(grid)
        case 'd':
            grid = move_right(grid)
        case _:
            print_help()

    if check_win(grid):
        print("You won!")
        break

    if not check_blanks(grid):
        print("You lose!")
        break

    grid = place_2(grid)
    print_grid(grid)

    todo = input("What would you like to do? ")

print("Game over.  Final board: ")
print_grid(grid)