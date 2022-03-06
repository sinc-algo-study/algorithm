import heapq


def solution(n, graph):
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = graph[nx][ny] + dist
            if distance[nx][ny] <= cost:
                continue
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

    return distance[n - 1][n - 1]


if __name__ == '__main__':
    problem_count = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    INF = int(1e9)
    while True:
        N = int(input())
        if N == 0:
            break
        cave = [list(map(int, input().split())) for _ in range(N)]
        print(f"Problem {problem_count}: {solution(N, cave)}")
        problem_count += 1
