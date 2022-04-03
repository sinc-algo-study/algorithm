from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
# i 번째 도로는 서로 다른 두 건물 Ai 번과 Bi 번 사이를 1 시간에 양방향으로 이동할 수 있는 도로
# 건물 X 의 접근성은 X 에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단 시간 : 플로이드와샬 알고리즘,,

road = [[10000] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    road[x-1][y-1] = road[y-1][x-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                road[i][j] = 0
            else:
                road[i][j] = min(road[i][j], road[i][k]+road[k][j])

num = []
for combi in combinations(range(N), 2):
    dist = 0
    for n in range(N):
        dist += min(road[combi[0]][n], road[combi[1]][n])
    num.append((dist, combi[0], combi[1]))

num.sort()
ans = sorted(num)[0]
print(ans[1]+1, ans[2]+1, ans[0]*2)
