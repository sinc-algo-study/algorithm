import collections
import heapq


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def check(x, y, board, visited):
    return in_range(x, y) and not visited[x][y] and board[x][y] != 1


def bfs1(sx, sy, board):
    q = collections.deque()
    visited = [[False] * N for _ in range(N)]

    q.append((sx, sy, 0))
    visited[sx][sy] = True
    min_dist = INF
    candidates = []

    while q:
        x, y, dist = q.popleft()
        if board[x][y] > 1 and min_dist >= dist:
            min_dist = dist
            heapq.heappush(candidates, (x, y))
            continue
        elif dist > min_dist:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not check(nx, ny, board, visited):
                continue

            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True

    if not candidates:
        return -1, -1, INF
    px, py = heapq.heappop(candidates)
    return px, py, min_dist


def bfs2(px, py, ex, ey, board):
    q = collections.deque()
    visited = [[False] * N for _ in range(N)]

    q.append((px, py, 0))
    visited[px][py] = True

    while q:
        x, y, dist = q.popleft()
        if x == ex and y == ey:
            return dist

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not check(nx, ny, board, visited):
                continue

            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True

    return INF


def solution(sx, sy, fuel, board, destinations):
    for _ in range(M):
        px, py, dist = bfs1(sx, sy, board)
        if px == -1 and py == -1:
            return -1

        fuel -= dist
        if fuel < 0:
            return -1

        passenger = board[px][py] - 2
        board[px][py] = 0
        ex, ey = destinations[passenger]
        dist = bfs2(px, py, ex, ey, board)

        if fuel - dist < 0:
            return -1

        fuel += dist
        sx, sy = ex, ey

    return fuel


if __name__ == '__main__':
    INF = int(1e9)
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]

    N, M, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    taxi_x, taxi_y = map(int, input().split())
    taxi_x, taxi_y = taxi_x - 1, taxi_y - 1
    destinations = []
    for i in range(M):
        sx, sy, ex, ey = map(int, input().split())
        board[sx - 1][sy - 1] = i + 2
        destinations.append((ex - 1, ey - 1))

    print(solution(taxi_x, taxi_y, fuel, board, destinations))
