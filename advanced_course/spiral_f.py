n, m = [int(i) for i in input().split()]

counter = 2
matrix = [[0] * m for _ in range(n)]
x, y = 0, 0
dx, dy = 0, 1
matrix[0][0] = str(1).ljust(3)

while counter <= m * n:
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and matrix[x + dx][y + dy] == 0:
        matrix[x + dx][y + dy] = str(counter).ljust(3)
        counter += 1
        x += dx
        y += dy
    else:
        if dy == 1:
            dy = 0
            dx = 1

        elif dx == 1:
            dx = 0
            dy = -1

        elif dy == -1:
            dy = 0
            dx = -1

        elif dx == -1:
            dx = 0
            dy = 1

for row in matrix:
    print(*row)