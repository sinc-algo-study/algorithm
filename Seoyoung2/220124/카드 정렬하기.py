import heapq
from sys import stdin

N = int(stdin.readline())
size = [int(stdin.readline()) for _ in range(N)]

# 계속 작은거끼리 연산 -> heapq
ans = 0
size.sort()
while len(size) > 1:
    a = heapq.heappop(size)
    b = heapq.heappop(size)
    heapq.heappush(size, a+b)
    ans += (a + b)

print(ans)
