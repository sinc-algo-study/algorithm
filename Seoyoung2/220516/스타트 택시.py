from collections import deque
import heapq
from math import inf

N, M, oil = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

x, y = map(int, input().split())        # 택시의 위치
end = []
for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    grid[x1-1][y1-1] = m+2       # 2부터
    end.append((x2-1, y2-1))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

'''
같은거리일 경우 행이 작은, 열이 작은 승객 => [상-좌-우-하] 순회하면 될 줄 알았는데 안됨
 : 모든 승객 거리 계산 필요 (우선순위큐)
'''


def next_cust():
    global oil, x, y

    dq = deque([(x, y, 0)])
    pq = []
    visit = [[False] * N for _ in range(N)]
    visit[x][y] = True

    mdist = inf
    while dq:
        cx, cy, coil = dq.popleft()
        if grid[cx][cy] > 1 and coil <= mdist:
            mdist = coil
            heapq.heappush(pq, (cx, cy))
        elif coil > mdist:
            continue
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                dq.append((nx, ny, coil+1))

    cust = -1
    if len(pq) > 0:
        x, y = heapq.heappop(pq)
        cust = grid[x][y] - 2
        grid[x][y] = 0
    oil -= mdist
    return cust


def move(ex, ey):
    global oil, x, y

    dq = deque([(x, y, 0)])
    visit = [[False] * N for _ in range(N)]
    visit[x][y] = True

    mdist = inf
    while dq:
        cx, cy, coil = dq.popleft()
        if cx == ex and cy == ey:
            x, y, mdist = cx, cy, coil
            break
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                dq.append((nx, ny, coil+1))

    oil -= mdist
    return mdist


x -= 1
y -= 1
while M > 0:
    customer = next_cust()
    if oil <= 0:     # 승객한테 가는 도중 연료 다 씀
        oil = -1
        break

    ex, ey = end[customer]
    eoil = move(ex, ey)
    if oil < 0:
        oil = -1
        break

    oil += eoil*2
    M -= 1

print(oil)