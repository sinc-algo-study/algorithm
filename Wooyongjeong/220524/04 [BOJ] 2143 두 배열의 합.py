"""
n, m <= 1000이므로
A와 B 배열의 모든 부분 배열의 합에 대한 경우의 수 O(N^2)으로 구하고
정렬 O(NlogN) 후 이진 탐색 O(logN)으로 가능
"""


import bisect


def get_subarray_sums(n, arr):
    result = []
    for i in range(n):
        a = arr[i]
        result.append(a)
        for j in range(i + 1, n):
            a += arr[j]
            result.append(a)
    return result


def solution(t, n, a, m, b):
    # A와 B의 모든 부 배열의 합 경우의 수를 구함
    a_sums = get_subarray_sums(n, a)
    b_sums = get_subarray_sums(m, b)

    # (A 부분배열의 합) + (B 부분배열의 합) = T 가 되는 경우의 수를 구해야 하므로
    # 모든 B 부분배열의 합에 대해서, (B 부분배열의 합) = T - (A 부분배열의 합)
    # 을 만족하는 B 부분배열의 개수를 구하면 됨
    # 이는 이진 탐색을 이용.. -> a_sums와 b_sums를 sort
    a_sums.sort()
    b_sums.sort()

    answer = 0
    for a_sum in a_sums:
        left = bisect.bisect_left(b_sums, t - a_sum)
        right = bisect.bisect_right(b_sums, t - a_sum)
        answer += right - left
    return answer


if __name__ == '__main__':
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    print(solution(T, N, A, M, B))
