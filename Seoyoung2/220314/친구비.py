from sys import stdin
from math import inf

N, M, k = map(int, stdin.readline().split())
price = list(map(int, stdin.readline().split()))


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


root = [i for i in range(N)]
for _ in range(M):
    v, w = map(int, stdin.readline().split())
    union(v-1, w-1)

# 찐 root를 찾기위해
for i in range(N):
    find(i)

res = {}
for n in range(N):
    r = root[n]
    if r not in res:
        res[r] = inf
    res[r] = min(res[r], price[n])
ans = sum(res.values())
print(ans if ans <= k else "Oh no")

'''
5 4 100
1 2 3 4 5
1 5
4 2
2 3
4 5

3 1 100
10 10 10 
1 2
'''