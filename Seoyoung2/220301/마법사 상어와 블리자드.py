from sys import stdin
from collections import deque
'''
1차원으로 변환해서 생각하기... 값 말고 좌표를 넣기

1) 파편 던져 구슬 파괴
2) 비어있는 공간 채우기 (이동)
3) 4개 이상 연속하면 구슬 폭발 (반복)
4) 비어있는 공간 채우기 (이동)
5) 그룹당 구슬의 개수+구슬의 번호로 변환
'''


def make_map(x, y):
    dxdy = (0, -1), (1, 0), (0, 1), (-1, 0)
    t_list = []
    d, num = 0, 0
    while True:
        if x == 0 and y == -1:
            return t_list[:-1]
        if d % 2 == 0:      # 2번씩 반복되니까
            num += 1
        for _ in range(num):
            x += dxdy[d][0]
            y += dxdy[d][1]
            t_list.append((x, y))
        d = (d + 1) % 4


def fill_map():
    tmp = deque([])
    for x, y in pos_list:
        if grid[x][y] == 0:     # 빈 공간,,
            tmp.append((x, y))
        elif grid[x][y] != 0 and tmp:   # 빈공간 아닌데 앞에 빈공간 있으면
            tx, ty = tmp.popleft()
            grid[tx][ty] = grid[x][y]
            grid[x][y] = 0
            tmp.append((x, y))


def destroy():
    # 더이상 4개 연속 없으면 True 리턴
    before, cnt = 0, 0
    flag = True
    visit = deque([])
    for x, y in pos_list:
        now = grid[x][y]
        if now == before:
            cnt += 1
            visit.append((x, y))
        else:
            if cnt >= 4:
                flag = False
                while visit:
                    vx, vy = visit.popleft()
                    score[grid[vx][vy]] += 1
                    grid[vx][vy] = 0
            cnt = 1
            visit.clear()
            visit.append((x, y))
            before = now
    # 폭파 여부에 따라 폭파 종료 or 빈 공간 채우고 다시 반복
    if flag:
        return True
    else:
        fill_map()
        return False


def make_group():
    new = deque([])
    before, cnt = grid[pos_list[0][0]][pos_list[0][1]], 1
    for x, y in pos_list[1:]:
        now = grid[x][y]
        if now == before:
            cnt += 1
        else:
            new.append(cnt)
            new.append(before)
            cnt = 1
            before = now
    return new


N, M = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(N)]
dxdy = (0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)

grid[N//2][N//2] = 9                # 예외처리 대신 9로 고정
pos_list = make_map(N//2, N//2)     # pos_list는 고정 위치 리스트로 변하지 않음

score = [0] * 4
for _ in range(M):
    d, s = map(int, stdin.readline().split())

    # 파편 던져 구슬 파괴
    nx = ny = N//2
    for _ in range(1, s+1):
        nx, ny = nx + dxdy[d][0], ny + dxdy[d][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        grid[nx][ny] = 0

    # 비어있는 공간 채우기
    fill_map()

    # 4개 이상 연속하면 구슬 폭발 (반복)
    while True:
        if destroy():
            break

    # 그룹당 구슬의 개수+구슬의 번호로 변환
    new = make_group()
    for x, y in pos_list:
        if new:
            grid[x][y] = new.popleft()
        else:
            grid[x][y] = 0

print(score[1] + score[2] * 2 + score[3] * 3)