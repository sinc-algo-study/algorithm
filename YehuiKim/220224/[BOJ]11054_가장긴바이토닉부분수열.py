import sys
input = sys.stdin.readline

'''
=> [BOJ]11053_가장 긴 증가하는 부분 수열
'''

def getDp(arr):
    dp1 = [1 for _ in range(n)]
    dp2 = [1 for _ in range(n)]
    reversedArr = list(reversed(arr))
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp1[i] = max(dp1[i], dp1[j]+1)
            if reversedArr[i]>reversedArr[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp = [dp1[i]+dp2[n-i-1] for i in range(n)]
    return max(dp)-1


if '__main__' == __name__:
    n = int(input())
    arr = list(map(int, input().split()))
    print(getDp(arr))