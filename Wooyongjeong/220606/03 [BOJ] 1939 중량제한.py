import collections

n, m = map(int, input().split())
con = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    con[a].append((b, c))
    con[b].append((a, c))

factory1, factory2 = map(int, input().split())


def can_go(weight):
    q = collections.deque()
    visited = [False] * (n + 1)

    q.append(factory1)
    visited[factory1] = True

    while q:
        now = q.popleft()

        if now == factory2:
            return True

        for island, capacity in con[now]:
            if visited[island] or capacity < weight:
                continue
            visited[island] = True
            q.append(island)

    return False


def simulate():
    left, right = 0, int(1e9)

    while left <= right:
        mid = left + (right - left) // 2
        if can_go(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


ans = simulate()
print(ans)
