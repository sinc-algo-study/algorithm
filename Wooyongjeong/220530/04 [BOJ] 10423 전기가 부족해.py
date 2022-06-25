n, m, k = map(int, input().split())
parents = [i for i in range(n + 1)]
power_plants = list(map(int, input().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a not in power_plants and b in power_plants:
        # b만 발전소에 연결되어 있는 경우
        parents[a] = b
    elif a in power_plants and b not in power_plants:
        # a만 발전소에 연결되어 있는 경우
        parents[b] = a
    elif a < b:
        parents[b] = a
    else:
        parents[a] = b


def same_parents(a, b):
    if find_parent(a) in power_plants and find_parent(b) in power_plants:
        return True
    return find_parent(a) == find_parent(b)


edges.sort()
answer = 0
for w, u, v in edges:
    if not same_parents(u, v):
        answer += w
        union_parent(u, v)
print(answer)
