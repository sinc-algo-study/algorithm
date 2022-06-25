INF = int(1e9)
n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = [i for i in range(n)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i, j)


result = set()
for city in plan:
    result.add(find_parent(city - 1))

print("YES" if len(result) == 1 else "NO")
