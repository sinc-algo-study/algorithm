from sys import stdin
from collections import deque

N = int(stdin.readline())
space = [list(map(int, stdin.readline().split())) for _ in range(N)]

'''
map을 계속 만들어야하나?
'''
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby = (i, j)
            space[i][j] = 0
# baby = [(i, j) for i in range(N) for j in range(N) if space[i][j] == 9]


def bfs(baby):
    q = deque([baby])
    step = [[0] * N for _ in range(N)]
    step[baby[0]][baby[1]] = 1
    fish = []
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and step[nx][ny] == 0:
                    if 0 < space[nx][ny] < size:    # 먹을 수 있는 물고기 발견
                        fish.append((nx, ny))
                    elif space[nx][ny] == 0 or space[nx][ny] == size: # 먹을 순 없지만 지나갈 수 있음
                        q.append((nx, ny))
                    step[nx][ny] = step[x][y] + 1
        if fish:    # 먹을게 있으면 먹고 return, 없으면 가던길 계속
            fish.sort()
            space[fish[0][0]][fish[0][1]] = 0
            return fish[0], step[fish[0][0]][fish[0][1]]-1
    return 0, 0


size = 2
eat = 0
ans = 0
while True:
    baby, d = bfs(baby)
    if d == 0:
        break
    ans += d
    eat += 1
    if eat >= size:
        size += 1
        eat = 0
print(ans)
