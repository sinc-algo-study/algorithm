'''
맨 바깥쪽 변(?)값부터 numbers에 넣기
numbers에서 회전수만큼 맨 뒤 원소->맨 앞으로 가져오기
numbers 값들 board에 다시 넣기

힌트 : min(N, M) mod 2 = 0
'''
#board 값 -> numbers에 넣기
def BToN(board,numbers,start,N,M):
    for r in range(start,N):
        numbers[start].append(board[r][start])
    for c in range(start,M):
        numbers[start].append(board[N][c])
    for r in range(N,start,-1):
        numbers[start].append(board[r][M])
    for c in range(M,start,-1):
        numbers[start].append(board[start][c])
    return numbers

#numbers 값 -> board에 넣기
def NToB(numbers,board,start,N,M):
    count=0
    for r in range(start,N):
        board[r][start]=numbers[start][count]
        count+=1
    for c in range(start,M):
        board[N][c]=numbers[start][count]
        count+=1
    for r in range(N,start,-1):
        board[r][M]=numbers[start][count]
        count+=1
    for c in range(M,start,-1):
        board[start][c]=numbers[start][count]
        count+=1
    return board

def solution(board,R):
    # 바깥 숫자부터 numbers에 저장
    check=min(len(board),len(board[0]))//2
    numbers=[]
    start=0;
    N=len(board)-1
    M=len(board[0])-1
    while start<check:
        numbers.append([])
        numbers=BToN(board,numbers,start,N,M)
        start+=1
        N-=1
        M-=1

    #숫자 회전
    for count in range(R):
        for i in range(len(numbers)):
            lastNum=numbers[i][-1]
            numbers[i].pop(-1)
            numbers[i].insert(0,lastNum)

    #회전된 숫자 board에 넣기
    start=0;
    N=len(board)-1
    M=len(board[0])-1
    while start<check:
        board=NToB(numbers,board,start,N,M)
        start+=1
        N-=1
        M-=1

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
