import sys
input = sys.stdin.readline
from collections import defaultdict, deque


# 1초에 한 칸
# 크기 2로 시작, 자기보다 큰 물고기칸 지날 수 없음. 같으면 지날순 있음. 작으면 먹을수 있음
# 먹는 우선순위 : 가장 가깝 > 가장 위 > 가장 왼쪽
# 우선순위에 맞는 칸으로 이동
# => 현재 칸에서 이동할 칸 사이 거리를 시간에 +해줌


def moving_shark(sx, sy):
    global shark
    shark = 2
    time = 0
    eat = 0
    caneat = []
    maps[sy][sx]=0
    while 1:
        temp = []
        for i in fish.keys():
            if i < shark:
                temp.append(i)
        # 먹을 수 있는 물고기는 caneat 리스트에 옮기기
        if temp:
            for i in temp:
                caneat += fish[i]
                del fish[i]
        else:
            if not caneat:
                return time
        #print(caneat)
        temp = []
        for i in range(len(caneat)):
            y, x = caneat[i]
            dist = check_can_go(y, x, sy, sx)
            if dist:
                temp.append((dist, y, x, i))
        if not temp:
            return time
        else:
            temp = sorted(temp, key=lambda x: (x[0], x[1], x[2]))
            dist, sy, sx, i = temp[0]
            time += dist
            # 먹기
            del caneat[i]
            maps[sy][sx]=0
            eat += 1
            if eat==shark:
                shark += 1
                eat = 0
        #for i in range(n):
            #print(maps[i])
    return time


def check_can_go(ty, tx, sy, sx):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[sy][sx]=1
    que = deque()
    que.append((sy, sx))
    while que:
        sy, sx = que.popleft()
        if sy == ty and sx == tx:
            return visit[sy][sx]-1
        for dy, dx in direct:
            ny, nx = sy+dy, sx+dx
            if ny<0 or ny>=n or nx<0 or nx>=n:
                continue
            if maps[ny][nx] > shark:
                visit[ny][nx] = -1
                continue
            if visit[ny][nx] != 0: #방문 했거나 벽이었으면,
                continue
            visit[ny][nx] = visit[sy][sx]+1
            que.append((ny, nx))
    return 0


if '__main__'==__name__:
    n = int(input())
    maps = []
    fish = defaultdict(list)
    direct = [(-1, 0), (1,0), (0,-1), (0, 1)]
    for y in range(n):
        temp = list(map(int,input().split()))
        for x in range(n):
            if temp[x]==9:
                sx, sy = x, y
                temp[x]=0
            if temp[x]!=0:
                fish[temp[x]].append((y,x))
        maps.append(temp)
    print(moving_shark(sx, sy))

# 기존 : 현재 상어크기에서 먹을 수 있는 모든 물고기 => 위치 따짐
# (TIME)
# 일단 현재 위치, 현재 상어 크기에서 도달할 수 있는 물고기만 찾기
# => 거리 기억해두고, 제일 거리 가까운 물고기 먹고 위치로 이동
# ==> 상어 크기 키워가면서, 먹을 수 있는 물고기 체크
# ===> 반복 => 더이상 먹을 수 있는 물고기가 주위 범위에 없으면 stop return
