import sys
input = sys.stdin.readline
from collections import deque


'''
1. 맨 아래부터 이어진 것 4칸 이상인 것 전체 체크 (BFS)
   -방문처리
   -범위 밖 or 방문한 곳 or 다른 색이면 pass
   -좌표 que에 담아두다가 같은 색 cnt>3넘는 순간 해당 좌표 0으로 바꾸고, 큐 return해서
    큐에 있는 좌표들 빼서 0으로 바꿔주기 
2. 터트리고 위의 칸에 있는걸 아래로 당긴다. 빈 칸 나오기 전까지. (cnt+1)
3. 1-2반복. 1에서 return False면, 멈추기. cnt 출력
'''

# 메인
def puyoPuyo():
    noneFlag = False
    ans = -1
    while not noneFlag:
        ans += 1
        noneFlag = True
        visited = [[0 for _ in range(6)] for _ in range(12)]
        willBeDel = [[0 for _ in range(6)] for _ in range(12)]
        for y in range(11, -1, -1):
            if field[y]==[".",".",".",".",".","."]:
                break
            for x in range(6):
                # 방문하지 않은 좌표이고, 해당 좌표!=.이면
                if visited[y][x] == 0 and field[y][x]!=".":
                    funcFlag = bfs(y, x, visited, willBeDel)
                    if not funcFlag:
                        noneFlag = False
                    #print("-")
        delPuyo(willBeDel)
    return ans

# 연속된 칸 계산
def bfs(y, x, visited, willBeDel):
    color = field[y][x]
    cnt = 0
    que = deque()
    que.append((y,x))
    visited[y][x] = 1
    tmp = []
    tmp.append((y, x))
    while que:
        yy, xx = que.popleft()
        cnt += 1
        for d in range(4):
            dx, dy = dir[d]
            ny, nx = yy+dy, xx+dx
            # 범위 내인지 확인
            if 0<=ny<12 and 0<=nx<6:
                # 미방문&같은색이면 큐에 추가
                if visited[ny][nx]==0 and field[ny][nx]==color:
                    que.append((ny, nx))
                    visited[ny][nx]=1 # 방문처리
                    tmp.append((ny, nx))
    # 3개 넘으면 삭제표시
    if cnt>3:
        for y, x in tmp:
            willBeDel[y][x]=1
        return False
    else:
        return True

# 삭제
def delPuyo(willBeDel):
    for y in range(12):
        if not any(willBeDel[y]):
            continue
        for x in range(6):
            if willBeDel[y][x] == 1:
                field[y][x]="."
                dropDown(y,x)

# 하나씩 내리기
def dropDown(y,x):
    # 상
    dx, dy = dir[0]
    flag = True
    while flag:
        ny, nx = y + dy, x + dx
        if 0<=ny<12:
            upper = field[ny][nx]
            if upper == ".":
                flag = False
            else:
                field[y][x], field[ny][nx] = field[ny][nx], field[y][x]
                y, x = ny, nx
        else:
            flag = False


if '__main__' == __name__:
    field = [list(input().strip()) for _ in range(12)]
    dir = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 상하좌우
    print(puyoPuyo())

