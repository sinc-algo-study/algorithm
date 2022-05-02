from sys import stdin
from collections import deque

'''
1. 낚시왕이 오른쪽으로 한 칸 이동한다.
2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
3. 상어가 이동한다. (주어진 속도로, 경계에서 방향바꿔 계속 전진, 여러마리 있으면 큰 상어가 남음)

한칸씩 가면 시간초과남,, 한번에 가는법 생각해야함
'''
R, C, M = map(int, stdin.readline().split())
shark = [[deque() for _ in range(C)] for _ in range(R)]
ans = 0
for m in range(M):
    # s는 속력, d는 이동 방향(1-위, 2-아래, 3-오른쪽, 4-왼쪽), z는 크기
    r, c, s, d, z = map(int, stdin.readline().split())
    shark[r-1][c-1].append((z, s, d))
if M == 0:
    print(0)
    exit(0)


def move():
    dxdy = (0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)

    # 상어가 있는 위치 체크
    check = []
    for x in range(R):
        for y in range(C):
            if shark[x][y]:
                check.append((x, y))
    RR, CC = 2 * R - 2, 2 * C - 2
    while check:
        x, y = check.pop()
        z, s, d = shark[x][y].popleft()     # 기존 상어가 움직여야해서 popleft
        if d == 1:
            x = (RR - x + s) % RR
            if x >= R:
                shark[RR-x][y].append((z, s, 1))
            else:
                shark[x][y].append((z, s, 2))
        elif d == 2:
            x = (x + s) % RR
            if x >= R:
                shark[RR-x][y].append((z, s, 1))
            else:
                shark[x][y].append((z, s, 2))
        elif d == 4:
            y = (CC - y + s) % CC
            if y >= C:
                shark[x][CC-y].append((z, s, 4))
            else:
                shark[x][y].append((z, s, 3))
        elif d == 3:
            y = (y + s) % CC
            if y >= C:
                shark[x][CC-y].append((z, s, 4))
            else:
                shark[x][y].append((z, s, 3))
    # 먹고 먹히기
    for x in range(R):
        for y in range(C):
            if len(shark[x][y]) > 1:
                big = max(shark[x][y])
                shark[x][y] = deque([big])


for pos in range(C):
    # attack
    for i in range(R):
        if shark[i][pos]:
            kill = shark[i][pos].pop()
            ans += kill[0]
            break
    move()
print(ans)
