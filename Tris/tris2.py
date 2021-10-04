import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    def currentSymbol():
        screen.fill(WHITE)
        drawSymbol(players[current], 1, 3, BLACK)

    def playerMove():
        if pygame.mouse.get_pressed()[0]:
            (col, row) = pygame.mouse.get_pos()

            col = col // 100
            row = row // 100

            if grid[row][col] == '':
                grid[row][col] = players[current]
                return (current + 1) % 2
        return current

    players = ['X', 'O']
    current = 0
    initial = 0
    grid = [['' for _ in range(3)] for _ in range(3)]

    done = False
    finished = False
    clock = pygame.time.Clock()

    screen.fill(WHITE)
    drawGrid()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
                elif event.key == pygame.K_r:
                    grid = [['' for _ in range(3)] for _ in range(3)]
                    initial = (initial + 1) % 2
                    current = initial
                    finished = False
                    screen.fill(WHITE)
                    drawGrid()

        if not finished:
            currentSymbol()

            current = playerMove()
            drawGrid()
            printSymbols(grid)

            winner = winnerPlayer(grid)
            if winner is not None:
                greenSquares(grid, winner)
                finished = True
            elif isFull(grid):
                finished = True
                yellowSquares(grid)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def drawGrid():
    pygame.draw.line(screen, BLACK, (0, 1), (299, 1), width=3)
    pygame.draw.line(screen, BLACK, (0, 298), (299, 298), width=3)
    pygame.draw.line(screen, BLACK, (1, 0), (1, 299), width=3)
    pygame.draw.line(screen, BLACK, (298, 0), (298, 299), width=3)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 299), width=3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 299), width=3)
    pygame.draw.line(screen, BLACK, (0, 100), (299, 100), width=3)
    pygame.draw.line(screen, BLACK, (0, 200), (299, 200), width=3)


def printSymbols(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != '':
                drawSymbol(grid[i][j], i, j, BLACK)


def greenSquares(grid, locs):
    for loc in locs:
        square = (loc[1] * 100, loc[0] * 100)
        rect = pygame.Rect(square, (100, 100))
        pygame.draw.rect(screen, GREEN, rect)
    drawGrid()
    printSymbols(grid)


def yellowSquares(grid):
    rect = pygame.Rect((0, 0), (300, 300))
    pygame.draw.rect(screen, YELLOW, rect)
    drawGrid()
    printSymbols(grid)


def isFull(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '':
                return False
    return True


def winnerPlayer(grid):
    for i in range(3):
        if (grid[i][0] == grid[i][1] == grid[i][2]) and grid[i][0] != '':
            return ((i, 0), (i, 1), (i, 2))
        elif grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '':
            return ((0, i), (1, i), (2, i))

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != '':
        return ((0, 0), (1, 1), (2, 2))
    elif grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != '':
        return ((0, 2), (1, 1), (2, 0))
    return None


def drawSymbol(symbol, row, col, color):
    if symbol == 'O':
        center = (50 + 100 * col, 50 + 100 * row)
        pygame.draw.circle(screen, color, center, 40, width=3)
    else:
        tleft = (100 * col + 10, 100 * row + 10)
        bleft = (100 * col + 90, 100 * row + 90)
        tright = (100 * col + 10, 100 * row + 90)
        bright = (100 * col + 90, 100 * row + 10)

        pygame.draw.line(screen, color, tleft, bleft, width=3)
        pygame.draw.line(screen, color, tright, bright, width=3)


if __name__ == "__main__":
    main()
