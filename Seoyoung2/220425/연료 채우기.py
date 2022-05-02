from sys import stdin
import heapq

N = int(stdin.readline())

oils = []
for _ in range(N):
    a, b = map(int, stdin.readline().split())   # 시작 위치에서 주유소 까지의 거리, 거기서 채울 수 있는 연료의 양
    heapq.heappush(oils, (a, b))    # 거리 작은 순서
L, P = map(int, stdin.readline().split())   # 성경이의 위치에서 마을까지의 거리, 트럭에 원래 있던 연료의 양

if L <= P:
    print(0)
    exit(0)

ans = 0
can_go = []
while P < L:
    # 갈 수 있는 거리의 주유소 찾기
    while oils and oils[0][0] <= P:
        distance, oil = heapq.heappop(oils)
        heapq.heappush(can_go, (-oil, distance))    # 연료가 많은 주유소 순

    if not can_go:      # 갈 수 있는 곳이 없다면 -1
        ans = -1
        break

    oil, distance = heapq.heappop(can_go)
    P += (-oil)
    ans += 1

print(ans)



'''
4
4 4
5 2
11 5
15 10
25 10
=> 3

2
2 3
4 7
14 4
=> 2
'''