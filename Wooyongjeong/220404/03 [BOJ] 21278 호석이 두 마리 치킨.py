import itertools


def get_dist(n, chickens, graph):
    dist = 0

    for i in range(1, n + 1):
        dist += min(graph[i][chickens[0]] * 2, graph[i][chickens[1]] * 2)

    return dist


def floyd_warshall(n, edges):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph


def solution(n, edges):
    # 건물 X 의 접근성은 X 에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단 시간이다.
    graph = floyd_warshall(n, edges)

    ans = [0, 0, INF]
    for chickens in itertools.combinations(range(1, n + 1), 2):
        dist = get_dist(n, chickens, graph)
        if dist < ans[-1]:
            ans = list(chickens) + [dist]
    return ans


if __name__ == '__main__':
    INF = int(1e9)
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(*solution(N, edges))
