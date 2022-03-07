import sys
input = sys.stdin.readline
from bisect import bisect_left

# DP
def dp_func(arr):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 이분탐색
def bisect_func(arr):
    dp = [arr[0]]
    for i in range(n):
        if arr[i]>dp[-1]:
            dp.append(arr[i])
        else :
            idx = bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    return len(dp)


if '__main__' == __name__:
    n = int(input())
    arr = list(map(int, input().split()))

    print(dp_func(arr))
    print(bisect_func(arr))


