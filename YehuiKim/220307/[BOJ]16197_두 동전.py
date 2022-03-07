import sys
input = sys.stdin.readline
'''
1. 상하좌우 이동시켜본다.
2. 이동시킨 결과, 동전이 0개거나 변화없으면 해당 방향 pass. 1개면 정답에 담아둠. 2개면 1-2반복
    => dfs : 4 방향 돌림. cnt 전달해서 10 넘치면 -1 리턴. visit 표시함.
    - 벽이면 이동여부 +1 
    => 범위밖이면 일단 무조건 종료됨. 1개든 2개든 떨어졌으니.
    => 두 동전 위치 같아지면 해당 case는 무조건 실패로 종료. => 둘이 생사를 함께하니까
3. 10번까지만 해봤는데 끝 안나면 -1 출력한다.
'''
def dfs(oneX, oneY, twoX, twoY, cnt, visit):
    res = 11
    cnt += 1
    if cnt == 11:
        return 11
    for dx, dy in dir:
        ret = 11
        fallCnt = 0
        visit[oneY][oneX] = 1
        visit[twoY][twoX] = 1
        nOneX, nOneY = oneX+dx, oneY+dy
        nTwoX, nTwoY = twoX+dx, twoY+dy
        # 두 동전 위치 같으면 => 종료
        if nOneX==nTwoX and nOneY==nTwoY:
            visit[oneY][oneX] = 0
            visit[twoY][twoX] = 0
            continue
        # 각 코인이 낙하하면
        if nOneX<0 or nOneX>=m or nOneY<0 or nOneY>=n:
            fallCnt += 1
        if nTwoX<0 or nTwoX>=m or nTwoY<0 or nTwoY>=n:
            fallCnt += 1

        if fallCnt>1: # 둘 다 낙하 => 종료
            visit[oneY][oneX] = 0
            visit[twoY][twoX] = 0
            continue
        elif fallCnt==1: # 하나만 낙하 => 성공
            ret = cnt
        else: # 낙하 둘다 안함
            if visit[nOneY][nOneX]==0 or visit[nTwoY][nTwoX]==0:
                one = board[nOneY][nOneX]
                two = board[nTwoY][nTwoX]
                if one == '#':
                    if two == '#': # 둘다 벽이면 이동 불가 => 종료
                        visit[oneY][oneX] = 0
                        visit[twoY][twoX] = 0
                        continue
                    else: # 첫번째만 벽
                        ret = dfs(oneX, oneY, nTwoX, nTwoY, cnt, visit)
                else:
                    if two == '#': # 두번째만 벽
                        ret = dfs(nOneX, nOneY, twoX, twoY, cnt, visit)
                    else: # 둘 다 벽 아님
                        ret = dfs(nOneX, nOneY, nTwoX, nTwoY, cnt, visit)
        visit[oneY][oneX] = 0
        visit[twoY][twoX] = 0
        res = min(ret, res)
    return res


if "__main__" == __name__:
    n, m = map(int, input().split()) # y, x
    coins = []
    board = []
    for y in range(n):
        tmp = list(input().rstrip())
        # 코인만 좌표 모으기
        for x in range(m):
            if tmp[x] == "o":
                coins.append((x, y))
        board.append(tmp)
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    oneX, oneY = coins[0]
    twoX, twoY = coins[1]
    maxPush = min(11, dfs(oneX, oneY, twoX, twoY, 0, visit))
    if maxPush == 11:
        print(-1)
    else:
        print(maxPush)