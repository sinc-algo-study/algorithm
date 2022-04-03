from sys import stdin
from itertools import combinations

N, M, H = map(int, stdin.readline().split())
ladder = [[False] * (N+1) for _ in range(H+1)]
garo = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

empty = []
for i in range(1, H+1):
    for j in range(1, N):
        if (i, j) in garo:
            ladder[i][j] = True
        else:
            empty.append((i, j))

# 조합으로 가능..?
ans = -1
for i in range(4):
    for combi in combinations(empty, i):
        stop = False

        # 가로선이 맞닿아 있으면 안됨
        add_l = [l[:] for l in ladder]
        for cx, cy in combi:
            add_l[cx][cy] = True    # 본인들 끼리도 닿으면 안됨
        for cx, cy in combi:
            if add_l[cx][cy-1] or add_l[cx][cy+1]:
                stop = True
                break
        if stop:
            continue

        # 내려가기, 틀리면 바로 끝
        for idx in range(1, N+1):
            num = idx
            for down in range(1, H+1):
                if add_l[down][num-1]:
                    num -= 1
                elif add_l[down][num]:
                    num += 1
            if num != idx:
                stop = True
                break
        if stop:
            continue
        else:
            ans = i
            print(ans)
            exit(0)
print(ans)
