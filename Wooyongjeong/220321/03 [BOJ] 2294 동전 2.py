def solution(n, k, coins):
    INF = int(1e9)
    dp = [INF] * (k + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i], k + 1):
            dp[j] = min(dp[j - coins[i]] + 1, dp[j])
    return dp[k] if dp[k] != INF else -1


if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    print(solution(n, k, coins))
