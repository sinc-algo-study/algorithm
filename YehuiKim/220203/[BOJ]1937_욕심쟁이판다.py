import sys
input = sys.stdin.readline


def check_maps():
    ans = 1
    for y in range(n):
        for x in range(n):
            move(x, y)
            ans = max(ans, memo[y][x])
    return ans


def move(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[ny][nx] > maps[y][x]:
                temp = memo[ny][nx]
                if temp < 0:
                    memo[ny][nx] = 1
                    move(nx, ny)
                memo[y][x] = max(memo[y][x], memo[ny][nx] + 1)


if '__main__' == __name__:
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    print(check_maps())
