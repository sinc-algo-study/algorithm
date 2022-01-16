'''
반시계방향으로 배열을 돌림
-> 반시계방향으로 값 바꿀려면 임시변수를 많이 사용해야 함.
-> 간단하게 반대방향인 시계방향으로 돌면서 그 이전값 넣어주면 됨
'''

def solution(board,R):
    check=min(len(board),len(board[0]))//2    

    #시작행은 0->1->...
    for rotate in range(R):
        for start in range(check):
            N=len(board)-start-1
            M=len(board[0])-start-1

            #시작점 값 저장
            tmp=board[start][start];

            # 위 변 / 방향 : ->
            for c in range(start,N):
                board[start][c]=board[start][c+1]
            # 오른쪽  변/ 방향 : ↓
            for r in range(start,N):
                board[r][N]=board[r+1][N]
            #아래 변 / 방향 : <-
            for c in range(N,start,-1):
                board[N][c]=board[N][c-1]
            #왼쪽 변 / 방향 : ↑
            for r in range(N,start,-1):
                board[r][start]=board[r-1][start]

            #시작점 값이 바뀐 상태이므로 기존 값으로 다시 저장
            board[start+1][start]=tmp       

    return board
    

if __name__=='__main__':
    N, M ,R=input().split()
    board=[[0 for i in range(int(M))] for j in range(int(N))]
    
    #board 초기화
    for i in range(int(N)):
        list=input().split()
        for j in range(int(M)):
            board[i][j]=int(list[j])

    board=solution(board,int(R))
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
