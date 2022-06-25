import collections

n, health, durability = map(int, input().split())
grid = [list(input()) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_start_pos():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                return i, j


def simulate():
    sx, sy = get_start_pos()
    health_check = [[0 for _ in range(n)] for _ in range(n)]
    q = collections.deque()
    q.append((sx, sy, health, 0, 0))

    while q:
        x, y, h, d, cnt = q.popleft()

        # 상하좌우로 이동
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                # 격자 밖이면 이동할 수 없다
                continue

            if grid[nx][ny] == 'E':
                # 안전지대라면 반복 종료
                return cnt + 1

            nh, nd = h, d  # 다음 체력과 들고 있는 우산의 다음 내구도
            if grid[nx][ny] == 'U':
                # 다음 칸이 우산이면 새 우산으로 교체
                nd = durability

            if nd == 0:
                # 들고 있는 우산의 내구도가 다 됐으면 체력을 1 깜
                nh -= 1
            else:
                # 우산의 내구도가 남아 있으면 내구도 1을 깜
                nd -= 1

            if nh == 0:
                # 체력이 0이 됐으면 더 못 감
                continue

            if health_check[nx][ny] >= nh:
                # 이전에 해당 칸을 더 높은 체력으로 방문한 적이 있다면 더 이상 진행하지 않음
                continue

            health_check[nx][ny] = nh  # 해당 칸에 현재 체력을 기록해 놓는다
            q.append((nx, ny, nh, nd, cnt + 1))  # 이어서 계속 진행

    return -1


ans = simulate()
print(ans)
