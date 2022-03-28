from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
vip = [0] + [int(stdin.readline()) for _ in range(M)] + [N+1]

'''
dp[n] = n의 자리까지 있을 때의 경우의 수
      = dp[n-1] + dp[n-2]
      = n이 n자리에 앉는 경우 나머지애들 잘 앉히면 됨 + n이 n-1자리에 앉는 경우 n-1은 n자리에 앉아야하고 나머지애들 잘 앉히면 됨
'''

dp = [0] * (N+1)
dp[0] = dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# vip들 사이 공간의 경우의 수 모두 곱하기 vip=[0,4,7,10] space=[3,2,2]
space = [vip[i+1]-vip[i]-1 for i in range(M+1)]
ans = 1
for sp in space:
    ans *= dp[sp]
print(ans)

