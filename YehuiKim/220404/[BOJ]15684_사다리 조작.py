'''
n - 세로선, m - 가로선
맨 처음부터 1->1인지 확인
=> 맞으면, 다음 세로선으로 넘어가서 확인
=> 아니면, 줄 그을 수 있는 모든 경우를 그어서 1되는지 체크
1 / 1 <-> 2
3 / 2 <-> 3
5 / 1 <-> 2
2 / 3 <-> 4
5 / 4 <-> 5
'''
# 연속되지 않는, 가능한 가로선 수가 3개 미만인데, 그걸로 안되면 끝.
# 최대 3개까지 : 3개 놨는데도 해결 안되면 끝.
'''import sys
input = sys.stdin.readline


def move():
    for i in range(h):
        tmp = i
        for j in range(n):
            if lines[i][j]:
                tmp += 1
            elif i>0 and lines[i-1][j]:
                tmp -= 1
        if i != tmp:
            return 0
    return 1


def dfs(cnt, idx, l):
    global ans
    if move():  # 모든 i가 i로 향하면
        ans = min(ans, cnt)  # 최솟값 갱신
        return
    if cnt==3 or cnt >= ans:  # 결과(최소그은횟수)보다 현재 cnt가 더 크면 할 필요x
        return

    for i in range(idx, h):
        if i == idx:
            k = l
        else :
            k = 0
        for j in range(k, n-1):
            if lines[j][i]:
                continue
            if j>0 and lines[j-1][i]:
                continue
            lines[j][i]=1
            dfs(cnt+1, i, j+2)
            lines[j][i]=0


if "__main__"==__name__:
    n, m, h = map(int, input().split())
    lines = [[0 for _ in range(h)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        lines[a-1][b-1]=1
    ans = 1000000
    dfs(0, 0, 0)
    print(ans if ans<4 else -1)'''

import sys
input = sys.stdin.readline


def move():
    for i in range(n):
        tmp = i
        for j in range(h):
            if lines[j][tmp]:
                tmp += 1
            elif tmp>0 and lines[j][tmp-1]:
                tmp -= 1
        if i != tmp:
            return 0
    return 1


def dfs(cnt, idx, l):
    global ans
    if move():  # 모든 i가 i로 향하면
        ans = min(ans, cnt)  # 최솟값 갱신
        return
    if cnt==3 or cnt >= ans:  # 결과(최소그은횟수)보다 현재 cnt가 더 크면 할 필요x
        return

    for i in range(idx, h):
        if i == idx:
            k = l
        else:
            k = 0
        for j in range(k, n-1):
            if lines[i][j] or lines[i][j+1]:
                continue
            if j>0 and lines[i][j-1]:
                continue
            lines[i][j]=1
            dfs(cnt+1, i, j+2)
            lines[i][j]=0


if "__main__"==__name__:
    n, m, h = map(int, input().split())
    lines = [[0 for _ in range(n)] for _ in range(h)]
    for _ in range(m):
        a, b = map(int, input().split())
        lines[a-1][b-1]=1
    if m == 0:
        print(0)
    else:
        ans = 4
        dfs(0, 0, 0)
        print(ans if ans<4 else -1)

