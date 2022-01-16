'''

1. 각 회전마다 새로운 배열 만들기?
메모리 초과 위험성
-> 300 * 300 배열이 1000개 필요
-> 4byte * 90,000 * 1,000 = 약 316MB
-> 512 제한이지만 왠지 불안. 별로 좋은 방법은 아닌 듯.

2. 시작 변수 하나만 따로 뺴놓고 마지막 빈칸에 그걸 집어넣으면?
"min(N, M) mod 2 = 0" 가 힌트?

'''

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(R):  # R번 회전
        for start in range(min(N, M) // 2):  # 배열이 총 몇 겹인지 알 수 있다
            temp = board[start][start]  # 회전 시작 위치. 각 겹의 좌측 상단 좌표
            r, c = start, start  # [r][c] == 새로운 값 넣을 타겟 좌표
            max_r = N - start - 1  # 이번 겹의 테두리 행 인덱스
            max_c = M - start - 1  # 이번 겹의 테두리 열 인덱스

            # 좌
            for j in range(start + 1, max_c + 1):  # j is column
                board[r][c] = board[r][j]  # 내껄 주고
                c = j                      # 내가 다음 타겟이 된다
            # 상
            for j in range(start + 1, max_r + 1):  # j is row
                board[r][c] = board[j][c]  # 내껄 주고
                r = j                      # 내가 다음 타겟이 된다
            # 우
            for j in range(max_c - 1, start - 1, -1):  # j is column
                board[r][c] = board[r][j]
                c = j
            # 상.  여기선 start - 1이 아닌 이유? -> temp를 따로 보관하고 있기 떄문
            for j in range(max_r - 1, start, -1):  # j is row
                board[r][c] = board[j][c]
                r = j
            board[r][c] = temp

    for arr in board:
        print(*arr)