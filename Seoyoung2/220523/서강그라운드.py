from sys import stdin
from math import inf

n, m, r = map(int, stdin.readline().split())    # m:수색범위
item_cnt = list(map(int, stdin.readline().split()))

road = [[inf] * n for _ in range(n)]
for i in range(n):
    road[i][i] = 0

for _ in range(r):
    a, b, l = map(int, stdin.readline().split())
    road[a-1][b-1] = road[b-1][a-1] = l

# 플로이드 와샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            road[i][j] = min(road[i][j], road[i][k]+road[k][j])

ans = 0
for cur in range(n):
    cnt = 0
    for dest in range(n):
        if road[cur][dest] <= m:
            cnt += item_cnt[dest]
    ans = max(ans, cnt)
print(ans)