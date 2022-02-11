import collections


def solution(n, m, pool):
    def get_min_max_height():
        min_height = int(1e9)
        max_height = 0
        for i in range(n):
            for j in range(m):
                if max_height < pool[i][j]:
                    max_height = pool[i][j]
                if min_height > pool[i][j]:
                    min_height = pool[i][j]
        return min_height, max_height

    def bfs(x, y, height):
        q = collections.deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            x, y = q.popleft()
            water[x][y] -= 1  # 물 한칸 제거
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 이미 제거했거나 가장자리라면 continue
                if visited[nx][ny] or nx == 0 or nx == n - 1 or \
                        ny == 0 or ny == m - 1:
                    continue
                # 현재 층에서 이 칸에 물이 height까지 차 있고, 흘러내리는 경우
                if pool[nx][ny] + water[nx][ny] == height and water[nx][ny] > 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    min_height, max_height = get_min_max_height()
    water = [[0] * m for _ in range(n)]  # max_height까지 채운 물의 높이
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            water[i][j] = max_height - pool[i][j]

    # 가장 윗층부터 순서대로 물을 제거
    for h in range(max_height, min_height, -1):
        visited = [[False] * m for _ in range(n)]
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                # 현재 칸에 물이 있고, 아직 제거하지 않은 경우
                if water[x][y] > 0 and not visited[x][y]:
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        # 현재 칸보다 옆 칸이 더 낮아서 물이 흘러내리는 경우
                        if pool[nx][ny] + water[nx][ny] < \
                                pool[x][y] + water[x][y]:
                            bfs(x, y, h)
                            break

    answer = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            answer += water[i][j]
    return answer


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    N, M = map(int, input().split())
    pool = [list(map(int, input())) for _ in range(N)]
    print(solution(N, M, pool))
