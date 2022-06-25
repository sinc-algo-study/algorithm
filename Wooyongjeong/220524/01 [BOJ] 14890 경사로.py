def get_roads(n, board):
    roads = []
    for road in board:
        roads.append(road)

    for j in range(n):
        road = []
        for i in range(n):
            road.append(board[i][j])
        roads.append(road)

    return roads


def can_pass(n, length, road):
    def in_range(i):
        return 0 <= i < n

    check_ramp = [False] * n

    for i in range(n - 1):
        if road[i] == road[i + 1]:
            continue
        elif abs(road[i] - road[i + 1]) > 1:
            return False

        if road[i] > road[i + 1]:
            # 낮아지는 경사로 설치
            # i + 1부터 length만큼 끝방향으로 설치
            height = road[i + 1]
            ramp_range = range(i + 1, i + 1 + length)
        else:
            # 높아지는 경사로 설치
            # i부터 length만큼 시작방향으로 설치
            height = road[i]
            ramp_range = range(i, i - length, -1)

        for j in ramp_range:
            if not in_range(j) or road[j] != height or check_ramp[j]:
                return False
            check_ramp[j] = True
    return True


def solution(n, length, board):
    pass_cnt = 0
    for road in get_roads(n, board):
        if can_pass(n, length, road):
            pass_cnt += 1
    return pass_cnt


if __name__ == '__main__':
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, L, board))
