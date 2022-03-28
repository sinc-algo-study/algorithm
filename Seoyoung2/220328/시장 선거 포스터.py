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

'''
from sys import stdin

input = stdin.readline
n = int(input())
poster = [tuple(map(int, input().split())) for _ in range(n)]
count = 1
covered = [poster[n - 1]]


def fixcovered(new: tuple):
    global covered
    a, b = new[0], new[1]
    start, end = a, b
    for (x, y) in covered[:]:
        if b + 1 < x or y < a - 1:
            pass
        else:
            start = min(start, x)
            end = max(end, y)
            covered.remove((x, y))

    covered.append((start, end))


for i in range(n - 2, -1, -1):
    seen = True
    for (x, y) in covered:
        if x <= poster[i][0] and poster[i][1] <= y:
            seen = False
            break
    if seen:
        count += 1
        fixcovered(poster[i])
print(count)
'''
