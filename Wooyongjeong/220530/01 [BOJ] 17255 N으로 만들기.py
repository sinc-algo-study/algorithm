N = input()
ans = set()

# 경로를 모두 이어 붙였을 때 길이
# 예) 1 -> 21 -> 521 => 121521
# 1 ~ len(N)까지의 합
target = len(N) * (len(N) + 1) // 2


def dfs(left, right, now):
    if len(now) == target:
        ans.add(now)
        return

    if left > 0:
        # 왼쪽거를 이어붙일 수 있는 경우
        # 경로를 계속해서 now에 붙여야 하므로 N[left - 1: right + 1]을 붙여줌
        dfs(left - 1, right, now + N[left - 1: right + 1])
    if right < len(N):
        # 오른쪽거를 이어붙일 수 있는 경우
        # 경로를 계속해서 now에 붙여야 하므로 N[left: right + 2]를 붙여줌
        dfs(left, right + 1, now + N[left: right + 2])


for i in range(len(N)):
    dfs(i, i, N[i])
print(len(ans))
