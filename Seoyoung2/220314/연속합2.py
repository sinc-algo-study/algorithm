from sys import stdin
from math import inf

N = int(stdin.readline())
num = list(map(int, stdin.readline().split()))

# 음수의 개수만큼 열을 만들어서 dp ==> 메모리초과
# m_idx = [idx for idx in range(N) if num[idx] < 0]
# m_cnt = len(m_idx)
#
# dp = [[-inf] * N for _ in range(m_cnt+1)]
# for i in range(N):
#     dp[0][i] = max(num[i], dp[0][i-1]+num[i])
# for i in range(1, m_cnt+1):
#     for j in range(N):
#         if j == m_idx[i-1]:
#             dp[i][j] = dp[i][j-1]
#         else:
#             dp[i][j] = max(num[j], dp[i][j-1]+num[j])
dp = [[-inf] * N for _ in range(2)]
for i in range(N):
    dp[0][i] = max(num[i], dp[0][i-1]+num[i])
    # i번째를 제외하는 경우, 이전에 이미 제외해서 i번째 포함하는 경우
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+num[i])

ans = max(map(max, dp))
print(num[0] if N == 1 else ans)
