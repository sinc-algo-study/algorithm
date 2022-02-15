from sys import stdin

s = stdin.readline().strip()
t = stdin.readline().strip()

# 2차원 dp 배열 (x축과 y축에 문자열,,)
sl, tl = len(s), len(t)
dp = [[0] * (tl+1) for _ in range(sl+1)]
''' 같은 글자 나오면 dp[현재 글자들] = dp[전 글자들 값] + 1 
  E C A D A D A B R B C R D A R A
A 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1
B 0 0 0 0 0 0 0 2 0 1 0 0 0 0 0 0
R 0 0 0 0 0 0 0 0 3 0 0 1 0 0 1 0
A 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 2
C 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 힘들당
'''
for i in range(sl):
    for j in range(tl):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
print(max(map(max, dp)))
