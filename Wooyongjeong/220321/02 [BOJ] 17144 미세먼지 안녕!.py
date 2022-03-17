import collections
import math


def solution(r, c, t, room):
    def is_able_to_spread(x, y):
        return 0 <= x < r and 0 <= y < c and (x, y) not in air_purifiers

    def spread_dust():
        tmp = [[0] * c for _ in range(r)]
        while q:
            x, y = q.popleft()
            dust = math.trunc(room[x][y] / 5)
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if is_able_to_spread(nx, ny):
                    cnt += 1
                    tmp[nx][ny] += dust
            tmp[x][y] -= dust * cnt

        for i in range(r):
            for j in range(c):
                room[i][j] += tmp[i][j]

    def run_air_purifier(purifier):
        x, y = air_purifiers[purifier]
        d = 0
        dust = 0
        while True:
            nx = x + purifier_dx[d]
            ny = y + purifier_dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if (nx, ny) == air_purifiers[purifier]:
                    room[nx][ny] = 0
                    break
                room[nx][ny], dust = dust, room[nx][ny]
                x, y = nx, ny
            else:
                if purifier == 1:
                    d -= 1
                    if d < 0:
                        d = 3
                else:
                    d += 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    purifier_dx = [0, -1, 0, 1]
    purifier_dy = [1, 0, -1, 0]

    q = collections.deque()
    air_purifiers = []
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                air_purifiers.append((i, j))
            elif room[i][j] > 0:
                q.append((i, j))

    for time in range(t):
        # 1. 미세먼지 확산
        spread_dust()

        # 2. 공기청정기 작동
        for i in range(2):
            run_air_purifier(i)

        if time < t:
            for i in range(r):
                for j in range(c):
                    if room[i][j] > 0:
                        q.append((i, j))

    return sum(sum(x) for x in room)


if __name__ == '__main__':
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    print(solution(R, C, T, room))
