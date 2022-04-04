'''
0 c
r
상 바닥 하 천장 / 좌 우
  1
5 2 6 4
  3
=> 동&서 - 상,하 고정 / 남&북 - 좌,우 고정
=> (동) 1 2 3 4 / 5 6 -> 1 6 3 5 / 2 4 => 바닥->좌,천장->우,좌->천장,우->바닥
=> (서) 1 2 3 4 / 5 6 -> 1 5 3 6 / 4 2 => 바닥->우,천장->좌,좌->바닥,우->천장
=> (남) 1 2 3 4 / 5 6 -> 2 3 4 1 / 5 6 => 천장->하,하->바닥,바닥->상,상->천장
=> (북) 1 2 3 4 / 5 6 -> 4 1 2 3 / 5 6 => 상->바닥,바닥->하,하->천장,천장->상
주사위 윗 면 1, 오른쪽 3 (x,y) => 처음엔 모든 면 0
지도에 정수 있음
주사위 굴려서,
-이동한 칸 0이면 주사위 바닥의 수가 칸에 복사
-이동한 칸 0아니면 칸에 쓰인 수가 주사위 바닥으로 이동 (칸은 0 됨)
'''
'''
@ x, y 방향 잘 읽고 풀기!!! (일반적인 기준이 아닐 수 있음)
@ 어렵게 생각할 필요 없이, 동서남북 이동시 주사위 list 내의 순서 바뀌는 방식 그대로 구현!
'''

import sys
input = sys.stdin.readline


def copyDice(c,r):
    num = maps[r][c]
    if num == 0:
        maps[r][c] = dice[1]
    else:
        dice[1], maps[r][c] = num, 0


def arrangeDice(d):
    if d==1:
        dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
    elif d==2:
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
    elif d==3:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    else:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]


def moving(x, y):
    answer = []
    # 주사위에 복사
    copyDice(x,y)
    for d in todo:
        dr,dc = dirs[d]
        nr,nc = y+dr,x+dc
        if nr<0 or nr>n-1 or nc<0 or nc>m-1:
            continue
        y,x=nr,nc
        arrangeDice(d)
        copyDice(x,y)
        answer.append(dice[3])
    for i in answer:
        print(i)


if "__main__"==__name__:
    n, m, y, x, k = map(int, input().split())
    dirs = [(0,0), (0,1), (0,-1), (-1,0), (1,0) ] # r,c : 0 동 서 북 남
    maps = [list(map(int, input().split())) for _ in range(n)]
    todo = list(map(int, input().split()))
    dice = [0,0,0,0,0,0]  # 상 바닥(복사) 하 천장(출력) / 좌 우
    moving(x, y)
'''
======> 4 (남) : 0 0 0 0 0 0 -> 0 3 0 0 0 0
  0
0 3 0 0
  0
======> 4 (남) : 3 0 0 0 0 0 -> 3 5 0 0 0 0
  3
0 5 0 0
  0
======> 4 (남) : 5 0 0 3 0 0 -> 5 7 0 3 0 0
  5
0 7 0 3 
  0
======> 1 (동) : 5 0 0 0 7 3 -> 5 8 0 0 7 3
  5
7 8 3 0
  0
======> 3 (북) : 0 5 8 0 7 3 -> 0 6 8 0 7 3
  0          0
7 5 3 0 -> 7 6 3 0
  8          8
======> 3 (북) : 0 0 6 8 7 3 -> 0 4 6 8 7 3
  0
7 4 3 8
  6
======> 3 (북) : 8 0 4 6 7 3 -> 8 2 4 6 7 3 
  8
7 2 3 6
  4
======> 2 (서) : 8 7 4 3 6 2
  8
6 7 2 3
  4 
'''
