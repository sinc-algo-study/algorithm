import sys
input = sys.stdin.readline
from collections import deque


def bfs(y, x, h, visit):
    que = deque()
    que.append((y,x))
    cnt = 1
    visit[y][x]=1
    flag = 0
    while que:
        y, x = que.popleft()
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0<=ny<n and 0<=nx<m:
                if not visit[ny][nx] and pool[ny][nx]<h:
                    cnt += 1
                    que.append((ny,nx))
                    visit[ny][nx] = 1
            else:
                flag = 1
    if flag:
        return 0
    return cnt


def watering(pool):
    ans = 0
    for h in range(2, maxi+1):
        visit = [[0 for _ in range(m)] for _ in range(n)]
        for y in range(1, n):
            for x in range(1, m):
                if not visit[y][x] and pool[y][x]<h:
                    ans += bfs(y, x, h, visit)
    return ans


if '__main__' == __name__ :
    n, m = map(int, input().split())
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    maxi = 0
    pool = []

    for _ in range(n):
        temp = list(map(int, list(input().rstrip())))
        maxi = max(max(temp), maxi)
        pool.append(temp)
    print(watering(pool))