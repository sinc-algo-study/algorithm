import heapq


def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)
        if dist > distance[cur]:
            continue

        for node, node_dist in graph[cur]:
            cost = dist + node_dist
            if cost >= distance[node]:
                continue
            heapq.heappush(q, (cost, node))
            distance[node] = cost

    return distance


def farming(start, maximum_dist, n, items, graph):
    item_cnt = 0
    dist = dijkstra(start, n, graph)
    for node in range(1, n + 1):
        if dist[node] > maximum_dist:
            continue
        item_cnt += items[node - 1]
    return item_cnt


def solution(n, m, items, graph):
    answer = 0
    for start in range(1, n + 1):
        answer = max(answer, farming(start, m, n, items, graph))
    return answer


if __name__ == '__main__':
    INF = int(1e9)
    N, M, R = map(int, input().split())
    items = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(R):
        u, v, dist = map(int, input().split())
        graph[u].append([v, dist])
        graph[v].append([u, dist])
    print(solution(N, M, items, graph))
