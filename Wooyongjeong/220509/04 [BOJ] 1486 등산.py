import collections
import pprint


def convert(a):
    if a.isupper():
        return ord(a) - ord('A')
    return ord(a) - ord('a') + 26


def convert_to_height(mountain):
    for i in range(N):
        for j in range(M):
            mountain[i][j] = convert(mountain[i][j])


def climb_up(mountain):
    """
    등산하는 함수
    문제에서 주어진 대로 BFS
    현재 위치와 높이가 같거나 낮은 곳으로 갈 때는 1만큼
    현재 위치보다 높은 데로 갈 때는 (두 위치의 높이 차) ** 2만큼
    걸리는 시간 계산

    걸리는 시간이 D보다 크면 못 감
    """
    def get_time(x, y, nx, ny):
        if mountain[x][y] >= mountain[nx][ny]:
            return 1
        return (mountain[nx][ny] - mountain[x][y]) ** 2

    dist = [[-1] * M for _ in range(N)]
    q = collections.deque()

    dist[0][0] = 0
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if abs(mountain[nx][ny] - mountain[x][y]) > T:
                # 높이 차가 T보다 같거나 작은 데로만 다닐 수 있음
                continue

            time = get_time(x, y, nx, ny)
            if dist[x][y] + time > D:
                # 시간이 D보다 많이 걸리면 못 감
                continue
            if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + time:
                dist[nx][ny] = dist[x][y] + time
                q.append((nx, ny))

    return dist


def climb_down(mountain):
    """
    하산하는 함수
    모든 위치에서 호텔로 돌아가는 BFS를 돌리지 말고, 반대로 생각

    (등산) 현재 위치와 높이가 같거나 낮은 곳으로 갈 때는 1만큼
    => (하산) 현재 위치와 높이가 같거나 높은 데로 갈 때는 1만큼

    (등산) 현재 위치보다 높은 데로 갈 때는 (두 위치의 높이 차) ** 2만큼
    => (하산) 현재 위치보다 낮은 데로 갈 때 (두 위치의 높이 차) ** 2만큼
    걸리는 시간 계산

    걸리는 시간이 D보다 크면 못 감
    """
    def get_time(x, y, nx, ny):
        if mountain[x][y] <= mountain[nx][ny]:
            return 1
        return (mountain[x][y] - mountain[nx][ny]) ** 2

    dist = [[-1] * M for _ in range(N)]
    q = collections.deque()

    dist[0][0] = 0
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if abs(mountain[nx][ny] - mountain[x][y]) > T:
                # 높이 차가 T보다 같거나 작은 데로만 다닐 수 있음
                continue

            time = get_time(x, y, nx, ny)
            if dist[x][y] + time > D:
                # 시간이 D보다 많이 걸리면 못 감
                continue
            if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + time:
                dist[nx][ny] = dist[x][y] + time
                q.append((nx, ny))

    return dist


def solution(mountain):
    convert_to_height(mountain)
    up = climb_up(mountain)
    down = climb_down(mountain)

    answer = 0

    for i in range(N):
        for j in range(M):
            if up[i][j] == -1 or down[i][j] == -1:
                continue
            if up[i][j] + down[i][j] <= D:
                answer = max(answer, mountain[i][j])

    return answer


if __name__ == '__main__':
    INF = int(1e9)
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]

    N, M, T, D = map(int, input().split())
    mountain = [list(input()) for _ in range(N)]
    print(solution(mountain))
