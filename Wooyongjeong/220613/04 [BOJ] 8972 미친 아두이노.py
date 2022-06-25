n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
board = [[0 for _ in range(m)] for _ in range(n)]
moves = list(map(int, input()))

sx, sy = 0, 0
enemies = []
dxs = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dys = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def get_dist(enemy_x, enemy_y):
    return abs(enemy_x - sx) + abs(enemy_y - sy)


def find_next_enemy_pos(enemy_x, enemy_y):
    next_x, next_y = enemy_x, enemy_y
    min_dist = float('inf')
    for dx, dy in zip(dxs, dys):
        if dx == 0 and dy == 0:
            continue
        nx, ny = enemy_x + dx, enemy_y + dy
        if not in_range(nx, ny):
            continue

        dist = get_dist(nx, ny)
        if min_dist > dist:
            min_dist = dist
            next_x, next_y = nx, ny
    return next_x, next_y


def find_and_destroy_enemies():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                enemies.append((i, j))
            elif board[i][j] > 1:
                board[i][j] = 0


def simulate(move):
    global sx, sy

    # 1. 종수가 아두이노를 이동
    board[sx][sy] = 0
    sx, sy = sx + dxs[move], sy + dys[move]

    # 2. 종수의 아두이노가 미친 아두이노가 있는 칸으로 이동한 경우 게임 종료
    if board[sx][sy] > 0:
        return True
    board[sx][sy] = -1

    while enemies:
        # 3. 미친 아두이노는 종수의 아두이노와 가장 가까워지는 방향으로 한 칸 이동
        x, y = enemies.pop()
        board[x][y] -= 1
        nx, ny = find_next_enemy_pos(x, y)

        # 4. 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우 게임 종료
        if board[nx][ny] == -1:
            return True
        board[nx][ny] += 1

    # 5. 2개 이상의 미친 아두이노가 같은 칸에 있는 경우 해당 칸의 미친 아두이노들 모두 파괴
    find_and_destroy_enemies()

    return False


def print_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                print("I", end="")
            elif board[i][j] == 0:
                print(".", end="")
            else:
                print("R", end="")
        print()


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'I':
            sx, sy = i, j
            board[i][j] = -1
        elif grid[i][j] == 'R':
            enemies.append((i, j))
            board[i][j] = 1

for cnt, move in enumerate(moves):
    is_end = simulate(move)
    if is_end:
        print(f"kraj {cnt + 1}")
        break
else:
    print_board()
