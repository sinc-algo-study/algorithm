from sys import stdin

n = int(stdin.readline())
poster = []
num = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    poster.append((x, y))
    if x not in num:
        num.append(x)
    if y not in num:
        num.append(y)
num.sort()          # [1,2,3,4,6,7,8,10]

wall = [-1] * len(num)
for idx, (x, y) in enumerate(poster):
    n1 = num.index(x)
    n2 = num.index(y)
    for i in range(n1, n2+1):
        wall[i] = idx

print(len(set(wall)))
