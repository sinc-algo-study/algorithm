import collections


def get_new_dirs(d):
    if 0 <= d <= 1:  # 원래 상 or 화 -> 좌, 우
        return [2, 3]
    return [0, 1]  # 원래 좌 or 우 -> 상, 하


def solution(n, house):
    def is_able_to_go(x, y):
        if 0 <= x < n and 0 <= y < n and house[x][y] != '*':
            return True
        return False

    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    doors = []
    for i in range(n):
        for j in range(n):
            if house[i][j] == '#':
                doors.append((i, j))

    # mirrors[i][j][d]: (i, j)에서 진행 방향이 d일 때에 설치한 거울의 최소 개수
    mirrors = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    sx, sy = doors.pop()
    ex, ey = doors.pop()

    q = collections.deque()
    for d in range(4):
        q.append((sx, sy, d))
        mirrors[sx][sy][d] = 0

    while q:
        x, y, d = q.popleft()

        nx = x + dx[d]
        ny = y + dy[d]
        if not is_able_to_go(nx, ny):
            continue

        if nx == ex and ny == ey:
            if mirrors[nx][ny][d] > mirrors[x][y][d]:
                mirrors[nx][ny][d] = mirrors[x][y][d]
            continue

        if mirrors[nx][ny][d] > mirrors[x][y][d]:
            mirrors[nx][ny][d] = mirrors[x][y][d]
        q.append((nx, ny, d))

        if house[nx][ny] == '!':  # 거울 설치
            dirs = get_new_dirs(d)
            for nd in dirs:
                if mirrors[nx][ny][nd] > mirrors[x][y][d] + 1:
                    mirrors[nx][ny][nd] = mirrors[x][y][d] + 1
                    q.append((nx, ny, nd))

    answer = INF
    for mirror in mirrors[ex][ey]:
        answer = min(answer, mirror)
    return answer


if __name__ == '__main__':
    INF = int(1e9)
    N = int(input())
    house = [list(input()) for _ in range(N)]
    print(solution(N, house))
