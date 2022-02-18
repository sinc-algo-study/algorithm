from sys import stdin
'''
대표적인 dp 문제

포도주 잔을 선택하면 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i])
             선택X     한칸 떨어져서 선택     두칸 떨어지고 전꺼랑 지금 선택
             O X        O X O               O X O O
'''

N = int(stdin.readline())
wine = [int(stdin.readline()) for _ in range(N)]

if N == 1:
    print(wine[0])
else:
    dp = [0] * (N+1)
    dp[0], dp[1], dp[2] = 0, wine[0], wine[0]+wine[1]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+wine[i-1], dp[i-3]+wine[i-2]+wine[i-1])
    print(max(dp))