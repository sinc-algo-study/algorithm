import heapq

N, M, K = map(int, input().split())

power = list(map(int, input().split()))
edge = []
for _ in range(M):
    u, v, w = map(int, input().split())
    heapq.heappush(edge, (w, u, v))


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


# 발전소의 parent는 0으로
parent = [0] * (N+1)
for i in range(N+1):
    if i not in power:
        parent[i] = i

ans = cnt = 0
while cnt < N-K:
    d, n1, n2 = heapq.heappop(edge)
    p_n1, p_n2 = find(n1), find(n2)
    if p_n1 != p_n2:
        # union
        parent[max(p_n1, p_n2)] = min(p_n1, p_n2)
        ans += d
        cnt += 1
print(ans)
