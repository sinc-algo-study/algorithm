"""
전형적인 dp문제
1. 한 잔만 마시고 건너뛰기
2. 두 잔 마시고 건너뛰기
를 계속 비교해 나가며 dp 배열 완성
"""


def solution(n, wines):
    wines.insert(0, 0)
    dp = [0] * (n + 1)
    dp[1] = wines[1]
    if n == 1:
        return dp[n]
    dp[2] = dp[1] + wines[2]
    if n == 2:
        return dp[n]
    for i in range(3, n + 1):
        # 이전 와인을 먹은 경우, 이전 와인을 안 먹은 경우 (위에서부터 1, 2)
        # 이전 와인과 그 이전 와인까지 안 먹고 왔을 수도 있음 (3)
        dp[i] = max(
            dp[i - 3] + wines[i - 1] + wines[i],  # i-3: ?, i-2: X, i-1: O, i:O
            dp[i - 2] + wines[i],  # i-2: ?, i-1: X, i: O
            dp[i - 1]  # i-2: ?, i-1: ?, i: X
        )
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    wines = [int(input()) for _ in range(n)]
    print(solution(n, wines))
