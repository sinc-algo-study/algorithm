"""
'S': 이다솜파, 'Y': 임도연파

1. 7명의 여학생으로 구성
2. 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 함
3. 임도연파도 들어가도 됨
4. 하지만 이다솜파가 적어도 4명 이상이 되도록 구성해야 함
"""
from itertools import combinations
from collections import deque

N = 5
PRINCESSES = 7

board = [list(input()) for _ in range(N)]
positions = [(i, j) for i in range(N) for j in range(N)]
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

ans = 0
component = 0
selected = []


def check(comb):
    visited = [False for _ in range(PRINCESSES)]  # 방문 체크
    q = deque()
    q.append(comb[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in comb:
                continue
            i = comb.index((nx, ny))
            if visited[i]:
                continue
            q.append((nx, ny))
            visited[i] = True

    return sum(visited) == PRINCESSES


def count_dasom(comb):
    dasom = 0
    for x, y in comb:
        if board[x][y] == 'S':
            dasom += 1
    return dasom


# 25개의 자리 중 7개를 조합으로 구함
for comb in combinations(positions, PRINCESSES):
    # 이다솜파가 4명 이상이어야 함
    dasom = count_dasom(comb)
    if dasom < 4:
        continue

    # 이번 조합의 자리들이 모두 인접해 있다면 정답
    if check(comb):
        ans += 1

print(ans)
