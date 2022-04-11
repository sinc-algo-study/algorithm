def solution(gems, bag_idx, cur):
    # 가방을 다 썼거나, 보석을 다 썼으면
    if gems == (1 << N) - 1 or bag_idx >= M:
        return 0

    if dp[gems][bag_idx][cur] != 0:
        return dp[gems][bag_idx][cur]

    dp[gems][bag_idx][cur] = 0
    for i in range(N):
        # 지금 쓸려는 보석이 이미 사용한 보석이면
        if (gems & (1 << i)) != 0 or jewels[i] > C:
            continue

        # 이번 가방에 넣을 수 있으면
        if cur >= jewels[i]:
            dp[gems][bag_idx][cur] = \
                max(dp[gems][bag_idx][cur],
                    solution(gems | (1 << i), bag_idx, cur - jewels[i]) + 1)
        # 못 넣으면 다음 가방으로
        else:
            dp[gems][bag_idx][cur] = \
                max(dp[gems][bag_idx][cur],
                    solution(gems, bag_idx + 1, C))

    return dp[gems][bag_idx][cur]


if __name__ == '__main__':
    N, M, C = map(int, input().split())  # 보석 개수, 가방 개수, 가방 최대 한도
    jewels = list(map(int, input().split()))
    dp = [[[0] * (C + 1) for _ in range(M + 1)] for _ in range(1 << 14)]
    print(solution(0, 0, C))
