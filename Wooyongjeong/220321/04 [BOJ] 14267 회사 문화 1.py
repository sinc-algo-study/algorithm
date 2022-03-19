import sys
sys.setrecursionlimit(10**6)


def dfs(curr):
    for node in child[curr]:
        compliments[node] += compliments[curr]
        dfs(node)


if __name__ == '__main__':
    n, m = map(int, input().split())
    bosses = [0] + list(map(int, input().split()))
    child = [[] for _ in range(n + 1)]
    for u in range(2, n + 1):
        v = bosses[u]
        child[v].append(u)

    compliments = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        compliments[a] += b

    dfs(1)
    for i in range(1, n + 1):
        print(compliments[i], end=' ')
    print()
