from random import randrange

all_grid = [1]
best_result = 0
EPOCHS = 10000
h = 0

rows = 10
columns = 10

finish = False

while h<EPOCHS and not finish:
    grid = [[0 for x in range(columns)] for y in range(rows)]
    grid[0][0] = 1
    cur_pos = [0,0]
    done = False

    while not done:
        pos = [[  cur_pos[0], cur_pos[1]+3],
               [cur_pos[0]+2, cur_pos[1]+2],
               [cur_pos[0]+3,   cur_pos[1]],
               [cur_pos[0]-2, cur_pos[1]+2],
               [  cur_pos[0], cur_pos[1]-3],
               [cur_pos[0]-2, cur_pos[1]-2],
               [cur_pos[0]-3,   cur_pos[1]],
               [cur_pos[0]+2, cur_pos[1]-2]]

        points = []

        for p in pos:
            if (p[0] >= 0 and p[0] < rows) and (p[1] >= 0 and p[1] < columns and \
                grid[p[0]][p[1]] == 0):
                points.append(p)

        if (len(points) > 0):
            spot = points[randrange(0, len(points))]
            grid[spot[0]][spot[1]] = (grid[cur_pos[0]][cur_pos[1]] + 1)
            cur_pos = spot
        else:
            done = True
            result = grid[cur_pos[0]][cur_pos[1]]

    if result > best_result:
        best_result = result
        all_grid[0] = grid

    if result==100:
        finish = True

    if h%(EPOCHS/10)==0:
        print("tentativo", h)

    h += 1

print("\n")
print("finito")
print("risultato =", best_result)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in all_grid[0]]))