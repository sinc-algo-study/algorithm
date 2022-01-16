from collections import deque

'''
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

이전세대 다음세대 비교해보면,
↑ 는 ← 이 되고 == 1 은 2가 되고
← 는 ↓ 이 되고 == 2 는 3이 되고
↓ 는 → 이 되고 == 3 은 0이 되고
→ 는 ↑ 이 됨 == 0 은 1이 됨

식으로 만들면 dir = (dir + 1) % 4
'''
board=[[False for i in range(101)] for j in range(101)]
dirY=[0,-1,0,1]
dirX=[1,0,-1,0]
def makeCurve(x,y,d,g):
    curve=[d]
    for gen in range(1,g+1):
        dq=deque()
        #이전 세대 방향 stack에 넣기
        for i in range(len(curve)):
            dq.append(curve[i])

        #다음 세대 커브 만들기
        while len(dq)>0:
            dir=dq.pop()
            curve.append((dir+1)%4)
    
    #격자에 g세대 드래곤 커브 표시
    for d in curve:
        y+=dirY[d]
        x+=dirX[d]
        board[y][x]=True


def solution(info):
    answer=0;

    #격자에 드래곤 커브 표시
    for i in range(len(info)):
        x,y,d,g=info[i]
        board[y][x]=True
        makeCurve(x,y,d,g)
    
    for r in range(100):
        for c in range(100):
            if board[r][c] and board[r][c+1] and board[r+1][c] and board[r+1][c+1]:
                answer+=1;

    return answer


if __name__=='__main__':
    N=int(input())
    info=[]
    for i in range(N):
        info.append(map(int,input().split()))
    print(solution(info))
