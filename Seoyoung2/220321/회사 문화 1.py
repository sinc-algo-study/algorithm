from sys import stdin

n, k = map(int, stdin.readline().split())

coins = [int(stdin.readline()) for _ in range(n)]
dp = [0] + [100000] * k

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(-1 if dp[k] == 100000 else dp[k])
