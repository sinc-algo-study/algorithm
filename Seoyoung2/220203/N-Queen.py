# from sys import stdin
#
# N = int(stdin.readline())
# ans = 0
# board = [-1] * N    # board[i]: i번째 열에 있는 Queen의 행 번호
#
#
# def is_okay(idx):
#     for j in range(idx):    # idx번 열의 행, 대각선 확인
#         if board[idx] == board[j] or idx-j == abs(board[idx] - board[j]):
#             return False
#     return True
#
#
# def put_q(cnt):
#     global ans
#     if cnt == N:
#         ans += 1
#         return
#     for i in range(N):
#         board[cnt] = i
#         if is_okay(cnt):
#             put_q(cnt+1)
#
#
# put_q(0)
# print(ans)


from sys import stdin

N = int(stdin.readline())
ans = 0
board = [-1] * N    # board[i]: i번째 열에 있는 Queen의 행 번호
visit = [False] * N


def is_okay(idx):
    for j in range(idx):    # idx번 열의 행, 대각선 확인
        if idx-j == abs(board[idx] - board[j]):
            return False
    return True


def put_q(cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        if visit[i]:
            continue
        board[cnt] = i
        if is_okay(cnt):
            visit[i] = True
            put_q(cnt+1)
            visit[i] = False


put_q(0)
print(ans)
