from sys import stdin
from collections import deque

puyo = [list(stdin.readline().rstrip()) for _ in range(12)]
ans = 0


def check_puyo():
    bomb = []
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] == '.':
                continue
            # 연결된 같은 색 뿌요들 찾기
            q = deque([(i, j)])
            visit = [(i, j)]
            while q:
                x, y = q.popleft()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 12 and 0 <= ny < 6 and puyo[nx][ny] == puyo[x][y] and (nx, ny) not in visit:
                        q.append((nx, ny))
                        visit.append((nx, ny))
            # 4개 이상 모이면 터짐
            if len(visit) >= 4:
                bomb.extend(visit)
    if bomb:
        bomb_puyo(bomb)
    else:
        return True


def bomb_puyo(visit):
    for vx, vy in visit:
        puyo[vx][vy] = '.'
    # 터진 자리 채우기
    vys = set(vy for vx, vy in visit)
    for vy in vys:
        tmp = deque([puyo[vx][vy] for vx in range(11, -1, -1) if puyo[vx][vy] != '.'])
        for vx in range(11, -1, -1):
            if tmp:
                puyo[vx][vy] = tmp.popleft()
            else:
                puyo[vx][vy] = '.'


while True:
    if check_puyo():
        break
    ans += 1

print(ans)
