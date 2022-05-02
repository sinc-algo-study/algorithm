N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

x, y = N//2, N//2
dxdy = (0, -1), (1, 0), (0, 1), (-1, 0)
scatter = [{(-2, 0): 2, (-1, 0): 7, (-1, -1): 10, (-1, 1): 1, (0, -2): 5, (1, -1): 10, (1, 0): 7, (1, 1): 1, (2, 0): 2}
           ,{(0, -2): 2, (0, -1): 7, (1, -1): 10, (-1, -1): 1, (2, 0): 5, (1, 1): 10, (0, 1): 7, (-1, 1): 1, (0, 2): 2}
           ,{(-2, 0): 2, (-1, 0): 7, (-1, 1): 10, (-1, -1): 1, (0, 2): 5, (1, 1): 10, (1, 0): 7, (1, -1): 1, (2, 0): 2}
           ,{(0, -2): 2, (0, -1): 7, (-1, -1): 10, (1, -1): 1, (-2, 0): 5, (-1, 1): 10, (0, 1): 7, (1, 1): 1, (0, 2): 2}]
last = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def solve(x, y):
    global over
    cnt = 1
    d = 0
    while True:
        for n in range(cnt):
            x += dxdy[d][0]
            y += dxdy[d][1]
            if x < 0 or y < 0:
                return
            valid = grid[x][y]
            if valid != 0:
                for (dx, dy), p in scatter[d].items():
                    nx, ny = x + dx, y + dy
                    tmp = grid[x][y] * p // 100
                    if 0 <= nx < N and 0 <= ny < N:
                        grid[nx][ny] += tmp
                    else:
                        over += tmp
                    valid -= tmp

                if 0 <= x + last[d][0] < N and 0 <= y + last[d][1] < N:
                    grid[x + last[d][0]][y + last[d][1]] += valid
                else:
                    over += valid
                grid[x][y] = 0

        if d == 1 or d == 3:
            cnt += 1
        d = (d+1) % 4


over = 0
solve(x, y)
print(over)