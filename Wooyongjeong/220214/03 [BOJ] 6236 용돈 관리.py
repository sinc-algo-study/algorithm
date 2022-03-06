def solution(n, m, to_spent):
    def withdraw(k):
        money = 0  # 남은 돈
        count = 0  # 인출 횟수
        for i in range(n):
            # 인출할 돈이 써야할 돈보다 작으면 안됨
            if k < to_spent[i]:
                return m + 1
            # 남은 돈이 써야할 돈보다 크거나 같으면 (써야할 돈)을 사용하고 다음날로 넘어감
            if money >= to_spent[i]:
                money -= to_spent[i]
            # 남은 돈이 써야할 돈보다 적다면, 인출해서 써야함
            # 인출 count를 1 증가시키고, 남은 돈을 (인출한 돈) - (써야할 돈)으로 세팅하고
            # 다음 날로 넘어감
            else:
                count += 1
                money = k - to_spent[i]
        return count

    lo = 0
    hi = sum(to_spent)
    answer = int(1e9)
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        withdrawal_count = withdraw(mid)
        if withdrawal_count > m:
            lo = mid + 1
        else:
            hi = mid - 1
            answer = min(answer, mid)
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    to_spent = [int(input()) for _ in range(N)]
    print(solution(N, M, to_spent))
