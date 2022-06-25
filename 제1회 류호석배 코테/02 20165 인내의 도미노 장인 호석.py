N, M, R = map(int, input().split())
domino = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]
dirs = {
    'E': (0, 1),
    'W': (0, -1),
    'S': (1, 0),
    'N': (-1, 0),
}


def attack(x, y, d):
    global score
    if check[x][y]:
        return

    dx, dy = dirs[d]
    cnt = domino[x][y]

    while 0 <= x < N and 0 <= y < M and cnt > 0:
        if not check[x][y]:
            score += 1
            cnt = max(cnt - 1, domino[x][y] - 1)
        else:
            cnt -= 1
        check[x][y] = True
        x += dx
        y += dy


score = 0
for _ in range(R):
    # attack
    x, y, d = input().split()
    x = int(x) - 1
    y = int(y) - 1
    attack(x, y, d)

    # defense
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    check[x][y] = False

print(score)
for i in range(N):
    for j in range(M):
        print('F' if check[i][j] else 'S', end=' ')
    print()
