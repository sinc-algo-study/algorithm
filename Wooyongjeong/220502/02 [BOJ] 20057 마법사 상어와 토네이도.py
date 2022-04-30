import math


def rotate_percents(percents: list[list[int]]) -> list[list[int]]:
    # 비율 배열을 시계 방향으로 90도 회전하여 반환하는 함수
    new_percents = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_percents[5 - j - 1][i] = percents[i][j]
    return new_percents


def get_sand(origin: int, percent: float) -> int:
    # 원래 모래의 양 origin과 흩날릴 비율 percent에 맞게 흩날릴 모래의 양을 반환하는 함수
    if percent == 0:
        return 0
    elif percent < 0.4:
        return math.floor(origin * percent)
    return origin \
           - math.floor(origin * 0.01) * 2 \
           - math.floor(origin * 0.02) * 2 \
           - math.floor(origin * 0.07) * 2 \
           - math.floor(origin * 0.1) * 2 \
           - math.floor(origin * 0.05)


def in_range(x: int, y: int) -> bool:
    return 0 <= x < N and 0 <= y < N


def move_sand_and_get_out_sand(x: int, y: int, a: list[list[int]],
                               percents: list[list]) -> int:
    # 모래를 흩날리고 격자 밖으로 나간 모래를 계산하여 반환하는 함수
    out_sand = 0
    origin = a[x][y]
    a[x][y] = 0

    if origin == 0:
        return out_sand

    for i in range(-2, 3):
        for j in range(-2, 3):
            percent = percents[i + 2][j + 2]

            if percent == 0:
                continue

            sand = get_sand(origin, percent)

            nx, ny = x + i, y + j
            if not in_range(nx, ny):
                out_sand += sand
                continue

            a[nx][ny] += sand

    return out_sand


def solution(n: int, a: list[list[int]]) -> int:
    percents = [
        [0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0.45, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]
    ]

    ans = 0
    x, y = n // 2, n // 2
    cnt = 1
    d = 0
    while True:
        # 같은 횟수만큼 2번씩 돔
        for _ in range(2):
            # 이동하는 횟수
            for _ in range(cnt):
                x += dx[d]
                y += dy[d]

                ans += move_sand_and_get_out_sand(x, y, a, percents)

                if x == 0 and y == 0:
                    return ans

            d = (d + 1) % 4  # 방향 전환
            percents = rotate_percents(percents)  # 비율 배열을 회전

        cnt += 1


if __name__ == '__main__':
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, A))
