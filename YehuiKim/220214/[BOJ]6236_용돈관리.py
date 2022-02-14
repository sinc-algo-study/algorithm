import sys
input = sys.stdin.readline


def withdraw(days):
    sorted_days = sorted(days)
    # 용돈의 최소값
    global small
    small = sorted_days[n-1]
    # 최대ni로 먼저 돌려봄
    ans = n_days(small)
    for r in range(n-1, 0, -1):
        for l in range(r,-1,-1):
            k = sorted_days[r] + sorted_days[l]
            # 최대ni보다 작은 k는 pass
            if k < small :
                break
            if k >= ans :
                continue
            ans = min(n_days(k), ans)
    return ans


def n_days(k):
    global small
    now = k
    cnt = 1
    for j in days:
        if j <= now:
            now -= j
        else:
            cnt += 1
            now = (k - j)
        if cnt > m:
            small = k
            return 10001
    return k

###########################
def new_withdraw(days):
    left = min(days)
    right = sum(days)

    while left <= right:
        k = (left + right)//2
        if k < max(days):
            left = k+1
            continue
        now = k
        cnt = 1
        for money in days:
            if now < money:
                now = k
                cnt += 1
            now -= money
        if cnt > m:
            left = k+1
        else:
            right = k-1
            ans = k

    return ans


if '__main__' == __name__ :
    n, m = map(int, input().split())
    days = [int(input()) for _ in range(n)]
    print(new_withdraw(days))
