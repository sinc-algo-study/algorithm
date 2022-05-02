from sys import stdin
from itertools import combinations
from collections import deque

N, M, D = map(int, stdin.readline().split())
map = [list(map(int, stdin.readline().split())) for _ in range(N)]
map.append([2] * M)     # 성의 위치

'''
격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성 - 궁수 3명을 배치
궁수는 매 턴마다 동시에 공격, 적은 거리가 D이하인 적 중에서 가장 가까운 적(여럿일 경우에 가장 왼쪽에 있는 적)
* 같은 적이 여러 궁수에게 공격당할 수 있다, 공격받은 적은 게임에서 제외됨
* 공격이 끝나면, 적이 이동 (아래로 한 칸)
* 모든 적이 격자판에서 제외되면 게임이 끝난다
'''


# ??? visit 체크 안하니까 시간 더 줄음
def attack(px, py, kill):
    q = deque([(px, py, 0)])
    while q:
        x, y, d = q.popleft()
        if d >= D: return
        for dx, dy in (0, -1), (-1, 0), (0, 1):  # 왼쪽, 위, 오른쪽
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or tmap[nx][ny] == 2:
                continue
            if tmap[nx][ny] == 1:
                kill.add((nx, ny))
                return
            q.append((nx, ny, d+1))


enemy = sum(m.count(1) for m in map)
ans = 0
for team in combinations(range(M), 3):
    cnt, pos = 0, N
    tmap = [m[:] for m in map]
    while pos > 0:
        kill = set()  # 여러번 공격당한 적 있을수도 있으니 집합으로
        for t in team:
            attack(pos, t, kill)
        # 공격받은 적 게임에서 제외
        for kx, ky in kill:
            tmap[kx][ky] = 0
            cnt += 1
        if ans == enemy:
            print(ans)
            exit(0)
        # 적이 한칸씩 내려옴 -> 궁수가 올라가는 걸루
        pos -= 1
        for i in range(M):
            tmap[pos][i] = 2
    ans = max(ans, cnt)
print(ans)





