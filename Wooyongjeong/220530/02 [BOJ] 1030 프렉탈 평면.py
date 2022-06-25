s, N, K, R1, R2, C1, C2 = map(int, input().split())


def is_black(x, y, border):
    """
    한 변의 길이가 length인 평면의 가운데 K * K 영역에 속해있는 지 판별

    border = length // N라고 했을 때,
    x, y가 모두 [border * (N - K) // 2, border * (N + K) // 2]에 속해 있으면 됨
    """
    return border * (N - K) // 2 <= x < border * (N + K) // 2 and \
           border * (N - K) // 2 <= y < border * (N + K) // 2


def solve(length, x, y):
    if length == 1:
        return 0
    border = length // N
    if is_black(x, y, border):
        return 1
    return solve(border, x % border, y % border)


if s == 0:
    print(0)
else:
    length = pow(N, s)
    for i in range(R1, R2 + 1):
        for j in range(C1, C2 + 1):
            print(solve(length, i, j), end='')
        print()
