import sys
input = sys.stdin.readline
from collections import deque

# n 홀수, 49 이하
# 항상 가운데 ((n+1)/2, (n+1)/2)
# m 100 이하, s (n-1)/2 이하
'''
마법 시전 -> 구슬 파괴 -> (구슬 이동) -> 구슬 폭발 -> (구슬 이동) -> 구슬 변화
1. 마법 시전 : 방향 d - 1,2,3,4(상하좌우) 거리 s
2. 구슬 파괴 => map에서 0으로 만들기
3. 구슬 이동하면서 구슬 수집하면서 폭발(4개 이상 연속시) => letFlag=True, chgFlag=False
4. 수집한 구슬 놓으면서 구슬 변화 => letFlag=False, chgFlag=True
=> 마법 이후 폭발한 각 구슬 개수 구하기 
'''
# 구슬 가져오기
# : 좌 하 우우 상상 좌좌좌 하하하 우우우우 상상상상 좌좌좌좌
# => 좌 하 우 상 순서로 1씩 늘어나면서 두 번씩. 마지막 순서(n-1번째)만 3번함

# 공 차례대로 줄세운 뒤 폭발처리
def getBalls(sx, sy):
    num = 1
    d = 0
    sameBallCnt = 0
    beforeBall = 0
    canExplode = False
    for i in range(1, n):  # 0-4
        if i != n - 1:
            cnt = 2
        else:
            cnt = 3
        for _ in range(cnt):  # 같은 방향 반복 두번씩 or 세번씩
            for j in range(num):  # 반복수
                dx, dy = ball_dir[d % 4]
                sx, sy = dx + sx, dy + sy
                nowBall = maps[sy][sx]

                if sx==0 and sy==0:
                    if nowBall==0:
                        if beforeBall != 0:
                            balls.append((beforeBall, sameBallCnt))
                    elif nowBall>0:
                        if nowBall == beforeBall:
                            sameBallCnt += 1
                            balls.append((beforeBall, sameBallCnt))
                        else:
                            balls.append((beforeBall, sameBallCnt))
                            balls.append((nowBall, 1))
                    else:
                        balls.append((beforeBall, sameBallCnt))
                    if sameBallCnt > 3: # 폭발할 수 있다는 거 표시
                        canExplode = True
                    return canExplode

                # 현재공 = 0이면 pass
                if nowBall == 0:
                    continue
                # nowBall > 0이면 이하 진행
                # 지금 구슬이랑 이전 구슬이 같으면
                if beforeBall == nowBall:
                    sameBallCnt += 1
                # 지금 구슬이랑 이전 구슬 다르면
                else:
                    # 카운트 한 값 저장해주기
                    balls.append((beforeBall, sameBallCnt))
                    if sameBallCnt > 3: # 폭발할 수 있다는 거 표시
                        canExplode = True
                    beforeBall = nowBall
                    sameBallCnt = 1
                    if nowBall == -1:
                        return canExplode
                print(balls)
            d += 1
        num += 1
    return canExplode

# 공 변화시킨것 채워넣기
def doChgBalls(sx, sy):
    num = 1
    d = 0
    keepValue = 0

    for i in range(1, n):  # 0-4
        if i != n - 1:
            cnt = 2
        else:
            cnt = 3
        for _ in range(cnt):  # 같은 방향 반복 두번씩 or 세번씩
            for _ in range(num):  # 반복수
                dx, dy = ball_dir[d % 4]
                sx, sy = dx + sx, dy + sy
                if keepValue != 0:
                    maps[sy][sx] = keepValue
                    keepValue = 0
                else:
                    if balls:
                        keepValue, maps[sy][sx]=balls.popleft()
                    else:
                        maps[sy][sx]=-1
            d += 1
        num += 1

# 폭발시키기
def exploding():
    newBalls = deque()
    flag = False
    while balls:
        ball, cnt = balls.popleft()
        # 4개 이상
        if cnt>3:
            explodeBall[ball] += cnt
            if newBalls:
                befB, befC = newBalls.pop()
                if befB == ball:
                    befC += cnt
                    newBalls.append((ball, befC))
                    if befC>3:
                        flag = True
                else:
                    newBalls.append((befB, befC))
        # 3개 이하
        else:
            newBalls.append((ball, cnt))
    return flag

# 블리자드 마법 시전
def severalMagics():
    for i in range(m):
        d, s = magics[i][0], magics[i][1]
        dx, dy = dir[d]
        mx, my = sx, sy
        for j in range(s):
            mx, my = mx+dx, my+dy
            maps[my][mx]=0
        canExplodeFlg = getBalls(sx, sy)
        while canExplodeFlg:
            # balls 폭발 반복
            canExplodeFlg = exploding()
        doChgBalls(sx, sy) #balls 변화시킨 후 배치
    return sum([i*explodeBall[i] for i in range(1, 4)])


if '__main__' == __name__:
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    magics = [list(map(int, input().split())) for _ in range(m)]
    # 상어 위치를 9로 둠
    global sx, sy
    sx, sy = (n-1)//2, (n-1)//2
    maps[sx][sy] = 9
    dir = [(0,0), (0,-1), (0,1), (-1,0), (1,0)]  # 0상하좌우
    ball_dir = [(-1,0),(0,1),(1,0),(0,-1)] # 좌하우상
    balls = deque()
    explodeBall = [0, 0, 0, 0]
    print(severalMagics())
