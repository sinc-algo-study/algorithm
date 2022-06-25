import collections

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [
        [False for _ in range(4)]
        for _ in range(m)
    ]
    for _ in range(n)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def get_air_conditioners_pos():
    pos = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 9:
                pos.append((i, j))
    return pos


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def get_next_dir(item, d):
    # 해당 칸으로 d 방향으로 바람이 들어오고, item번 물건이 있을 때
    # 바뀌는 바람의 방향을 반환
    if item == 1:
        return d if d % 2 == 0 else (d + 2) % 4
    elif item == 2:
        return d if d % 2 == 1 else (d + 2) % 4
    elif item == 3:
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        else:
            return 2
    elif item == 4:
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        else:
            return 0
    else:
        return d


def run_air_conditioner(sx, sy):
    q = collections.deque()
    for d in range(4):
        visited[sx][sy][d] = True
        q.append((sx, sy, d))

    while q:
        x, y, d = q.popleft()

        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):
            # 연구실 끝에 다다르면 더 이상 바람이 갈 수 없음
            continue
        if visited[nx][ny][d]:
            # 이전에 바람이 해당 칸에 해당 방향으로 분 적이 있다면 종료
            continue

        visited[nx][ny][d] = True
        nd = get_next_dir(grid[nx][ny], d)
        q.append((nx, ny, nd))


def is_windy(x, y):
    for d in range(4):
        if visited[x][y][d]:
            return True
    return False


def simulate():
    air_conditioners = get_air_conditioners_pos()

    for air_conditioner in air_conditioners:
        sx, sy = air_conditioner
        run_air_conditioner(sx, sy)


def count_windy_seat():
    return sum([
        is_windy(i, j)
        for i in range(n)
        for j in range(m)
    ])


simulate()
print(count_windy_seat())
