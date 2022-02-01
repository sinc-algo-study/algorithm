import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    global answer

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and data[x][y] < data[nx][ny]:
            bamboo = 1
            bamboo += dfs(nx, ny)
            dp[x][y] = max(dp[x][y], bamboo)
    answer = max(answer, dp[x][y])
    return dp[x][y]


if __name__ == '__main__':
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    dp = [[-1] * N for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            dfs(i, j)
    print(answer)
