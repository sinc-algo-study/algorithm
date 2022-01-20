# - 조건
#     - 육목이 되면 안됨
#         - 마지막 돌에서 같은 방향으로 다음 돌 있는지 확인
#         - 맨 마지막 돌, 맨 첫돌에 돌 있는지 확인
#     - 제일 왼쪽의 좌표 (세로면 제일 위) 리턴해야 함
# - 풀이핵심
#     - 4가지 방향으로 각각 돌면서, 해당 방향에 같은 돌 없을 때까지 해당 방향 쭉 파기
#     - 이때 제일 왼쪽 좌표 리턴할 수 있는 방법
#     - 오목이면 육목여부 확인하기

import sys

omok=[[0]*20] #1~19로 맞추려고
black =[]
white =[]
dir = [(1,0),(0,1),(-1,1),(1,1)] #→, ↓, ↙, ↘

for y in range(1, 20):
    temp = [0]+list(map(int, sys.stdin.readline().split()))
    for x in range(1,20):
        if temp[x]==1: #검은색
            black.append((x,y))
        elif temp[x]==2: #흰색
            white.append((x,y))
    omok.append(temp)

def checkValid(x,y):
    if x < 1 or x > 19 or y < 1 or y > 19: #범위밖이면 true
        return True
    return False

def moving(x,y,c,n,cnt,fx,fy):
    global rfy, rfx, rc
    dx, dy = dir[n]
    nx, ny = x+dx, y+dy
    if checkValid(nx, ny):
        return False
    if omok[ny][nx]==c:
        cnt+=1
        # 좌표
        if nx<x:
            fx, fy=nx, ny
        elif nx==x:
            if ny<y:
                fy=ny
        if cnt == 4:
            chx, chy = nx+dx, ny+dy
            bfx, bfy = nx - 5*dx, ny - 5*dy
            if omok[bfy][bfx]==c:
                return False
            if checkValid(chx, chy):
                rfy, rfx, rc = fy, fx, c
                return True
            if omok[chy][chx]!=c:
                rfy, rfx, rc = fy, fx, c
                return True
            else:
                return False
        return moving(nx,ny,c,n,cnt,fx,fy) #오목성공 제외 전부다
    return False

def main():
    result = 0
    for x,y in black:
        c=1
        for n in range(0,4): #방향 하나
            fx, fy = x, y
            cnt = 0
            if True==moving(x,y,c,n,cnt,fx,fy):
                result = 1
                return rc, rfx, rfy
    for x,y in white:
        c=2
        for n in range(0,4): #방향 하나
            cnt = 0
            fx, fy = x, y
            if True==moving(x,y,c,n,cnt,fx,fy):
                result =1
                return rc, rfx, rfy
    return 0

rfx, rfy, rc = 0, 0, 0
ans = main()
if (ans == 0):
    print(0)
else :
    rc, rfx, rfy = ans
    print(rc)
    print(rfy, rfx)