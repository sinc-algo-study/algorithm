import collections


def find_parent(parents, x):
    if parents[x] != x:
        return find_parent(parents, parents[x])
    return x


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def solution(n, m, k, friend_fees, edges):
    graph = [[] for _ in range(n + 1)]
    parents = [0] * (n + 1)
    for i in range(1, n + 1):
        parents[i] = i

    for v, w in edges:
        graph[v].append(w)
        graph[w].append(v)
        union_parent(parents, v, w)

    friend_groups = collections.defaultdict(list)
    for i in range(1, n + 1):
        group = find_parent(parents, i)
        friend_groups[group].append(i)

    result = 0
    for group in friend_groups.values():
        min_fee = int(1e9)
        for friend in group:
            min_fee = min(min_fee, friend_fees[friend])
        result += min_fee

    return result if result <= k else "Oh no"


if __name__ == '__main__':
    N, M, k = map(int, input().split())
    friend_fees = [0] + list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(solution(N, M, k, friend_fees, edges))
