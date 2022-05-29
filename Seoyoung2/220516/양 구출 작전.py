import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
sheep = [0] * N
wolf = [0] * N
tree = [[] for _ in range(N)]
for i in range(1, N):
    t, a, p = sys.stdin.readline().split()     # i에서 p가는 다리 존재
    if t == 'S':
        sheep[i] = int(a)
    else:
        wolf[i] = int(a)
    tree[int(p)-1].append(i)


def dfs(idx):
    num = sheep[idx]
    for next in tree[idx]:
        num += dfs(next)
    # 늑대 있을 때
    if wolf[idx] > 0:
        if num < wolf[idx]:
            wolf[idx] -= num
            num = 0
        else:
            num -= wolf[idx]
            wolf[idx] = 0
    return num


print(dfs(0))