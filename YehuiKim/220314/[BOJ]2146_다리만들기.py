import sys
input = sys.stdin.readline
from collections import deque
'''
1. BFS로 섬 찾아서 섬 번호 1,2,3순으로 바꿔주면서, 섬의 가장자리들 모으기.
2. 각 섬 가장자리에서 다른 섬 나올때까지 BFS 돌려서 최소 거리 찾기
  or 각 섬 가장자리에서 다른 섬 가장자리 사이의 거리 구해서, 최소 거리 찾기
'''

# 섬 구분 및 섬의 가장자리 가져오기
def isolatingBFS():
    que = deque()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            # 섬이고 방문 안했으면
            if maps[y][x] and not visit[y][x]:
                que.append((y,x))
                edge = set()
                cnt += 1
                while que:
                    y, x = que.popleft()
                    maps[y][x] = cnt
                    visit[y][x] = 1
                    for dy, dx in dir:
                        ny, nx = y+dy, x+dx
                        # 범위 밖이면, 건너뜀
                        if ny<0 or ny>=n or nx<0 or nx>=n:
                            continue
                        # 방문 했으면, 건너뜀
                        if visit[ny][nx]:
                            continue
                        # 섬이면, 큐에 추가
                        if maps[ny][nx]:
                            que.append((ny,nx))
                            visit[ny][nx] = 1
                        # 섬 아니면, 기존 y,x를 외곽으로 추가
                        else:
                            edge.add((y,x))
                edges.append(edge)


# 섬외곽 셀 : 최대 50*100개 (지도의 경계 x=0, x=n-1 등은 외곽으로 치지 않음)
# 모든 섬 개수 : 최대 50*100개 (바둑판처럼 배치될 경우)
# BFS로 체크할 주변셀개수 : 섬 영역 늘어날수록, 줄어듦
# (섬외곽 셀 x BFS로 체크할 주변셀개수) x 모든 섬들 = < 1억
# => 변경 : BFS 말고 그냥 각 외곽 간의 최소거리를 구하기!

def edgeBFS():
    dist = 200
    for edge in edges:
        for ry,rx in edge:
            que2 = deque()
            que2.append((ry,rx))
            visit = [[0 for _ in range(n)] for _ in range(n)]
            # 현재 섬 번호
            num = maps[ry][rx]
            while que2:
                y, x = que2.popleft()
                visit[y][x]=1
                for dy, dx in dir:
                    ny, nx = y+dy, x+dx
                    # 범위 밖이면, 건너뜀
                    if ny<0 or ny>=n or nx<0 or nx>=n:
                        continue
                    # 방문 했으면, 건너뜀
                    if visit[ny][nx]:
                        continue
                    # 바다면, 큐에 추가
                    if maps[ny][nx]==0:
                        que2.append((ny, nx))
                        visit[ny][nx]=1
                    # 다른 섬이면, 거리 체크해서 ans 갱신
                    elif maps[ny][nx] != num:
                        dist = min(dist, abs(ny-ry)+abs(nx-rx)-1)
                        break
    return dist


def edgeJustCalcul():
    dist = 200
    numOfIsland = len(edges)
    for i in range(1, numOfIsland-1):
        for y,x in edges[i]:
            for j in range(i+1, numOfIsland):
                for ny,nx in edges[j]:
                    dist = min(dist, abs(y-ny)+abs(x-nx)-1)
    return dist


if "__main__"==__name__:
    n = int(input().rstrip())
    maps = [list(map(int, input().split())) for _ in range(n)]
    dir = [(0,-1), (0,1), (-1,0), (1,0)] # dy,dx
    # 섬 외곽 표시해두기
    edges = [[]]
    isolatingBFS()
    print(edgeJustCalcul())

## 줄여도줄여도 시간 5400ms 정도 나왔는데 450ms 나온 사람들은 뭐임....