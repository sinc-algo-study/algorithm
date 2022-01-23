import math
from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))


def get_dist(store):
    res = 0
    for hx, hy in home:
        tmp = 101
        for sx, sy in store:
            tmp = min(tmp, abs(hx-sx)+abs(hy-sy))
        res += tmp
    return res


ans = math.inf
if len(chicken) > M:
    for combi in combinations(chicken, M):
        ans = min(ans, get_dist(combi))
else:
    ans = get_dist(chicken)

print(ans)
