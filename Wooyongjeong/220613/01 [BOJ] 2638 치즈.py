import collections

BLANK, CHEESE = 0, 1
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(m)] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

elapsed_time = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def init():
    for i in range(n):
        for j in range(m):
            next_grid[i][j] = grid[i][j]
            visited[i][j] = False


def melt():
    init()

    q = collections.deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            if grid[nx][ny] != BLANK:
                grid[nx][ny] += 1
            else:
                visited[nx][ny] = True
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 2:
                next_grid[i][j] = BLANK
            grid[i][j] = next_grid[i][j]


def is_cheese_exist():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == CHEESE:
                return True
    return False


def simulate():
    global elapsed_time

    while is_cheese_exist():
        melt()
        elapsed_time += 1


simulate()
print(elapsed_time)
