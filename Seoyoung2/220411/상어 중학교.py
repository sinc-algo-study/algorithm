from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(N)]

'''
# 일반 블록은 M가지 색상(색은 M이하의 자연수), 검은색 블록은 -1, 무지개 블록은 0

그룹에는 일반 블록이 적어도 하나(색은 모두 같아야 함), 검은색 블록은 X, 무지개 블록은 상관없다
그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행이 가장 작은 블록, 여러개면 열이 가장 작은 블록

1. 크기가 가장 큰 블록 그룹을 찾는다. ->포함된 무지개 블록의 수가 가장 많은 -> 기준 블록의 행이 가장 큰 것을 ->열이 가장 큰 것
2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
3. 격자에 중력이 작용한다.
4. 격자가 90도 반시계 방향으로 회전한다.
5. 다시 격자에 중력이 작용한다.
'''


def find_group():
    global ans
    # 그룹찾기용 방문여부 체크 배열 (일반블록만 체크)
    visit = [[False] * N for _ in range(N)]
    candi = (0, 0, 0, 0)
    bomb = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0 and not visit[i][j]:
                visit[i][j] = True
                color = grid[i][j]
                rainbow, row, col = 0, i, j
                group = set()   # 레인보우 블록 포함해서 방문여부 체크 용도
                group.add((i, j))
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        # 무지개 블록이거나 같은색 블록이면 계속 진행
                        if (nx, ny) not in group and (grid[nx][ny] == color or grid[nx][ny] == 0):
                            q.append((nx, ny))
                            group.add((nx, ny))
                            if grid[nx][ny] == color:
                                visit[nx][ny] = True    # 그룹찾기 이미 한 블록인거 체크
                                # 기준 블록 구하기
                                row = min(row, nx)
                                col = min(col, ny)
                            else:
                                rainbow += 1
                if candi < (len(group), rainbow, row, col):
                    candi = (len(group), rainbow, row, col)
                    bomb = group
    if len(bomb) > 1:
        ans += len(bomb) * len(bomb)
        # 블록 그룹의 모든 블록 제거 (-2)
        for bx, by in bomb:
            grid[bx][by] = -2
        return True
    else:
        return False


def down_grid():        # 비효율적인듯..
    for j in range(N):
        for i in range(N-2, -1, -1):
            if grid[i][j] > -1:
                # -1이 아니면 아래로 down
                now = i
                while True:
                    if 0 <= now+1 < N and grid[now+1][j] == -2:
                        grid[now+1][j] = grid[now][j]
                        grid[now][j] = -2
                        now += 1
                    else:
                        break


def rotate_grid():
    global grid
    new_grid = []
    for i in range(N-1, -1, -1):
        tmp = [g[i] for g in grid]
        new_grid.append(tmp)
    grid = [ng[:] for ng in new_grid]


ans = 0
while True:
    if not find_group():
        break
    down_grid()
    rotate_grid()
    down_grid()
print(ans)
