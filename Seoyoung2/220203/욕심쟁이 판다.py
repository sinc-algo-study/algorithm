# bfs 풀이는 시간초과
# dfs로 모든 지점에서의 값들을 구해야
#  -> 시간초과를 피하기 위해서는 dp도 함께 이용

from sys import stdin

N = int(stdin.readline())
forest = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]


def dfs(x, y):
    if not check[x][y]:
        check[x][y] = 1
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and forest[x][y] < forest[nx][ny]:
                check[x][y] = max(check[x][y], dfs(nx, ny) + 1)
    return check[x][y]


for i in range(N):
    for j in range(N):
        dfs(i, j)

print(max(map(max, check)))

