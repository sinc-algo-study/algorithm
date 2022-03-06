def get_lis(n, s):
    # LIS. 가장 긴 증가하는 부분수열
    lis = [0] * n
    for i in range(n):
        lis[i] = 1
        for j in range(i):
            if s[i] > s[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return lis


def get_reverse_lis(n, s):
    # (뒤쪽 인덱스부터 앞쪽 인덱스 방향으로) 가장 긴 증가하는 부분수열
    reverse_lis = [0] * n
    for i in range(n - 1, -1, -1):
        reverse_lis[i] = 1
        for j in range(n - 1, i - 1, -1):
            if s[i] > s[j]:
                reverse_lis[i] = max(reverse_lis[i], reverse_lis[j] + 1)
    return reverse_lis


def solution(n, s):
    lis = get_lis(n, s)
    reverse_lis = get_reverse_lis(n, s)

    answer = 0
    for a, b in zip(lis, reverse_lis):
        answer = max(answer, a + b - 1)
    return answer


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    print(solution(N, S))
