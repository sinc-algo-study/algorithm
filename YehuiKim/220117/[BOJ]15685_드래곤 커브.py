# 방향성 0 → 0, 1 → 0, 1, 2, 1 → 0, 1, 2, 1, 2, 3, 2, 1 식으로
# 한 세대 늘어날 때마다 이전세대의 방향+1한게 reverse돼서 합쳐짐
# 단, (방향+d)%4 처리해줘야 함

import sys
n = int(sys.stdin.readline())
arr = []
maps = [[0]*101 for _ in range(101)]
# 우, 상, 좌, 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0

for i in range(n):
    x,y,d,g=map(int, sys.stdin.readline().split())
    arr.append((x,y,d,g))

for x,y,d,g in arr:
    # 첫 시작
    curv = [d]
    hist = [d]
    maps[y][x]=1
    # g+1해줘야 해당 세대까지 for문 진행
    for _ in range(g+1):
        for i in curv:
            x, y = x+dx[i], y+dy[i]
            maps[y][x] = 1
        curv = []
        # history에 있던 것 그대로 +1 하고 reverse
        for i in range(len(hist)):
            curv.append((hist[i]+1)%4)
        curv.reverse()
        hist+= curv

# 1~100까지만 돌면서, 우&우하&하 좌표가 1이면 카운트
for y in range(100):
    for x in range(100):
        if maps[y][x]==1:
            if maps[y][x+1]==1 and maps[y+1][x]==1 and maps[y+1][x+1]==1:
                ans+=1
print(ans)
