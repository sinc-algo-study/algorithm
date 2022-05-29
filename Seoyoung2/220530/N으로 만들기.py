N = input()


# 하나씩 지워보기 ..?
def dfs(snum):
    global ans
    if len(snum) == 1:
        ans += 1
        return
    # 숫자를 적는 과정에서 나온 수가 순서대로 모두 같다면 같은 방법
    S = set(snum)
    if len(S) == 1:
        ans += 1
        return
    dfs(snum[1:])
    dfs(snum[:-1])


ans = 0
dfs(N)
print(ans)