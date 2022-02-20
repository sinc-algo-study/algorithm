import collections


def solution(n, space):
    INF = int(1e9)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def get_distance():
        distance = [[-1] * n for _ in range(n)]
        q = collections.deque()
        q.append((shark_x, shark_y))
        distance[shark_x][shark_y] = 0
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 격자 안이면서, 방문한 적 없고 빈 칸이거나 상어보다 작은 물고기가 있는 칸
                if 0 <= nx < n and 0 <= ny < n and \
                        distance[nx][ny] == -1 and space[nx][ny] <= size:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
        return distance

    def find_closest_fish(distance):
        x, y = 0, 0
        min_dist = INF
        for i in range(n):
            for j in range(n):
                # 상어가 잡아먹을 수 있는 물고기 탐색
                if distance[i][j] != -1 and 1 <= space[i][j] < size and \
                        min_dist > distance[i][j]:
                    min_dist = distance[i][j]
                    x, y = i, j

        # 잡아먹을 수 있는 물고기가 없었음
        if min_dist == INF:
            return None
        return x, y, min_dist

    shark_x, shark_y = -1, -1
    size = 2
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                shark_x, shark_y = i, j
                space[i][j] = 0

    time = 0
    eat_count = 0
    while True:
        # 모든 맵에 대해 상어와의 거리를 구함
        distance = get_distance()
        # distance로부터 가장 가까운 물고기를 결정
        fish = find_closest_fish(distance)
        if fish is None:
            return time

        shark_x, shark_y, dist = fish
        space[shark_x][shark_y] = 0
        time += dist
        eat_count += 1
        if eat_count == size:
            size += 1
            eat_count = 0


if __name__ == '__main__':
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, space))
