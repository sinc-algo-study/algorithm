# 8개로 만들 수 있는 조합: 2개 + 6개
# 9개로 만들 수 있는 조합: 2개 + 7개
# 10개로 만들 수 있는 조합: 5개 + 5개
# ... 15개로 만들 수 있는 조합: 8개(2개 + 6개) + 7개
# dp[n] = min(dp[n-2] + min_numbers[2], dp[n-3] + min_numbers[3],
#                ..., dp[n-7] + min_numbers[7])
def get_min(n):
    arr = [0, 0, 1, 7, 4, 2, 0, 8]
    dp = arr[:]
    dp[6] = 6

    for _ in range(n - len(arr) + 1):
        dp.append(INF)

    for num in range(8, n + 1):
        for i in range(2, 8):
            dp[num] = min(dp[num], dp[num - i] * 10 + arr[i])

    return dp


def get_max(n):
    # n이 짝수면 111...1
    # n이 홀수면 711...1
    if n % 2 == 1:
        return '7' + '1' * ((n - 3) // 2)
    return '1' * (n // 2)


if __name__ == '__main__':
    INF = int(1e9)
    test_case = int(input())
    min_arr = get_min(100)
    for _ in range(test_case):
        n = int(input())
        print(min_arr[n], get_max(n))
