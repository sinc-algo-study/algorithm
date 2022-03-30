def get_fibo(n):
    fibo = [0] * (n + 1)
    fibo[0] = 1
    fibo[1] = 1
    fibo[2] = 2
    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo


def solution(n, m, vip):
    fibo = get_fibo(n)

    ans = 1
    vip = [0] + vip
    for i in range(1, m + 1):
        ans *= fibo[vip[i] - vip[i - 1] - 1]

    ans *= fibo[n - vip[-1]]
    return ans


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    vip = [int(input()) for _ in range(M)]
    print(solution(N, M, vip))
