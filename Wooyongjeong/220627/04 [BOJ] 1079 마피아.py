"""
마피아가 한 명 남은 상황임

각 사람의 '유죄 지수'
이건 낮에 누굴 죽일지 고름 -> 누가 죽으면 각자의 '반응'만큼 유죄 지수가 변함

1. 밤에 마피아가 한 명을 죽임. 이 때, 유죄 지수가 '반응 R'만큼 변하는데
    -> 만약 참가자 i가 죽으면, 참가자 j의 '유죄 지수'는 R[i][j]만큼 변함
2. 낮에는 현재 남아 있는 참가자 중 '유죄 지수'가 가장 높은 사람을 죽임
    -> 동일한 유죄 지수인 참가자가 여러 명이면 번호가 가장 작은 사람을 죽임
    -> 이 땐 유죄 지수 안 바뀜

매번 최적의 선택을 한다
N <= 16
걍 완탐 돌려도 될 거 같은데?
"""
N = int(input())
guilty = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
player = int(input())

ans = 0
killed = [False for _ in range(N)]


def find_fall_guy():
    max_guilty = 0
    fall_guy = 0

    for i in range(N):
        if not killed[i] and guilty[i] > max_guilty:
            max_guilty = guilty[i]
            fall_guy = i

    return fall_guy


def play_mafia_game(remain_player, night):
    global ans

    # 은진이가 죽었거나, 남아 있는 플레이어가 1명이라면 게임 종료
    if killed[player] or remain_player == 1:
        ans = max(ans, night)
        return

    # 밤
    if remain_player % 2 == 0:
        # 남은 사람들을 하나씩 다 죽여봄
        for i in range(N):
            # 은진이는 당연히 넘어가고, 이미 죽은 사람도 넘어감
            if i == player or killed[i]:
                continue

            killed[i] = True  # 죽이고
            for j in range(N):  # 유죄 지수 변화
                if killed[j]:
                    continue
                guilty[j] += R[i][j]

            play_mafia_game(remain_player - 1, night + 1)

            for j in range(N):  # 유죄 지수 되돌림
                if killed[j]:
                    continue
                guilty[j] -= R[i][j]
            killed[i] = False  # 살리고 (백트래킹)
    # 낮
    else:
        fall_guy = find_fall_guy()  # 가장 유죄 지수가 높은 사람을 찾음

        killed[fall_guy] = True  # 그 사람을 죽이고
        play_mafia_game(remain_player - 1, night)  # 다음으로
        killed[fall_guy] = False  # 다시 살리고 (백트래킹)


play_mafia_game(N, 0)
print(ans)
