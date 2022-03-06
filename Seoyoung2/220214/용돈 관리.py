from sys import stdin

N, M = map(int, stdin.readline().split())
# N일 동안 사용할 금액을 계산, 정확히 M번만 통장에서 돈을 빼서 쓰기로.
# 통장에서 K원을 인출하며, K원으로 하루를 보낼 수 있으면 그대로 사용하고 모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다.
# 다만 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.
# 필요한 최소 금액 K?

out = [int(stdin.readline()) for _ in range(N)]
# 이분탐색을 위해 총 사용 금액 기준 left, right 설정 (부족하면 입금하고 다시 인출이기 떄문에 K의 최속값은 소비금액의 최댓값)
left = max(out)
right = sum(out)

while left <= right:
    mid = (left + right) // 2
    price, cnt = mid, 1         # 처음 인출 (mid원)
    for o in out:
        if price < o:
            price = mid         # 부족하면 입금하고 다시 인출
            cnt += 1
        price -= o
    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid               # min(ans, mid)값 안구해도 작아지는 값

print(ans)

'''
7 5 <K=500>
100 500(1) -> 400위에
400 400(1) -> 0
300 500(2) -> 200
100 200(2) -> 100(남은금액 입금)
500 500(3) -> 0
101 500(4) -> 399(남은금액 입금)
400 500(5) -> 100
'''