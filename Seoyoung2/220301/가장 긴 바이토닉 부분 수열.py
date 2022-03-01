from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

# 올라가는거 따로, 내려가는거 따로 만들고 합치기
# A : 1 5 2 1 4 3 4 5 2 1
# dp: 1 2 2 1 3 3 4 5 2 1 (올라가는거)
# dp: 1 5 2 1 4 3 3 3 2 1 (역순으로 올라가는거=내려가는거)


def make_dp(num, dp):
    for i in range(N):
        for j in range(i):
            if num[i] > num[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1


up, down = [1] * N, [1] * N
make_dp(A, up)
make_dp(A[::-1], down)

print(up)           # [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
print(down[::-1])   # [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]

print(max([x+y for x, y in zip(up, down[::-1])]) - 1)


